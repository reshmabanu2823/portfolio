import os

WORKSPACE = os.path.dirname(os.path.abspath(__file__))

# Delete extensionless files in works and www.noth.in/works
for d in [os.path.join(WORKSPACE, 'works'), os.path.join(WORKSPACE, 'www.noth.in', 'works')]:
    if os.path.exists(d):
        for f in os.listdir(d):
            p = os.path.join(d, f)
            if os.path.isfile(p) and not os.path.splitext(f)[1]:
                os.remove(p)
                print(f"Removed extensionless file: {p}")

print("Cleaned up extensionless files!")
