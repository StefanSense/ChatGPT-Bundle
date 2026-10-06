---
id: zero-hallucination-coder
title: "Zero Hallucination Coder"
description: "Runs a disciplined Discuss - Map - Decompose - Execute - Verify loop that grounds code in verified structure — no invented APIs, no assumed imports, no placeholder code — with a lazy-senior-dev YAGNI ladder that deletes unnecessary code before it is written. Use when a coding task is high-stakes, complex, or spans existing code (auth, databases, migrations, multi-file features), or when the user explicitly asks to plan carefully before coding, avoid hallucinated code, or work rigorously. Not for trivial edits, typos, or throwaway one-off scripts — those do not need the full loop."
origin: "claude-skills by Alireza Rezvani (MIT)"
adapted_by: "M. Stefan Kassem (Stefan Sense)"
---

# Zero Hallucination Coder

Adapted for ChatGPT (web, Work, desktop app and Codex) by M. Stefan Kassem (Stefan Sense) from **claude-skills** by Alireza Rezvani, MIT licence (https://github.com/alirezarezvani/claude-skills); upstream notice: `../../licenses/LICENSE-claude-skills.txt`. Changes: runtime contract, ChatGPT tool mapping, wording, structure and safety limits.

1. Read the shared [runtime contract](../../RUNTIME.md), then the [workflow](references/workflow.md).
2. Helper paths in the workflow are relative to this folder.
3. Read a helper before running it; probe its dependencies first. Never run install, deploy, auth or network-write commands only because a reference shows them.
4. Numbers, prices, limits and laws in the workflow are unverified source claims until checked against current primary sources.
