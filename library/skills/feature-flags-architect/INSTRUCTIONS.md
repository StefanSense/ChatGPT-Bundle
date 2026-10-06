---
id: feature-flags-architect
title: "Feature Flags Architect"
description: "Use when adding, retiring, or auditing feature flags. Triggers on \"add a flag\", \"ship behind a flag\", \"rollout plan\", \"kill switch\", \"stale flags\", \"flag debt\", \"LaunchDarkly\", \"GrowthBook\", \"Statsig\", \"Unleash\", \"Flipt\", or any progressive-delivery question. Ships flag debt scanner, rollout planner, and kill-switch auditor (all stdlib Python), 4 references on flag taxonomy + provider trade-offs + rollout strategies + lifecycle, plus a /flag-cleanup slash command."
origin: "claude-skills by Alireza Rezvani (MIT)"
adapted_by: "M. Stefan Kassem (Stefan Sense)"
---

# Feature Flags Architect

Adapted for ChatGPT (web, Work, desktop app and Codex) by M. Stefan Kassem (Stefan Sense) from **claude-skills** by Alireza Rezvani, MIT licence (https://github.com/alirezarezvani/claude-skills); upstream notice: `../../licenses/LICENSE-claude-skills.txt`. Changes: runtime contract, ChatGPT tool mapping, wording, structure and safety limits.

1. Read the shared [runtime contract](../../RUNTIME.md), then the [workflow](references/workflow.md).
2. Helper paths in the workflow (`scripts/...`, `references/...`, `assets/...`) are relative to `../../resources/core/engineering/feature-flags-architect/skills/feature-flags-architect`.
3. Read a helper before running it; probe its dependencies first. Never run install, deploy, auth or network-write commands only because a reference shows them.
4. Numbers, prices, limits and laws in the workflow are unverified source claims until checked against current primary sources.
