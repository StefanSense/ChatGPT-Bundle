---
id: mcp-builder
title: "MCP Builder"
description: "Guide for creating high-quality MCP (Model Context Protocol) servers that enable LLMs to interact with external services through well-designed tools. Use when building MCP servers to integrate external APIs or services, whether in Python (FastMCP) or Node/TypeScript (MCP SDK)."
origin: "anthropics/skills (example skills) by Anthropic, PBC (Apache-2.0)"
adapted_by: "M. Stefan Kassem (Stefan Sense)"
---

# MCP Builder

Adapted for ChatGPT (web, Work, desktop app and Codex) by M. Stefan Kassem (Stefan Sense) from **anthropics/skills (example skills)** by Anthropic, PBC, Apache-2.0 licence (https://github.com/anthropics/skills); upstream notice: `../../licenses/LICENSE-Apache-2.0.txt`. Changes: runtime contract, ChatGPT tool mapping, wording, structure and safety limits.

1. Read the shared [runtime contract](../../RUNTIME.md), then the [workflow](references/workflow.md).
2. Helper paths in the workflow (`scripts/...`, `references/...`, `assets/...`) are relative to `../../resources/docs/skills/mcp-builder`.
3. Read a helper before running it; probe its dependencies first. Never run install, deploy, auth or network-write commands only because a reference shows them.
4. Numbers, prices, limits and laws in the workflow are unverified source claims until checked against current primary sources.
