---
id: process-mapper
title: "Process Mapper"
description: "Use when a BizOps lead, COO, or process-improvement owner needs to document an end-to-end business process (procurement, employee onboarding, incident handoff, customer-onboarding, claims adjudication) in BPMN-style notation, measure cycle times by stage, surface where work spends most of its time waiting vs. being worked, and quantify the gap between processing time and total elapsed time. Pairs Lean / Six Sigma / Theory-of-Constraints canon with deterministic stdlib-only Python tools to produce a process map, a ranked bottleneck list (with severity + root-cause hypothesis), and a cycle-time analysis (P50, P90, value-add ratio, Little's-Law throughput). Distinct from sales-pipeline, system-reliability (SLO), and strategic-OKR work — this is tactical process documentation for internal operations."
origin: "claude-skills by Alireza Rezvani (MIT)"
adapted_by: "M. Stefan Kassem (Stefan Sense)"
---

# Process Mapper

Adapted for ChatGPT (web, Work, desktop app and Codex) by M. Stefan Kassem (Stefan Sense) from **claude-skills** by Alireza Rezvani, MIT licence (https://github.com/alirezarezvani/claude-skills); upstream notice: `../../licenses/LICENSE-claude-skills.txt`. Changes: runtime contract, ChatGPT tool mapping, wording, structure and safety limits.

1. Read the shared [runtime contract](../../RUNTIME.md), then the [workflow](references/workflow.md).
2. Helper paths in the workflow (`scripts/...`, `references/...`, `assets/...`) are relative to `../../resources/core/business-operations/skills/process-mapper`.
3. Read a helper before running it; probe its dependencies first. Never run install, deploy, auth or network-write commands only because a reference shows them.
4. Numbers, prices, limits and laws in the workflow are unverified source claims until checked against current primary sources.
