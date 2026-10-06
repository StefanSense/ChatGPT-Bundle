---
id: deal-desk
title: "Deal Desk"
description: "Use when reviewing a specific inbound deal before close — when sales has asked for a discount that exceeds AE authority, when the customer has redlined the MSA, when per-deal economics (margin after discount, multi-year payment shape, indemnity exposure) need to be quantified, or when discount approval needs to be routed to a named human approver (Sales Director, VP Sales, CFO, CRO, General Counsel). Covers deal review, discount approval routing, per-deal margin scoring, deal exception handling, MSA redline triage, contract landmine detection (uncapped indemnity, MFN, perpetual license-back, missing DPA), and named-approver chain assembly. NEVER auto-approves — every output is a numeric scorecard plus a routing recommendation to a named human."
origin: "claude-skills by Alireza Rezvani (MIT)"
adapted_by: "M. Stefan Kassem (Stefan Sense)"
---

# Deal Desk

Adapted for ChatGPT (web, Work, desktop app and Codex) by M. Stefan Kassem (Stefan Sense) from **claude-skills** by Alireza Rezvani, MIT licence (https://github.com/alirezarezvani/claude-skills); upstream notice: `../../licenses/LICENSE-claude-skills.txt`. Changes: runtime contract, ChatGPT tool mapping, wording, structure and safety limits.

1. Read the shared [runtime contract](../../RUNTIME.md), then the [workflow](references/workflow.md).
2. Helper paths in the workflow (`scripts/...`, `references/...`, `assets/...`) are relative to `../../resources/core/commercial/skills/deal-desk`.
3. Read a helper before running it; probe its dependencies first. Never run install, deploy, auth or network-write commands only because a reference shows them.
4. Numbers, prices, limits and laws in the workflow are unverified source claims until checked against current primary sources.
