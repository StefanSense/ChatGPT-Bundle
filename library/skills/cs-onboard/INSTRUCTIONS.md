---
id: cs-onboard
title: "Cs Onboard"
description: "Founder onboarding interview that captures company context across 7 dimensions. Invoke with ar-setup for initial interview or update for quarterly refresh. Generates .agents/company-context.md used by all C-suite advisor skills. Use when setting up the C-suite advisors for the first time, or when company context is missing or more than 90 days old — e.g. after a fundraise or pivot."
origin: "claude-skills by Alireza Rezvani (MIT)"
adapted_by: "M. Stefan Kassem (Stefan Sense)"
---

# Cs Onboard

Adapted for ChatGPT (web, Work, desktop app and Codex) by M. Stefan Kassem (Stefan Sense) from **claude-skills** by Alireza Rezvani, MIT licence (https://github.com/alirezarezvani/claude-skills); upstream notice: `../../licenses/LICENSE-claude-skills.txt`. Changes: runtime contract, ChatGPT tool mapping, wording, structure and safety limits.

1. Read the shared [runtime contract](../../RUNTIME.md), then the [workflow](references/workflow.md).
2. Helper paths in the workflow (`scripts/...`, `references/...`, `assets/...`) are relative to `../../resources/core/c-level-advisor/skills/cs-onboard`.
3. Read a helper before running it; probe its dependencies first. Never run install, deploy, auth or network-write commands only because a reference shows them.
4. Numbers, prices, limits and laws in the workflow are unverified source claims until checked against current primary sources.
