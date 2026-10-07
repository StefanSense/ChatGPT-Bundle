"""Portable, offline diagnostic of the bundle's core functions using temporary files."""
from pathlib import Path
import tempfile
import json
import importlib.util


def run():
    import sense, docs, text_scan
    passed, failed, skipped = [], [], []
    def check(name, fn):
        try:
            value = fn()
            if value is False: raise AssertionError('unexpected result')
            passed.append(name)
        except Exception as e: failed.append({'test': name, 'error': type(e).__name__ + ': ' + str(e)})
    def require(condition, label):
        if not condition: raise AssertionError(label)
    with tempfile.TemporaryDirectory(prefix='sense-selftest-') as directory:
        out = Path(directory)
        check('core workflows readable', lambda: all(sense.show(w['id']) for w in sense.core_index()))
        check('SOC 2 search', lambda: any(w['id'] in ('soc2-compliance', 'soc2-audit-prep') for w in sense.search('SOC 2')))
        check('Russian search', lambda: sense.search('очеловечь')[0]['id'] == 'humanize-ru')
        check('core-only filter', lambda: all(w['tier'] == 'core' for w in sense.search('soc2-compliance', tier='core')))
        def extraction():
            r = sense.extract('soc2-compliance', out / 'workflow')
            require(all(Path(r[k]).is_file() for k in ('runtime', 'instructions', 'workflow')), 'missing entrypoint')
            require(sense.extract('soc2-compliance', out/'workflow')['reused_existing_extraction'], 'cache not reused')
            Path(r['workflow']).write_text('changed', encoding='utf-8')
            try: sense.extract('soc2-compliance', out/'workflow')
            except ValueError: return True
            raise AssertionError('modified cache accepted')
        check('extract and cache verification', extraction)
        check('English negation', lambda: bool(text_scan.diff("We don't sell data.", 'We sell data.', 'en')['removed_negations']))
        check('Curly apostrophe negation', lambda: bool(text_scan.diff('We don’t sell data.', 'We sell data.', 'en')['removed_negations']))
        check('Russian names', lambda: 'Пётр' in text_scan.diff('Иван оплатил.', 'Пётр оплатил.', 'ru')['added_capitalized_words'])
        check('numeric diff', lambda: text_scan.diff('До 15% не подтверждено.', '20% подтверждено.', 'ru')['removed_numbers'] == ['15%'])
        spec = {'title':'Проверка', 'subtitle':'Подзаголовок', 'blocks':[{'type':'paragraph','text':'Сумма 42 сум.'},{'type':'table','headers':['Товар','Цена'],'rows':[['А',42]]},{'type':'page_break'},{'type':'paragraph','text':'Страница 2.'}]}
        def document():
            docs.create_docx(spec,str(out/'test.docx'))
            data=docs.inspect_docx(str(out/'test.docx'))
            require(data['tables'][0][1][1]=='42','table lost')
            from docx import Document
            d=Document(out/'test.docx')
            require(d.paragraphs[1].runs[0].italic is True,'subtitle not italic')
            require(abs(d.sections[0].page_width.mm-210)<.1,'page is not A4')
        def pdf():
            docs.create_pdf(spec,str(out/'test.pdf'))
            data=docs.inspect_pdf(str(out/'test.pdf'));require(data['pages']==2,'wrong page count')
            require('Сумма 42' in data['text_by_page'][0],'Cyrillic text lost')
            docs.merge_pdf([str(out/'test.pdf')]*2,str(out/'merged.pdf'))
            require(len(docs.split_pdf(str(out/'merged.pdf'),str(out/'pages'))['outputs'])==4,'merge/split failed')
        def spreadsheet():
            docs.create_xlsx({'sheets':[{'name':'Inputs','rows':[['Value'],[20]]},{'name':'Calc','rows':[['Total'],['=Inputs!A2*2']]},{'name':'Text','formulas':False,'rows':[['Text'],['=literal']]}]},str(out/'test.xlsx'))
            data=docs.inspect_xlsx(str(out/'test.xlsx'))
            require([s['formula_cells'] for s in data['sheets']]==[0,1,0],'formula count incorrect')
        def presentation():
            docs.create_pptx({'title':'Презентация','slides':[{'title':'Таблица','layout':'table','headers':['Товар','Цена'],'rows':[['А',42]]}]},str(out/'test.pptx'))
            data=docs.inspect_pptx(str(out/'test.pptx'));require(data['slides'][1]['tables'][0][1][1]=='42','table missing')
            require(not any(s['outside_slide'] for s in data['slides']),'shape out of bounds')
        for name, modules, fn in [('DOCX', ['docx'], document), ('PDF merge/split', ['reportlab','pypdf'],pdf), ('XLSX',['openpyxl'],spreadsheet),('PPTX',['pptx'],presentation)]:
            missing=[m for m in modules if importlib.util.find_spec(m) is None]
            if missing: skipped.append({'test':name,'reason':'missing '+', '.join(missing)})
            elif name.startswith('PDF') and not docs.find_font({}):skipped.append({'test':name,'reason':'Cyrillic TTF font not found'})
            else: check(name,fn)
        for ext, creator in docs.CREATORS.items():
            def invalid(creator=creator,ext=ext):
                try:creator([],str(out/('invalid'+ext)))
                except docs.SpecError:return True
                raise AssertionError('invalid spec accepted')
            check('spec validation '+ext,invalid)
    return {'status':'problems' if failed else 'partial' if skipped else 'ok',
            'passed':passed,'failed':failed,'skipped':skipped,
            'scope':'Core local smoke tests only; no network or external-service certification.'}

if __name__ == '__main__':
    import sys
    result=run();print(json.dumps(result,ensure_ascii=False,indent=2));sys.exit(0 if result['status']=='ok' else 1)
