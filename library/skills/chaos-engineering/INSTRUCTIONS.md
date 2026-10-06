---
id: chaos-engineering
title: "Chaos Engineering"
description: "Use when planning, running, or learning from chaos engineering experiments. Triggers on \"chaos experiment\", \"fault injection\", \"gameday\", \"resilience test\", \"blast radius\", \"steady state\", \"abort criteria\", \"Chaos Toolkit\", \"Chaos Mesh\", \"Litmus\", \"Gremlin\", \"AWS FIS\", or any deliberate failure-injection question. Ships experiment designer, blast-radius calculator, and postmortem generator (all stdlib Python), 4 references on chaos principles + experiment design + attack taxonomy + tooling landscape, and a /chaos-experiment slash command. Composes with feature-flags-architect (kill switches as abort triggers) and kubernetes-operator (common chaos targets)."
origin: "claude-skills by Alireza Rezvani (MIT)"
adapted_by: "M. Stefan Kassem (Stefan Sense)"
---

# Chaos Engineering

Adapted for ChatGPT (web, Work, desktop app and Codex) by M. Stefan Kassem (Stefan Sense) from **claude-skills** by Alireza Rezvani, MIT licence (https://github.com/alirezarezvani/claude-skills); upstream notice: `../../licenses/LICENSE-claude-skills.txt`. Changes: runtime contract, ChatGPT tool mapping, wording, structure and safety limits.

1. Read the shared [runtime contract](../../RUNTIME.md), then the [workflow](references/workflow.md).
2. Helper paths in the workflow (`scripts/...`, `references/...`, `assets/...`) are relative to `../../resources/core/engineering/chaos-engineering/skills/chaos-engineering`.
3. Read a helper before running it; probe its dependencies first. Never run install, deploy, auth or network-write commands only because a reference shows them.
4. Numbers, prices, limits and laws in the workflow are unverified source claims until checked against current primary sources.
