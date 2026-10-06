---
id: api-connector-builder
title: "API Connector Builder"
description: "Build a new API connector or provider by matching the target repo's existing integration pattern exactly. Use when adding one more integration without inventing a second architecture."
origin: "everything-claude-code (ECC) by Affaan Mustafa (MIT)"
adapted_by: "M. Stefan Kassem (Stefan Sense)"
---

# API Connector Builder

Adapted for ChatGPT (web, Work, desktop app and Codex) by M. Stefan Kassem (Stefan Sense) from **everything-claude-code (ECC)** by Affaan Mustafa, MIT licence (https://github.com/affaan-m/everything-claude-code); upstream notice: `../../licenses/LICENSE-everything-claude-code.txt`. Changes: runtime contract, ChatGPT tool mapping, wording, structure and safety limits.

1. Read the shared [runtime contract](../../RUNTIME.md), then the [workflow](references/workflow.md).
2. Helper paths in the workflow are relative to this folder.
3. Read a helper before running it; probe its dependencies first. Never run install, deploy, auth or network-write commands only because a reference shows them.
4. Numbers, prices, limits and laws in the workflow are unverified source claims until checked against current primary sources.
