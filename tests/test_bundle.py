"""Tests for the Stefan Sense Bundle scripts. Run: python -m pytest -q  (builds the bundle first if needed)."""
import importlib.util, json, subprocess, sys, zipfile
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parent.parent
STAGE = REPO / 'build' / 'stefan-sense-bundle'


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
    return mod


@pytest.fixture(scope='session')
def bundle():
    if not (STAGE / 'library' / 'library.zip').exists():
        subprocess.run([sys.executable, str(REPO / 'tools' / 'build.py')], check=True, capture_output=True)
    return STAGE


@pytest.fixture(scope='session')
def sense(bundle):
    return load('sense', bundle / 'scripts' / 'sense.py')


docs = load('docs', REPO / 'skill' / 'scripts' / 'docs.py')
scan = load('text_scan', REPO / 'skill' / 'scripts' / 'text_scan.py')


# ---------------------------------------------------------------- router
def test_check_passes(sense):
    res = sense.check()
    assert res['status'] == 'ok', res['problems']
    assert res['core_workflows'] >= 30 and res['library_workflows'] > 500


@pytest.mark.parametrize('query,expected', [
    ('очеловечь текст', 'humanize-ru'), ('убери канцелярит', 'humanize-ru'), ('переведи договор', 'translate'),
    ('сделай презентацию', 'presentations'), ('таблица excel бюджет', 'spreadsheets'), ('проверь факты', 'fact-check'),
    ('landing page copy', 'copywriting'), ('meeting minutes', 'meeting'), ('коммерческое предложение кп', 'sales'),
    ('work-copywriting', 'copywriting'), ('резюме для вакансии', 'career'), ('seo-audit', 'seo-audit'),
])
def test_search_routes(sense, query, expected):
    ids = [r['id'] for r in sense.search(query, limit=3)]
    assert expected in ids, (query, ids)


def test_show_core(sense):
    text = sense.show('copywriting')
    assert 'Corey Haines' in text and text.startswith('---')


def test_extract_library_only_needed_files(sense, tmp_path):
    res = sense.extract('seo-audit', tmp_path / 'x')
    instr = Path(res['instructions']).read_text(encoding='utf-8')
    assert 'Stefan Sense' in instr and 'Alireza Rezvani' in instr
    assert Path(res['workflow']).is_file() and Path(res['runtime']).is_file()
    extracted = [p for p in (tmp_path / 'x').rglob('*') if p.is_file()]
    assert 0 < len(extracted) < 200  # not the whole library
    # every resource link in the workflow resolves inside the extraction
    wf = Path(res['workflow'])
    for link in __import__('re').findall(r'\]\((\.\./[^)#]+)\)', wf.read_text(encoding='utf-8')):
        assert (wf.parent / link).resolve().exists(), link
    again = sense.extract('seo-audit', tmp_path / 'x')
    assert again['reused_existing_extraction']


def test_unknown_id(sense):
    with pytest.raises(ValueError):
        sense.extract('definitely-not-a-workflow')


def test_all_library_dependencies_resolve(bundle, sense):
    cat = json.loads((bundle / 'library' / 'catalog.json').read_text(encoding='utf-8'))
    with zipfile.ZipFile(bundle / 'library' / 'library.zip') as z:
        names = z.namelist()
    for w in cat['workflows']:
        for f in w['files']:
            assert any(n == f or n.startswith(f) for n in names), (w['id'], f)


# ---------------------------------------------------------------- documents
SPEC = {'title': 'Отчёт Q3', 'subtitle': 'Тест', 'author': 'Stefan Sense', 'blocks': [
    {'type': 'heading', 'text': 'Итоги', 'level': 1}, {'type': 'paragraph', 'text': 'Выручка выросла на 12 %.'},
    {'type': 'bullets', 'items': ['Один', 'Два']}, {'type': 'table', 'headers': ['A', 'B'], 'rows': [['1', '2']]}]}


def test_docx_roundtrip(tmp_path):
    out = tmp_path / 'r.docx'
    docs.create_docx(SPEC, str(out))
    info = docs.inspect_docx(str(out))
    assert 'Итоги' in info['headings'] and info['tables'] == [[['A', 'B'], ['1', '2']]]


