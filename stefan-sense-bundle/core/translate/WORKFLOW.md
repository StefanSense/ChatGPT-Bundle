---
id: translate
title: Translation and localization
description: Translate texts, documents, interfaces and marketing copy between languages with correct terminology, register and cultural adaptation; bilingual review of an existing translation. Triggers - переведи, перевод, локализация, translate, localize, translation review.
based_on: Stefan Sense original; i18n practices informed by i18n-sync (ECC, Affaan Mustafa, MIT)
author: M. Stefan Kassem (Stefan Sense)
---

# Translation and localization

Goal: the target reader gets the same meaning, intent and tone as the source reader.

## 1. Clarify (only if not obvious)
- Source and target language **and variety** (pt-BR vs pt-PT, en-US vs en-GB, Russian for RU vs KZ audience).
- Purpose: understand only (gist) / publish (polished) / legal or technical (faithful) / marketing (transcreation).
- Glossary, brand terms that stay untranslated, forms of address (ты/вы, tu/vous, du/Sie).

## 2. Procedure
1. Read the whole source first; note terms, ambiguities, idioms, references, units, dates, currencies.
2. Build a mini-glossary for recurring terms and keep it consistent. Do not translate product names, code, URLs, variables (`{name}`, `%s`, HTML tags).
3. Translate meaning, not words: natural word order, target-language punctuation and typography (« » in Russian/French, decimal comma, date order).
4. Localize only when the purpose allows: units, currency, examples, idioms. Mark every substantive localization in notes.
5. Back-check: compare sentence by sentence for omissions, additions, negations, numbers and modality ("must" ≠ "should").

## 3. Mode specifics
- **Legal / medical / technical**: faithful over elegant; keep structure and numbering; flag ambiguous source wording instead of resolving it silently; recommend a certified human translator where legally required.
- **Marketing (transcreation)**: keep the message and effect; offer 2–3 options for headlines/slogans with back-translations.
- **UI strings / JSON**: keep keys, placeholders and length limits; report strings that exceed limits.
- **Review of an existing translation**: table `source → current → suggested → reason (accuracy / fluency / terminology / style)`.

## 4. Output
Translation first. Then (if relevant): glossary, translator notes for ambiguities and localizations, untranslatable items.
For files: return the same format (DOCX/XLSX/PPTX via `docx`/`xlsx`/`pptx` workflows), preserving layout as far as tools allow.
