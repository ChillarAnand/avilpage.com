Models: mlx-community/Qwen3.6-35B-A3B-4bit, mlx-community/Qwen3.8-27B-4bit on M5 Pro 48GB
Server: omlx (OpenAI-compatible) at port 8004

## Speed wins (easiest first)

1. **Soft thinking mode** — omit `enable_thinking`, model auto-decides per query
2. **Budget thinking** — cap reasoning, not binary on/off
   ```python
   extra_body={"enable_thinking": True, "thinking_budget": 1024}
   extra_body={"enable_thinking": False}  # force off
   ```
3. **Prefix cache** — big win for repeated system prompts (coding)
   ```bash
   omlx serve --paged-ssd-cache-dir ~/.omlx/cache --hot-cache-max-size 4GB
   ```
4. **Shorter system prompts + `max_tokens` cap** — free token reduction
5. **Batch size 4-8** — better ANE utilization than batch=1
6. **Speculative decoding** — pair 35B with 0.5B draft, 2-3x throughput, zero quality loss
7. **ASCII-Condensed** — limit to ASCII-only vocabulary, reduces vocab search space
8. **Sliding window / smaller ctx** — cut KV cache memory for short tasks

## Thinking: when to use

| Task | Mode |
|------|------|
| Debug, architecture, multi-step logic | think on |
| Summarize, translate, extract, reformat, Q&A | think off |
