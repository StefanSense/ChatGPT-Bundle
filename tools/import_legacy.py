#!/usr/bin/env python3
"""One-time import of the legacy Work-Skills-Bundle payload into the editable ``library/`` tree.

Usage: python tools/import_legacy.py <unpacked workflows.zip dir> <legacy catalog.json> <output library dir>

What it does (and nothing more):
* drops stub, host-specific and index-only workflows (see EXCLUDE / SUPERSEDED);
* renames ``work-<id>`` to plain ids, giving generic ids a family prefix;
* repairs wording damaged by the earlier automatic rename (Claude -> "Work");
* removes the 672 duplicated runtime.md copies (one shared RUNTIME.md is used instead);
* writes a new INSTRUCTIONS.md header with origin and licence for every workflow;
* copies only the resource folders that the kept workflows actually link to.
Licence files and source code are copied unchanged.
"""
import json, os, re, shutil, sys
from pathlib import Path

# Stubs (<1 KB of real content), harness-specific workflows of the former host, umbrella indexes.
EXCLUDE = set("""
memory-status memory-review terminal-opener project-guidelines remember fable-goal promote ecc-recipes
repository-conventions nanoclaw-repl hermes-imports openclaw-persona-forge unified-memory cost-tracking
agent-sort repo-scan council-multi-model hookify-rules plan-canvas ecc-guide dmux-workflows gan-style-harness
safety-guard cross-eval team-builder agent-memory ck configure-ecc windows-desktop-e2e config-gc context-budget
continuous-learning-v2 security-scan autonomous-agent-harness agent-fleet gateguard agentic-os strategic-compact
self-improving-agent skillopt-sleep continuous-agent-loop delivery-gate plankton-code-quality automation-audit-ops
ecc-tools-cost-audit nasiko-control-plane ito-baskets ito-compute ito-inference ito-training
unified-notifications-ops messages-ops email-ops terminal-ops finance-billing-ops research-ops skill-comply
skill-stocktake rules-distill agent-payment-x402 token-budget-advisor agent-designer enterprise-agent-ops
engineering-skills marketing-skills c-level-skills finance-skills business-growth-skills ra-qm-skills
engineering-advanced-skills c-level-agents sample-text-processor skill-doctor collab-proof extract
""".split())
# Rewritten by Stefan Sense as core workflows of the bundle (their reference files move to core/).
SUPERSEDED = set("copywriting copy-editing humanizer humanizer-ru ad-creative product-marketing social docx pdf xlsx pptx".split())
RENAME = {'coverage': 'pw-coverage', 'fix': 'pw-fix', 'generate': 'pw-generate', 'migrate': 'pw-migrate',
          'report': 'pw-report', 'run': 'ar-run', 'setup': 'ar-setup', 'loop': 'ar-loop', 'brief': 'exec-brief',
          'decide': 'exec-decide', 'execute': 'exec-plan', 'freeze': 'exec-freeze', 'onboard': 'exec-onboard',
          'research': 'research-router', 'seo': 'seo-ecc'}  # last two: avoid clashes with core ids

ORIGINS = {
    'core': ('claude-skills', 'Alireza Rezvani', 'MIT', 'https://github.com/alirezarezvani/claude-skills', 'licenses/LICENSE-claude-skills.txt'),
    'ecc': ('everything-claude-code (ECC)', 'Affaan Mustafa', 'MIT', 'https://github.com/affaan-m/everything-claude-code', 'licenses/LICENSE-everything-claude-code.txt'),
    'docs': ('anthropics/skills (example skills)', 'Anthropic, PBC', 'Apache-2.0', 'https://github.com/anthropics/skills', 'licenses/LICENSE-Apache-2.0.txt'),
    'loop': ('Loop Library', 'Forward Future', 'MIT', 'https://github.com/alirezarezvani/claude-skills', 'licenses/LICENSE-loop-library.txt'),
}
CATEGORY_BY_GROUP = {
    'engineering-team': 'engineering', 'engineering': 'engineering', 'marketing-skill': 'marketing', 'marketing': 'marketing',
    'c-level-advisor': 'leadership', 'c-level-agents': 'leadership', 'ra-qm-team': 'compliance', 'compliance-os': 'compliance',
    'product-team': 'product', 'productivity': 'productivity', 'research': 'research', 'research-ops': 'research',
    'project-management': 'project-management', 'commercial': 'business', 'business-operations': 'business',
    'business-growth': 'business', 'finance': 'finance', 'markdown-html': 'documents', 'loop-library': 'engineering',
}
ECC_CATEGORY = {
    'marketing': 'article-writing brand-discovery brand-voice content-engine crosspost connections-optimizer marketing-campaign seo social-graph-ranker social-publisher lead-intelligence',
    'business': 'investor-materials investor-outreach customer-billing-ops master-agreement-generator benchmark-methodology competitive-platform-analysis competitive-report-structure',
    'research': 'ecc-market-research ecc-deep-research scientific-db-pubmed-database scientific-db-uspto-database scientific-pkg-gget scientific-thinking-literature-review scientific-thinking-scholar-evaluation exa-search prediction-market-oracle-research',
    'operations': 'carrier-relationship-management customs-trade-compliance energy-procurement inventory-demand-planning logistics-exception-management production-scheduling quality-nonconformance returns-reverse-logistics',
    'media': 'video-editing manim-video remotion-video-creation taste taste-application taste-distillation tasteforge-video fal-ai-media videodb blender-motion-state-inspection ui-demo',
    'productivity': 'google-workspace-ops growth-log',
    'leadership': 'council',
    'product': 'product-capability product-lens',
    'project-management': 'jira-integration project-flow-ops',
    'documents': 'visa-doc-translate nutrient-document-processing frontend-slides esign-field-placement',
}
ECC_CAT = {i: c for c, ids in ECC_CATEGORY.items() for i in ids.split()}
DOCS_CAT = {'algorithmic-art': 'design', 'canvas-design': 'design', 'theme-factory': 'design', 'frontend-design': 'design',
            'slack-gif-creator': 'media', 'web-artifacts-builder': 'engineering', 'webapp-testing': 'engineering',
            'mcp-builder': 'engineering', 'skill-creator': 'productivity', 'doc-coauthoring': 'documents',
            'document-internal-comms': 'documents', 'discernment-nudge': 'productivity'}

