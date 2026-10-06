---
id: md-slides
title: "MD Slides"
description: "Converts a markdown deck (slides separated by `---` HR boundaries or by `# ` H1 headings, with optional `!-- notes: ... --` presenter notes blocks) into a single-file HTML presentation with arrow-key / space / PgDn / PgUp / Home / End / P / Esc keyboard navigation, presenter mode (split view with current slide + speaker notes + clock + next-slide preview), URL-hash deep linking, and `@media print` page-per-slide for PDF export. Triggers when the markdown-html-orchestrator classifies an input as SLIDES, or when invoked directly via md-slides. Reuses md-document's markdown parser for slide-body rendering and reads design-system tokens via config_loader.py. Refuses if input has no clear slide boundaries, produces a 1-slide deck, or `--strict-notes` is on with  50% notes coverage. Use after orchestrator routing."
origin: "claude-skills by Alireza Rezvani (MIT)"
adapted_by: "M. Stefan Kassem (Stefan Sense)"
---

# MD Slides

Adapted for ChatGPT (web, Work, desktop app and Codex) by M. Stefan Kassem (Stefan Sense) from **claude-skills** by Alireza Rezvani, MIT licence (https://github.com/alirezarezvani/claude-skills); upstream notice: `../../licenses/LICENSE-claude-skills.txt`. Changes: runtime contract, ChatGPT tool mapping, wording, structure and safety limits.

1. Read the shared [runtime contract](../../RUNTIME.md), then the [workflow](references/workflow.md).
2. Helper paths in the workflow (`scripts/...`, `references/...`, `assets/...`) are relative to `../../resources/core/markdown-html/skills/md-slides`.
3. Read a helper before running it; probe its dependencies first. Never run install, deploy, auth or network-write commands only because a reference shows them.
4. Numbers, prices, limits and laws in the workflow are unverified source claims until checked against current primary sources.
