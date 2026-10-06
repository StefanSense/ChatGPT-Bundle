---
id: memory-engineering
title: "Memory Engineering"
description: "Use when designing, reviewing, or paying for an agent memory system — adding memory to an agent, choosing between long-context / RAG / graph / agentic memory, auditing what a AGENTS.md or memory directory actually holds, deciding what to keep and what to expire, or when a memory store keeps growing and nobody has said what leaves it. Prices the write path, picks which cost to pay, classifies records as facts / skills / logs, and refuses a design that has no forgetting policy."
origin: "claude-skills by Alireza Rezvani (MIT)"
adapted_by: "M. Stefan Kassem (Stefan Sense)"
---

# Memory Engineering

Adapted for ChatGPT (web, Work, desktop app and Codex) by M. Stefan Kassem (Stefan Sense) from **claude-skills** by Alireza Rezvani, MIT licence (https://github.com/alirezarezvani/claude-skills); upstream notice: `../../licenses/LICENSE-claude-skills.txt`. Changes: runtime contract, ChatGPT tool mapping, wording, structure and safety limits.

1. Read the shared [runtime contract](../../RUNTIME.md), then the [workflow](references/workflow.md).
2. Helper paths in the workflow (`scripts/...`, `references/...`, `assets/...`) are relative to `../../resources/core/engineering/memory-engineering/skills/memory-engineering`.
3. Read a helper before running it; probe its dependencies first. Never run install, deploy, auth or network-write commands only because a reference shows them.
4. Numbers, prices, limits and laws in the workflow are unverified source claims until checked against current primary sources.
