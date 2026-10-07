#!/usr/bin/env python3
"""Stefan Sense Bundle - workflow router.

Find, show and unpack workflows of the bundle. Standard library only; no network, no installs,
never executes workflow helpers.

  python scripts/sense.py search "landing page copy"     # find workflows (core first)
  python scripts/sense.py show copywriting                # print a core or library workflow
  python scripts/sense.py extract seo-audit               # unpack one library workflow + its resources
  python scripts/sense.py list [--category marketing] [--core]
  python scripts/sense.py check                           # verify bundle integrity
  python scripts/sense.py doctor                          # which optional libraries are installed

Author: M. Stefan Kassem (Stefan Sense). MIT licence.
"""
import argparse, hashlib, importlib.util, json, os, re, stat, sys, tempfile, zipfile, shutil, posixpath, warnings
from runtime_probe import probe_module, probe_tool
from pathlib import Path, PurePosixPath

ROOT = Path(__file__).resolve().parent.parent
CORE = ROOT / 'core'
LIB_ZIP = ROOT / 'library' / 'library.zip'
LIB_CATALOG = ROOT / 'library' / 'catalog.json'
MANIFEST = ROOT / 'library' / 'manifest.json'
MAX_EXTRACT_BYTES = 200 * 1024 * 1024

# Russian (and a few colloquial) words -> English search terms.
ALIASES = {
    'напиши': 'write', 'статью': 'write article', 'статья': 'write article', 'пост': 'social post',
    'письмо': 'email', 'переписка': 'email', 'ответ': 'email reply', 'редактура': 'edit',
    'вычитка': 'edit proofread', 'отредактируй': 'edit', 'ошибки': 'edit proofread',
    'очеловечь': 'humanize', 'канцелярит': 'humanize-ru', 'нейросеть': 'humanize', 'штампы': 'humanize',
    'русский': 'humanize-ru russian', 'перевод': 'translate', 'переведи': 'translate', 'локализация': 'translate localize',
    'кратко': 'summarize', 'выжимка': 'summarize', 'конспект': 'summarize', 'суммируй': 'summarize',
    'реклама': 'ad-creative ads paid-ads', 'креатив': 'ad-creative creative', 'объявление': 'ad-creative',
    'копирайтинг': 'copywriting', 'лендинг': 'copywriting landing page-cro', 'оффер': 'copywriting offer',
    'соцсети': 'social', 'телеграм': 'social telegram', 'линкедин': 'linkedin social',
    'контент': 'content-plan content', 'контент-план': 'content-plan', 'сео': 'seo', 'семантика': 'seo keywords',
    'позиционирование': 'product-marketing positioning', 'бренд': 'brand product-marketing brand-voice',
    'исследование': 'research', 'исследуй': 'research', 'источники': 'research sources', 'рынок': 'strategy market research',
    'конкуренты': 'strategy competitor competitive', 'факты': 'fact-check', 'фактчекинг': 'fact-check', 'проверь': 'fact-check review',
    'данные': 'data-analysis data', 'анализ': 'data-analysis analysis', 'статистика': 'data-analysis statistical',
    'график': 'data-analysis chart', 'решение': 'decision', 'выбор': 'decision', 'риски': 'decision risk',
    'стратегия': 'strategy', 'бизнес-план': 'strategy business', 'юнит-экономика': 'strategy unit economics finance',
    'встреча': 'meeting', 'протокол': 'meeting minutes', 'повестка': 'meeting agenda', 'созвон': 'meeting',
    'проект': 'project-plan project', 'сроки': 'project-plan', 'продукт': 'product', 'тз': 'product prd',
    'продажи': 'sales', 'кп': 'sales proposal', 'возражения': 'sales objection', 'резюме': 'career cv resume',
    'собеседование': 'career interview', 'обучение': 'learn', 'объясни': 'learn explain', 'промпт': 'prompt',
    'код': 'code', 'скрипт': 'code script', 'отладка': 'code debug', 'ревью': 'code review', 'sql': 'code sql',
    'документ': 'documents docx', 'ворд': 'documents docx', 'word': 'documents docx', 'пдф': 'documents pdf',
    'pdf': 'documents pdf', 'эксель': 'spreadsheets xlsx', 'excel': 'spreadsheets xlsx', 'таблица': 'spreadsheets xlsx',
    'презентация': 'presentations pptx slides', 'слайды': 'presentations slides', 'powerpoint': 'presentations pptx',
    'картинка': 'visual image', 'изображение': 'visual image', 'схема': 'visual diagram', 'диаграмма': 'visual diagram',
    'договор': 'contract-review contract', 'контракт': 'contract-review', 'юрист': 'contract-review legal',
    'планирование': 'productivity plan', 'задачи': 'productivity tasks', 'цели': 'productivity goals okr',
    'питч': 'pitch deck investor presentations', 'инвесторов': 'investor', 'инвестор': 'investor',
    'тест': 'testing test', 'автотесты': 'testing e2e playwright', 'безопасность': 'security', 'аудит': 'audit', 'соответствие': 'compliance', 'персональные': 'gdpr privacy', 'тесты': 'testing test', 'финансы': 'finance financial', 'комплаенс': 'compliance',
}
STOP = set('the a an and or of for to in on with my me i you it this that как и в на с для по мне мой это что'.split())


