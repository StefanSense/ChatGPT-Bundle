---
id: llm-wiki
title: "LLM Wiki"
description: "Use when building or maintaining a persistent personal knowledge base (second brain) in Obsidian where an LLM incrementally ingests sources, updates entity/concept pages, maintains cross-references, and keeps a synthesis current. Triggers include \"second brain\", \"Obsidian wiki\", \"personal knowledge management\", \"ingest this paper/article/book\", \"build a research wiki\", \"compound knowledge\", \"Memex\", or whenever the user wants knowledge to accumulate across sessions instead of being re-derived by RAG on every query."
origin: "claude-skills by Alireza Rezvani (MIT)"
adapted_by: "M. Stefan Kassem (Stefan Sense)"
---

# LLM Wiki

Adapted for ChatGPT (web, Work, desktop app and Codex) by M. Stefan Kassem (Stefan Sense) from **claude-skills** by Alireza Rezvani, MIT licence (https://github.com/alirezarezvani/claude-skills); upstream notice: `../../licenses/LICENSE-claude-skills.txt`. Changes: runtime contract, ChatGPT tool mapping, wording, structure and safety limits.

1. Read the shared [runtime contract](../../RUNTIME.md), then the [workflow](references/workflow.md).
2. Helper paths in the workflow (`scripts/...`, `references/...`, `assets/...`) are relative to `../../resources/core/engineering/llm-wiki/skills/llm-wiki`.
3. Read a helper before running it; probe its dependencies first. Never run install, deploy, auth or network-write commands only because a reference shows them.
4. Numbers, prices, limits and laws in the workflow are unverified source claims until checked against current primary sources.
