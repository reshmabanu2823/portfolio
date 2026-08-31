import os
import subprocess

WORKSPACE = os.path.dirname(os.path.abspath(__file__))

res = subprocess.run(['git', 'log', '--stat', 'origin/main..HEAD'], cwd=WORKSPACE, capture_output=True, text=True)
print("Commits ahead of origin/main:")
print(res.stdout[:2000])
