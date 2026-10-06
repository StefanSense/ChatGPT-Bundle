---
id: product
title: Product management - discovery, PRD, prioritization
description: Product work - problem discovery, user interview scripts and synthesis, jobs to be done, PRD/one-pager, user stories with acceptance criteria, prioritization (RICE, ICE, MoSCoW, Kano), roadmap, metrics and experiments. Triggers - PRD, ТЗ на продукт, пользовательские истории, приоритизация, roadmap, продуктовые метрики, user stories, product spec, discovery, RICE.
based_on: product-manager-toolkit, product-discovery, agile-product-owner, ux-researcher-designer, product-strategist (claude-skills, Alireza Rezvani, MIT); product-lens and product-capability (ECC, MIT); rewritten by Stefan Sense
author: M. Stefan Kassem (Stefan Sense)
---

# Product management

## Discovery
- Problem statement: who, which job, what pain, how often, current workaround, evidence.
- Interview script (open, past behavior, no leading questions): "Tell me about the last time you…", "What did you do next?", "What was hardest?". 5–8 interviews per segment before conclusions.
- Synthesis: quotes → patterns → insights → opportunities (opportunity-solution tree). Label how many users said what; no invented quotes.

## PRD / one-pager
```
Problem and evidence · Goal and success metrics (leading + lagging, with target and timeframe)
Users and use cases · Scope (in / out / later) · Requirements (functional, non-functional)
User flows · Edge cases · Dependencies · Risks and open questions · Launch plan · Analytics events
```
## User stories
"As a <user>, I want <action> so that <outcome>." + acceptance criteria in Given/When/Then; INVEST check; split large stories by workflow step, rule, data variation or interface.

## Prioritization
- **RICE** = Reach × Impact × Confidence / Effort (compute in code; show inputs, not just scores).
- **ICE** for quick experiments; **MoSCoW** for release scope; **Kano** for delighters vs basics.
- Always show the top assumptions behind the ranking.

## Roadmap
Now / Next / Later by outcomes (not feature lists), with confidence levels; dated roadmaps only with capacity data.

## Metrics
North star + input metrics; funnel (activation, retention, revenue, referral); experiments with hypothesis, metric, minimum detectable effect, duration (see `data-analysis`).

Library: `product-manager-toolkit`, `product-discovery`, `agile-product-owner`, `ux-researcher-designer`, `experiment-designer`, `product-analytics`, `roadmap-communicator`, `code-to-prd`, `product-lens`.
