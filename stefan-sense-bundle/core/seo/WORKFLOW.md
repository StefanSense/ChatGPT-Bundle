---
id: seo
title: SEO and AI-search optimization (SEO/AEO/GEO)
description: Plan and optimize content for search engines (Google, Yandex) and AI answer engines - keyword/intent research, briefs, on-page optimization, titles and meta, structure, schema markup, quick technical audit of a page. Triggers - SEO, сео, семантика, мета-теги, оптимизируй статью, AEO, GEO, keywords, meta description.
based_on: seo-audit, aeo, schema-markup, programmatic-seo (claude-skills, Alireza Rezvani, MIT) and seo (ECC, Affaan Mustafa, MIT); condensed by Stefan Sense
author: M. Stefan Kassem (Stefan Sense)
---

# SEO and AI-search optimization

Rule: no invented search volumes, rankings or traffic numbers. Without a data source (the user's Search Console / Yandex Webmaster / keyword tool export or live web search), give relative judgments and say so.

## 1. Choose the task
- **Keyword and intent map** → clusters by intent (informational, commercial, transactional, navigational), one page per cluster, priority by business value.
- **Content brief** → target query cluster, intent, angle that beats current results (check them via web search if available), outline H1–H3, entities/questions to cover, internal links, CTA.
- **On-page optimization** of a text or URL → checklist below with concrete rewrites.
- **Quick technical check** of a page (HTML provided or fetched) → indexability, title/meta, headings, canonical, hreflang, structured data, image alts, links, Core Web Vitals hints (measure only with real tools).
- **AEO/GEO** (AI answers, featured snippets) → direct answer in the first 40–60 words under a question heading, clear definitions, lists/tables, sources cited, author and date, structured data.

## 2. On-page checklist
- Title: primary intent first, unique, roughly up to ~60 characters (display is pixel-based; verify in a SERP preview).
- Meta description: benefit + CTA, roughly ~150–160 characters (often rewritten by search engines).
- One H1 matching intent; logical H2/H3; question headings for FAQ-type intent.
- First paragraph answers the query. Depth beats length; E-E-A-T signals: author, experience, sources, date.
- Internal links with descriptive anchors; external links to authoritative sources.
- Images: descriptive file names, alt text, compression.
- Structured data (JSON-LD): Article, FAQPage, HowTo, Product, Organization, LocalBusiness, BreadcrumbList — only for content actually on the page; validate with Google Rich Results Test / Schema.org validator.
- Yandex specifics when relevant: regionality, commercial factors, Webmaster tools.

## 3. Output
Prioritized list (impact × effort) with exact rewrites (new title, meta, headings, paragraphs), JSON-LD code if requested, and what to measure afterwards (impressions, CTR, positions in the user's tools).

Library deep dives: `seo-audit`, `aeo`, `schema-markup`, `programmatic-seo`, `site-architecture`, `local-seo-manager`, `seo` (ECC).
