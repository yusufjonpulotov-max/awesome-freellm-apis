# -*- coding: utf-8 -*-
import re, sys, importlib.util
from docx import Document
docx, cont, P = sys.argv[1], sys.argv[2], int(sys.argv[3])
spec = importlib.util.spec_from_file_location('m57t', cont)
m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
titles = [t[0] for t in m.TOC]
pts = [p.text.strip() for p in Document(docx).paragraphs]
tot = sum(len(t) for t in pts)
pos = []
for t in titles:
    idx = next((i for i, x in enumerate(pts) if x == t), None)
    pos.append(sum(len(x) for x in pts[:idx]) if idx is not None else tot)
mx = max(pos) or 1
pages = [str(3 + round((P - 3) * c / mx)) for c in pos]
new = 'TOC = [\n' + ''.join(' ("%s", "%s"),\n' % (t, p) for t, p in zip(titles, pages)) + ']'
s = open(cont, encoding='utf-8').read()
s = re.sub(r'TOC = \[.*?\n\]', new, s, count=1, flags=re.S)
open(cont, 'w', encoding='utf-8').write(s)
print('toc %d 3 -> %d' % (len(titles), int(pages[-1])))
