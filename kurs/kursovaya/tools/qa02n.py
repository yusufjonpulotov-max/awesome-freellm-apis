#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""QA: HaminTarz, arab, vhead, sents-dups, Rleft, capdups, examples-seq, over18.
Истифода: qa02n.py x contentNN.py   |   qa02n.py file.docx contentNN.py
"""
import re, sys, os, math, glob

HAMIN = re.compile(r"Ҳамин (тарз|тавр|нуқта)")
VHEAD = ["ва ғайра", "ва амсоли ҳамин", "муайян нест аст", "ҳар гуна бошад", "таври номаълум"]
TOKEN = re.compile(r"\{R:(\w+)(?:\|([^}]+))?\}")
NORM = re.compile(r"[^\w\s]", re.UNICODE)

def refs_from_build(dirpath, content_name):
    m = re.search(r"content(\d+)", content_name)
    pref = f"build_docx{m.group(1)}.py" if m else None
    path = os.path.join(dirpath, pref) if pref and os.path.exists(os.path.join(dirpath, pref)) else None
    if not path:
        cands = sorted(glob.glob(os.path.join(dirpath, "build_docx*.py")))
        path = cands[-1] if cands else None
    t = open(path, encoding="utf-8").read()
    i = t.index("REFS = {"); j = t.index("\n}", i)
    return eval(t[i + 6:j + 2])

def clean(s):
    return TOKEN.sub("", s)

def sentences(texts):
    full = " ".join(clean(t) for t in texts)
    out = []
    for t in texts:
        for s in re.split(r"(?<=[.!?])\s+", clean(t)):
            s = s.strip()
            if s:
                out.append(s)
    return full, out

def skey(s):
    return re.sub(r"\s+", " ", NORM.sub("", s.lower())).strip()

def check_core(full, sents):
    ham = len(HAMIN.findall(full))
    arab = sum(1 for ch in full if 0x0600 <= ord(ch) <= 0x06FF)
    vhead = sum(full.count(v) for v in VHEAD)
    keys = {}
    for s in sents:
        k = skey(s)
        w = k.split()
        if len(w) >= 4:
            keys.setdefault(k, []).append(s)
    dups = [(v[0], len(v)) for v in keys.values() if len(v) > 1]
    return ham, arab, vhead, dups

def stats(sents):
    wc = [len(s.split()) for s in sents]
    avg = round(sum(wc) / len(wc), 1) if wc else 0.0
    return len(wc), avg, sum(1 for w in wc if w > 18)

def mode_x(src):
    ns = {}
    exec(compile(open(src, encoding="utf-8").read(), src, "exec"), ns)
    C, TOC = ns["C"], ns.get("TOC", [])
    texts, dup_texts = [], []
    for b in C:
        k = b[0]
        if k == "title_p":
            texts += [l[0] for l in b[1] if l[0]]
        elif k in ("p", "h1", "h2", "h3", "cap", "small", "center"):
            texts.append(b[1])
            if k in ("p", "cap", "small", "center"):
                dup_texts.append(b[1])
        elif k == "toc":
            texts.append(b[1])
        elif k == "table":
            for row in b[3]:
                texts += list(row)
            dup_texts += [c for row in b[3] for c in row]
    full, sents = sentences(texts)
    refs = refs_from_build(os.path.dirname(os.path.abspath(src)) or ".", os.path.basename(src))
    rleft = sum(1 for k in TOKEN.findall(full) if k[0] not in refs)
    ham, arab, vhead, _ = check_core(full, sents)
    _, dup_sents = sentences(dup_texts)
    dups = check_core(full, dup_sents)[3]
    print(f"HaminTarz: {ham} arab: {arab} vhead: {vhead} sents-dups: {len(dups)} Rleft: {rleft}")
    for s, c in dups:
        print(f"  DUPx{c}: {s[:60]}")
    n, avg, o18 = stats(dup_sents)
    print(f"sents: {n} avg-words: {avg} over18: {o18}")

def mode_docx(docx_path, src):
    from docx import Document
    from docx.oxml.ns import qn
    from docx.text.paragraph import Paragraph
    from docx.table import Table
    doc = Document(docx_path)
    units, cum = [], 0
    for child in doc.element.body.iterchildren():
        if child.tag == qn("w:p"):
            t = clean(Paragraph(child, doc).text.strip())
            if t:
                cum += len(t)
                units.append(("p", t, cum))
        elif child.tag == qn("w:tbl"):
            tb = Table(child, doc)
            seen_tc = set()
            for row in tb.rows:
                for cell in row.cells:
                    if id(cell._tc) in seen_tc:
                        continue
                    seen_tc.add(id(cell._tc))
                    t = clean(cell.text.strip())
                    if t:
                        cum += len(t)
                        units.append(("c", t, cum))
    full = " ".join(u[1] for u in units)
    sents = []
    for u in units:
        for s in re.split(r"(?<=[.!?])\s+", u[1]):
            if s.strip():
                sents.append(s.strip())
    ns = {}
    exec(compile(open(src, encoding="utf-8").read(), src, "exec"), ns)
    refs = refs_from_build(os.path.dirname(os.path.abspath(src)) or ".", os.path.basename(src))
    rleft = sum(1 for k in TOKEN.findall(" ".join(ns["C"][i][1] for i in range(len(ns["C"])) if ns["C"][i][0] in ("p", "h1", "h2", "h3", "cap", "small", "center"))) if k[0] not in refs)
    ham, arab, vhead, dups = check_core(full, sents)
    print(f"HaminTarz: {ham} arab: {arab} vhead: {vhead} sents-dups: {len(dups)} Rleft: {rleft}")
    seen = set()
    for s, c in dups:
        first = None
        for i, u in enumerate(units):
            if skey(u[1]) == skey(s):
                first = u
                break
        loc = ""
        if first:
            pg = max(1, math.ceil(first[2] / 1900))
            idx = units.index(first) + 1
            loc = f" [{pg}, {idx}-б.]"
        print(f"  DUPx{c}: {s[:60]}.{loc}")
    caps = {}
    for k, t, _ in units:
        if k == "p" and t.startswith("Расми "):
            caps.setdefault(t, []).append(t)
    print(f"capdups: {sum(1 for v in caps.values() if len(v) > 1)}")
    n, avg, o18 = stats(sents)
    print(f"sents: {n} avg-words: {avg} over18: {o18}")
    nums = [int(x) for x in re.findall(r"Мисоли (\d+)", full)]
    ok = nums == list(range(1, len(nums) + 1))
    print(f"examples: {len(nums)} seq ok: {ok}")

if __name__ == "__main__":
    if sys.argv[1] == "x":
        mode_x(sys.argv[2])
    else:
        mode_docx(sys.argv[1], sys.argv[2])
