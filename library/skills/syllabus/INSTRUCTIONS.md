---
id: syllabus
title: "Syllabus"
description: "Generates a curated supplementary reading list from any course syllabus using Consensus academic search. Grill-me intake (syllabus input format + course audience + year range) plus a grouping forcing-options checkpoint before any search runs — so the reading list matches the course's level and recency need. Parses the syllabus to extract topics and learning outcomes, searches Consensus for recent peer-reviewed papers per topic, and produces a professionally formatted .docx with clickable Consensus links, plain-language summaries calibrated to audience level, and Bloom-higher-order discussion questions tied to course learning goals. Use when the user uploads a syllabus, course outline, or curriculum document and wants supplementary readings (e.g., 'create a reading list from this syllabus', 'find recent papers for my course') — even casual mentions with a syllabus attached should trigger"
origin: "claude-skills by Alireza Rezvani (MIT)"
adapted_by: "M. Stefan Kassem (Stefan Sense)"
---

# Syllabus

Adapted for ChatGPT (web, Work, desktop app and Codex) by M. Stefan Kassem (Stefan Sense) from **claude-skills** by Alireza Rezvani, MIT licence (https://github.com/alirezarezvani/claude-skills); upstream notice: `../../licenses/LICENSE-claude-skills.txt`. Changes: runtime contract, ChatGPT tool mapping, wording, structure and safety limits.

1. Read the shared [runtime contract](../../RUNTIME.md), then the [workflow](references/workflow.md).
2. Helper paths in the workflow (`scripts/...`, `references/...`, `assets/...`) are relative to `../../resources/core/research/syllabus/skills/syllabus`.
3. Read a helper before running it; probe its dependencies first. Never run install, deploy, auth or network-write commands only because a reference shows them.
4. Numbers, prices, limits and laws in the workflow are unverified source claims until checked against current primary sources.
