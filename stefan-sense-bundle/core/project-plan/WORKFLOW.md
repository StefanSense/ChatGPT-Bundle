---
id: project-plan
title: Project planning and status reporting
description: Plan and run projects - goals and scope, work breakdown, timeline/Gantt, dependencies, RACI, risk register, budget, status reports, retrospectives, plans for Jira/Trello/Notion. Triggers - план проекта, дорожная карта, сроки, риски проекта, статус-отчёт, RACI, project plan, roadmap, WBS, status report, Gantt.
based_on: senior-pm, scrum-master, jira-expert (claude-skills, Alireza Rezvani, MIT); blueprint and plan-orchestrate (ECC, Affaan Mustafa, MIT); rewritten by Stefan Sense
author: M. Stefan Kassem (Stefan Sense)
---

# Project planning

## 1. Charter (one page)
Goal and measurable success criteria · scope in / out · stakeholders and decision-maker · deadline and fixed constraints · budget · assumptions · top risks.

## 2. Plan
1. **WBS**: deliverables → work packages (each ≤ ~1–2 weeks of effort, with a clear "done" definition).
2. **Estimates**: ranges (optimistic / likely / pessimistic) from the user or marked assumptions; PERT expected = (O + 4M + P) / 6 when useful.
3. **Dependencies and critical path**; milestones with dates; buffers on the critical path.
4. **RACI** for key deliverables (one Accountable per row).
5. **Risk register**: risk · probability · impact · owner · mitigation · trigger.
6. **Communication plan**: who gets what, how often.
Calculate dates with code (calendar, working days, holidays the user names).

## 3. Formats
Inline tables; XLSX with Gantt-style bars via conditional formatting (`spreadsheets`); CSV for import into Jira/Trello/Asana/Notion (columns: summary, description, assignee, due date, labels, epic/parent); Mermaid `gantt` diagram code when a diagram is wanted.

## 4. Status report
```
Status: 🟢/🟡/🔴 + one line why
Done since last report · Next · Blockers and decisions needed (with deadline) · Risks changed · Milestones (plan vs forecast)
```
Honest RAG: yellow/red as soon as the forecast slips; no "watermelon" reporting.

## 5. Retrospective
What happened (facts) → what worked → what didn't → root causes (5 whys) → 1–3 actions with owners.

Agile variant: backlog with user stories (see `product`), sprint goal, capacity, velocity from the user's history only.

Library: `senior-pm`, `scrum-master`, `jira-expert`, `confluence-expert`, `blueprint`, `runbook-generator`, `postmortem`.
