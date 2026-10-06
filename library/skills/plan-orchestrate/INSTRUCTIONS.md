---
id: plan-orchestrate
title: "Plan Orchestrate"
description: "Read a plan document, decompose it into steps, design a per-step agent chain from the ECC catalogue, and emit ready-to-paste /orchestrate custom prompts. Generative only — never invokes /orchestrate itself. Use when the user has a multi-step plan and wants to drive it through orchestrate without composing chains by hand."
origin: "everything-claude-code (ECC) by Affaan Mustafa (MIT)"
adapted_by: "M. Stefan Kassem (Stefan Sense)"
---

# Plan Orchestrate

Adapted for ChatGPT (web, Work, desktop app and Codex) by M. Stefan Kassem (Stefan Sense) from **everything-claude-code (ECC)** by Affaan Mustafa, MIT licence (https://github.com/affaan-m/everything-claude-code); upstream notice: `../../licenses/LICENSE-everything-claude-code.txt`. Changes: runtime contract, ChatGPT tool mapping, wording, structure and safety limits.

1. Read the shared [runtime contract](../../RUNTIME.md), then the [workflow](references/workflow.md).
2. Helper paths in the workflow are relative to this folder.
3. Read a helper before running it; probe its dependencies first. Never run install, deploy, auth or network-write commands only because a reference shows them.
4. Numbers, prices, limits and laws in the workflow are unverified source claims until checked against current primary sources.
