import os

brain_health_dir = r"C:\Users\Reshma Banu\Downloads\Projects for portfolio\Brain_health"
if os.path.exists(brain_health_dir):
    files = os.listdir(brain_health_dir)
    print(f"Found {len(files)} files in Brain_health:")
    for f in sorted(files):
        p = os.path.join(brain_health_dir, f)
        print(f"  {f} ({os.path.getsize(p)/(1024):.1f} KB)")
else:
    print("Directory not found:", brain_health_dir)
