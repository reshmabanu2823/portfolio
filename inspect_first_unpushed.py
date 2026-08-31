import os
import subprocess

WORKSPACE = os.path.dirname(os.path.abspath(__file__))

res = subprocess.run(['git', 'show', '--stat', '777002077cbaa6f2508dc1790dea6d232893a368'], cwd=WORKSPACE, capture_output=True, text=True)
print(res.stdout)
