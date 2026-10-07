---
id: documents
title: Word and PDF documents
description: Create, read, edit, convert and check Word (.docx) and PDF files - reports, memos, letters, contracts drafts, CVs, proposals; extract text and tables; merge/split PDFs; fill templates. Triggers - документ Word, docx, PDF, сделай файл, отчёт в ворде, объедини pdf, извлеки текст, create document, Word file, PDF report, merge PDF.
based_on: Stefan Sense original (independent implementation; not derived from proprietary document skills)
author: M. Stefan Kassem (Stefan Sense)
---

# Word and PDF documents

## 0. Use the best available path
1. If ChatGPT can natively create the file in this session (e.g. ChatGPT Work or code execution with python-docx / reportlab), use it.
2. Otherwise use the bundled helper `scripts/docs.py` (paths relative to the bundle root). Check `python scripts/docs.py doctor` first — it reports which libraries are installed.
3. No code execution at all → deliver the content as well-structured Markdown and say the file could not be generated here.

## 1. Plan the document
Purpose, reader, required sections, length, language, branding (fonts, colors, logo the user provides), page size (A4 by default for RU/EU, Letter for US), numbering, header/footer.

## 2. Create
- DOCX from a JSON spec: `python scripts/docs.py create spec.json out.docx`.
  Spec: `{"title": "...", "subtitle": "...", "author": "...", "blocks": [{"type": "heading", "text": "...", "level": 1}, {"type": "paragraph", "text": "..."}, {"type": "bullets", "items": ["..."]}, {"type": "numbered", "items": ["..."]}, {"type": "table", "headers": ["..."], "rows": [["..."]]}, {"type": "page_break"}]}`.
- PDF from the same spec: `python scripts/docs.py create spec.json out.pdf` (Cyrillic needs a TTF font; the helper finds DejaVu/Liberation/Noto/Arial if installed, or pass `"font_path"`).
- For rich layouts beyond the helper, write python-docx / reportlab code directly.

## 3. Read and edit
- Inspect: `python scripts/docs.py inspect file.docx|file.pdf` → JSON with paragraphs, headings, tables / pages and text.
- Edit DOCX: modify only the targeted runs/paragraphs; replacing `paragraph.text` drops formatting. Tracked changes and comments need OOXML-level work — state the limitation if not done.
- PDF: `python scripts/docs.py merge a.pdf b.pdf out.pdf`; `split in.pdf outdir/`. Image-only PDFs need OCR (only if an OCR engine is available); empty text extraction is not proof of an empty document.

## 4. Verify before delivery
Reopen the file; compare headings, numbers, names and tables with the source; check page count. If a renderer is available (LibreOffice, `pdftoppm`), render pages to images and look at them for overflow, broken tables, missing glyphs. If not, say visual QA was not performed. Provide a download link only for files that exist.

Legal documents: drafts only; recommend review by a qualified lawyer for the relevant jurisdiction.

Library: `doc-coauthoring`, `document-internal-comms`, `md-document`, `nutrient-document-processing`, `visa-doc-translate`.
