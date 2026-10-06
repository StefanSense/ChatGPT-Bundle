---
id: pm-skills
title: "PM Skills"
description: "Use when coordinating project-delivery work across the 8 project-management sub-skills — sprint/velocity analytics, portfolio health, Jira/JQL, Confluence, Atlassian admin, templates, meeting analysis, team comms. Triggers on 'our sprints feel off', 'project health report', 'audit our Jira permissions', 'when will it be done', 'run the delivery loop'. Forks context to route to one sub-skill via a deterministic signal router and returns a digest; can also drive a full goal→plan→execute→verify→close delivery loop through the repo-wide agent-harness with Jira MCP data bridged into the domain's analytics tools. Distinct from product-team (what to build vs how to deliver it), business-operations (internal ops), and engineering/agent-harness (the generic loop engine this orchestrator plugs into)."
origin: "claude-skills by Alireza Rezvani (MIT)"
adapted_by: "M. Stefan Kassem (Stefan Sense)"
---

# PM Skills

Adapted for ChatGPT (web, Work, desktop app and Codex) by M. Stefan Kassem (Stefan Sense) from **claude-skills** by Alireza Rezvani, MIT licence (https://github.com/alirezarezvani/claude-skills); upstream notice: `../../licenses/LICENSE-claude-skills.txt`. Changes: runtime contract, ChatGPT tool mapping, wording, structure and safety limits.

1. Read the shared [runtime contract](../../RUNTIME.md), then the [workflow](references/workflow.md).
2. Helper paths in the workflow (`scripts/...`, `references/...`, `assets/...`) are relative to `../../resources/core/project-management/skills/pm-skills`.
3. Read a helper before running it; probe its dependencies first. Never run install, deploy, auth or network-write commands only because a reference shows them.
4. Numbers, prices, limits and laws in the workflow are unverified source claims until checked against current primary sources.
