import os, re
pattern = re.compile(r'[\U00010000-\U0010ffff\u2600-\u26ff\u2700-\u27bf]')
for root, dirs, files in os.walk('nirvana-ii'):
    for f in files:
        if f.endswith(('.html', '.css', '.js', '.md', '.json')):
            path = os.path.join(root, f)
            with open(path, 'r', encoding='utf-8', errors='ignore') as fh:
                text = fh.read()
                matches = [(m.start(), hex(ord(m.group(0)))) for m in pattern.finditer(text)]
                if matches:
                    print(f'{path}: {len(matches)} matches: {matches[:5]}')
print('Finished checking text files for nirvana-ii.')
