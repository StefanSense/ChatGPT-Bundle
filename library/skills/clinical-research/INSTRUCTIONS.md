---
id: clinical-research
title: "Clinical Research"
description: "Use when designing a prospective clinical study before submission — selecting and classifying endpoints (primary / key-secondary / exploratory, with surrogate-endpoint flagging), estimating sample size and power for two-arm designs (means / proportions / survival), or scoring a study plan for feasibility and a GO / GO-WITH-CONDITIONS / REDESIGN / NO-GO phase-gate decision. Every output is an ESTIMATE plus a named human owner (clinician / biostatistician / regulatory owner) — never clinical fact, never a finished protocol. Distinct from ra-qm-team, which handles the regulatory/QM submission (ISO 13485, EU MDR, FDA 510(k)/PMA/QSR), not the study design."
origin: "claude-skills by Alireza Rezvani (MIT)"
adapted_by: "M. Stefan Kassem (Stefan Sense)"
---

# Clinical Research

Adapted for ChatGPT (web, Work, desktop app and Codex) by M. Stefan Kassem (Stefan Sense) from **claude-skills** by Alireza Rezvani, MIT licence (https://github.com/alirezarezvani/claude-skills); upstream notice: `../../licenses/LICENSE-claude-skills.txt`. Changes: runtime contract, ChatGPT tool mapping, wording, structure and safety limits.

1. Read the shared [runtime contract](../../RUNTIME.md), then the [workflow](references/workflow.md).
2. Helper paths in the workflow (`scripts/...`, `references/...`, `assets/...`) are relative to `../../resources/core/research-ops/skills/clinical-research`.
3. Read a helper before running it; probe its dependencies first. Never run install, deploy, auth or network-write commands only because a reference shows them.
4. Numbers, prices, limits and laws in the workflow are unverified source claims until checked against current primary sources.
