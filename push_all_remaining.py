import os
import subprocess

WORKSPACE = os.path.dirname(os.path.abspath(__file__))

res = subprocess.run(['git', 'rev-list', '--reverse', 'origin/main..HEAD'], cwd=WORKSPACE, capture_output=True, text=True)
commits = [c.strip() for c in res.stdout.strip().split('\n') if c.strip()]
print(f"Total remaining commits to push: {len(commits)}")

for idx, c in enumerate(commits):
    print(f"[{idx+1}/{len(commits)}] Pushing {c}...")
    p = subprocess.run(['git', 'push', 'origin', f'{c}:refs/heads/main'], cwd=WORKSPACE, capture_output=True, text=True)
    if p.returncode != 0:
        print(f"Failed at commit {c}: {p.stderr}")
        break
    else:
        print(f"  Success: {c}")

print("All unpushed commits processed!")
