---
id: product-skills
title: "Product Skills"
description: "Use when coordinating product work across the 12 bundled product sub-skills (RICE, OKRs, UX research, design tokens, competitive teardown, analytics, experiments, discovery, roadmaps, spec-to-repo, landing pages, SaaS scaffolding) or the 4 standalone product-team plugins (user stories, Apple HIG, code-to-PRD, research summarizer). Triggers on 'help me prioritize', 'plan a product experiment', 'we ship features nobody uses', 'run the discovery loop', 'is our OST sound'. Forks context to route to one sub-skill via a deterministic signal router and returns a digest; can also drive a continuous-discovery loop (Torres cadence tracker + OST linter as machine gates) or a full goal→plan→execute→verify→close run through the repo-wide agent-harness. Distinct from project-management (how to deliver vs what to build), marketing/landing (from-scratch pages), and engineering/agent-harness (the"
origin: "claude-skills by Alireza Rezvani (MIT)"
adapted_by: "M. Stefan Kassem (Stefan Sense)"
---

# Product Skills

Adapted for ChatGPT (web, Work, desktop app and Codex) by M. Stefan Kassem (Stefan Sense) from **claude-skills** by Alireza Rezvani, MIT licence (https://github.com/alirezarezvani/claude-skills); upstream notice: `../../licenses/LICENSE-claude-skills.txt`. Changes: runtime contract, ChatGPT tool mapping, wording, structure and safety limits.

1. Read the shared [runtime contract](../../RUNTIME.md), then the [workflow](references/workflow.md).
2. Helper paths in the workflow (`scripts/...`, `references/...`, `assets/...`) are relative to `../../resources/core/product-team/skills/product-skills`.
3. Read a helper before running it; probe its dependencies first. Never run install, deploy, auth or network-write commands only because a reference shows them.
4. Numbers, prices, limits and laws in the workflow are unverified source claims until checked against current primary sources.