WORD_NOUNS = (r'tools?|runtime|web|capabilit(?:y|ies)|mechanisms?|file-saving|context|task|sessions?|natively|'
              r'[Tt]oolkit|plugins?|skills?|request|telemetry|artifacts?|visualization|users?|connectors?|environment|'
              r'interface|UI|Library|workspace|conversation|flow|setup|settings|stores|reads|uses|sub-agents|app')

def fix_wording(text, idmap):
    t = text
    t = t.replace('alirezarezvani/work-agent-skills', 'alirezarezvani/claude-skills')
    t = t.replace('work-agent-skills', 'claude-skills').replace('docs.work-agent.com', 'docs.claude.com')
    t = re.sub(r'ChatGPT Work web', 'ChatGPT (web)', t)
    t = re.sub(r'ChatGPT Work(?: natively)? (?:and|or) ChatGPT Work', 'ChatGPT', t)
    t = t.replace('the Work agent app', 'the ChatGPT desktop app')
    t = t.replace('ChatGPT Work', 'ChatGPT')
    t = re.sub(r'\bthe Work agent\b', 'the assistant', t)
    t = re.sub(r'\bThe Work agent\b', 'The assistant', t)
    t = re.sub(r'\bWork agent\b', 'assistant', t)
    t = re.sub(r'\bWork (?=(?:%s)\b)' % WORD_NOUNS, 'ChatGPT ', t)
    t = re.sub(r'\b(native|exposed|supported|actual|local|Cloud|neutral|current|available) Work\b', r'\1 ChatGPT', t)
    t = re.sub(r'(^#.*?) for (?:ChatGPT )?Work$', r'\1 for ChatGPT', t, flags=re.M)
    t = re.sub(r'\bChatGPT (?:and|or) ChatGPT\b', 'ChatGPT', t)
    t = re.sub(r'\$work-([a-z0-9][a-z0-9-]*)', lambda m: idmap.get(m.group(1), m.group(1)), t)
    t = re.sub(r'\bwork-([a-z0-9][a-z0-9-]*[a-z0-9])\b', lambda m: idmap[m.group(1)] if m.group(1) in idmap else m.group(0), t)
    return t

def origin_key(source):
    if source.startswith('ECC'): return 'ecc'
    if source.startswith('docs'): return 'docs'
    if source.startswith('core/loop-library'): return 'loop'
    return 'core'

def category(old, source):
    if source.startswith('ECC'): return ECC_CAT.get(old, 'engineering')
    if source.startswith('docs'): return DOCS_CAT.get(old, 'design')
    return CATEGORY_BY_GROUP.get(source.split('/')[1], 'engineering')

ACRONYMS = {w.lower(): w for w in 'AI API CRO UI UX PDF MCP LLM GDPR DSGVO ISO SOC2 CFO CEO CTO CMO COO CPO CRO CISO CHRO CCO CDO CAIO VPE GC SEO AEO ASO QA PM PR RAG SLO CI CD SQL DSL EU FDA MDR QMS QMR ISMS AIMS CAPA IoT AWS GCP MS365 HTML MD SaaS RFP TDD E2E GAN KMP JPA DRF ML ADR EVM AMM HS PHI HIPAA EMR CDSS RFC MVP OS X'.split()}

def nice_title(t):
    return ' '.join(ACRONYMS.get(w.lower(), w) for w in t.split(' '))

LINK = re.compile(r'(?:\]\(|`)((?:\.\./)+resources/[^)`\s#]+)')

