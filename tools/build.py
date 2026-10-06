#!/usr/bin/env python3
"""Build and validate the Stefan Sense Bundle archive.

    python tools/build.py            # -> dist/Stefan-Sense-Bundle-v<VERSION>.zip

Steps: validate core workflows -> pack library/ into library.zip with a dependency-aware catalog ->
stage skill/ + licenses/ -> validate against ChatGPT skill upload limits -> write a deterministic zip.
"""
import hashlib, json, os, re, shutil, sys, zipfile
from pathlib import Path, PurePosixPath

REPO = Path(__file__).resolve().parent.parent
SKILL = REPO / 'skill'
LIB = REPO / 'library'
LICENSES = REPO / 'licenses'
BUILD = REPO / 'build'
DIST = REPO / 'dist'
TOP = 'stefan-sense-bundle'
FIXED_DATE = (2026, 10, 6, 0, 0, 0)

# Conservative limits published for OpenAI skills uploads (checked 2026-10): one SKILL.md per bundle,
# <= 500 files, zip <= 50 MB, each uncompressed file <= 25 MB. Name/description follow the Agent Skills spec.
MAX_FILES, MAX_ZIP, MAX_FILE = 500, 50 * 1024 * 1024, 25 * 1024 * 1024
NAME_RE = re.compile(r'^[a-z0-9]+(?:-[a-z0-9]+)*$')
LINK = re.compile(r'(?:\]\(|`)((?:\.\./|\./)?[A-Za-z0-9_./-]+\.(?:md|py|js|mjs|ts|json|sh|txt|html|csv|yaml|yml|sql|ttf|png|svg|jpg|template))(?:#[^)`]*)?[)`]')
ORIGINS = {
    'core': {'project': 'claude-skills', 'author': 'Alireza Rezvani', 'license': 'MIT', 'url': 'https://github.com/alirezarezvani/claude-skills'},
    'ecc': {'project': 'everything-claude-code (ECC)', 'author': 'Affaan Mustafa', 'license': 'MIT', 'url': 'https://github.com/affaan-m/everything-claude-code'},
    'docs': {'project': 'anthropics/skills (example skills)', 'author': 'Anthropic, PBC', 'license': 'Apache-2.0', 'url': 'https://github.com/anthropics/skills'},
    'loop': {'project': 'Loop Library (via claude-skills)', 'author': 'Forward Future', 'license': 'MIT', 'url': 'https://github.com/alirezarezvani/claude-skills'},
}


def frontmatter(text):
    m = re.match(r'^---\n(.*?)\n---\n', text, re.S)
    if not m:
        return None
    out = {}
    for line in m.group(1).splitlines():
        if ':' in line:
            k, v = line.split(':', 1)
            out[k.strip()] = v.strip()
    return out


def fail(msg):
    print('BUILD FAILED: ' + msg, file=sys.stderr)
    sys.exit(1)


def validate_core():
    ids = []
    for wf in sorted((SKILL / 'core').glob('*/WORKFLOW.md')):
        fm = frontmatter(wf.read_text(encoding='utf-8'))
        if not fm: fail(f'{wf}: missing frontmatter')
        for key in ('id', 'title', 'description', 'based_on', 'author'):
            if not fm.get(key): fail(f'{wf}: missing {key}')
        if fm['id'] != wf.parent.name: fail(f'{wf}: id does not match folder')
        if not NAME_RE.match(fm['id']): fail(f'{wf}: bad id')
        ids.append(fm['id'])
    return ids


def closure(workflow_id, base, names_on_disk):
    """Files/folders a library workflow needs: its folder, its resource base, and linked resources."""
    needed = {f'skills/{workflow_id}/'}
    if base:
        needed.add(base.rstrip('/') + '/')
    queue = [p for p in (LIB / 'skills' / workflow_id).rglob('*.md')]
    seen = set()
    while queue:
        md = queue.pop()
        if md in seen: continue
        seen.add(md)
        text = md.read_text(encoding='utf-8', errors='ignore')
        for link in LINK.findall(text):
            target = os.path.normpath(os.path.join(md.parent.relative_to(LIB), link)).replace(os.sep, '/')
            if target.startswith('resources/') and target in names_on_disk:
                if not any(target.startswith(n) for n in needed if n.endswith('/')):
                    needed.add(target)
                    if target.endswith('.md'): queue.append(LIB / target)
    return sorted(needed)


