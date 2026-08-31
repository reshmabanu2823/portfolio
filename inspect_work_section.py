with open('www.noth.in/index.html', 'r', encoding='utf-8') as f:
    c = f.read()

idx = c.find('class="work_list_w')
chunk = c[idx-800:idx+2500]
print(chunk.encode('ascii', errors='replace').decode('ascii'))
