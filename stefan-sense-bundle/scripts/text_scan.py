#!/usr/bin/env python3
"""Stefan Sense Bundle - heuristic text scanner for the humanize-ru / humanize-en workflows.

  python scripts/text_scan.py input.txt [--lang ru|en|auto] [--genre general|business|academic|legal|fiction]
  python scripts/text_scan.py result.txt --before input.txt      # also diff numbers, qualifiers, negations
  cat text.txt | python scripts/text_scan.py - --lang ru

Counts editing markers and compares facts between versions. It is NOT an AI-authorship detector and
produces no "quality score". Author: M. Stefan Kassem (Stefan Sense), MIT licence.
"""
import argparse, collections, json, re, statistics, sys
from pathlib import Path

RU = {
    'empty_contrast': r'\bне (?:просто|только)\b',
    'empty_opener': r'\b(?:в современном мире|в условиях (?:современн|быстро|постоянно)\w*|стоит отметить|важно (?:понимать|помнить|отметить)|следует отметить|нельзя не отметить|можно с уверенностью сказать)\b',
    'announcement': r'\b(?:давайте (?:разбер[её]мся|посмотрим|рассмотрим)|погрузимся|самое интересное)\b',
    'bureaucratic': r'\b(?:осуществл\w*|функционировани\w*|в целях|в рамках|данн(?:ый|ая|ое|ые|ого|ой|ом|ым|ых)|является|являются|соответствующ\w*|определ[её]нн(?:ый|ая|ое|ые))\b',
    'inflation': r'\b(?:новый уровень|раскры\w* потенциал|открыва\w* (?:новые )?(?:горизонты|перспективы|возможности)|(?:ключевую|важную) роль|комплексн\w* (?:подход|решени)\w*|уникальн\w*|инновационн\w*)\b',
    'vague_authority': r'\b(?:эксперты (?:считают|отмечают)|исследования показывают|многие специалисты|учёные доказали)\b',
    'summary_opener': r'(?:^|[.!?]\s+)(?:подводя итог|таким образом,|в заключение)',
    'chatbot_residue': r'\b(?:надеюсь, (?:это )?помог|отличный вопрос|вот (?:вариант|пример|текст)\s*:|если хотите, я могу)\b',
}
EN = {
    'staged_contrast': r"\b(?:it'?s not (?:just |only )?\w+[^.]{0,40}, (?:it'?s|but)|not (?:just|only) [^.]{1,60}, but)\b",
    'ai_vocabulary': r'\b(?:delve|tapestry|testament|pivotal|seamless(?:ly)?|robust|landscape|realm|leverag\w+|unlock\w*|elevat\w+|showcas\w+|underscor\w+|intricate|multifaceted|navigate the|game-changer|cutting-edge)\b',
    'empty_opener': r"\b(?:in today'?s (?:fast-paced |digital |modern )?world|it'?s (?:important|worth) (?:to note|noting)|whether you'?re)\b",
    'inflation': r'\b(?:plays? a (?:crucial|pivotal|key|vital) role|stands? as a|serves? as a testament|rich (?:history|heritage)|to the next level)\b',
    'vague_authority': r'\b(?:experts (?:say|agree|believe)|studies show|research suggests|many believe)\b',
    'chatbot_residue': r"\b(?:great question|i hope this helps|certainly!|let me know if you(?:'d| would) like|as an ai\b|here'?s (?:a|the) (?:revised|rewritten) )",
    'colon_reveal': r'(?:^|[.!?]\s+)(?:the (?:result|best part|catch|answer)\??[:?])',
}
QUALIFIERS = {
    'ru': r'\b(?:может|могут|мог(?:ут|ла|ли)?|примерно|около|обычно|часто|иногда|как правило|вероятно|возможно|не обязательно|ожидаем\w*|до|от)\b',
    'en': r'\b(?:may|might|can|could|about|around|approximately|usually|often|sometimes|typically|likely|possibly|up to|at least|roughly)\b',
}
NEGATIONS = {'ru': r'\b(?:не|нет|ни|никогда|без)\b', 'en': r"\b(?:not|no|never|without|none|cannot)\b|\b[A-Za-z]+n['’]t\b"}
DASH = r'\s[—–-]\s|—'
SKIP_IN_GENRE = {'academic': {'bureaucratic', 'vague_authority'}, 'legal': {'bureaucratic', 'empty_opener', 'vague_authority', 'summary_opener'},
                 'business': set(), 'fiction': {'bureaucratic'}, 'general': set()}


def detect_lang(text):
    cyr = len(re.findall(r'[А-Яа-яЁё]', text)); lat = len(re.findall(r'[A-Za-z]', text))
    return 'ru' if cyr >= lat else 'en'


def sentences(text):
    return [s.strip() for s in re.split(r'(?<=[.!?…])\s+', text) if s.strip()]