def test_pdf_roundtrip_and_merge_split(tmp_path):
    if not docs.find_font({}):
        pytest.skip('no unicode font available')
    a, b = tmp_path / 'a.pdf', tmp_path / 'b.pdf'
    docs.create_pdf(SPEC, str(a)); docs.create_pdf(dict(SPEC, blocks=[{'type': 'page_break'}] + SPEC['blocks']), str(b))
    assert 'Итоги' in ''.join(docs.inspect_pdf(str(a))['text_by_page'])
    docs.merge_pdf([str(a), str(b)], str(tmp_path / 'm.pdf'))
    total = docs.inspect_pdf(str(tmp_path / 'm.pdf'))['pages']
    assert total == docs.inspect_pdf(str(a))['pages'] + docs.inspect_pdf(str(b))['pages']
    assert len(docs.split_pdf(str(tmp_path / 'm.pdf'), str(tmp_path / 'parts'))['outputs']) == total


def test_pdf_requires_font_for_cyrillic(tmp_path, monkeypatch):
    monkeypatch.setattr(docs, 'FONT_CANDIDATES', [])
    with pytest.raises(docs.SpecError):
        docs.create_pdf(SPEC, str(tmp_path / 'x.pdf'))


def test_xlsx_formulas_and_text_safety(tmp_path):
    out = tmp_path / 't.xlsx'
    docs.create_xlsx({'sheets': [{'name': 'Calc', 'rows': [['Q', 'P', 'T'], [2, 10, '=A2*B2']]},
                                 {'name': 'Raw', 'formulas': False, 'rows': [['note'], ['=HYPERLINK("http://x")']]}]}, str(out))
    from openpyxl import load_workbook
    wb = load_workbook(out)
    assert wb['Calc']['C2'].data_type == 'f'
    assert wb['Raw']['A2'].data_type == 's'
    info = docs.inspect_xlsx(str(out))
    assert info['sheets'][0]['formula_cells'] == 1


def test_pptx_roundtrip(tmp_path):
    out = tmp_path / 'd.pptx'
    docs.create_pptx({'title': 'Deck', 'slides': [
        {'layout': 'bullets', 'title': 'Рост 12 %', 'bullets': ['a', 'b'], 'notes': 'n'},
        {'layout': 'section', 'title': 'Part 2'},
        {'layout': 'table', 'title': 'T', 'headers': ['x', 'y'], 'rows': [[1, 2]]}]}, str(out))
    info = docs.inspect_pptx(str(out))
    assert info['count'] == 4 and info['slides'][1]['notes'] == 'n'


def test_bad_table_rejected(tmp_path):
    with pytest.raises(docs.SpecError):
        docs.create_docx({'blocks': [{'type': 'table', 'headers': ['a', 'b'], 'rows': [['1']]}]}, str(tmp_path / 'x.docx'))


def test_docs_cli_create(tmp_path):
    spec = tmp_path / 's.json'; spec.write_text(json.dumps(SPEC, ensure_ascii=False), encoding='utf-8')
    assert docs.main(['create', str(spec), str(tmp_path / 'o.docx')]) == 0
    assert docs.main(['create', str(spec), str(tmp_path / 'o.txt')]) == 1


# ---------------------------------------------------------------- scanner
def test_scan_ru_markers():
    r = scan.scan('В современном мире данный подход является ключевым. Это не просто инструмент, а комплексное решение.', 'ru')
    assert r['marker_counts']['empty_opener'] >= 1 and r['marker_counts']['empty_contrast'] == 1
    assert r['marker_counts']['bureaucratic'] >= 2


def test_scan_en_markers():
    r = scan.scan("In today's fast-paced world, we delve into a seamless landscape. Great question! I hope this helps.", 'en')
    assert r['marker_counts']['ai_vocabulary'] >= 3 and r['marker_counts']['chatbot_residue'] >= 2


def test_scan_diff_detects_fact_changes():
    d = scan.diff('Примерно 30 % клиентов могут не заметить.', 'Клиенты заметят: 45 %.', 'ru')
    assert '30 %' in d['removed_numbers'] and '45 %' in d['added_numbers']
    assert 'примерно' in d['removed_qualifiers'] and 'не' in d['removed_negations']


def test_scan_auto_lang():
    assert scan.scan('Hello world, this is English.')['lang'] == 'en'
    assert scan.scan('Привет, это русский текст.')['lang'] == 'ru'