def build_library(core_ids):
    index = json.loads((LIB / 'index.json').read_text(encoding='utf-8'))
    names_on_disk = {str(p.relative_to(LIB)).replace(os.sep, '/') for p in LIB.rglob('*') if p.is_file()}
    workflows = []
    for r in index:
        if r['id'] in core_ids: fail('library id clashes with core: ' + r['id'])
        files = closure(r['id'], r.get('resource_base'), names_on_disk)
        workflows.append({'id': r['id'], 'title': r['title'], 'category': r['category'], 'description': r['description'],
                          'origin': ORIGINS[r['origin']], 'adapted_by': 'M. Stefan Kassem (Stefan Sense)', 'files': files})
    out_dir = BUILD / 'library'
    out_dir.mkdir(parents=True, exist_ok=True)
    zpath = out_dir / 'library.zip'
    members = sorted(n for n in names_on_disk if n.startswith(('skills/', 'resources/')) or n == 'RUNTIME.md')
    with zipfile.ZipFile(zpath, 'w', zipfile.ZIP_DEFLATED, compresslevel=9) as z:
        for n in members:
            _add(z, LIB / n, n)
        for lic in sorted(LICENSES.iterdir()):
            _add(z, lic, 'licenses/' + lic.name)
    digest = hashlib.sha256(zpath.read_bytes()).hexdigest()
    catalog = {'bundle': 'Stefan Sense Bundle', 'author': 'M. Stefan Kassem (Stefan Sense)',
               'library_sha256': digest, 'count': len(workflows), 'workflows': workflows}
    (out_dir / 'catalog.json').write_text(json.dumps(catalog, ensure_ascii=False, indent=1), encoding='utf-8')
    return zpath, out_dir / 'catalog.json', len(workflows)


def _add(z, src, arcname):
    info = zipfile.ZipInfo(arcname, FIXED_DATE)
    info.compress_type = zipfile.ZIP_DEFLATED
    info.external_attr = (0o755 if src.suffix in ('.py', '.sh') else 0o644) << 16
    z.writestr(info, src.read_bytes())


def stage(lib_zip, catalog):
    dst = BUILD / TOP
    if dst.exists(): shutil.rmtree(dst)
    shutil.copytree(SKILL, dst, ignore=shutil.ignore_patterns('__pycache__', '*.pyc', '.DS_Store'))
    shutil.copytree(LICENSES, dst / 'licenses')
    (dst / 'library').mkdir()
    shutil.copy2(lib_zip, dst / 'library' / 'library.zip')
    shutil.copy2(catalog, dst / 'library' / 'catalog.json')
    return dst


def validate_stage(dst):
    files = [p for p in dst.rglob('*') if p.is_file() or p.is_symlink()]
    skill_md = [p for p in files if p.name.lower() == 'skill.md']
    if len(skill_md) != 1 or skill_md[0].parent != dst: fail('exactly one SKILL.md at the bundle root is required')
    if len(files) > MAX_FILES: fail(f'{len(files)} files > {MAX_FILES}')
    for p in files:
        if p.is_symlink(): fail('symlink: ' + str(p))
        if p.stat().st_size > MAX_FILE: fail(f'file too large: {p}')
        rel = str(p.relative_to(dst))
        if not rel.isascii(): fail('non-ASCII path: ' + rel)
    fm = frontmatter(skill_md[0].read_text(encoding='utf-8'))
    if not fm or set(fm) != {'name', 'description'}: fail('SKILL.md frontmatter must contain exactly name and description')
    name = fm['name']; desc = fm['description'].strip('"')
    if not NAME_RE.match(name) or len(name) > 64 or name != TOP: fail('invalid skill name: ' + name)
    if not 1 <= len(desc) <= 1024: fail(f'description length {len(desc)} not in 1..1024')
    if any(c in desc for c in '<>'): fail('description must not contain angle brackets')
    return len(files)


def write_zip(dst, version):
    DIST.mkdir(exist_ok=True)
    out = DIST / f'Stefan-Sense-Bundle-v{version}.zip'
    with zipfile.ZipFile(out, 'w', zipfile.ZIP_DEFLATED, compresslevel=9) as z:
        for p in sorted(dst.rglob('*')):
            if p.is_file():
                _add(z, p, f'{TOP}/' + str(p.relative_to(dst)).replace(os.sep, '/'))
    with zipfile.ZipFile(out) as z:
        if z.testzip() is not None: fail('CRC check failed')
        for n in z.namelist():
            q = PurePosixPath(n)
            if q.is_absolute() or '..' in q.parts: fail('unsafe path in zip')
    if out.stat().st_size > MAX_ZIP: fail('zip larger than 50 MB')
    return out


def main():
    version = (SKILL / 'VERSION').read_text().strip()
    core_ids = validate_core()
    if BUILD.exists(): shutil.rmtree(BUILD)
    lib_zip, catalog, n_lib = build_library(set(core_ids))
    dst = stage(lib_zip, catalog)
    n_files = validate_stage(dst)
    out = write_zip(dst, version)
    sha = hashlib.sha256(out.read_bytes()).hexdigest()
    (DIST / (out.name + '.sha256')).write_text(f'{sha}  {out.name}\n')
    print(json.dumps({'archive': str(out.relative_to(REPO)), 'size_mb': round(out.stat().st_size / 1e6, 2),
                      'files_in_skill': n_files, 'core_workflows': len(core_ids), 'library_workflows': n_lib,
                      'library_zip_mb': round(lib_zip.stat().st_size / 1e6, 2), 'sha256': sha}, indent=2))


if __name__ == '__main__':
    main()
