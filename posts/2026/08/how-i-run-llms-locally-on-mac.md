<!--
.. title: How I run LLMs locally on Mac
.. slug: how-i-run-llms-locally-on-mac
.. date: 2026-08-27 22:33:44 UTC+05:30
.. tags: AI, macbook
.. category: 
.. link: 
.. description: 
.. type: text
-->

![Harness, Server, and Models](/images/mac-local-llms.svg)


### Harness

OpenCode & oh-my-pi come with batteries included and works out of the box.

Pi is barebones & lightweight. 
There are quality plugins available to extend the functionality & customise the behaviour.
It is extremely extensible.


### Inference Server

Ollama MLX doesn't generate tokens efficiently.

Rapix-MLX, omlx are excellent at utilizing resources and generating tokens efficiently.
With M5 Pro 48GB RAM, they are able to generate ~50 tokens/second with `Qwen3.6-35B-A3B-4bit` model.

Llama.cpp is cross-platform and it is extremely fast as well.

### Local LLMs

![dense vs moe](/images/dense-vs-moe-llm.svg)

Qwen3.6-35B-A3B model made locall LLMs usable on decent hardware. 

Qwen3.6-35B-A3B - has 35B parameters & only 3B are active at a time. I use 4bit quantized model as it provides
a better tradeoff between speed and accuracy. It fits in 48GB RAM with some headroom for other applications.

Bonsai has highest intelligent densisty and it can run on ~5 GB RAM.

It is surprising how fast & powerful the local LLMs have become.

