---
id: presentations
title: Presentations and slide decks
description: Plan and build presentations - storyline, slide-by-slide outline, speaker notes, editable PowerPoint (.pptx) generation, review and redesign of an existing deck, pitch decks, reports, training decks. Triggers - презентация, слайды, питч-дек, pptx, powerpoint, сделай презентацию, presentation, slides, pitch deck, deck review.
based_on: Stefan Sense original (independent implementation); storyline guidance informed by board-deck-builder and md-slides (claude-skills, MIT) and investor-materials (ECC, MIT)
author: M. Stefan Kassem (Stefan Sense)
---

# Presentations

## 1. Storyline first
Audience, goal (decide / approve / learn / buy), time slot, format (live, sent as a file, printed).
Structure options: situation → complication → resolution (SCR); problem → solution → proof → ask (pitch); context → findings → recommendations → next steps (report).
Write the **slide titles as full-sentence messages** first ("Churn fell 18 % after onboarding redesign") — reading only the titles must tell the story.

## 2. Slide rules
One message per slide; ≤ ~30–40 words of body text; visuals that prove the title (chart, diagram, image, table); readable font sizes (≥ 18 pt body for live decks); consistent layout; sources on data slides; speaker notes carry the detail.
Pitch deck (typical 10–12 slides): problem, solution, why now, market, product, traction (real), business model, competition, team, financials, ask.

## 3. Build
- Path: native ChatGPT slide creation if available → bundled helper → python-pptx code → outline only (say so).
- Helper: `python scripts/docs.py create deck.json out.pptx` with `{"title": "...", "subtitle": "...", "theme": {"accent": "1F4E79", "font": "Calibri"}, "slides": [{"layout": "bullets", "title": "...", "bullets": ["..."], "notes": "..."}, {"layout": "section", "title": "..."}, {"layout": "table", "title": "...", "headers": ["..."], "rows": [["..."]]}, {"layout": "image", "title": "...", "image": "chart.png"}]}` (16:9).
- Charts: generate PNG with matplotlib from real data, then insert.

## 4. Review an existing deck
`python scripts/docs.py inspect deck.pptx` → slide texts and notes. Report: story gaps, slides with several messages, unsupported claims, text overload, inconsistencies; propose a revised outline and rewritten titles.

## 5. Verify
Reopen the file and check slide count and text. Render with LibreOffice to images if available and inspect for overflow/overlap; otherwise state that visual QA was not done.

Library: `board-deck-builder`, `md-slides`, `frontend-slides`, `investor-materials`, `theme-factory`.
