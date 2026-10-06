# Changelog

## 1.0.0 — 2026-10-06
First release as **Stefan Sense Bundle** (replaces the earlier "Work Toolkit" assembly).
- New router `SKILL.md` with always-on accuracy rules, automatic invocation enabled (`agents/openai.yaml`).
- 32 core workflows written for everyday work, readable as plain files (no unpacking needed).
- Specialist library: 586 workflows (from 672). Removed 75 stubs/host-only/index items, 11 items replaced by core workflows.
  Fixed text damaged by the earlier automatic renaming (e.g. broken URLs, "ChatGPT Work and ChatGPT Work").
  One shared `RUNTIME.md` instead of 672 copies; unpacking now extracts one workflow and only its resources.
- New scripts: `sense.py` (search RU/EN, show, extract, check, doctor), `docs.py` (DOCX/PDF/XLSX/PPTX create, inspect,
  merge, split; Cyrillic-safe PDF fonts; formula-injection guard), `text_scan.py` (RU/EN markers + fact diff).
- Authorship, credits, licences and modification notices added.
