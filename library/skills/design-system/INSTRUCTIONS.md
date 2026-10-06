---
id: design-system
title: "Design System"
description: "Captures the user's brand identity once via a 10-question onboarding wizard (primary/accent HEX + heading + body Google Fonts + design style editorial/technical/minimal/playful + default output directory + syntax theme + TOC behavior + optional logo/company), validates body-text and link contrast against WCAG 2.2 AA, derives 12 CSS custom properties in HSL space, and stores the result for every markdown-html converter to consume. Use before any markdown-html conversion. Triggers on first-run onboarding (\"set up the brand\", \"configure markdown-html\", \"run onboarding\"), on explicit reset (\"reset the design system\", \"re-onboard\"), and is checked by every converter via config_loader.py before rendering. Refuses to save if body-text contrast fails AA 4.5:1 or the output dir isn't writable. Precedence is project (./.markdown-html/)  global (~/.config/markdown-html/)  built-in defaults;"
origin: "claude-skills by Alireza Rezvani (MIT)"
adapted_by: "M. Stefan Kassem (Stefan Sense)"
---

# Design System

Adapted for ChatGPT (web, Work, desktop app and Codex) by M. Stefan Kassem (Stefan Sense) from **claude-skills** by Alireza Rezvani, MIT licence (https://github.com/alirezarezvani/claude-skills); upstream notice: `../../licenses/LICENSE-claude-skills.txt`. Changes: runtime contract, ChatGPT tool mapping, wording, structure and safety limits.

1. Read the shared [runtime contract](../../RUNTIME.md), then the [workflow](references/workflow.md).
2. Helper paths in the workflow (`scripts/...`, `references/...`, `assets/...`) are relative to `../../resources/core/markdown-html/skills/design-system`.
3. Read a helper before running it; probe its dependencies first. Never run install, deploy, auth or network-write commands only because a reference shows them.
4. Numbers, prices, limits and laws in the workflow are unverified source claims until checked against current primary sources.
