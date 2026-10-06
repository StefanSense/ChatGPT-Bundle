# Stefan Sense Bundle — an everyday work toolkit for ChatGPT

**Author:** M. Stefan Kassem (**Stefan Sense**). Workflows were written and adapted by the author, building on
open-source work by Corey Haines, Siqi Chen, Alireza Rezvani, Affaan Mustafa, Anthropic (example skills),
Forward Future and Humanizer-RU — see [AUTHORS.md](AUTHORS.md).

One ChatGPT skill that routes each request to the right method: writing, editing, translation, marketing,
research, fact-checking, data analysis, decisions, projects, sales, careers, learning, prompts, code,
contracts, visuals, and Word/PDF/Excel/PowerPoint files.

## Contents
- `SKILL.md` — router and always-on accuracy rules.
- `core/` — 32 everyday workflows (plain files).
- `library/` — 586 specialist workflows, searched and unpacked one at a time with `scripts/sense.py`.
- `scripts/` — `sense.py` (search/show/extract/check), `docs.py` (DOCX/PDF/XLSX/PPTX), `text_scan.py` (RU/EN markers).

## Install
Upload the **ZIP as is** (one top folder, exactly one `SKILL.md`).
- **ChatGPT web / Work:** Profile → Skills → New skill → Upload from your computer → select the ZIP → enable it.
  Availability depends on plan, region and workspace admin settings; menu names may differ.
- **ChatGPT desktop app:** same upload; reportedly web and desktop skills may not sync — upload again if missing.
- **Codex:** unzip to `~/.codex/skills/stefan-sense-bundle/` (Windows: `%USERPROFILE%\.codex\skills\stefan-sense-bundle\`)
  and restart; check current Codex docs if the path has changed.
- **No skills support:** add the files to a Project or custom GPT and paste the operating rules into its instructions.

## Use
Just describe the task. For niche needs: "find a Stefan Sense workflow for SOC 2" → `python scripts/sense.py search "SOC 2"`.

## Limits
Format compliance and scripts are tested; the actual upload to your account must be checked by you. Numbers,
platform limits, prices and legal rules inside library references are unverified source claims. `text_scan.py` is
a heuristic editing aid, not an AI detector. Legal, medical and financial outputs are not professional advice.

Licence: MIT for the original work (see `LICENSE`); third-party material under its own licences.
