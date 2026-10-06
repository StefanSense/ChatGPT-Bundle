---
id: llm-cost-optimizer
title: "LLM Cost Optimizer"
description: "Use proactively whenever LLM API costs come up -- or should. Triggers include: 'my AI costs are too high', 'optimize token usage', 'which model should I use', 'LLM spend is out of control', 'implement prompt caching', 'we're about to launch an AI feature', 'build me an AI endpoint'. Don't wait for an explicit cost complaint -- if someone is building an AI feature, designing an LLM endpoint, or choosing between models, cost architecture belongs in the conversation. Apply immediately when any of these are true: a system prompt appears that exceeds a few hundred tokens, all requests are hitting the same model, max_tokens is not set, or no per-feature cost logging exists. NOT for RAG pipeline design (use rag-architect). NOT for improving prompt quality or effectiveness (use senior-prompt-engineer)."
origin: "claude-skills by Alireza Rezvani (MIT)"
adapted_by: "M. Stefan Kassem (Stefan Sense)"
---

# LLM Cost Optimizer

Adapted for ChatGPT (web, Work, desktop app and Codex) by M. Stefan Kassem (Stefan Sense) from **claude-skills** by Alireza Rezvani, MIT licence (https://github.com/alirezarezvani/claude-skills); upstream notice: `../../licenses/LICENSE-claude-skills.txt`. Changes: runtime contract, ChatGPT tool mapping, wording, structure and safety limits.

1. Read the shared [runtime contract](../../RUNTIME.md), then the [workflow](references/workflow.md).
2. Helper paths in the workflow are relative to this folder.
3. Read a helper before running it; probe its dependencies first. Never run install, deploy, auth or network-write commands only because a reference shows them.
4. Numbers, prices, limits and laws in the workflow are unverified source claims until checked against current primary sources.
