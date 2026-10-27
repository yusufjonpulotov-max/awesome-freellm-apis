#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Танзими рақамҳои саҳифаи TOC дар contentNN.py.
Истифода: toc02n.py - contentNN.py [ҳаҷми умумӣ]
Модели v3: PAGE=1900; title→P=2.0; p/cap len/1900; table chars/1900+rows*0.02;
img +0.35; brk → int(P)+1; refs +2.6.
"""
import re, sys, math

def block_text(b):
    k = b[0]
    if k == "title_p": return "".join(l[0] for l in b[1])
    if k in ("p", "h1", "h2", "h3", "cap", "small", "center"): return b[1]
    if k == "toc": return b[1]
    if k == "table": return " ".join(" ".join(r) for r in b[3])
    return ""

def main():
    src = sys.argv[2]
    ns = {}
    exec(compile(open(src, encoding="utf-8").read(), src, "exec"), ns)
    C, TOC = ns["C"], ns["TOC"]
    P = 0.0
    pages = {}
    for b in C:
        k = b[0]
        if k == "title_p":
            P = 2.0
        elif k == "toc":
            P += len(block_text(b)) / 1900.0
        elif k == "pagebreak":
            P = int(P) + 1.0
        elif k in ("p", "cap", "small", "center", "h1", "h2", "h3"):
            if k in ("h1", "h2"):
                pg = int(P)
                pages[b[1]] = pg
            P += len(block_text(b)) / 1900.0
        elif k == "table":
            P += len(block_text(b)) / 1900.0 + len(b[3]) * 0.02
        elif k == "img":
            P += 0.35
        elif k == "refs":
            P += 2.6
    total = math.ceil(P)
    s = open(src, encoding="utf-8").read()
    changes = 0
    def fix(m):
        nonlocal changes
        title, old = m.group(1), m.group(2)
        new = str(pages.get(title, old))
        if new != old:
            changes += 1
        return f'("{title}", "{new}")'
    s2 = re.sub(r'\("([^"]+)", "(\d+)"\)', fix, s)
    open(src, "w", encoding="utf-8").write(s2)
    print(f"toc02n: {changes} тағйир")

if __name__ == "__main__":
    main()
