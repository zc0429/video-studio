#!/usr/bin/env python3
"""Read-only executable/version probes. Does not install tools or validate production readiness."""
import json
import shutil
import subprocess
import sys

def main():
    results = []
    probes = [('python', [sys.executable, '--version']), ('node', ['node', '--version']),
              ('ffmpeg', ['ffmpeg', '-version']), ('ffprobe', ['ffprobe', '-version']),
              ('chromium', ['chromium', '--version']), ('blender', ['blender', '--version'])]
    for name, command in probes:
        executable = shutil.which(command[0])
        row = {'name': name, 'path': executable, 'status': 'unavailable' if not executable else 'found'}
        if executable:
            try:
                result = subprocess.run([executable, *command[1:]], capture_output=True, text=True, timeout=15)
                lines = (result.stdout or result.stderr).strip().splitlines()
                row.update(returncode=result.returncode, version_line=lines[0][:240] if lines else '', status='available' if result.returncode == 0 else 'probe_failed')
            except (subprocess.TimeoutExpired, OSError) as exc:
                row.update(status='probe_failed', reason=type(exc).__name__)
        results.append(row)
    print(json.dumps({'tools': results, 'limits': 'Presence/version only; no GPU, model/API access, fonts, browser automation, license or rendering success is established. Recheck per environment.'}, ensure_ascii=False, indent=2))

if __name__ == '__main__':
    main()
