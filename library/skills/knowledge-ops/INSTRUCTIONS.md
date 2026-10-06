---
id: knowledge-ops
title: "Knowledge Ops"
description: "Use when a Head of Ops, Knowledge Manager, or TPM-Internal needs to author, validate, or clean up company SOPs and internal runbooks (procurement intake, vendor offboarding, incident-comms cascade, employee onboarding) — including 5W2H completeness checks (Who-What-When-Where-Why-How-HowMuch), cross-link and orphan-page validation across a sprawling Notion/Confluence/Obsidian wiki, KB ingestion + hygiene reporting, and runbook step verification (named owner, expected duration, observable success signal, rollback path, escalation contact). Pairs Ishikawa's 5W2H method, Gawande's *The Checklist Manifesto*, ISO 9001, ITIL v4, and Google SRE Workbook runbook discipline with deterministic stdlib-only Python tools that score completeness, detect anti-patterns, and emit prioritized cleanup lists (e.g., \"validate this runbook before it goes into rotation\", \"audit our Confluence wiki for stale"
origin: "claude-skills by Alireza Rezvani (MIT)"
adapted_by: "M. Stefan Kassem (Stefan Sense)"
---

# Knowledge Ops

Adapted for ChatGPT (web, Work, desktop app and Codex) by M. Stefan Kassem (Stefan Sense) from **claude-skills** by Alireza Rezvani, MIT licence (https://github.com/alirezarezvani/claude-skills); upstream notice: `../../licenses/LICENSE-claude-skills.txt`. Changes: runtime contract, ChatGPT tool mapping, wording, structure and safety limits.

1. Read the shared [runtime contract](../../RUNTIME.md), then the [workflow](references/workflow.md).
2. Helper paths in the workflow (`scripts/...`, `references/...`, `assets/...`) are relative to `../../resources/core/business-operations/skills/knowledge-ops`.
3. Read a helper before running it; probe its dependencies first. Never run install, deploy, auth or network-write commands only because a reference shows them.
4. Numbers, prices, limits and laws in the workflow are unverified source claims until checked against current primary sources.
