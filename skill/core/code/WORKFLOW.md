---
id: code
title: Code - write, review, debug, explain
description: Everyday programming help - write functions and scripts, review code for bugs and security, debug errors from logs or stack traces, refactor, write tests, explain code, SQL queries, regular expressions, automation scripts (Python, JS/TS, SQL, Bash, Excel/Sheets formulas, Apps Script). Triggers - код, скрипт, ошибка в коде, отладка, ревью кода, SQL запрос, регулярка, code, debug, code review, write a script, fix this error, regex.
based_on: code-reviewer, focused-fix, karpathy-coder, strict-api, sql-database-assistant (claude-skills, Alireza Rezvani, MIT); coding-standards, tdd-workflow, security-review (ECC, Affaan Mustafa, MIT); rewritten by Stefan Sense
author: M. Stefan Kassem (Stefan Sense)
---

# Code

Principles: understand before changing; smallest correct change; no invented APIs — if unsure a function/flag exists, say so or check documentation (web search); run code when execution is available.

## Write
1. Restate requirements, inputs/outputs, edge cases, environment (language version, libraries, OS).
2. Simple, readable solution first; no unnecessary dependencies or abstractions.
3. Handle errors at boundaries; no secrets in code (use environment variables).
4. Include a minimal usage example and tests (pytest / Jest etc.) for non-trivial logic.
5. Execute and test in the sandbox when possible; report the real output. Note what could not be tested (network, OS-specific, credentials).

## Debug
1. Reproduce: exact error, stack trace, input, expected vs actual, what changed recently.
2. Hypotheses ranked by likelihood; test the cheapest first; read the actual error line.
3. Fix the root cause, not the symptom; add a regression test.
4. Explain the cause in 2–3 sentences.

## Review
Order of importance: correctness → security (injection, auth, secrets, unsafe deserialization, path traversal, SSRF) → data loss/concurrency → performance → readability → style. Each finding: location, problem, concrete failing scenario, fix. Separate "must fix" from "nice to have". Don't nitpick style that a formatter handles.

## SQL
Ask for schema and dialect (PostgreSQL, MySQL, SQLite, BigQuery, ClickHouse, MS SQL); explicit JOIN conditions, NULL handling, indexes for heavy filters, parameterized queries; test on sample data in SQLite when possible; warn before UPDATE/DELETE without WHERE.

## Spreadsheet formulas and automation
Excel/Google Sheets formulas with regional separators (`,` vs `;`) noted; Apps Script / VBA / Power Query when asked; explain each part.

## Output
Code in fenced blocks with file names; how to run; test results (real); limitations and next steps. Desktop/Codex users: changes to their repository only within the folder they opened, with a summary of edited files.

Library (frameworks and depth): `code-reviewer`, `focused-fix`, `tdd-workflow`, `security-review`, `senior-backend`, `senior-frontend`, `python-patterns`, `react-patterns`, `postgres-patterns`, `docker-patterns`, `git-workflow`, `api-design`, and 250+ more — search the library.
