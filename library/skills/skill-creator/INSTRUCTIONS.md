---
id: skill-creator
title: "Skill Creator"
description: "Create new skills, modify and improve existing skills, and measure skill performance. Use when users want to create a skill from scratch, edit, or optimize an existing skill, run evals to test a skill, benchmark skill performance with variance analysis, or optimize a skill's description for better triggering accuracy."
origin: "anthropics/skills (example skills) by Anthropic, PBC (Apache-2.0)"
adapted_by: "M. Stefan Kassem (Stefan Sense)"
---

# Skill Creator

Adapted for ChatGPT (web, Work, desktop app and Codex) by M. Stefan Kassem (Stefan Sense) from **anthropics/skills (example skills)** by Anthropic, PBC, Apache-2.0 licence (https://github.com/anthropics/skills); upstream notice: `../../licenses/LICENSE-Apache-2.0.txt`. Changes: runtime contract, ChatGPT tool mapping, wording, structure and safety limits.

1. Read the shared [runtime contract](../../RUNTIME.md), then the [workflow](references/workflow.md).
2. Helper paths in the workflow (`scripts/...`, `references/...`, `assets/...`) are relative to `../../resources/docs/skills/skill-creator`.
3. Read a helper before running it; probe its dependencies first. Never run install, deploy, auth or network-write commands only because a reference shows them.
4. Numbers, prices, limits and laws in the workflow are unverified source claims until checked against current primary sources.
