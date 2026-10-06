---
id: spec-to-repo
title: "Spec To Repo"
description: "Use when the user says 'build me an app', 'create a project from this spec', 'scaffold a new repo', 'generate a starter', 'turn this idea into code', 'bootstrap a project', 'I have requirements and need a codebase', or provides a natural-language project specification and expects a complete, runnable repository. Stack-agnostic: Next.js, FastAPI, Rails, Go, Rust, Flutter, and more."
origin: "claude-skills by Alireza Rezvani (MIT)"
adapted_by: "M. Stefan Kassem (Stefan Sense)"
---

# Spec To Repo

Adapted for ChatGPT (web, Work, desktop app and Codex) by M. Stefan Kassem (Stefan Sense) from **claude-skills** by Alireza Rezvani, MIT licence (https://github.com/alirezarezvani/claude-skills); upstream notice: `../../licenses/LICENSE-claude-skills.txt`. Changes: runtime contract, ChatGPT tool mapping, wording, structure and safety limits.

1. Read the shared [runtime contract](../../RUNTIME.md), then the [workflow](references/workflow.md).
2. Helper paths in the workflow (`scripts/...`, `references/...`, `assets/...`) are relative to `../../resources/core/product-team/skills/spec-to-repo`.
3. Read a helper before running it; probe its dependencies first. Never run install, deploy, auth or network-write commands only because a reference shows them.
4. Numbers, prices, limits and laws in the workflow are unverified source claims until checked against current primary sources.
