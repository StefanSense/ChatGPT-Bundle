---
id: research
title: Research with sources
description: Research any question with current, cited sources - market and competitor research, technology or vendor comparison, background briefing, literature overview, "what is known about X" - and produce a sourced brief. Triggers - исследуй, найди информацию, сравни, обзор рынка, источники, research, find sources, compare options, deep research.
based_on: research, deepread, dossier, litreview (claude-skills, Alireza Rezvani, MIT); deep-research and market-research (ECC, Affaan Mustafa, MIT); rewritten by Stefan Sense
author: M. Stefan Kassem (Stefan Sense)
---

# Research with sources

Principle: every factual claim in the output is traceable to a source the reader can open, or is explicitly labeled as model knowledge with its approximate date, or as an assumption.

## 1. Frame the question
- Decision the research supports, scope (geography, period, segment), depth (quick scan ~15 min vs deep), output format.
- Split into 3–7 sub-questions. Define what evidence would answer each.

## 2. Gather
- Use ChatGPT web search when available; for very deep work suggest ChatGPT deep research if the user has it. Without web access, say so clearly and answer from model knowledge with a cutoff caveat.
- Prefer primary sources: official statistics, regulators, company filings/reports, standards, peer-reviewed papers, official documentation. Use secondary sources (media, blogs) for context, and aggregators only to find primaries.
- Record for each source: title, publisher, date, URL, what exactly it supports.
- Search in the relevant languages (e.g. Russian and English for Russian-market questions).

## 3. Evaluate
- Date: is it current enough for the claim (prices, laws, specs change fast)?
- Authority and incentive (vendor marketing vs independent).
- Method for numbers (sample, definition, region). Two independent sources for key numbers when possible.
- Conflicts between sources → report both, explain the likely reason.

## 4. Synthesize
```
Answer (3–5 lines): the bottom line with confidence level (high / medium / low).
Findings: per sub-question, claims with inline citations [1], [2].
Comparison table (if options are compared): criteria × options, with sources.
Uncertainties and gaps: what could not be verified and why.
Implications / next steps for the user's decision.
Sources: numbered list with date accessed.
```

## 5. Rules
- No fabricated citations, URLs, quotes or numbers. If a source cannot be found, say "not found".
- Separate facts, estimates and opinions explicitly.
- Medical, legal, financial and safety topics: primary sources only, and a note that this is not professional advice.

Library: `deep-research`, `dossier`, `deepread`, `litreview`, `market-research`, `competitive-intel`, `patent`, `pulse`, `ecc-deep-research`, `scientific-thinking-literature-review`.
