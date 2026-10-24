#!/usr/bin/env python3
"""Copy project templates to a new directory without overwriting existing work."""
from pathlib import Path
import argparse,shutil

def create_project(target):
    target=Path(target)
    if target.exists() and (not target.is_dir() or any(target.iterdir())):raise ValueError('Target is not an empty directory; existing work will not be overwritten')
    source=Path(__file__).resolve().parents[1]/'assets'
    shutil.copytree(source,target,dirs_exist_ok=True)
    return target

if __name__=='__main__':
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('directory',type=Path);args=ap.parse_args()
    try:print('Templates copied to',create_project(args.directory))
    except (ValueError,OSError) as e:ap.exit(2,str(e)+'\n')
