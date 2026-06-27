<!--
.. title: Everyday AI Tools
.. slug: everyday-ai-tools
.. date: 2026-05-31 23:17:04 UTC+05:30
.. tags: AI
.. category: 
.. link: 
.. description: 
.. type: text
-->

CLI Tools: GitHub Copilot CLI, Claude Code & Open Code

IDE: GitHub Copilot Plugin

### Caveman

![caveman](/images/caveman.png)

Reduces token usage by eliminating clutter. It doesn't affect thinking/reasoning.

Alternatives: [Ponytail]()

These tools will help in saving more than 30% of our time to read model output and money(tokens).

### Claude-mem

![claude-mem](/images/claude-mem.png)

Claude-mem preserves context across sessions by automatically capturing tool usage observations, 
generating semantic summaries, and making them available to future sessions. 
This enables Claude to maintain continuity of knowledge about projects even after sessions end or reconnect.

This will improve developer productivity as well.

Alternatives: [AgentMemory](https://github.com/rohitg00/agentmemory) (backed by Linux Foundation)

### CodeGraph

We work with multiple code bases on a daily basis and claude-code spawns Explore agents 
that scan files with grep, glob and read. They consume tokens on every tool call.

CodeGraph provides a pre-indexed knowledge graph to those agents, which reduces 50% tokens.

*Alternatives*: [Graphify](https://github.com/safishamsi/graphify)

### rtk


CLI proxy that reduces LLM token consumption by ~75% on common dev commands like ls, cat, git, etc.

*Similar tool*: [Headroom](https://github.com/headroomlabs-ai/headroom)

### Misc

andrej-karpathy-skills

ccstatusline

Custom instructions for agents in plain markdown files
