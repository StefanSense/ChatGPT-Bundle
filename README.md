# Stefan Sense Bundle 1.1.1 — навык для ChatGPT

Автор: **M. Stefan Kassem (Stefan Sense)**. 32 основных направления работы и 586 специализированных методик:
тексты, маркетинг, исследования, аналитика, проекты и документы. Сторонние авторы и лицензии —
[AUTHORS.md](stefan-sense-bundle/AUTHORS.md) и [THIRD_PARTY_NOTICES.md](stefan-sense-bundle/THIRD_PARTY_NOTICES.md).

## ⬇️ Скачать для ChatGPT

**[Stefan-Sense-Bundle.zip](https://github.com/StefanSense/ChatGPT-Bundle/raw/HEAD/Stefan-Sense-Bundle.zip)** — прямая ссылка на готовый архив (всегда последняя версия).

1. Скачайте архив по ссылке выше (не распаковывайте).
2. ChatGPT → **Plugins → Skills → Create → Upload from your computer** → выберите ZIP.
3. Дождитесь проверки ChatGPT и включите навык. В чате: `@Stefan Sense Bundle` или «Используй Stefan Sense Bundle: …».

Контрольная сумма SHA-256: [Stefan-Sense-Bundle.zip.sha256](Stefan-Sense-Bundle.zip.sha256).

> Ссылки «установить в ChatGPT в один клик» для навыков из GitHub OpenAI не предоставляет. Ссылку для установки
> внутри ChatGPT может создать только владелец навыка после загрузки — в меню общего доступа навыка («copy the sharing link»)
> (доступность общего доступа зависит от тарифа и рабочего пространства).

## Codex (CLI, IDE, приложение) — установка одной командой

macOS / Linux:
```bash
git clone --depth 1 https://github.com/StefanSense/ChatGPT-Bundle.git /tmp/stefan-sense && mkdir -p ~/.agents/skills && cp -R /tmp/stefan-sense/stefan-sense-bundle ~/.agents/skills/
```
Windows (PowerShell):
```powershell
git clone --depth 1 https://github.com/StefanSense/ChatGPT-Bundle.git $env:TEMP\stefan-sense; New-Item -ItemType Directory -Force "$env:USERPROFILE\.agents\skills" | Out-Null; Copy-Item -Recurse -Force "$env:TEMP\stefan-sense\stefan-sense-bundle" "$env:USERPROFILE\.agents\skills\"
```
Затем перезапустите Codex и вызовите `$stefan-sense-bundle`. Если ваша версия Codex читает навыки из `~/.codex/skills/`, скопируйте папку туда.

## Состав репозитория
| Путь | Что это |
|---|---|
| `Stefan-Sense-Bundle.zip` | готовый архив для загрузки в ChatGPT (байт в байт как выпущенный 1.1.1) |
| `stefan-sense-bundle/` | содержимое архива: `SKILL.md`, `core/`, `library/`, `scripts/`, лицензии |
| `LICENSE` | MIT — авторская часть бандла |

Подробная инструкция и проверка после установки — [stefan-sense-bundle/README.md](stefan-sense-bundle/README.md) · English: [README.en.md](stefan-sense-bundle/README.en.md).

## Лицензия
Авторская часть (M. Stefan Kassem / Stefan Sense) — [MIT](LICENSE): можно свободно использовать, изменять и
распространять с сохранением уведомления об авторстве. Сторонние материалы сохраняют свои лицензии (MIT, Apache-2.0) —
см. [THIRD_PARTY_NOTICES.md](stefan-sense-bundle/THIRD_PARTY_NOTICES.md) и [licenses/](stefan-sense-bundle/licenses/).
