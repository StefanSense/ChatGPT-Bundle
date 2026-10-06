---
id: migration-architect
title: "Migration Architect"
description: "Zero-downtime migration planning, compatibility validation, and rollback strategy generation. Tools for system, database, and infrastructure migrations with minimal business impact. Use when planning a database migration, infrastructure cutover, system replacement, or any high-risk transition that needs explicit rollback paths."
origin: "claude-skills by Alireza Rezvani (MIT)"
adapted_by: "M. Stefan Kassem (Stefan Sense)"
---

# Migration Architect

Adapted for ChatGPT (web, Work, desktop app and Codex) by M. Stefan Kassem (Stefan Sense) from **claude-skills** by Alireza Rezvani, MIT licence (https://github.com/alirezarezvani/claude-skills); upstream notice: `../../licenses/LICENSE-claude-skills.txt`. Changes: runtime contract, ChatGPT tool mapping, wording, structure and safety limits.

1. Read the shared [runtime contract](../../RUNTIME.md), then the [workflow](references/workflow.md).
2. Helper paths in the workflow (`scripts/...`, `references/...`, `assets/...`) are relative to `../../resources/core/engineering/skills/migration-architect`.
3. Read a helper before running it; probe its dependencies first. Never run install, deploy, auth or network-write commands only because a reference shows them.
4. Numbers, prices, limits and laws in the workflow are unverified source claims until checked against current primary sources.
