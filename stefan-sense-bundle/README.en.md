# Stefan Sense Bundle 1.1.1

32 core workflows and 586 specialist reference workflows. Credits and licensing: AUTHORS.md and THIRD_PARTY_NOTICES.md.

Upload the ZIP through ChatGPT **Plugins → Skills → Create → Upload from your computer**. Complete the host review and enable/install the skill when offered. Select it with `@` in a new chat. Availability depends on your account and workspace settings.

For local Codex, place the folder under `~/.agents/skills/` and invoke `$stefan-sense-bundle`. Refresh the skills list if needed. Installing a skill does not grant external API access or add tools to the host.

Python 3.10+ commands (from this folder):

```bash
python scripts/sense.py check
python scripts/sense.py selftest
python scripts/sense.py doctor
python scripts/sense.py doctor soc2-compliance
python scripts/sense.py search "SOC 2"
python scripts/sense.py show soc2-compliance
```

`check` validates file integrity and syntax, `selftest` exercises core local functions and explicitly reports skipped optional dependencies, and `doctor [id]` runs import/version probes. None of these certifies external APIs. Use the host's native file tools first; optional document libraries are python-docx, reportlab, pypdf, openpyxl and python-pptx. Non-Latin PDFs require a suitable TTF font. No automatic dependency installation.

Search uses English keywords and Russian aliases; translate other-language queries to English first. Read RUNTIME.md before specialist workflows. Review source before running helpers. Only access user-selected files and authorized services. Facts, prices, laws and specifications in references require current primary sources. Text scanning is a heuristic; document rendering and task-specific checks remain necessary. Uploaded ZIP acceptance must be checked in the target account.

Official installation references, checked 2026-10-07: https://help.openai.com/en/articles/20001066-skills-in-chatgpt and https://learn.chatgpt.com/docs/build-skills.

## Experiment safety in 1.1.1

The autoresearch-agent module uses explicit project boundaries and finite run/time limits. It does not commit or roll back project files. Review the command and evaluator before --approve-eval. Recreate legacy config.cfg experiments explicitly through setup. Replace shell pipelines with reviewed standalone scripts. Installation remains subject to the service safety review; this archive is not evidence of approval.