def frontmatter(text):
    m = re.match(r'^---\n(.*?)\n---\n', text, re.S)
    data = {}
    if m:
        for line in m.group(1).splitlines():
            if ':' in line:
                k, v = line.split(':', 1)
                v = v.strip()
                if len(v) >= 2 and v[0] == v[-1] == '"':
                    try: v = json.loads(v)
                    except ValueError: v = v[1:-1]
                data[k.strip()] = v
    return data


def core_index():
    items = []
    for wf in sorted(CORE.glob('*/WORKFLOW.md')):
        meta = frontmatter(wf.read_text(encoding='utf-8'))
        items.append({'id': meta.get('id', wf.parent.name), 'title': meta.get('title', ''), 'tier': 'core',
                      'category': 'core', 'description': meta.get('description', ''),
                      'path': str(wf.relative_to(ROOT)), 'based_on': meta.get('based_on', '')})
    return items


def library_catalog():
    if not LIB_CATALOG.exists():
        return {'workflows': []}
    return json.loads(LIB_CATALOG.read_text(encoding='utf-8'))


def all_items():
    lib = [dict(w, tier='library') for w in library_catalog().get('workflows', [])]
    return core_index() + lib


def normalize_id(ident):
    ident = ident.strip().lower().lstrip('@$/')
    return ident[5:] if ident.startswith('work-') else ident


def find(ident):
    ident = normalize_id(ident)
    for item in all_items():
        if item['id'] == ident:
            return item
    return None


def tokens(text):
    return [t for t in re.findall(r'[\w][\w+#.-]*', text.lower()) if t not in STOP]


def search(query, limit=8, tier=None):
    q = normalize_id(query)
    exact = find(q)
    words = [w for w in tokens(q) if not w.isdigit()]
    raw = tokens(q)
    weights = {w: 1.0 for w in words}
    for a, b in zip(raw, raw[1:]):  # "soc 2" -> soc2 / soc-2, "page cro" -> page-cro
        weights.setdefault(a + b, 1.0); weights.setdefault(a + '-' + b, 1.0)
    for w in words:  # Russian words -> English terms; aliases count less than literal words
        hits = ALIASES.get(w, '').split()
        if not hits and len(w) > 5:  # crude stemming: share the first 5 letters with an alias key
            hits = [t for k, v in ALIASES.items() if k[:5] == w[:5] for t in v.split()]
        for t in hits:
            weights.setdefault(t, 0.7)
    cyrillic = bool(re.search('[а-яё]', q))
    scored = []
    for item in all_items():
        if tier and item['tier'] != tier:
            continue
        ident = item['id']
        id_parts = set(ident.split('-'))
        title_words = set(tokens(item.get('title', '')))
        desc_words = set(tokens(item.get('description', '')))
        score = 0
        for t, wt in weights.items():
            s = 0
            if t == ident: s += 50
            elif t in id_parts: s += 12
            elif len(t) >= 4 and t in ident: s += 6
            if t in title_words: s += 5
            elif len(t) >= 4 and any(w.startswith(t) for w in title_words): s += 3
            if t in desc_words: s += 2
            elif len(t) >= 5 and any(w.startswith(t) for w in desc_words): s += 1
            score += s * wt
        if score >= 10 and ident.endswith(('-ru', '-en')):  # language-specific workflows follow the query language
            score += 8 if ident.endswith('-ru') == cyrillic else -8
        score = int(round(score))
        if score > 0:
            if item['tier'] == 'core': score = int(score * 1.3) + 2
            scored.append((score, item))
    scored.sort(key=lambda p: (-p[0], p[1]['tier'] != 'core', p[1]['id']))
    out = [dict(_short(i), score=s) for s, i in scored[:limit]]
    if exact and (tier is None or exact['tier'] == tier) and (not out or out[0]['id'] != exact['id']):
        out = [o for o in out if o['id'] != exact['id']]
        out.insert(0, dict(_short(exact), score='exact'))
    return out[:limit]


