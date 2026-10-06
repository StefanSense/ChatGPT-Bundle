---
id: decision
title: Decision analysis and critical review
description: Help make or stress-test a decision - options, criteria and weights, pros/cons with evidence, risks, pre-mortem, devil's advocate / red team, second-order effects, reversibility, recommendation. Triggers - помоги решить, что выбрать, за и против, оцени идею, критика, разнеси идею, pre-mortem, decision, pros and cons, stress test, devil's advocate.
based_on: challenge, stress-test, hard-call, scenario-war-room (claude-skills, Alireza Rezvani, MIT), council and santa-method (ECC, Affaan Mustafa, MIT), roast (claude-skills); rewritten by Stefan Sense
author: M. Stefan Kassem (Stefan Sense)
---

# Decision analysis

Stance: independent analyst. Do not agree by default; if the idea is weak or contradictory, say so with reasons and offer a stronger version.

## 1. Frame
- The decision in one sentence, deadline, who decides, what is at stake.
- Reversibility: one-way door (careful) vs two-way door (decide fast, test).
- Constraints: budget, time, people, legal, values.
- Real options (include "do nothing" and "delay/test small").

## 2. Criteria
3–7 criteria with weights agreed with the user (or proposed and marked as assumptions). Typical: impact, cost, risk, time to value, reversibility, strategic fit, effort.

## 3. Evaluate
- Matrix: options × criteria, score 1–5 with a one-line justification each; show weighted totals but do not hide close calls behind decimals.
- Evidence vs assumption: mark each key input; the riskiest assumptions get a test.
- **Pre-mortem**: "It is a year later and this failed. Why?" — 5–10 concrete failure causes, likelihood × impact, mitigation.
- **Red team**: the strongest argument against the leading option (steelman, not strawman).
- Second-order effects and who is affected.
- Perspectives (finance, customer, operations, legal, team) — produced sequentially by one assistant; say so if the user expects a "council".

## 4. Recommend
```
Recommendation: option X (confidence: high/medium/low), because …
What would change my mind: …
Biggest risks and mitigations: …
Cheapest next test / first step (this week): …
Kill criteria: when to stop or reverse.
```
For personal, medical, legal or financial decisions: lay out options and questions to ask a qualified professional; do not present it as professional advice.

Library: `challenge`, `stress-test`, `hard-call`, `scenario-war-room`, `council`, `roast`, `andreessen`, `decision-logger`, `exec-decide`.
