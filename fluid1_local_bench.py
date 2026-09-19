#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = ["requests", "anthropic"]
# ///
"""Benchmark: Fluid-1 post-processing vs local Qwen / Gemma, over FluidVoice export.

Judge subcommand scores results with Claude Sonnet 5 (pointwise, blind,
label order swapped per pass to cancel position bias).
"""

import argparse
import json
import sys
import time
from pathlib import Path

import requests

MODELS = {
    "qwen": {
        "endpoint": "http://localhost:8004/v1/chat/completions",
        "model": "mlx-community/Qwen3.6-35B-A3B-4bit",
    },
    "gemma": {
        "endpoint": "http://localhost:8002/v1/chat/completions",
        "model": "gemma-4-e2b-4bit",
    },
    "qwen1.5b": {
        "endpoint": "http://localhost:8005/v1/chat/completions",
        "model": "mlx-community/Qwen2.5-1.5B-Instruct-4bit",
    },
}

SYSTEM_PROMPT = (
    "You clean up raw speech-to-text dictation output for readability. "
    "Fix capitalization, punctuation, and obvious word-choice errors from "
    "the speech recognizer (e.g. misheard words). Keep the speaker's meaning "
    "and wording otherwise unchanged. Do not add commentary. Output only the "
    "cleaned text, nothing else."
)


def load_samples(json_path, limit=None):
    data = json.loads(Path(json_path).read_text())
    history = data.get("transcriptionHistory", [])
    samples = [h for h in history if h.get("wasAIProcessed") and h.get("rawText")]
    if limit:
        samples = samples[:limit]
    return samples


def call_model(endpoint, model, raw_text, timeout=60):
    resp = requests.post(
        endpoint,
        json={
            "model": model,
            "messages": [
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": raw_text},
            ],
            "temperature": 0.2,
        },
        timeout=timeout,
    )
    resp.raise_for_status()
    return resp.json()["choices"][0]["message"]["content"].strip()


JUDGE_MODEL = "claude-sonnet-5"

JUDGE_SYSTEM_PROMPT = (
    "You judge speech-to-text dictation cleanup quality. You are given the raw "
    "dictation and several candidate cleaned versions, labeled with letters. "
    "Rank the candidates from best to worst at fixing capitalization, "
    "punctuation, and misheard words while preserving the speaker's meaning and "
    "wording. Reply with ONLY a JSON object: "
    '{"ranking": ["<label>", "<label>", ...], "reason": "<one short sentence>"}. '
    "ranking must list every label given, best first."
)


def judge_call(client, raw_text, labeled_candidates):
    candidates_block = "\n\n".join(
        f"[{label}]\n{text}" for label, text in labeled_candidates.items()
    )
    msg = client.messages.create(
        model=JUDGE_MODEL,
        max_tokens=1000,
        system=JUDGE_SYSTEM_PROMPT,
        messages=[
            {
                "role": "user",
                "content": f"RAW:\n{raw_text}\n\nCANDIDATES:\n{candidates_block}",
            }
        ],
    )
    text = next(b.text for b in msg.content if b.type == "text").strip()
    start, end = text.find("{"), text.rfind("}")
    if start == -1 or end == -1:
        raise ValueError(f"no JSON object in judge response: {text!r}")
    return json.loads(text[start : end + 1])


def judge_sample(client, entry, candidate_keys):
    candidates = {k: entry.get(k) for k in candidate_keys}
    candidates = {k: v for k, v in candidates.items() if v}
    if len(candidates) < 2:
        return None

    labels = ["A", "B", "C", "D"][: len(candidates)]
    keys = list(candidates.keys())

    passes = []
    for pass_i in range(2):
        order = keys[::-1] if pass_i == 1 else keys
        mapping = dict(zip(labels, order))
        labeled = {label: candidates[k] for label, k in mapping.items()}
        try:
            verdict = judge_call(client, entry["rawText"], labeled)
        except Exception as e:
            print(f"  judge call failed: {e}", file=sys.stderr)
            continue
        ranking_keys = [mapping[label] for label in verdict.get("ranking", []) if label in mapping]
        passes.append({"rankingKeys": ranking_keys, "reason": verdict.get("reason", "")})

    return passes


