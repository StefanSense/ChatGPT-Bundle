---
id: agent-harness
title: "Agent Harness"
description: "Turn any domain folder of skills into a bounded agentic loop: compile a goal into a verifiable task plan, execute tasks with the domain's own tools, verify every task with machine-run checks, retry with caps, escalate to a human when budgets exhaust, and refuse to close until everything is verified or explicitly waived. Use when you want an agent or subagent to pick up a goal and drive it to a verified close across one of this repo's 18 domains ('run this goal through the engineering harness', 'set up an agentic loop for marketing work', 'make the finance domain self-verifying'). NOT for authoring ChatGPT Workflow-tool .js scripts (workflow-builder), N-agent tournaments on one task (agenthub), single-file metric optimization (autoresearch-agent), or discovering published loop recipes (loop-library)."
origin: "claude-skills by Alireza Rezvani (MIT)"
adapted_by: "M. Stefan Kassem (Stefan Sense)"
---

# Agent Harness

Adapted for ChatGPT (web, Work, desktop app and Codex) by M. Stefan Kassem (Stefan Sense) from **claude-skills** by Alireza Rezvani, MIT licence (https://github.com/alirezarezvani/claude-skills); upstream notice: `../../licenses/LICENSE-claude-skills.txt`. Changes: runtime contract, ChatGPT tool mapping, wording, structure and safety limits.

1. Read the shared [runtime contract](../../RUNTIME.md), then the [workflow](references/workflow.md).
2. Helper paths in the workflow (`scripts/...`, `references/...`, `assets/...`) are relative to `../../resources/core/engineering/agent-harness/skills/agent-harness`.
3. Read a helper before running it; probe its dependencies first. Never run install, deploy, auth or network-write commands only because a reference shows them.
4. Numbers, prices, limits and laws in the workflow are unverified source claims until checked against current primary sources.
