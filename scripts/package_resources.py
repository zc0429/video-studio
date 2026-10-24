#!/usr/bin/env python3
"""Rebuild portable skill, source bundle and hashes from current files, excluding credentials and build caches."""
import hashlib
import zipfile
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
SKILL=ROOT/'.agents/skills/video-production-director'
EXCLUDED={'.git','__pycache__','node_modules','.venv','venv','cache','frames'}

def included(path):
    parts=path.relative_to(ROOT).parts
    return (parts[0]!='projects' or parts==('projects','README.md')) and not any(p in EXCLUDED for p in parts) and not path.name.startswith('.env') and path.suffix not in {'.pyc','.mp4','.wav'}

def main():
    dist=ROOT/'dist';dist.mkdir(exist_ok=True)
    portable=dist/'video-production-director.zip';bundle=dist/'video-studio-resources.zip'
    with zipfile.ZipFile(portable,'w',zipfile.ZIP_DEFLATED,compresslevel=9) as z:
        for p in sorted(SKILL.rglob('*')):
            if p.is_file() and included(p):z.write(p,Path(SKILL.name)/p.relative_to(SKILL))
    files=[p for p in sorted(ROOT.rglob('*')) if p.is_file() and included(p) and p not in {bundle,ROOT/'MANIFEST.sha256'}]
    manifest=ROOT/'MANIFEST.sha256'
    manifest.write_text(''.join(f'{hashlib.sha256(p.read_bytes()).hexdigest()}  {p.relative_to(ROOT).as_posix()}\n' for p in files))
    with zipfile.ZipFile(bundle,'w',zipfile.ZIP_DEFLATED,compresslevel=9) as z:
        for p in files+[manifest]:z.write(p,Path(ROOT.name)/p.relative_to(ROOT))
    for p in [portable,bundle]:
        with zipfile.ZipFile(p) as z:
            bad=z.testzip()
            if bad:raise ValueError(f'Bad ZIP entry: {bad}')
    print(f'Packaged {len(files)+1} files; source manifest and ZIP CRC checks complete.')

if __name__=='__main__':main()
