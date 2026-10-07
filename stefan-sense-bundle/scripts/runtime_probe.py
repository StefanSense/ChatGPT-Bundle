"""Bounded, real import/version probes for optional local dependencies; no installs."""
import subprocess
import sys
import shutil
import re

def probe_module(name):
    if not re.fullmatch(r'[A-Za-z_]\w*(?:\.[A-Za-z_]\w*)*', name):
        return {'available': False, 'reason': 'invalid module name'}
    code = 'import importlib,sys; importlib.import_module(sys.argv[1])'
    try:
        proc = subprocess.run([sys.executable, '-c', code, name], capture_output=True, text=True, timeout=12)
        return {'available': proc.returncode == 0, 'reason': proc.stderr.strip()[-700:] if proc.returncode else ''}
    except (OSError, subprocess.TimeoutExpired) as e:
        return {'available': False, 'reason': str(e)}

def probe_tool(name):
    executable = shutil.which(name)
    if not executable: return {'available': False, 'reason': 'not on PATH'}
    try:
        flag = '-v' if name == 'pdftoppm' else '--version'
        p = subprocess.run([executable, flag], capture_output=True, text=True, timeout=12)
        return {'available': p.returncode == 0, 'path': executable, 'detail': (p.stdout + p.stderr).strip()[:500]}
    except (OSError, subprocess.TimeoutExpired) as e:
        return {'available': False, 'path': executable, 'reason': str(e)}
