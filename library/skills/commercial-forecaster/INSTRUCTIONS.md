---
id: commercial-forecaster
title: "Commercial Forecaster"
description: "Use when building a quarterly bookings forecast, ARR projection, pipeline forecast, NRR projection, or commit/best-case/pipe-only board number — especially when the CRO needs to walk the board through funnel math + cohort ARR + per-stage conversion assumptions without the theatre of a single undefended number. Decomposes pipeline into commit, best-case, and pipe-only tiers; projects cohort-level NRR/GRR to surface leaky cohorts before they show up in the consolidated number; scores per-stage funnel confidence so soft-floor stages get treated differently from high-confidence ones. Every output explicitly names the conversion rate used, the data window, and the weighting choice. For Head of Commercial, RevOps, VP Sales, and CRO at quarterly forecast or board prep. NOT financial close (see finance/financial-analysis). NOT strategic CRO hiring/territory (see c-level-advisor/cro-advisor)."
origin: "claude-skills by Alireza Rezvani (MIT)"
adapted_by: "M. Stefan Kassem (Stefan Sense)"
---

# Commercial Forecaster

Adapted for ChatGPT (web, Work, desktop app and Codex) by M. Stefan Kassem (Stefan Sense) from **claude-skills** by Alireza Rezvani, MIT licence (https://github.com/alirezarezvani/claude-skills); upstream notice: `../../licenses/LICENSE-claude-skills.txt`. Changes: runtime contract, ChatGPT tool mapping, wording, structure and safety limits.

1. Read the shared [runtime contract](../../RUNTIME.md), then the [workflow](references/workflow.md).
2. Helper paths in the workflow (`scripts/...`, `references/...`, `assets/...`) are relative to `../../resources/core/commercial/skills/commercial-forecaster`.
3. Read a helper before running it; probe its dependencies first. Never run install, deploy, auth or network-write commands only because a reference shows them.
4. Numbers, prices, limits and laws in the workflow are unverified source claims until checked against current primary sources.
