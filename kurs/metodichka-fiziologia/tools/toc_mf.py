# -*- coding: utf-8 -*-
# toc_mf: `toc_mf.py - content_mf.py` — ҳисоби саҳифаҳо ва навиштан ба TOC
import sys, os, re, math
TOKEN = re.compile(r"\{R:(\w+)(?:\|([^}]+))?\}")
PAGE = 1900.0

def sub_len(t):
    return len(TOKEN.sub(lambda m: "[99, с. 999]" if m.group(2) else "[99]", t))

def run(path):
    src = open(path, encoding="utf-8").read()
    ns = {}
    exec(compile(src, path, "exec"), ns)
    C = ns["C"]
    P, heads, toc_idx = 1.0, [], []
    for i, b in enumerate(C):
        if b[0] == "toc":
            toc_idx.append(i)
        elif b[0] in ("p", "cap", "small", "center", "h1", "h2", "h3"):
            P += sub_len(b[1]) / PAGE
            if b[0] == "h1" and b[1] != "СОДЕРЖАНИЕ":
                heads.append((b[1], int(math.ceil(P))))
        elif b[0] == "table":
            _, w, head, rows, ind = b
            chars = sum(sub_len(x) for x in head) + sum(sub_len(x) for r in rows for x in r)
            P += chars / PAGE + len(rows) * 0.02
        elif b[0] == "img":
            P += 0.35
        elif b[0] == "pagebreak":
            P = int(P) + 1
        elif b[0] == "refs":
            P += 2.6
    if len(heads) < len(toc_idx):
        print(f"toc_mf: heads({len(heads)}) < toc({len(toc_idx)}) — JADVAL/SECTION POMOSKA")
        return
    changes = 0
    for j, i in enumerate(toc_idx):
        title, old = C[i][1], C[i][2]
        new = heads[j][1]
        if str(old) == str(new): continue
        changes += 1
        pat = re.compile(r'("' + re.escape(title) + r'",\s*")' + str(old) + r'(")')
        src2, n = pat.subn(lambda m: m.group(1) + str(new) + m.group(2), src, count=1)
        assert n == 1, (title, old, new)
        src = src2
    if changes:
        open(path, "w", encoding="utf-8").write(src)
    print(f"toc_mf: {changes} тағйир")

if __name__ == "__main__":
    run(sys.argv[2])
