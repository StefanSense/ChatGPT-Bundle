---
id: prompt
title: Prompt engineering and custom GPT instructions
description: Write, diagnose and improve prompts, system instructions, custom GPT / Project instructions, ChatGPT skills (SKILL.md), and structured-output prompts; build test cases for prompts. Triggers - улучши промпт, напиши промпт, инструкции для GPT, системный промпт, prompt engineering, improve my prompt, custom GPT instructions, write a skill.
based_on: senior-prompt-engineer, prompt-engineer-toolkit, prompt-governance, write-a-skill (claude-skills, Alireza Rezvani, MIT); prompt-optimizer (ECC, MIT); skill-creator (Anthropic, Apache-2.0); rewritten by Stefan Sense
author: M. Stefan Kassem (Stefan Sense)
---

# Prompt engineering

## 1. Diagnose the current prompt (if given)
Check: goal stated? audience and context? input clearly separated (delimiters)? constraints and non-goals? output format specified? examples? success criteria? contradictions? hidden assumptions? Report the top issues before rewriting.

## 2. Build a strong prompt
```
Role / perspective (only if it changes behavior)
Task: what to produce and why (the purpose helps the model choose)
Context: audience, background, definitions
Input: delimited (""" … """, XML-style tags)
Constraints: must / must not, length, tone, language, sources
Process hints: steps for complex tasks; ask clarifying questions when X is missing
Output format: exact structure, schema or template
Quality bar: what "good" looks like; examples (1–3, diverse) if format matters
```
Principles: be specific and positive ("write X") rather than only negative; explain *why* a rule exists; one task per prompt or explicit stages; ask for uncertainty to be stated; never require hidden chain-of-thought output — ask for a brief rationale instead.

## 3. Custom GPT / Project instructions / skills
- Instructions: purpose, audience, behavior rules, tools usage (web, code, files), knowledge-file usage, refusal boundaries, output style, conversation starters.
- ChatGPT skill (SKILL.md): YAML frontmatter `name` (lowercase, hyphens, ≤ 64 chars) and `description` (what it does + when to use it, ≤ 1024 chars); concise body; details in `references/`; scripts in `scripts/`. One SKILL.md per uploaded skill folder.
- Knowledge files: clean, well-structured, with headings; avoid contradictory versions.

## 4. Test
Create 5–10 test inputs (typical, edge, adversarial/injection, wrong language, missing data); define expected properties; compare prompt versions side by side; iterate on failures, not on taste.

## 5. Output
Final prompt in a code block, a short changelog (what and why), test cases, and variables to fill `{{…}}`.

Library: `senior-prompt-engineer`, `prompt-engineer-toolkit`, `prompt-governance`, `write-a-skill`, `skill-creator`, `skill-security-auditor`.
