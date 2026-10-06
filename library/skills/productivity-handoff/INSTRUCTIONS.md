---
id: productivity-handoff
title: "Productivity Handoff"
description: "Compact the current conversation into a handoff document for another agent to pick up. Save to a user-configured location (OS temp, home folder, or per-project .handoff/), redact secrets before write, suggest skills for the next session, and auto-load the latest handoff on the next SessionStart. First-run setup asks where to save so the project folder never gets cluttered. Use when the user says 'hand this off', 'handoff doc', 'summarize this for a new session', 'compact this conversation', 'I'm ending this session', 'pick this up later', or any variation signaling intent to pass work to a fresh agent. Also trigger on implicit signals: the user announcing they're switching machines, ending the day mid-task, or context is growing long without a natural stopping point."
origin: "claude-skills by Alireza Rezvani (MIT)"
adapted_by: "M. Stefan Kassem (Stefan Sense)"
---

# Productivity Handoff

Adapted for ChatGPT (web, Work, desktop app and Codex) by M. Stefan Kassem (Stefan Sense) from **claude-skills** by Alireza Rezvani, MIT licence (https://github.com/alirezarezvani/claude-skills); upstream notice: `../../licenses/LICENSE-claude-skills.txt`. Changes: runtime contract, ChatGPT tool mapping, wording, structure and safety limits.

1. Read the shared [runtime contract](../../RUNTIME.md), then the [workflow](references/workflow.md).
2. Helper paths in the workflow (`scripts/...`, `references/...`, `assets/...`) are relative to `../../resources/core/productivity/handoff/skills/handoff`.
3. Read a helper before running it; probe its dependencies first. Never run install, deploy, auth or network-write commands only because a reference shows them.
4. Numbers, prices, limits and laws in the workflow are unverified source claims until checked against current primary sources.
