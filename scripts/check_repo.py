#!/usr/bin/env python3
"""Check portable file layout, JSON, local Markdown links and Python syntax without third-party packages."""
import ast
import json
import re
import hashlib
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def main():
    errors = []
    for rel in ['AGENTS.md', 'SOP.md', 'CREATOR_GROWTH.md', 'LAUNCH_TASK.txt',
                '.agents/skills/video-production-director/SKILL.md', 'resources/catalog.json']:
        if not (ROOT / rel).is_file():
            errors.append(f'missing: {rel}')
    counts = {'json': 0, 'python': 0, 'markdown': 0}
    for p in ROOT.rglob('*'):
        if not p.is_file() or any(part in {'.git', '__pycache__', 'node_modules', '.venv', 'frames', 'cache'} for part in p.relative_to(ROOT).parts):
            continue
        try:
            if p.suffix == '.json':
                json.loads(p.read_text()); counts['json'] += 1
            elif p.suffix == '.py':
                ast.parse(p.read_text(), filename=str(p)); counts['python'] += 1
            elif p.suffix == '.md':
                counts['markdown'] += 1
                for href in re.findall(r'\]\(([^)]+)\)', p.read_text()):
                    if href.startswith(('http:', 'https:', 'mailto:', '#', '/')):
                        continue
                    target = href.split('#', 1)[0]
                    if target and not (p.parent / target).exists():
                        errors.append(f'{p.relative_to(ROOT)}: missing linked file {href}')
        except (ValueError, SyntaxError, OSError) as exc:
            errors.append(f'{p.relative_to(ROOT)}: {exc}')
    skill = ROOT / '.agents/skills/video-production-director/SKILL.md'
    if skill.exists():
        text = skill.read_text()
        if not text.startswith('---\n') or len(text.split('---', 2)) < 3:
            errors.append('invalid skill frontmatter')
        elif not all(re.search(rf'^{key}:\s*\S', text.split('---', 2)[1], re.M) for key in ['name', 'description']):
            errors.append('missing name/description in frontmatter')
    template=ROOT/'.agents/skills/video-production-director/assets/project.json'
    if template.exists():
        default=json.loads(template.read_text())['format']
        for rel in ['README.md','LAUNCH_TASK.txt','.agents/skills/video-production-director/references/final-review-mode.md']:
            if f"{default['fps']}fps" not in (ROOT/rel).read_text():errors.append(f'{rel}: frame-rate default differs from project template')
    reference_index=ROOT/'aesthetics/INDEX.json'
    if reference_index.exists():
        entries=json.loads(reference_index.read_text()).get('entries',[]);seen=set()
        for entry in entries:
            if entry['id'] in seen:errors.append('duplicate aesthetic reference ID: '+entry['id'])
            seen.add(entry['id'])
            if not (reference_index.parent/entry['card']).is_file():errors.append('missing aesthetic reference card: '+entry['card'])
    manifest=ROOT/'MANIFEST.sha256'
    if manifest.exists():
        for line in manifest.read_text().splitlines():
            digest,relative=line.split('  ',1);path=ROOT/relative
            if not path.is_file() or hashlib.sha256(path.read_bytes()).hexdigest()!=digest:
                errors.append(f'manifest mismatch: {relative}')
    archive=ROOT/'dist/video-production-director.zip'
    if archive.exists():
        with zipfile.ZipFile(archive) as z:
            if z.testzip():errors.append('portable skill ZIP CRC failed')
            packaged={name.split('/',1)[1]:z.read(name) for name in z.namelist() if not name.endswith('/')}
        actual={p.relative_to(skill.parent).as_posix():p.read_bytes() for p in skill.parent.rglob('*') if p.is_file() and '__pycache__' not in p.parts}
        if packaged!=actual:errors.append('portable skill ZIP differs from current skill source')
    print(json.dumps({'passed': not errors, 'counts': counts, 'errors': errors,
                      'limits': 'Structure/syntax only, not film quality, market validation or target-client automatic discovery.'}, ensure_ascii=False, indent=2))
    return 0 if not errors else 2

if __name__ == '__main__':
    raise SystemExit(main())
