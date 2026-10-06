---
id: observability-designer
title: "Observability Designer"
description: "Design production-ready observability strategies combining metrics, logs, and traces. Includes SLI/SLO design, golden-signals monitoring, alert optimization. Use when adding observability to a new service, refactoring alerting that is too noisy, or designing an SLO program before scaling production load."
origin: "claude-skills by Alireza Rezvani (MIT)"
adapted_by: "M. Stefan Kassem (Stefan Sense)"
---

# Observability Designer

Adapted for ChatGPT (web, Work, desktop app and Codex) by M. Stefan Kassem (Stefan Sense) from **claude-skills** by Alireza Rezvani, MIT licence (https://github.com/alirezarezvani/claude-skills); upstream notice: `../../licenses/LICENSE-claude-skills.txt`. Changes: runtime contract, ChatGPT tool mapping, wording, structure and safety limits.

1. Read the shared [runtime contract](../../RUNTIME.md), then the [workflow](references/workflow.md).
2. Helper paths in the workflow (`scripts/...`, `references/...`, `assets/...`) are relative to `../../resources/core/engineering/skills/observability-designer`.
3. Read a helper before running it; probe its dependencies first. Never run install, deploy, auth or network-write commands only because a reference shows them.
4. Numbers, prices, limits and laws in the workflow are unverified source claims until checked against current primary sources.
