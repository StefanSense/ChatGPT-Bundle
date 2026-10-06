---
id: human-gate
title: "Human Gate"
description: "Runs the human-verification lane of an agent loop, and proves review happened before work is called done. Builds a single-file HTML review page, collects batched feedback as a structured artifact instead of chat prose, and runs a gate that refuses to close while a BLOCKER is open, the reviewer is unnamed, or nobody has reviewed at all. Use when a plan, spec, RFC, report, landing page, migration, or any irreversible action needs human sign-off before shipping, or on requests such as 'get sign-off', 'have someone check this', 'hold until reviewed', 'needs approval first'. NOT for making AI text sound human (use content-humanizer or behuman). NOT for reviewing code diffs (use md-review or code-reviewer)."
origin: "claude-skills by Alireza Rezvani (MIT)"
adapted_by: "M. Stefan Kassem (Stefan Sense)"
---

# Human Gate

Adapted for ChatGPT (web, Work, desktop app and Codex) by M. Stefan Kassem (Stefan Sense) from **claude-skills** by Alireza Rezvani, MIT licence (https://github.com/alirezarezvani/claude-skills); upstream notice: `../../licenses/LICENSE-claude-skills.txt`. Changes: runtime contract, ChatGPT tool mapping, wording, structure and safety limits.

1. Read the shared [runtime contract](../../RUNTIME.md), then the [workflow](references/workflow.md).
2. Helper paths in the workflow (`scripts/...`, `references/...`, `assets/...`) are relative to `../../resources/core/engineering/human-gate/skills/human-gate`.
3. Read a helper before running it; probe its dependencies first. Never run install, deploy, auth or network-write commands only because a reference shows them.
4. Numbers, prices, limits and laws in the workflow are unverified source claims until checked against current primary sources.
