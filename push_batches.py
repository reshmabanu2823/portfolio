import os
import subprocess

WORKSPACE = os.path.dirname(os.path.abspath(__file__))

res = subprocess.run(['git', 'rev-list', '--reverse', 'origin/main..HEAD'], cwd=WORKSPACE, capture_output=True, text=True)
commits = res.stdout.strip().split('\n')
print(f"Total unpushed commits: {len(commits)}")

# Push in steps of 5 commits
for i in range(0, len(commits), 5):
    c = commits[min(i + 4, len(commits) - 1)]
    print(f"Pushing up to commit {i}: {c}")
    p = subprocess.run(['git', 'push', 'origin', f'{c}:refs/heads/main'], cwd=WORKSPACE, capture_output=True, text=True)
    print("  Exit code:", p.returncode)
    print("  Stdout:", p.stdout)
    print("  Stderr:", p.stderr)
    if p.returncode != 0:
        print("Stopping at failed batch.")
        break