def scan(text, lang='auto', genre='general'):
    lang = detect_lang(text) if lang == 'auto' else lang
    if lang not in ('ru', 'en'): raise ValueError('lang must be ru, en or auto')
    rules = RU if lang == 'ru' else EN
    words = re.findall(r'\w+', text)
    findings = []
    for cat, pat in rules.items():
        if cat in SKIP_IN_GENRE.get(genre, set()): continue
        for m in re.finditer(pat, text, re.I | re.M):
            findings.append({'category': cat, 'match': m.group(0).strip(), 'offset': m.start()})
    dashes = [m.start() for m in re.finditer(DASH, text) if not re.match(r'\d', text[max(0, m.start() - 1):m.start()] or 'x')]
    lens = [len(re.findall(r'\w+', s)) for s in sentences(text)]
    counts = collections.Counter(f['category'] for f in findings)
    if lang == 'ru':
        yav = len(re.findall(r'\bявля(?:ется|ются)\b', text, re.I))
        counts['является_per_500_words'] = round(500 * yav / len(words), 2) if words else 0
    return {
        'scanner': 'stefan-sense-text-scan/1.1', 'lang': lang, 'genre': genre, 'words': len(words),
        'sentences': len(lens), 'sentence_length': {'mean': round(statistics.mean(lens), 1) if lens else 0,
                                                    'stdev': round(statistics.pstdev(lens), 1) if len(lens) > 1 else 0,
                                                    'max': max(lens) if lens else 0},
        'dash_connectors': len(dashes), 'marker_counts': dict(counts),
        'markers_per_100_words': round(100 * len(findings) / len(words), 2) if words else 0,
        'findings': sorted(findings, key=lambda f: f['offset']),
        'limits': 'Heuristic editing flags only. Not an AI detector; no authorship verdict; no quality score.',
    }


def diff(before, after, lang='auto'):
    lang = detect_lang(before or after) if lang == 'auto' else lang
    if lang not in ('ru', 'en'): raise ValueError('lang must be ru, en or auto')
    before, after = before.replace('’', "'"), after.replace('’', "'")
    num = lambda t: collections.Counter(re.findall(r'(?<!\w)[+−-]?\d+(?:[.,]\d+)*(?:[ \u00a0\u202f]\d{3})*(?:[ \u00a0\u202f]?%)?', t))
    words = lambda pat, t: collections.Counter(m.lower() for m in re.findall(pat, t, re.I))
    names = lambda t: collections.Counter(re.findall(r'\b[A-ZА-ЯЁ][\w-]{1,}', t))
    out = {
        'removed_numbers': list((num(before) - num(after)).elements()),
        'added_numbers': list((num(after) - num(before)).elements()),
        'removed_qualifiers': list((words(QUALIFIERS[lang], before) - words(QUALIFIERS[lang], after)).elements()),
        'removed_negations': list((words(NEGATIONS[lang], before) - words(NEGATIONS[lang], after)).elements()),
        'added_negations': list((words(NEGATIONS[lang], after) - words(NEGATIONS[lang], before)).elements()),
        'added_qualifiers': list((words(QUALIFIERS[lang], after) - words(QUALIFIERS[lang], before)).elements()),
        'removed_capitalized_words': list((names(before) - names(after)).elements())[:30],
        'added_capitalized_words': list((names(after) - names(before)).elements())[:30],
        'length_change_pct': round(100 * (len(after) - len(before)) / len(before), 1) if before else 0,
        'note': 'Review all changes against the source. Capitalized words include sentence starts and are only name candidates; differences are not proof of invented facts. This heuristic cannot certify semantic equivalence.',
    }
    return out


def main(argv=None):
    ap = argparse.ArgumentParser(description='Heuristic RU/EN editing scanner (not an AI detector)')
    ap.add_argument('file', help="text file or '-' for stdin")
    ap.add_argument('--lang', choices=['auto', 'ru', 'en'], default='auto')
    ap.add_argument('--genre', choices=sorted(SKIP_IN_GENRE), default='general')
    ap.add_argument('--before', help='original text file to compare facts with')
    ap.add_argument('--summary', action='store_true', help='omit the per-match list')
    a = ap.parse_args(argv)
    text = sys.stdin.read() if a.file == '-' else Path(a.file).read_text(encoding='utf-8')
    res = scan(text, a.lang, a.genre)
    if a.before:
        before = Path(a.before).read_text(encoding='utf-8')
        res['before'] = {k: v for k, v in scan(before, res['lang'], a.genre).items() if k != 'findings'}
        res['diff'] = diff(before, text, res['lang'])
    if a.summary:
        res.pop('findings', None)
    print(json.dumps(res, ensure_ascii=False, indent=2))
    return 0


if __name__ == '__main__':
    try:
        sys.exit(main())
    except (OSError, UnicodeError, ValueError) as e:
        print('error: ' + str(e), file=sys.stderr)
        sys.exit(1)
