import os
import subprocess

WORKSPACE = os.path.dirname(os.path.abspath(__file__))

res = subprocess.run(['git', 'show', '--stat', '209238e105d76e2fdae21a9f32baec2ea01e579a'], cwd=WORKSPACE, capture_output=True, text=True)
print(res.stdout)
