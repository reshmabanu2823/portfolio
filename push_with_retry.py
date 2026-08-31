import os
import subprocess
import time

WORKSPACE = os.path.dirname(os.path.abspath(__file__))

subprocess.run(['git', 'config', 'http.postBuffer', '1048576000'], cwd=WORKSPACE)
subprocess.run(['git', 'config', 'http.lowSpeedLimit', '0'], cwd=WORKSPACE)
subprocess.run(['git', 'config', 'http.lowSpeedTime', '999999'], cwd=WORKSPACE)

res = subprocess.run(['git', 'rev-list', '--reverse', 'origin/main..HEAD'], cwd=WORKSPACE, capture_output=True, text=True)
commits = [c.strip() for c in res.stdout.strip().split('\n') if c.strip()]
print(f"Total remaining commits: {len(commits)}")

for idx, c in enumerate(commits):
    print(f"[{idx+1}/{len(commits)}] Pushing {c}...")
    success = False
    for attempt in range(3):
        p = subprocess.run(['git', 'push', 'origin', f'{c}:refs/heads/main'], cwd=WORKSPACE, capture_output=True, text=True)
        if p.returncode == 0:
            print(f"  Success: {c}")
            success = True
            break
        else:
            print(f"  Attempt {attempt+1} failed: {p.stderr.strip()[:100]}")
            time.sleep(2)
    if not success:
        print(f"Aborting at commit {c}")
        break

print("Push script complete!")
