# -*- coding: utf-8 -*-
# QA v6 для методички: `qa_mf.py x content_mf.py` | `qa_mf.py file.docx content_mf.py`
import sys, os, re, glob, math
TOKEN = re.compile(r"\{R:(\w+)(?:\|([^}]+))?\}")

def refs_from_build(dirpath, content_name):
    path = os.path.join(dirpath, "build_mf.py")
    if not os.path.exists(path):
        cands = sorted(glob.glob(os.path.join(dirpath, "build_docx*.py")))
        path = cands[-1] if cands else None
    t = open(path, encoding="utf-8").read()
    i = t.index("REFS = {"); j = t.index("\n}", i)
    return eval(t[i + 6:j + 2])

def clean(s):
    return TOKEN.sub("", s)

def skey(s):
    s = re.sub(r"[^\w\s]", "", s.lower())
    return re.sub(r"\s+", " ", s).strip()

def split_sents(t, merge_init=False):
    parts = [x.strip() for x in re.split(r"(?<=[.!?])\s+", t) if x.strip()]
    if not merge_init:
        return parts
    out = []
    for p in parts:
        if out and re.search(r"[А-ЯЁA-Z]\.[,;]?$", out[-1]):
            out[-1] = out[-1] + " " + p
        elif out and re.match(r"^[а-яёa-z\[\—«]", p):
            out[-1] = out[-1] + " " + p
        else:
            out.append(p)
    return out

def text_units(C):
    out = []
    for b in C:
        if b[0] in ("p", "cap", "small", "center"):
            t = clean(b[1]).strip()
            if t: out.append((b[0], t))
        elif b[0] == "table":
            _, w, head, rows, ind = b
            for r in [head] + list(rows):
                for cell in r:
                    t = clean(cell).strip()
                    if t: out.append(("c", t))
    return out

def check_core(full, sents, C):
    ham = sum(full.count(x) for x in ("Ҳамин тарз", "Ҳамин тавр", "Ҳамин нуқта"))
    arab = sum(1 for ch in full if 0x600 <= ord(ch) <= 0x6FF)
    vhead = sum(1 for b in C if b[0] == "h2" and not re.match(r"^\d+\.\d+|^Приложение \d+", b[1]))
    first, cnt = {}, {}
    for s in sents:
        if len(s.split()) < 4: continue
        k = skey(s)
        if not k: continue
        cnt[k] = cnt.get(k, 0) + 1
        first.setdefault(k, s)
    dups = [(first[k], c) for k, c in cnt.items() if c > 1]
    return ham, arab, vhead, dups

def stats(sents):
    n = len(sents)
    avg = round(sum(len(s.split()) for s in sents) / n, 1) if n else 0
    o18 = sum(1 for s in sents if len(s.split()) > 18)
    return n, avg, o18

def mode_x(src):
    ns = {}
    exec(compile(open(src, encoding="utf-8").read(), src, "exec"), ns)
    C = ns["C"]
    refs = refs_from_build(os.path.dirname(os.path.abspath(src)) or ".", os.path.basename(src))
    toks = TOKEN.findall(" ".join(b[1] for b in C if b[0] in ("p","h1","h2","h3","cap","small","center")))
    rleft = sum(1 for k, _ in toks if k not in refs)
    units = text_units(C)
    full = " ".join(t for _, t in units)
    sents = []
    for _, t in units: sents.extend(split_sents(t))
    ham, arab, vhead, dups = check_core(full, sents, C)
    print(f"HaminTarz: {ham} arab: {arab} vhead: {vhead} sents-dups: {len(dups)} Rleft: {rleft}")
    for s, c in dups[:12]:
        print(f"  DUPx{c}: {s[:60]}")
    n, avg, o18 = stats(sents)
    print(f"sents: {n} avg-words: {avg} over18: {o18}")

def mode_docx(docx_path, src):
    from docx import Document
    from docx.oxml.ns import qn
    from docx.text.paragraph import Paragraph
    from docx.table import Table
    doc = Document(docx_path)
    units, cum, nosplit, bibs = [], 0, [], []
    for child in doc.element.body.iterchildren():
        if child.tag == qn("w:p"):
            par = Paragraph(child, doc)
            t = clean(par.text.strip())
            if t:
                bold = all((r.bold or False) for r in par.runs) and bool(par.runs)
                biblio = ("\u2014 С. " in t) or ("Указ. соч." in t) or ("СанПиН 2." in t)
                if bold or t.startswith("План темы") or "\t" in t:
                    cum += len(t); units.append(("p", t, cum))
                    if not biblio: nosplit.append(t)
                elif biblio:
                    cum += len(t); units.append(("p", t, cum)); bibs.append(t)
                else:
                    for part in split_sents(t, merge_init=True):
                        cum += len(part); units.append(("p", part, cum))
        elif child.tag == qn("w:tbl"):
            tb = Table(child, doc); seen = set()
            for row in tb.rows:
                for cell in row.cells:
                    if id(cell._tc) in seen: continue
                    seen.add(id(cell._tc))
                    t = clean(cell.text.strip())
                    if t:
                        cum += len(t); units.append(("c", t, cum))
    full = " ".join(u[1] for u in units)
    sents = [u[1] for u in units]
    body_sents = [t for t in sents if t not in nosplit and t not in bibs]
    ns = {}
    exec(compile(open(src, encoding="utf-8").read(), src, "exec"), ns)
    C = ns["C"]
    refs = refs_from_build(os.path.dirname(os.path.abspath(src)) or ".", os.path.basename(src))
    toks = TOKEN.findall(" ".join(b[1] for b in C if b[0] in ("p","h1","h2","h3","cap","small","center")))
    rleft = sum(1 for k, _ in toks if k not in refs)
    ham, arab, vhead, dups = check_core(full, sents, C)
    print(f"HaminTarz: {ham} arab: {arab} vhead: {vhead} sents-dups: {len(dups)} Rleft: {rleft}")
    for s, c in dups[:14]:
        loc = ""
        for u in units:
            if skey(u[1]) == skey(s):
                loc = f" [{max(1, math.ceil(u[2]/1900))}, {units.index(u)+1}]"
                break
        print(f"  DUPx{c}: {s[:90]} | {loc}")
    caps = {}
    for k, t, _ in units:
        if k == "p" and (t.startswith("Рисунок ") or t.startswith("Расми ")):
            caps.setdefault(t, []).append(t)
    print(f"capdups: {sum(1 for v in caps.values() if len(v) > 1)}")
    n, avg, o18 = stats(body_sents)
    print(f"sents: {n} avg-words: {avg} over18: {o18}")
    nums = [int(x) for x in re.findall(r"(?:Мисоли|Пример №?\s?)(\d+)", full)]
    ok = nums == list(range(1, len(nums) + 1))
    print(f"examples: {len(nums)} seq ok: {ok}")

if __name__ == "__main__":
    if sys.argv[1] == "x": mode_x(sys.argv[2])
    else: mode_docx(sys.argv[1], sys.argv[2])
