---
id: summarize
title: Summaries and key points
description: Summarize documents, articles, reports, meeting transcripts, chats, email threads, videos (from transcript) and books into TL;DR, key points, decisions and action items. Triggers - кратко, суммируй, выжимка, конспект, резюме документа, summarize, TL;DR, key takeaways.
based_on: Stefan Sense original; reading discipline informed by deepread and research-summarizer (claude-skills, Alireza Rezvani, MIT)
author: M. Stefan Kassem (Stefan Sense)
---

# Summaries

Goal: the reader gets what matters for their decision in a fraction of the time, with nothing invented.

## 1. Set the frame (infer; ask only if the use is unclear)
- **Who and why**: executive decision, study, briefing a colleague, legal review, personal notes.
- **Length**: one line / 5 bullets / one page / section-by-section.
- **Lens**: neutral overview, risks only, decisions and actions, arguments and evidence, changes vs a previous version.

## 2. Procedure
1. Read or process the **entire** source. For long files, work section by section with code execution and keep notes; never summarize only the beginning. If parts were unreadable (scans, images, truncated), say so.
2. Extract: main claim/purpose, key facts and numbers, decisions, open questions, risks, action items (owner, deadline if stated).
3. Rank by importance for the stated reader, not by order in the source.
4. Write the summary in the user's language; keep terms, names and numbers exact.
5. Verify: every statement is traceable to the source; mark interpretations as such ("Implication:" / «Вывод:»).

## 3. Formats
**Standard**
```
TL;DR: one or two sentences.
Key points: 3–7 bullets, most important first.
Decisions / numbers: …
Action items: [owner] task — deadline (only if stated)
Open questions / risks: …
```
**Meeting**: purpose → decisions → action items → disagreements → next meeting.
**Thread / chat**: current status → who wants what → what is blocked → suggested reply (if asked).
**Academic / report**: question → method → findings (with numbers) → limitations → relevance.
**Comparison of versions**: added / removed / changed meaning.

## 4. Rules
- Location references for important claims: page, section, timestamp or slide number.
- No new facts, no opinions disguised as content. Quotes are verbatim and marked.
- If the source contradicts itself, report the contradiction.
- Summarizing does not mean agreeing: note unsupported claims in a separate line when the user needs a critical read (see `fact-check`).
