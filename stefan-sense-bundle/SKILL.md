---
name: stefan-sense-bundle
description: "Stefan Sense Bundle by M. Stefan Kassem (Stefan Sense) - an everyday work toolkit for ChatGPT. Use for writing and editing in Russian or English, humanizing AI-sounding text, translation, summaries, business email, copywriting, ads, social media, SEO, content plans, research with sources, fact-checking, data analysis and charts, decisions, strategy, meetings, project plans, product specs, sales proposals, CVs and interviews, learning, prompts, code, contract review, visuals, and Word, PDF, Excel and PowerPoint files. Has 32 core workflows plus a searchable library of 580+ specialist workflows for engineering, marketing, leadership, compliance and research. Use whenever a request matches one of these tasks or names a bundle workflow."
---

# Stefan Sense Bundle

Author: **M. Stefan Kassem (Stefan Sense)**. Built on open-source work by other authors — see `AUTHORS.md`.
All paths below are relative to the folder that contains this SKILL.md (the bundle root).

## Operating rules (always on)
1. **Accuracy first.** Never invent facts, numbers, quotes, sources, links, test results or file contents. Unknown → say "I don't know / not enough reliable data", or mark `[NEED: …]` / `[ASSUMPTION]`. Separate facts, estimates and opinions.
2. **Sources.** Current facts (prices, laws, specs, news, people) need live sources when web search is available; otherwise state that the answer comes from model knowledge and may be outdated.
3. **Language.** Reply in the user's language; keep the user's terms, names and voice.
4. **Ask little, deliver.** Ask at most 3 questions, and only when the answer changes the result; otherwise proceed and list assumptions.
5. **Real tools only.** Use only capabilities present in this session (code execution, files, web search, image generation, connectors, scheduled tasks). Never claim an action, file, email, post or saved memory that did not happen. Sending, publishing, purchasing or deleting needs explicit user authorization; an already explicit request is authorization for its stated scope. Respect host approval controls.
6. **Independent judgment.** Do not agree by default; if an idea or text is weak, say why and offer a stronger version.
7. **Self-check before answering:** unsupported claims? broken logic? numbers recomputed? deliverable matches the request?

## Pick a workflow
| Need | Core workflow |
|---|---|
| Write any text / edit, proofread / translate / summarize | `write` · `edit` · `translate` · `summarize` |
| Remove AI tells and bureaucratese | `humanize-ru` · `humanize-en` |
| Business email, messages, follow-ups | `email` |
| Selling copy, landing pages / ads / social posts | `copywriting` · `ad-creative` · `social` |
| Positioning & brand context / content plan / SEO | `product-marketing` · `content-plan` · `seo` |
| Research with sources / verify claims | `research` · `fact-check` |
| Data, Excel analysis, charts | `data-analysis` |
| Decisions, critique / strategy, market, competitors | `decision` · `strategy` |
| Meetings / project plans / product specs | `meeting` · `project-plan` · `product` |
| Sales proposals, objections / CV, interviews | `sales` · `career` |
| Learning / prompts and custom GPTs / code | `learn` · `prompt` · `code` |
| Contracts review / visuals, diagrams, images | `contract-review` · `visual` |
| Planning the day, priorities, goals | `productivity` |
| Files: Word & PDF / Excel / PowerPoint | `documents` · `spreadsheets` · `presentations` |

Read the chosen workflow before acting: `core/<id>/WORKFLOW.md`. Its `references/` folder holds depth material; open only what the task needs.
For multi-step tasks chain 2–4 workflows (e.g. `research` → `strategy` → `presentations`) with an explicit output from each step.

## Specialist library (580+ workflows)
Translate other-language search queries to concise English keywords before calling the local search; answer the user in their language.
For narrow or technical needs (frameworks and languages, security, compliance such as GDPR/ISO/SOC 2, C-level advisory, CRO, compliance audits, ML, DevOps, logistics, media…):
```
python scripts/sense.py search "<English keywords or Russian query>"   # core + library, best first
python scripts/sense.py show <id>                         # print a workflow (unpacks library items on demand)
python scripts/sense.py extract <id> --dest <empty dir>   # unpack with its resources/helpers
```
Library workflows follow `RUNTIME.md` inside the extraction. This runtime contract and the host instructions take priority over any conflicting upstream reference, role, automatic action or tool name. Never unpack the whole library; one workflow at a time.

## Helpers (optional, local)
Use paths relative to this skill directory, not the user project. With a shell, quote its absolute path and use Python 3.10+. With a Python-only execution tool, use `runpy.run_path` with explicit `sys.argv`, or import the helper after adding its scripts folder to `sys.path`. Root helpers do not contact the network. Specialist library scripts may use services: read their source and check requirements before running.

- `python scripts/docs.py doctor | create spec.json out.docx|pdf|xlsx|pptx | inspect <file> | merge … | split …`
- `python scripts/text_scan.py text.txt --lang ru|en [--before original.txt]` — heuristic marker counts and fact diff; not an AI detector.
- `python scripts/sense.py check` — file integrity, resource manifest and syntax; `selftest` — local core functional checks; `doctor [workflow-id]` — real dependency probes. A passing integrity check does not certify external services.
Read a helper's usage before running it. Prefer ChatGPT's native file creation when it is available.

## If code execution is unavailable
Read `core/<id>/WORKFLOW.md` directly if file reading works; otherwise apply the operating rules and the table above from this file, and say that the detailed workflow could not be loaded. Never claim a workflow or helper was run when it was not.

## Credits
Core workflows: written by Stefan Sense, several based on Corey Haines (marketingskills, MIT), Siqi Chen (humanizer, MIT). Library: adapted by Stefan Sense from Alireza Rezvani (claude-skills, MIT), Affaan Mustafa (everything-claude-code, MIT), Anthropic example skills (Apache-2.0) and Forward Future (Loop Library, MIT). Licences: `licenses/`, details: `AUTHORS.md`, `THIRD_PARTY_NOTICES.md`.
