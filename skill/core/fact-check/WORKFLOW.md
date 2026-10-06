---
id: fact-check
title: Fact-checking and claim verification
description: Verify claims in a text, post, article, AI answer, presentation or report - extract checkable claims, find primary sources, rate each claim, flag manipulation and logical errors, propose corrections. Triggers - проверь факты, фактчекинг, это правда, проверь утверждение, источник?, fact-check, verify, is this true, debunk.
based_on: Stefan Sense original (strict analyst method); evaluation criteria informed by scholar-evaluation (ECC, MIT) and strict-api / zero-hallucination-coder (claude-skills, MIT)
author: M. Stefan Kassem (Stefan Sense)
---

# Fact-checking

Stance: neutral and strict. Check claims, not people. Absence of evidence is reported as such, not as refutation.

## 1. Extract claims
List every **checkable** claim: numbers, dates, quotes, attributions, causal claims, comparisons, "first/only/best", legal/medical/scientific statements. Skip pure opinions, but note opinions disguised as facts.

## 2. Check each claim
1. Find the **original source** (the study, the law, the dataset, the full quote in context) — not a repost of it.
2. Compare exactly: number and unit, date and period, geography, population, wording of the quote, conditions.
3. Look for later updates, retractions, corrections and opposing high-quality sources.
4. Without web access: say so; rate from model knowledge only with a date caveat and lower confidence.

## 3. Verdict scale
| Verdict | Meaning |
|---|---|
| ✅ Confirmed | primary source matches |
| ⚠️ Partly true / misleading | true core, but distorted context, period, scale or causality |
| ❌ False | primary sources contradict |
| ❓ Unverifiable | no reliable source found or data not public |
| 🕒 Outdated | was true, no longer current |

## 4. Also check the reasoning
Correlation presented as causation, cherry-picked periods, base-rate neglect, survivorship bias, false dichotomy, appeal to authority, misleading charts (truncated axes), percent vs percentage points, absolute vs relative risk.

## 5. Output
Table: `# | claim (quote) | verdict | what the source actually says | source (title, date, link)`.
Then: overall assessment (2–3 lines), corrected wording for each problematic claim, and what remains uncertain.
Self-check before sending: every verdict has a source or an explicit "not found"; no claim is rated on vibes.
