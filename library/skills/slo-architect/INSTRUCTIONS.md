---
id: slo-architect
title: "SLO Architect"
description: "Use when defining, reviewing, or operating SLOs/SLIs/error budgets. Triggers on \"define an SLO\", \"what should our SLO be\", \"error budget\", \"burn rate\", \"SLI\", \"service level objective\", \"Google SRE workbook\", \"multi-window burn-rate alert\", or any reliability-target question. Ships SLO designer, error-budget calculator with multi-window burn-rate thresholds, and SLO reviewer that catches the common bugs (target too aggressive, window too short, conflicting SLOs, no SLI definition). 4 references on SLO principles + SLI design + error budget math + composition with feature-flags-architect/chaos-engineering/kubernetes-operator. NOT a generic observability skill — specifically the SLO discipline."
origin: "claude-skills by Alireza Rezvani (MIT)"
adapted_by: "M. Stefan Kassem (Stefan Sense)"
---

# SLO Architect

Adapted for ChatGPT (web, Work, desktop app and Codex) by M. Stefan Kassem (Stefan Sense) from **claude-skills** by Alireza Rezvani, MIT licence (https://github.com/alirezarezvani/claude-skills); upstream notice: `../../licenses/LICENSE-claude-skills.txt`. Changes: runtime contract, ChatGPT tool mapping, wording, structure and safety limits.

1. Read the shared [runtime contract](../../RUNTIME.md), then the [workflow](references/workflow.md).
2. Helper paths in the workflow (`scripts/...`, `references/...`, `assets/...`) are relative to `../../resources/core/engineering/skills/slo-architect`.
3. Read a helper before running it; probe its dependencies first. Never run install, deploy, auth or network-write commands only because a reference shows them.
4. Numbers, prices, limits and laws in the workflow are unverified source claims until checked against current primary sources.