def run_judge(args):
    import anthropic

    results = json.loads(Path(args.results_path).read_text())
    candidate_keys = [k.strip() for k in args.candidates.split(",") if k.strip()]
    client = anthropic.Anthropic()

    scores = {k: 0.0 for k in candidate_keys}
    n_ranked = {k: 0 for k in candidate_keys}
    judged = []

    for i, entry in enumerate(results, 1):
        passes = judge_sample(client, entry, candidate_keys)
        if not passes:
            print(f"[{i}/{len(results)}] skipped (missing candidates)")
            continue
        for p in passes:
            n = len(p["rankingKeys"])
            for rank, key in enumerate(p["rankingKeys"]):
                scores[key] += (n - 1 - rank)  # borda: 1st place = n-1 points
                n_ranked[key] += 1
        judged.append({"id": entry.get("id"), "passes": passes})
        print(f"[{i}/{len(results)}] judged")

    print("\n--- win rates (avg borda score, higher = better) ---")
    for key in candidate_keys:
        if n_ranked[key]:
            print(f"{key}: {scores[key] / n_ranked[key]:.3f} (n={n_ranked[key]})")
        else:
            print(f"{key}: no data")

    Path(args.out).write_text(json.dumps(judged, indent=2))
    print(f"\nWrote per-sample judge verdicts to {args.out}")


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)

    run = sub.add_parser("run", help="generate candidate texts from local models")
    run.add_argument("json_path")
    run.add_argument("--limit", type=int, default=30)
    run.add_argument(
        "--models",
        default="qwen,gemma",
        help="comma-separated keys from MODELS to run (qwen,gemma)",
    )
    run.add_argument("--out", default="fluid1_vs_local_results.json")

    judge = sub.add_parser("judge", help="score candidates with Claude Sonnet 5")
    judge.add_argument("results_path")
    judge.add_argument(
        "--candidates",
        default="fluid1Text,qwenText,gemmaText",
        help="comma-separated result keys to compare",
    )
    judge.add_argument("--out", default="judge_verdicts.json")

    args = ap.parse_args()

    if args.cmd == "judge":
        run_judge(args)
        return

    model_keys = [k.strip() for k in args.models.split(",") if k.strip()]
    for k in model_keys:
        if k not in MODELS:
            sys.exit(f"unknown model key: {k} (choices: {list(MODELS)})")

    samples = load_samples(args.json_path, args.limit)
    print(f"Loaded {len(samples)} samples with rawText + AI-processed text.")
    print(f"Testing models: {model_keys}")

    results = []
    for i, s in enumerate(samples, 1):
        raw = s["rawText"]
        fluid1 = s.get("processedText", "")

        entry = {
            "id": s.get("id"),
            "appName": s.get("appName"),
            "rawText": raw,
            "fluid1Text": fluid1,
        }

        for key in model_keys:
            cfg = MODELS[key]
            try:
                t0 = time.time()
                text = call_model(cfg["endpoint"], cfg["model"], raw)
                elapsed = time.time() - t0
            except requests.RequestException as e:
                print(f"[{i}/{len(samples)}] {key} call failed: {e}", file=sys.stderr)
                entry[f"{key}Text"] = None
                entry[f"{key}LatencySec"] = None
                continue
            entry[f"{key}Text"] = text
            entry[f"{key}LatencySec"] = round(elapsed, 2)

        results.append(entry)
        print(f"[{i}/{len(samples)}] done")

    Path(args.out).write_text(json.dumps(results, indent=2))
    print(f"\nWrote {len(results)} results to {args.out}")
    print("Open the JSON and eyeball rawText / fluid1Text / <model>Text side by side.")


if __name__ == "__main__":
    main()