def _short(item):
    keep = ('id', 'tier', 'category', 'title', 'description')
    d = {k: item.get(k, '') for k in keep}
    if len(d['description']) > 240:
        d['description'] = d['description'][:237] + '...'
    return d


def verified_zip():
    cat = library_catalog()
    if not LIB_ZIP.exists():
        raise ValueError('library/library.zip is missing')
    digest = hashlib.sha256(LIB_ZIP.read_bytes()).hexdigest()
    if not cat.get('library_sha256') or digest != cat['library_sha256']:
        raise ValueError('library.zip checksum mismatch - the bundle was modified or damaged')
    return zipfile.ZipFile(LIB_ZIP)


def _safe(info):
    p = PurePosixPath(info.filename)
    if p.is_absolute() or '..' in p.parts or '\\' in info.filename or ':' in info.filename or stat.S_ISLNK(info.external_attr >> 16):
        raise ValueError('unsafe archive member: ' + info.filename)
    return info


def file_manifest():
    data = json.loads(MANIFEST.read_text(encoding='utf-8'))
    if data.get('schema') != 1 or not isinstance(data.get('files'), dict):
        raise ValueError('invalid library manifest')
    return data


def selected_members(z, item):
    prefixes = tuple(item['files']) + ('RUNTIME.md', 'licenses/')
    return [_safe(i) for i in z.infolist()
            if not i.is_dir() and any(i.filename == p or i.filename.startswith(p.rstrip('/') + '/') for p in prefixes)]


def default_dest(ident):
    digest = library_catalog()['library_sha256'][:16]
    user = str(os.getuid()) if hasattr(os, 'getuid') else 'local'
    return Path(tempfile.gettempdir()) / ('stefan-sense-' + user) / digest / ident


def extract(ident, dest=None):
    item = find(ident)
    if not item:
        raise ValueError(f'unknown workflow "{ident}" - try: sense.py search "{ident}"')
    if item['tier'] == 'core':
        return {'id': item['id'], 'tier': 'core', 'workflow': str(ROOT / item['path']),
                'note': 'Core workflows are plain files; nothing to extract.'}
    explicit = dest is not None
    destination = Path(dest).absolute() if explicit else default_dest(item['id'])
    if any(p.is_symlink() for p in [destination, *destination.parents]):
        raise ValueError('destination must not contain symbolic links')
    manifest = file_manifest()['files']
    with verified_zip() as z:
        members = selected_members(z, item)
        required = {f"skills/{item['id']}/INSTRUCTIONS.md", f"skills/{item['id']}/references/workflow.md", 'RUNTIME.md'}
        if not required.issubset({i.filename for i in members}):
            raise ValueError('workflow package is incomplete: ' + item['id'])
        if sum(i.file_size for i in members) > MAX_EXTRACT_BYTES:
            raise ValueError('workflow is unexpectedly large; refusing to extract')
        def intact():
            expected = {i.filename for i in members}
            actual = {p.relative_to(destination).as_posix() for p in destination.rglob('*') if p.is_file() or p.is_symlink()}
            if actual != expected: return False
            for info in members:
                path = destination / info.filename
                if (not path.is_file() or any(p.is_symlink() for p in [path, *path.parents])
                        or hashlib.sha256(path.read_bytes()).hexdigest() != manifest.get(info.filename)):
                    return False
            return True
        if destination.exists():
            if not destination.is_dir():
                raise ValueError('destination must be a directory')
            if intact():
                return _extract_result(item, destination, reused=True)
            if any(destination.iterdir()):
                if explicit:
                    raise ValueError('destination is incomplete, changed, or not empty; choose a NEW empty directory')
                # Preserve the old directory; never delete unrecognized user files.
                destination = Path(tempfile.mkdtemp(prefix=item['id'] + '-', dir=destination.parent))
        destination.parent.mkdir(parents=True, exist_ok=True)
        staging = Path(tempfile.mkdtemp(prefix='.sense-stage-', dir=destination.parent))
        try:
            for info in members:
                data = z.read(info)
                if hashlib.sha256(data).hexdigest() != manifest.get(info.filename):
                    raise ValueError('file checksum mismatch: ' + info.filename)
                target = staging / info.filename
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_bytes(data)
            # Only an empty destination can be replaced. Concurrent creation causes a clean failure.
            if destination.exists():
                destination.rmdir()
            staging.rename(destination)
        finally:
            if staging.exists():
                shutil.rmtree(staging)
    return _extract_result(item, destination, reused=False)


