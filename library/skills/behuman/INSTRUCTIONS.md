---
id: behuman
title: "Behuman"
description: "Use when the user wants more human-like AI responses — less robotic, less listy, more authentic. Triggers: 'behuman', 'be real', 'like a human', 'more human', 'less AI', 'talk like a person', 'mirror mode', 'stop being so AI', or when conversations are emotionally charged (grief, job loss, relationship advice, fear). NOT for technical questions, code generation, or factual lookups."
origin: "claude-skills by Alireza Rezvani (MIT)"
adapted_by: "M. Stefan Kassem (Stefan Sense)"
---

# Behuman

Adapted for ChatGPT (web, Work, desktop app and Codex) by M. Stefan Kassem (Stefan Sense) from **claude-skills** by Alireza Rezvani, MIT licence (https://github.com/alirezarezvani/claude-skills); upstream notice: `../../licenses/LICENSE-claude-skills.txt`. Changes: runtime contract, ChatGPT tool mapping, wording, structure and safety limits.

1. Read the shared [runtime contract](../../RUNTIME.md), then the [workflow](references/workflow.md).
2. Helper paths in the workflow (`scripts/...`, `references/...`, `assets/...`) are relative to `../../resources/core/engineering/behuman/skills/behuman`.
3. Read a helper before running it; probe its dependencies first. Never run install, deploy, auth or network-write commands only because a reference shows them.
4. Numbers, prices, limits and laws in the workflow are unverified source claims until checked against current primary sources.
