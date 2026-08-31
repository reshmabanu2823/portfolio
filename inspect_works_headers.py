with open('www.noth.in/index.html', 'r', encoding='utf-8') as f:
    c = f.read()

idx = c.find('id="works"')
if idx == -1:
    idx = c.find('class="section works')
if idx == -1:
    idx = c.find('works-word')

print(f"Index: {idx}")
chunk = c[max(0, idx-400):idx+1600]
print(chunk.encode('ascii', errors='replace').decode('ascii'))
