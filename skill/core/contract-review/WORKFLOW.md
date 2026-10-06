---
id: contract-review
title: Contract and document review (not legal advice)
description: Review contracts, offers, terms of service, NDAs, employment and lease agreements - plain-language summary, key terms, obligations and deadlines, risks and unusual clauses, missing protections, questions to ask, redline suggestions - with a clear not-legal-advice boundary. Triggers - проверь договор, риски в договоре, условия контракта, NDA, оферта, review contract, contract risks, terms and conditions, NDA review.
based_on: Stefan Sense original; structure informed by general-counsel-advisor and contract-and-proposal-writer (claude-skills, Alireza Rezvani, MIT)
author: M. Stefan Kassem (Stefan Sense)
---

# Contract and document review

Boundary (state it once, briefly): this is an informational review, not legal advice; for signing decisions with significant stakes consult a qualified lawyer in the relevant jurisdiction. Laws change — cite current primary sources (official legal databases) for any legal rule you mention, or say it needs verification.

## 1. Context
Which side the user is on, jurisdiction and governing law, deal value and importance, deadline, what worries them, whether there is a previous version to compare.

## 2. Read the whole document
Extract: parties, subject, term and renewal (auto-renewal!), price and payment terms, deliverables/acceptance, obligations of each side, deadlines and notice periods, liability and caps, indemnities, penalties, IP ownership, confidentiality, non-compete/non-solicit, data protection, termination rights and consequences, dispute resolution and venue, governing law, assignment, force majeure, amendments, signatures and annexes referenced but missing.

## 3. Assess risks (from the user's side)
| Clause (quote, section) | What it means in plain words | Risk level (high/med/low) | Why | Suggested change / question |
Look for: one-sided termination, unlimited liability, broad indemnities, unilateral price/terms changes, vague acceptance, IP assignment wider than needed, long auto-renewals, penalties without caps, missing SLAs, inconsistent definitions, conflicts between main text and annexes.

## 4. Output
1. Summary in 5–8 lines: what the user commits to and gets.
2. Key dates and obligations list.
3. Risk table (high first).
4. Suggested redlines (exact replacement wording) and questions for the counterparty.
5. What to verify with a lawyer.
Never state that a document is "safe to sign". Keep quotes exact; do not paraphrase legal terms into different meaning.

Library: `general-counsel-advisor`, `gdpr-dsgvo-expert`, `master-agreement-generator`, `contract-and-proposal-writer`.
