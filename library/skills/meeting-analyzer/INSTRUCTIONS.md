---
id: meeting-analyzer
title: "Meeting Analyzer"
description: "Analyzes meeting transcripts and recordings to surface behavioral patterns, communication anti-patterns, and actionable coaching feedback. Use this skill whenever the user uploads or points to meeting transcripts (.txt, .md, .vtt, .srt, .docx), asks about their communication habits, wants feedback on how they run meetings, requests speaking ratio analysis, mentions filler words or conflict avoidance, or wants to compare their communication across time periods. Also trigger when users mention tools like Granola, Otter, Fireflies, or Zoom transcripts. Even if the user just says \"look at my meetings\" or \"how do I come across in meetings\" — use this skill."
origin: "claude-skills by Alireza Rezvani (MIT)"
adapted_by: "M. Stefan Kassem (Stefan Sense)"
---

# Meeting Analyzer

Adapted for ChatGPT (web, Work, desktop app and Codex) by M. Stefan Kassem (Stefan Sense) from **claude-skills** by Alireza Rezvani, MIT licence (https://github.com/alirezarezvani/claude-skills); upstream notice: `../../licenses/LICENSE-claude-skills.txt`. Changes: runtime contract, ChatGPT tool mapping, wording, structure and safety limits.

1. Read the shared [runtime contract](../../RUNTIME.md), then the [workflow](references/workflow.md).
2. Helper paths in the workflow are relative to this folder.
3. Read a helper before running it; probe its dependencies first. Never run install, deploy, auth or network-write commands only because a reference shows them.
4. Numbers, prices, limits and laws in the workflow are unverified source claims until checked against current primary sources.
