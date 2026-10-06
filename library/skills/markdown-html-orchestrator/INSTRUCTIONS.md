---
id: markdown-html-orchestrator
title: "Markdown HTML Orchestrator"
description: "Use when a user wants to convert any markdown file in their the assistant project into a single-file, lightly-interactive HTML — long-form documents (specs, plans, RFCs, reports, explainers), code reviews with diffs and severity-tagged annotations, or slide decks. Triggers on \"convert this markdown to HTML\", \"make this an HTML file\", \"turn this into an interactive document\", \"render this report as HTML\", \"PR writeup as HTML\", \"slides from this markdown\". Forks context to route to one of three converter sub-skills (md-document, md-review, md-slides) based on a deterministic doctype classifier, after the user has run the design-system onboarding once. Refuses if input is under 100 lines (per Shihipar — markdown still wins below the threshold) or design-system isn't onboarded. Distinct from the original publisher's official Playground plugin (which is interactive prompt-tuning controls"
origin: "claude-skills by Alireza Rezvani (MIT)"
adapted_by: "M. Stefan Kassem (Stefan Sense)"
---

# Markdown HTML Orchestrator

Adapted for ChatGPT (web, Work, desktop app and Codex) by M. Stefan Kassem (Stefan Sense) from **claude-skills** by Alireza Rezvani, MIT licence (https://github.com/alirezarezvani/claude-skills); upstream notice: `../../licenses/LICENSE-claude-skills.txt`. Changes: runtime contract, ChatGPT tool mapping, wording, structure and safety limits.

1. Read the shared [runtime contract](../../RUNTIME.md), then the [workflow](references/workflow.md).
2. Helper paths in the workflow (`scripts/...`, `references/...`, `assets/...`) are relative to `../../resources/core/markdown-html/skills/markdown-html-orchestrator`.
3. Read a helper before running it; probe its dependencies first. Never run install, deploy, auth or network-write commands only because a reference shows them.
4. Numbers, prices, limits and laws in the workflow are unverified source claims until checked against current primary sources.