def _extract_result(item, dest, reused):
    base = dest / 'skills' / item['id']
    return {'id': item['id'], 'tier': 'library', 'instructions': str(base / 'INSTRUCTIONS.md'),
            'workflow': str(base / 'references' / 'workflow.md'), 'runtime': str(dest / 'RUNTIME.md'),
            'workspace': str(dest), 'reused_existing_extraction': reused,
            'note': 'Read INSTRUCTIONS.md, RUNTIME.md and workflow.md. Helpers were NOT executed.'}


def show(ident):
    item = find(ident)
    if not item:
        raise ValueError(f'unknown workflow "{ident}"')
    if item['tier'] == 'core':
        return (ROOT / item['path']).read_text(encoding='utf-8')
    res = extract(item['id'])
    parts = [Path(res['runtime']).read_text(encoding='utf-8'), Path(res['instructions']).read_text(encoding='utf-8')]
    wf = Path(res['workflow'])
    if wf.exists():
        parts.append(wf.read_text(encoding='utf-8'))
    parts.append(f"\n[files unpacked to {res['workspace']}; shared rules: {res['runtime']}]")
    return '\n\n'.join(parts)


def check():
    """Check packaged files and syntax. Does not certify external services or execute library helpers."""
    problems = []
    core = core_index()
    ids = [c['id'] for c in core]
    cat = library_catalog()
    lib_ids = [w['id'] for w in cat.get('workflows', [])]
    if len(ids) != len(set(ids)): problems.append('duplicate core ids')
    if len(lib_ids) != len(set(lib_ids)): problems.append('duplicate library ids')
    if set(ids) & set(lib_ids): problems.append('core/library id collision')
    if len(core) != 32 or cat.get('count') != len(lib_ids): problems.append('workflow count mismatch')
    for c in core:
        if not c['description']: problems.append('missing description: ' + c['id'])
    python_count = 0
    manifest = file_manifest()
    for name, digest in manifest.get('bundle_files', {}).items():
        path = ROOT / name
        if not path.is_file() or hashlib.sha256(path.read_bytes()).hexdigest() != digest:
            problems.append('bundle file checksum mismatch: ' + name)
    with verified_zip() as z:
        names = z.namelist()
        if len(names) != len(set(names)): problems.append('duplicate archive members')
        if set(names) != set(manifest['files']): problems.append('manifest/archive inventory differs')
        for info in z.infolist():
            _safe(info)
            data = z.read(info)
            if hashlib.sha256(data).hexdigest() != manifest['files'].get(info.filename):
                problems.append('checksum mismatch: ' + info.filename)
            try:
                if info.filename.endswith('.py'):
                    with warnings.catch_warnings():
                        warnings.simplefilter('ignore', SyntaxWarning)
                        compile(data, info.filename, 'exec')
                    python_count += 1
                elif info.filename.endswith('.json'):
                    json.loads(data)
            except (ValueError, SyntaxError, UnicodeError) as e:
                problems.append(info.filename + ': ' + str(e))
        for w in cat.get('workflows', []):
            selected = {i.filename for i in selected_members(z, w)}
            required = manifest['workflows'].get(w['id'], {}).get('required_files', [])
            if not required: problems.append('missing workflow manifest: ' + w['id'])
            for name in required:
                if name not in selected: problems.append(w['id'] + ': missing dependency ' + name)
        for path in (ROOT / 'scripts').glob('*.py'):
            try: compile(path.read_bytes(), str(path), 'exec')
            except SyntaxError as e: problems.append(str(e))
    return {'core_workflows': len(core), 'library_workflows': len(lib_ids),
            'status': 'ok' if not problems else 'problems', 'problem_count': len(problems),
            'problems': problems[:100], 'library_python_files_compiled': python_count,
            'scope': 'Integrity, required resources and Python/JSON syntax only; run selftest for core functions and doctor for runtime dependencies. External services are not certified.'}