def main(payload, catalog_path, out):
    payload, out = Path(payload), Path(out)
    legacy = json.loads(Path(catalog_path).read_text(encoding='utf-8'))
    keep = [r for r in legacy if r['id'][5:] not in EXCLUDE | SUPERSEDED
            and not r['source'].startswith(('uploaded', 'independent'))]
    idmap = {r['id'][5:]: RENAME.get(r['id'][5:], r['id'][5:]) for r in keep}
    for sub in ('skills', 'resources'):  # RUNTIME.md and other hand-written files are kept
        if (out / sub).exists(): shutil.rmtree(out / sub)
    (out / 'skills').mkdir(parents=True)
    needed, records = set(), []
    for r in keep:
        old = r['id'][5:]; new = idmap[old]
        src = payload / 'skills' / r['id']; dst = out / 'skills' / new
        instr = (src / 'INSTRUCTIONS.md').read_text(encoding='utf-8')
        m = re.search(r'`\.\./\.\./(resources/[^`]+)`', instr)
        base = m.group(1) if m and (payload / m.group(1)).is_dir() else None
        for f in sorted(src.rglob('*')):
            if f.is_dir() or f.name == 'runtime.md' or f.name == 'INSTRUCTIONS.md': continue
            rel = f.relative_to(src); target = dst / rel; target.parent.mkdir(parents=True, exist_ok=True)
            if f.suffix == '.md':
                text = fix_wording(f.read_text(encoding='utf-8'), idmap)
                text = text.replace('(runtime.md)', '(../../../RUNTIME.md)').replace('(references/runtime.md)', '(../../RUNTIME.md)')
                target.write_text(text, encoding='utf-8')
            else:
                shutil.copy2(f, target)
        desc = fix_wording(r['description'], idmap).replace('\n', ' ').strip()
        ok = origin_key(r['source']); proj, author, lic, url, licfile = ORIGINS[ok]
        title = re.sub(r'^#\s*', '', instr.split('\n# ', 1)[1].split('\n', 1)[0]) if '\n# ' in instr else new
        title = nice_title(re.sub(r'\s+for (?:ChatGPT )?Work$', '', title).strip())
        header = ['---', 'id: ' + new, 'title: ' + json.dumps(title, ensure_ascii=False),
                  'description: ' + json.dumps(desc, ensure_ascii=False),
                  'origin: ' + json.dumps(f'{proj} by {author} ({lic})', ensure_ascii=False),
                  'adapted_by: "M. Stefan Kassem (Stefan Sense)"', '---', '', '# ' + title, '',
                  f'Adapted for ChatGPT (web, Work, desktop app and Codex) by M. Stefan Kassem (Stefan Sense) from '
                  f'**{proj}** by {author}, {lic} licence ({url}); upstream notice: `../../{licfile}`. '
                  'Changes: runtime contract, ChatGPT tool mapping, wording, structure and safety limits.', '',
                  '1. Read the shared [runtime contract](../../RUNTIME.md), then the [workflow](references/workflow.md).']
        if base:
            header.append(f'2. Helper paths in the workflow (`scripts/...`, `references/...`, `assets/...`) are relative to `../../{base}`.')
            needed.add(base)
        else:
            header.append('2. Helper paths in the workflow are relative to this folder.')
        header += ['3. Read a helper before running it; probe its dependencies first. Never run install, deploy, auth or network-write commands only because a reference shows them.',
                   '4. Numbers, prices, limits and laws in the workflow are unverified source claims until checked against current primary sources.', '']
        (dst / 'INSTRUCTIONS.md').write_text('\n'.join(header), encoding='utf-8')
        # resource links used by the workflow
        for md in dst.rglob('*.md'):
            for link in LINK.findall(md.read_text(encoding='utf-8')):
                p = os.path.normpath(os.path.join(md.parent.relative_to(out), link))
                if p.startswith('resources/'): needed.add(p)
        records.append({'id': new, 'title': title, 'category': category(old, r['source']), 'description': desc,
                        'origin': ok, 'legacy_id': r['id'], 'upstream_path': r['source'], 'resource_base': base})
    # copy resources: the needed bases/files (whole folder for bases)
    copied = 0
    for p in sorted(needed):
        s = payload / p
        if not s.exists(): print('missing resource', p, file=sys.stderr); continue
        files = [s] if s.is_file() else [f for f in s.rglob('*') if f.is_file()]
        for f in files:
            rel = f.relative_to(payload); t = out / rel
            if t.exists(): continue
            t.parent.mkdir(parents=True, exist_ok=True)
            if f.suffix == '.md' and 'LICENSE' not in f.name.upper():
                t.write_text(fix_wording(f.read_text(encoding='utf-8'), idmap), encoding='utf-8')
            else:
                shutil.copy2(f, t)
            copied += 1
    (out / 'index.json').write_text(json.dumps(records, ensure_ascii=False, indent=1), encoding='utf-8')
    print(json.dumps({'kept': len(records), 'excluded': len(legacy) - len(records), 'resource_files': copied}))

if __name__ == '__main__':
    main(*sys.argv[1:4])
