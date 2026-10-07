---
id: data-analysis
title: Data analysis and charts
description: Analyze CSV, Excel, Google Sheets exports or pasted tables - cleaning, descriptive statistics, comparisons, trends, cohorts, A/B test significance, forecasts, pivot tables and charts - with code execution and honest uncertainty. Triggers - проанализируй данные, таблица, график, статистика, отчёт по продажам, data analysis, chart, CSV, pivot, A/B test result.
based_on: statistical-analyst, financial-analyst, data-quality-auditor (claude-skills, Alireza Rezvani, MIT); rewritten by Stefan Sense
author: M. Stefan Kassem (Stefan Sense)
---

# Data analysis

Rule: compute with code, never "by eye". Every number in the answer comes from executed code on the user's data.

## 1. Understand
Question to answer and decision behind it; definitions (what is a "customer", "active", "revenue" — gross/net, VAT); period; granularity.

## 2. Load and audit (always)
1. Load with pandas (`pd.read_csv` / `pd.read_excel(sheet_name=None)`); report sheets, rows, columns, dtypes.
2. Data quality: missing values, duplicates, impossible values, outliers, mixed units/currencies, date parsing, encoding issues, totals rows inside data.
3. Fix only with stated rules; keep the raw copy. List every cleaning step in the answer.

## 3. Analyze
- Descriptives: counts, sums, mean **and** median, spread, shares.
- Comparisons: segment × period; growth in % **and** absolute numbers; mind percent vs percentage points.
- Trends: rolling averages, seasonality; do not extrapolate beyond what data supports.
- Tests when relevant: A/B (conversion: two-proportion test / chi-square; means: t-test or Mann-Whitney), report effect size + confidence interval + sample size, not only p-value. Small samples → say results are inconclusive.
- Correlation ≠ causation; name plausible confounders.
- Forecasts: simple, explainable methods first; show the range, not a single point.

## 4. Visualize
One message per chart; correct type (line = time, bar = categories, scatter = relationship, histogram = distribution); labeled axes with units; zero baseline for bars; readable without color alone; title states the finding. Save as PNG for download when useful.

## 5. Output
```
Answer: 2–4 lines with the key numbers.
Details: table(s) and chart(s).
Method and cleaning steps.
Caveats: data limits, assumptions, what would change the conclusion.
Next: what to check or collect next.
```
Deliver files on request: cleaned dataset, XLSX with formulas (see `spreadsheets`), charts.

Library: `statistical-analyst`, `financial-analyst`, `data-quality-auditor`, `campaign-analytics`, `product-analytics`, `saas-metrics-coach`, `experiment-designer`.