def doctor(workflow=None):
    modules = ['docx', 'openpyxl', 'pptx', 'reportlab', 'pypdf', 'pandas', 'matplotlib']
    local = []
    if workflow:
        item = find(workflow)
        if not item: raise ValueError('unknown workflow: ' + workflow)
        if item['tier'] == 'library':
            meta = file_manifest()['workflows'][item['id']]
            modules = meta.get('external_imports', [])
            local = meta.get('local_imports', [])
    return {'python': sys.version.split()[0], 'modules': {m: probe_module(m) for m in modules},
            'tools': {t: probe_tool(t) for t in ('soffice', 'pdftoppm', 'tesseract')},
            'workflow': workflow, 'bundled_imports': local, 'bundle_root': str(ROOT),
            'note': 'Import/version probes only. API access, credentials and workflow outputs need a task-specific check; missing optional dependencies are reported, never installed automatically.'}


def list_items(category=None, tier=None):
    out = []
    for i in all_items():
        if tier and i['tier'] != tier: continue
        if category and i.get('category') != category: continue
        out.append({'id': i['id'], 'tier': i['tier'], 'category': i.get('category'), 'title': i.get('title')})
    return out


def main(argv=None):
    ap = argparse.ArgumentParser(description='Stefan Sense Bundle workflow router')
    sub = ap.add_subparsers(dest='cmd', required=True)
    p = sub.add_parser('search'); p.add_argument('query', nargs='+'); p.add_argument('--limit', type=int, default=8)
    p.add_argument('--core', action='store_true', help='core workflows only')
    p = sub.add_parser('show'); p.add_argument('id')
    p = sub.add_parser('extract'); p.add_argument('id'); p.add_argument('--dest')
    p = sub.add_parser('list'); p.add_argument('--category'); p.add_argument('--core', action='store_true')
    p.add_argument('--library', action='store_true')
    sub.add_parser('check'); p = sub.add_parser('doctor'); p.add_argument('workflow', nargs='?')
    sub.add_parser('selftest')
    a = ap.parse_args(argv)
    try:
        if a.cmd == 'search':
            res = search(' '.join(a.query), max(1, min(a.limit, 30)), 'core' if a.core else None)
        elif a.cmd == 'show':
            print(show(a.id)); return 0
        elif a.cmd == 'extract':
            res = extract(a.id, a.dest)
        elif a.cmd == 'list':
            res = list_items(a.category, 'core' if a.core else 'library' if a.library else None)
        elif a.cmd == 'check':
            res = check()
        elif a.cmd == 'selftest':
            from selftest import run
            res = run()
        else:
            res = doctor(a.workflow)
        print(json.dumps(res, ensure_ascii=False, indent=2))
        return 1 if a.cmd in ('check', 'selftest') and res['status'] != 'ok' else 0
    except (ValueError, OSError, KeyError, TypeError, zipfile.BadZipFile) as e:
        print('error: ' + str(e), file=sys.stderr)
        return 1


if __name__ == '__main__':
    sys.exit(main())
