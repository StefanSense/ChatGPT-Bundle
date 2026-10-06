# Stefan Sense Bundle — source repository

ChatGPT skill bundle by **M. Stefan Kassem (Stefan Sense)**.
Ready-to-upload archive: [`dist/Stefan-Sense-Bundle-v1.0.0.zip`](dist/) (upload the ZIP as is).
User guide (RU): [`skill/README.md`](skill/README.md) · English: [`skill/README.en.md`](skill/README.en.md) · Credits: [`skill/AUTHORS.md`](skill/AUTHORS.md)

## Layout
| Path | Purpose |
|---|---|
| `skill/` | the skill itself: `SKILL.md`, 32 core workflows, scripts, docs |
| `library/` | editable source of the 586-workflow specialist library (packed into `library.zip` at build time) |
| `licenses/` | upstream licence texts (copied into the bundle and the library) |
| `tools/build.py` | builds `dist/*.zip` and validates ChatGPT skill limits |
| `tools/import_legacy.py` | one-time importer used to convert the earlier "Work Toolkit" archive into `library/` |
| `tests/` | pytest suite for the scripts and the built bundle |

## Build and test
```bash
pip install python-docx openpyxl python-pptx reportlab pypdf pytest   # only for tests of docs.py
python tools/build.py      # -> dist/Stefan-Sense-Bundle-v<VERSION>.zip (+ .sha256)
python -m pytest
```
Bump `skill/VERSION` and `skill/CHANGELOG.md` for each release.
