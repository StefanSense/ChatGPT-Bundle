---
id: stock-analysis
title: "Stock Analysis"
description: "Produce a rigorous, sector-relative, multi-factor fundamental analysis of a publicly listed company — Indian (NSE/BSE) or US/global. Use when the user asks to analyse, research, evaluate, or value a stock, ticker, or listed company; asks whether a business is fundamentally strong, cheap, or expensive; compares companies or benchmarks one against its sector; or mentions OPM, ROCE, ROE, ROIC, P/E, EV/EBITDA, free cash flow, NIM, GNPA, CASA, promoter holding or pledging. Use it for accounting-quality and forensic questions — \"is the profit real\", \"why is profit rising but cash isn't\", auditor qualifications, related-party concerns — which route to the forensic-only mode, and for IPOs and not-yet-listed companies — \"should I apply to this IPO\", DRHP/RHP or S-1 questions, price band, grey market premium — which route to the IPO mode. Use it even when the request sounds casual (\"is Infosys"
origin: "claude-skills by Alireza Rezvani (MIT)"
adapted_by: "M. Stefan Kassem (Stefan Sense)"
---

# Stock Analysis

Adapted for ChatGPT (web, Work, desktop app and Codex) by M. Stefan Kassem (Stefan Sense) from **claude-skills** by Alireza Rezvani, MIT licence (https://github.com/alirezarezvani/claude-skills); upstream notice: `../../licenses/LICENSE-claude-skills.txt`. Changes: runtime contract, ChatGPT tool mapping, wording, structure and safety limits.

1. Read the shared [runtime contract](../../RUNTIME.md), then the [workflow](references/workflow.md).
2. Helper paths in the workflow (`scripts/...`, `references/...`, `assets/...`) are relative to `../../resources/core/finance/skills/stock-analysis`.
3. Read a helper before running it; probe its dependencies first. Never run install, deploy, auth or network-write commands only because a reference shows them.
4. Numbers, prices, limits and laws in the workflow are unverified source claims until checked against current primary sources.
