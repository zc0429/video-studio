#!/usr/bin/env python3
"""Build the human guide. Requires pandoc, Node, Playwright and Chromium; no automatic installation."""
import subprocess
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def main():
    version='.'.join((ROOT/'VERSION').read_text().strip().split('.')[:2])
    with tempfile.TemporaryDirectory(prefix='video-studio-docs-') as temporary:
        inputs = []
        for index, name in enumerate(['SOP.md', 'CREATOR_GROWTH.md', 'research/CASEBOOK.md']):
            item = Path(temporary) / f'{index}.md'
            item.write_text((ROOT / name).read_text().replace('**', ''))
            inputs.append(str(item))
        (ROOT / 'docs').mkdir(exist_ok=True)
        destination = ROOT / 'docs/SOP.html'
        subprocess.run(['pandoc', '-f', 'gfm', '-t', 'html5', '--standalone', '--embed-resources',
                        '--metadata', f'title=可控短片与自媒体收益 SOP v{version}', '--css', str(ROOT/'print.css'),
                        *inputs, '-o', str(destination)], check=True, cwd=ROOT)
        text = destination.read_text()
        start = text.find('<header id="title-block-header">')
        end = text.find('</header>', start)
        if start >= 0 and end >= 0:
            text = text[:start] + text[end+len('</header>'):]
        destination.write_text(text)
        subprocess.run(['node', 'scripts/build_pdf.js'], check=True, cwd=ROOT)

if __name__ == '__main__':
    main()
