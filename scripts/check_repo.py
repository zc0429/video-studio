#!/usr/bin/env python3
"""Check portable file layout, JSON, local Markdown links and Python syntax without third-party packages."""
import ast
import json
import re
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
        if not p.is_file() or any(part in {'.git', '__pycache__', 'node_modules'} for part in p.relative_to(ROOT).parts):
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
    print(json.dumps({'passed': not errors, 'counts': counts, 'errors': errors,
                      'limits': 'Structure/syntax only, not film quality, market validation or target-client automatic discovery.'}, ensure_ascii=False, indent=2))
    return 0 if not errors else 2

if __name__ == '__main__':
    raise SystemExit(main())
