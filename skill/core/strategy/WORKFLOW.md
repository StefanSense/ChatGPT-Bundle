---
id: strategy
title: Business strategy, market and competitor analysis
description: Analyze a business, market or competitors and produce strategy work - market sizing (TAM/SAM/SOM), competitor teardown, SWOT, Porter five forces, positioning, pricing logic, unit economics, business model canvas, go-to-market, one-page strategy. Triggers - анализ рынка, конкуренты, стратегия, бизнес-план, юнит-экономика, SWOT, market analysis, competitors, business plan, unit economics, go-to-market.
based_on: competitive-teardown, market-research, financial-analyst, pricing-strategy, ceo-advisor (claude-skills, Alireza Rezvani, MIT); competitive-platform-analysis and benchmark-methodology (ECC, MIT); rewritten by Stefan Sense
author: M. Stefan Kassem (Stefan Sense)
---

# Business strategy and market analysis

Rules: frameworks are thinking tools, not deliverables by themselves; every number has a source or is a labeled assumption; calculations run in code.

## 1. Pick the tool for the question
| Question | Tool |
|---|---|
| How big is the opportunity? | TAM/SAM/SOM — bottom-up (customers × price × frequency) preferred over top-down; show both if possible |
| Who are we up against? | competitor teardown: offer, price, audience, channels, strengths, weaknesses, reviews (real), positioning map |
| Where do we stand? | SWOT that ends in actions (SO/WO/ST/WT), not four lists |
| Is the industry attractive? | Porter's five forces with evidence |
| Will the money work? | unit economics: CAC, LTV (margin-based), payback, contribution margin, break-even; sensitivity table |
| How do we price? | value-based vs cost-plus vs competitive; packaging tiers; willingness-to-pay tests |
| How do we launch/grow? | GTM: ICP, channel hypotheses, offer, funnel metrics, 90-day plan |
| What is the business? | Business Model Canvas / Lean Canvas |

## 2. Procedure
1. Clarify the decision, market, geography, period, stage of the company.
2. Gather data: user's numbers first, then web search for current market data (official statistics, reports, filings). Russian market: Rosstat, CBR, industry associations, company reports, where relevant.
3. Build the analysis; compute with code; sensitivity for key assumptions (±20–30 %).
4. Synthesize: 3–5 strategic implications and concrete next steps with owners and metrics.

## 3. Output
One-page summary (situation, key insight, recommendation, risks, next steps) + supporting tables/charts + assumptions register (assumption, value, source/basis, confidence). Offer deck (`presentations`) or memo (`documents`).

Not investment, legal or tax advice; flag where a professional is needed.

Library: `competitive-teardown`, `market-research`, `financial-analyst`, `pricing-strategy`, `business-investment-advisor`, `intl-expansion`, `ceo-advisor`, `cfo-advisor`, `investor-materials`, `launch-strategy`.
