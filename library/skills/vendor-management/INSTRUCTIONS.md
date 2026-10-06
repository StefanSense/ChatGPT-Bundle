---
id: vendor-management
title: "Vendor Management"
description: "Use when reviewing, scoring, or auditing third-party SaaS / vendor relationships — running a vendor scorecard with industry tuning, tracking SLA compliance with credit-claim flags, classifying third-party risk across 4 risk vectors, preparing a tier-1 vendor review, or auditing the SaaS portfolio. Forks context so large vendor catalogs (50-500 line items) and SLA logs don't pollute the parent thread. Triggers on \"vendor SLA\", \"vendor scorecard\", \"third-party risk\", \"TPRM\", \"vendor review\", \"supplier performance\", \"vendor health check\", \"renewal review\"."
origin: "claude-skills by Alireza Rezvani (MIT)"
adapted_by: "M. Stefan Kassem (Stefan Sense)"
---

# Vendor Management

Adapted for ChatGPT (web, Work, desktop app and Codex) by M. Stefan Kassem (Stefan Sense) from **claude-skills** by Alireza Rezvani, MIT licence (https://github.com/alirezarezvani/claude-skills); upstream notice: `../../licenses/LICENSE-claude-skills.txt`. Changes: runtime contract, ChatGPT tool mapping, wording, structure and safety limits.

1. Read the shared [runtime contract](../../RUNTIME.md), then the [workflow](references/workflow.md).
2. Helper paths in the workflow (`scripts/...`, `references/...`, `assets/...`) are relative to `../../resources/core/business-operations/skills/vendor-management`.
3. Read a helper before running it; probe its dependencies first. Never run install, deploy, auth or network-write commands only because a reference shows them.
4. Numbers, prices, limits and laws in the workflow are unverified source claims until checked against current primary sources.
