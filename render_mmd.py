#!/usr/bin/env python3
"""Render all .mmd (mermaid) files in repo to .svg via mmdc.

Run from repo root:
    python3 render_mmd.py

Rewrites absolute img src="/assets/..." paths to relative paths (mmdc's
headless chrome resolves "/" against filesystem root, not repo root) before
rendering, using a temp copy so source .mmd files stay untouched.
"""
import os
import re
import subprocess
import sys
import tempfile

REPO_ROOT = os.path.dirname(os.path.abspath(__file__))
ABS_SRC_RE = re.compile(r'(src=")/([^"]+)')


def render(mmd_path: str) -> bool:
    mmd_dir = os.path.dirname(mmd_path)
    rel_root = os.path.relpath(REPO_ROOT, mmd_dir)

    with open(mmd_path) as f:
        content = f.read()

    fixed = ABS_SRC_RE.sub(lambda m: f'{m.group(1)}{rel_root}/{m.group(2)}', content)

    out_path = mmd_path.rstrip(".mmd") + ".svg"
    with tempfile.NamedTemporaryFile("w", dir=mmd_dir, delete=False) as tmp:
        tmp.write(fixed)
        tmp_path = tmp.name

    try:
        result = subprocess.run(
            ["mmdc", "-i", tmp_path, "-o", out_path],
            capture_output=True,
            text=True,
        )
        if result.returncode != 0:
            print(f"FAIL {mmd_path}\n{result.stderr}", file=sys.stderr)
            return False
        print(f"OK   {mmd_path} -> {out_path}")
        images_dir = os.path.join(REPO_ROOT, "images")
        os.makedirs(images_dir, exist_ok=True)
        img_dest = os.path.join(images_dir, os.path.basename(out_path))
        import shutil
        shutil.copy2(out_path, img_dest)
        print(f"     copied -> {img_dest}")
        return True
    finally:
        os.remove(tmp_path)


def main() -> int:
    mmd_files = []
    for dirpath, _, filenames in os.walk(REPO_ROOT):
        if "/.git" in dirpath or "/node_modules" in dirpath:
            continue
        for name in filenames:
            if name.endswith(".mmd"):
                mmd_files.append(os.path.join(dirpath, name))

    if not mmd_files:
        print("No .mmd files found.")
        return 0

    ok = all([render(p) for p in sorted(mmd_files)])
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
