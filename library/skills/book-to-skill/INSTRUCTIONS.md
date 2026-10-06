---
id: book-to-skill
title: "Book To Skill"
description: "Converts books, documentation folders, and source collections (PDF, EPUB, DOCX, HTML, Markdown, RST, AsciiDoc, RTF, MOBI/AZW) into structured agent skills — extracting named frameworks, principles, techniques, and anti-patterns into a master SKILL.md plus on-demand chapter files, a glossary, a patterns file, and a decision cheatsheet. Use when the user wants to study a document with an agent, apply an author's frameworks while working, turn internal docs or standards into a reusable knowledge base, or package a compiled book skill as a claude-skills plugin."
origin: "claude-skills by Alireza Rezvani (MIT)"
adapted_by: "M. Stefan Kassem (Stefan Sense)"
---

# Book To Skill

Adapted for ChatGPT (web, Work, desktop app and Codex) by M. Stefan Kassem (Stefan Sense) from **claude-skills** by Alireza Rezvani, MIT licence (https://github.com/alirezarezvani/claude-skills); upstream notice: `../../licenses/LICENSE-claude-skills.txt`. Changes: runtime contract, ChatGPT tool mapping, wording, structure and safety limits.

1. Read the shared [runtime contract](../../RUNTIME.md), then the [workflow](references/workflow.md).
2. Helper paths in the workflow (`scripts/...`, `references/...`, `assets/...`) are relative to `../../resources/core/engineering/book-to-skill/skills/book-to-skill`.
3. Read a helper before running it; probe its dependencies first. Never run install, deploy, auth or network-write commands only because a reference shows them.
4. Numbers, prices, limits and laws in the workflow are unverified source claims until checked against current primary sources.
