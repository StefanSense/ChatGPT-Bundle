---
id: spreadsheets
title: Excel and spreadsheets
description: Create, read, clean and check Excel/CSV/Google Sheets files - trackers, budgets, financial models, reports with formulas, pivot-style summaries, conditional formatting, charts, data validation. Triggers - Excel, эксель, таблица, xlsx, csv, формулы, бюджет в таблице, трекер, spreadsheet, workbook, formulas.
based_on: Stefan Sense original (independent implementation; not derived from proprietary document skills)
author: M. Stefan Kassem (Stefan Sense)
---

# Excel and spreadsheets

## 0. Path
Native ChatGPT file creation or code execution with openpyxl/pandas → bundled `scripts/docs.py` → Markdown/CSV fallback (say so). Check `python scripts/docs.py doctor`.

## 1. Design
- One table per sheet, headers in row 1, one row per record, no merged cells inside data.
- Separate sheets: Inputs (assumptions, blue font), Calculations, Outputs/Dashboard, Data, README (purpose, sources, date, author).
- Formulas instead of hard-coded results so the user can change inputs; named ranges for key assumptions.
- Units and currency in headers; consistent number formats; freeze header row; filters; sensible widths.

## 2. Create
`python scripts/docs.py create spec.json out.xlsx` with
`{"sheets": [{"name": "Data", "rows": [["Item", "Qty", "Price", "Total"], ["A", 2, 10, "=B2*C2"]], "number_formats": {"C": "#,##0.00", "D": "#,##0.00"}, "col_widths": {"A": 30}}]}`.
A string starting with `=` is a formula — only when intended; escape user text that begins with `=`, `+`, `-`, `@` (formula injection).
For complex workbooks write openpyxl code directly (charts, conditional formatting, data validation).

## 3. Read and analyze
`python scripts/docs.py inspect file.xlsx` → sheets, dimensions, formulas and values. For analysis switch to `data-analysis` (pandas).

## 4. Verify
openpyxl writes formulas but does not calculate them. If LibreOffice is available, recalculate a copy headless and read values back; otherwise verify key formulas by computing the same numbers in Python and say the workbook was not recalculated here. Check totals, ranges (no off-by-one), absolute/relative references, division by zero, regional separators for the user's Excel locale (`;` in many European/Russian locales when typing formulas manually).

## 5. Deliver
File + short guide: what each sheet does, which cells to edit, assumptions and sources.

Library: `financial-analyst`, `saas-metrics-coach`, `capacity-planner`, `commercial-forecaster`.
