# -*- coding: utf-8 -*-
"""Сохранитель курсовой работы (Мавзӯи 1) дар формати .docx."""
import io, os, re, glob, math

from docx import Document
from docx.shared import Pt, Cm, Mm
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_TAB_ALIGNMENT, WD_TAB_LEADER
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
from PIL import Image

import sys

SRC_DIR = sys.argv[1]
OUT = sys.argv[2]
TOPIC_ARG = sys.argv[3]
SRC = sorted(glob.glob(os.path.join(SRC_DIR, "*.md")))

INSTITUTION = "ДОНИШКАДАИ ИЛМҲОИ ДАҚИҚ ВА ТЕХНОЛОГИЯИ ТОҶИКИСТОН ДАР ШАҲРИ ХУҶАНД"
FACULTY = "Факултети фанҳои дақиқ ва технологияи инноватсионӣ"
CHAIR = "Кафедраи биохимия ва тиб"
SUBJECT = "аз фанни «Физиологияи инсон»"
TOPIC = TOPIC_ARG
CITY_YEAR = "Хуҷанд — 2026"

SOURCES = {
 "pokrovsky": "Покровский В.М., Коротько Г.Ф. Физиология человека. — М.: Медицина, 2003. — 656 с.",
 "guyton": "Guyton A.C., Hall J.E. Textbook of Medical Physiology. — 14th ed. — Philadelphia: Elsevier, 2021. — 1152 p.",
 "levy": "Levy M.N., Pappano A.J. Cardiovascular Physiology. — 11th ed. — Philadelphia: Elsevier, 2019. — 300 p.",
 "sarnoff": "Sarnoff S.J., Mitchell J.H. Control of the function of the heart // Handbook of Physiology. — Washington: American Physiological Society, 1962. — P. 489–532.",
 "solodkov": "Солодков А.С., Сологуб Е.Б. Физиология человека: общая, спортивная, возрастная. — М.: Спорт, 2018. — 620 с.",
 "agadzhanyan": "Агаджанян Н.А., Смирнов В.М. Нормальная физиология: учебник. — М.: Медицинское информационное агентство, 2021. — 576 с.",
 "kositsky": "Косицкий Г.И. Физиология человека. — М.: Медицина, 1985. — 544 с.",
 "shmidt": "Шмидт Р., Тевс Г. Физиология человека: в 3 т. — Т. 2. — М.: Мир, 1996. — 641 с.",
 "klabunde": "Klabunde R.E. Cardiovascular Physiology Concepts. — 3rd ed. — Philadelphia: Wolters Kluwer, 2021. — 336 p.",
 "boron": "Boron W.F., Boulpaep E.L. Medical Physiology. — 3rd ed. — Philadelphia: Elsevier, 2017. — 1312 p.",
 "levick": "Herring N., Paterson D.J. Levick's Introduction to Cardiovascular Physiology. — 6th ed. — Boca Raton: CRC Press, 2018. — 448 p.",
 "mohrman": "Mohrman D.E., Heller L.J. Cardiovascular Physiology. — 9th ed. — New York: McGraw-Hill, 2018. — 320 p.",
 "marieb": "Marieb E.N., Hoehn K. Human Anatomy and Physiology. — 12th ed. — Boston: Pearson, 2023. — 1264 p.",
 "opie": "Opie L.H. Heart Physiology: From Cell to Circulation. — 4th ed. — Philadelphia: Lippincott Williams and Wilkins, 2004. — 648 p.",
 "folkov": "Фолков Б., Нил Э. Кровообращение. — М.: Медицина, 1976. — 463 с.",
 "karo": "Каро К., Педли Т., Шротер Р., Сид У. Механика кровообращения. — М.: Мир, 1981. — 624 с.",
 "sudakov": "Судаков К.В. Нормальная физиология: учебник. — М.: Медицинское информационное агентство, 2006. — 920 с.",
 "smirnov2": "Смирнов В.М., Яковлев В.Н. Физиология: учебник. — М.: Академия, 2019. — 480 с.",
 "aha": "American Heart Association. Cardiac Output. — URL: https://www.heart.org/ (датаи муроҷиат: 15.11.2026).",
 "openstax": "OpenStax. Anatomy and Physiology 2e. — URL: https://openstax.org/books/anatomy-and-physiology-2e (датаи муроҷиат: 10.11.2026).",
 "teachme": "TeachMePhysiology. Cardiac Output. — URL: https://teachmephysiology.com/cardiovascular-system/cardiac-output/ (датаи муроҷиат: 14.11.2026).",
 "katz": "Katz A.M. Physiology of the Heart. — 5th ed. — Philadelphia: Lippincott Williams and Wilkins, 2011. — 576 p.",
 "patterson": "Patterson S.W., Starling E.H. On the mechanical factors which determine the output of the ventricles // Journal of Physiology. — 1914. — Vol. 48. — P. 357–379.",
 "statpearls": "StatPearls. Physiology, Cardiac Output. — NCBI Bookshelf. — URL: https://www.ncbi.nlm.nih.gov/books/NBK470455/ (датаи муроҷиат: 12.11.2026).",
}

NUM2KEY = {3: "pokrovsky", 4: "guyton", 5: "levy", 6: "sarnoff", 7: "solodkov",
           8: "agadzhanyan", 9: "kositsky", 10: "shmidt", 11: "klabunde",
           12: "boron", 13: "levick", 14: "mohrman", 15: "marieb", 16: "opie",
           17: "folkov", 18: "karo", 19: "sudakov", 20: "smirnov2",
           21: "aha", 22: "openstax", 23: "teachme", 24: "statpearls",
           25: "katz", 26: "patterson"}

# ---------------- 1. Чтение и разбор разметки ----------------
blocks = []
for path in SRC:
    lines = io.open(path, encoding="utf-8").read().split("\n")
    i = 0
    while i < len(lines):
        raw = lines[i].rstrip()
        s = raw.strip()
        if not s:
            i += 1
            continue
        if s.startswith("#H1 "):
            blocks.append(["h1", s[4:].strip()])
        elif s.startswith("#H2 "):
            blocks.append(["h2", s[4:].strip()])
        elif s == "#PB":
            if blocks and blocks[-1][0] == "pb":
                pass
            else:
                blocks.append(["pb", ""])
        elif s.startswith("#CAP "):
            blocks.append(["cap", s[5:].strip()])
        elif s.startswith("#FIG "):
            body = s[5:]
            p, cap = body.split("|", 1)
            blocks.append(["fig", p.strip(), cap.strip()])
        elif s.startswith("|"):
            rows = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                cells = [c.strip() for c in lines[i].strip().strip("|").split("|")]
                rows.append(cells)
                i += 1
            blocks.append(["tbl", rows])
            continue
        else:
            blocks.append(["p", s])
        i += 1

# убрать лишние разрывы страниц (pb перед h1 или перед другим pb)
clean = []
for b in blocks:
    if b[0] == "pb":
        nxt = None
        for c in blocks[blocks.index(b) + 1:] if False else []:
            pass
    clean.append(b)
tmp = []
for i, b in enumerate(blocks):
    if b[0] == "pb":
        nxt = blocks[i + 1][0] if i + 1 < len(blocks) else None
        if nxt in ("h1", "pb") or nxt is None:
            continue
        if tmp and tmp[-1][0] == "pb":
            continue
    tmp.append(b)
blocks = tmp

# удалить статический список литературы из исходника (он будет сгенерирован)
out = []
in_bib = False
for b in blocks:
    if b[0] == "h1":
        in_bib = b[1].strip().upper().startswith("РӮЙХАТИ АДАБИЁТ")
        out.append(b)
        continue
    if in_bib and b[0] == "p" and re.match(r"^\d+\.\s", b[1]):
        continue
    if in_bib and b[0] != "p":
        in_bib = False
    out.append(b)
blocks = out

# ---------------- 2. Перенумерация ссылок ----------------
order = []
num_of = {}


def renum(text):
    def rep(m):
        old = int(m.group(1))
        key = NUM2KEY.get(old)
        if key is None:
            return m.group(0)
        if key not in num_of:
            order.append(key)
            num_of[key] = len(order)
        return "[%d, %s]" % (num_of[key], m.group(2))
    return re.sub(r"\[(\d+), ([^\]]+)\]", rep, text)


for b in blocks:
    if b[0] in ("p", "cap", "h1", "h2"):
        b[1] = renum(b[1])

# ---------------- 3. Оценка объёма и страниц ----------------
PAGE_H = 257.0        # мм полезной высоты
LINE = 8.53           # мм, TNR 14 / 1.5
CPL = 67              # знаков в строке (14 пт, TNR, ширина 165 мм)
TROW = 4.87           # мм, строка таблицы 12 пт / 1.0
TCAP_GAP = 2.1
H1_AFTER = 4.2
H2_BEFORE = 4.2
H2_AFTER = 2.1


def table_widths(rows):
    ncol = max(len(r) for r in rows)
    weights = []
    for c in range(ncol):
        ml = max((len(r[c]) if c < len(r) else 0) for r in rows)
        weights.append(max(6, min(ml, 48)))
    tot = sum(weights)
    return [165.0 * w / tot for w in weights], ncol


def table_height(rows):
    widths, ncol = table_widths(rows)
    h = 0.0
    for r in rows:
        lines = 1
        for c in range(ncol):
            txt = r[c] if c < len(r) else ""
            cpl = max(6, int((widths[c] - 2.0) / 2.1))
            lines = max(lines, math.ceil(len(txt) / cpl) if txt else 1)
        h += lines * TROW + 1.8
    return h


def table_row_heights(rows):
    widths, ncol = table_widths(rows)
    hs = []
    for r in rows:
        lines = 1
        for c in range(ncol):
            txt = r[c] if c < len(r) else ""
            cpl = max(6, int((widths[c] - 2.0) / 2.1))
            lines = max(lines, math.ceil(len(txt) / cpl) if txt else 1)
        hs.append(lines * TROW + 1.8)
    return hs


def text_height(txt, cpl=CPL, lh=LINE):
    return max(1, math.ceil(len(txt) / cpl)) * lh


page = 2  # 1 — титул, 2 — содержание
y = PAGE_H  # содержание считаем на второй странице
toc = []
for b in blocks:
    kind = b[0]
    if kind == "pb" or kind == "h1":
        page += 1
        y = 0.0
        if kind == "h1":
            toc.append((1, b[1], page))
            y += text_height(b[1]) + H1_AFTER
        continue
    if kind == "h2":
        h = H2_BEFORE + text_height(b[1]) + H2_AFTER
        if y + h > PAGE_H:
            page += 1
            y = 0.0
        toc.append((2, b[1], page))
        y += h
        continue
    if kind == "tbl":
        for rh in table_row_heights(b[1]):
            if y + rh > PAGE_H:
                page += 1
                y = 0.0
            y += rh
        continue
    if kind == "p":
        # абзац может разрываться между страницами (как в Word)
        nlines = max(1, math.ceil(len(b[1]) / CPL))
        while nlines > 0:
            room = int((PAGE_H - y) // LINE)
            if room <= 0:
                page += 1
                y = 0.0
                continue
            take = min(nlines, room)
            y += take * LINE
            nlines -= take
            if nlines > 0:
                page += 1
                y = 0.0
        continue
    elif kind == "cap":
        h = text_height(b[1], 78, TROW) + TCAP_GAP
    elif kind == "fig":
        w, hh = Image.open(b[1]).size
        h = 150.0 * hh / w + text_height(b[2], 78, TROW)
    else:
        continue
    if y + h > PAGE_H:
        page += 1
        y = 0.0
    y += h

total_pages = page

for k in SOURCES:
    if k not in num_of:
        order.append(k)
        num_of[k] = len(order)

# ---------------- 4. Сборка docx ----------------
doc = Document()

st = doc.styles["Normal"]
st.font.name = "Times New Roman"
st.font.size = Pt(14)
rpr = st.element.get_or_add_rPr()
rf = rpr.find(qn("w:rFonts"))
if rf is None:
    rf = OxmlElement("w:rFonts")
    rpr.append(rf)
for a in ("w:ascii", "w:hAnsi", "w:cs", "w:eastAsia"):
    rf.set(qn(a), "Times New Roman")
st.paragraph_format.line_spacing = 1.5
st.paragraph_format.space_before = Pt(0)
st.paragraph_format.space_after = Pt(0)

sec = doc.sections[0]
sec.page_width = Cm(21)
sec.page_height = Cm(29.7)
sec.left_margin = Cm(3)
sec.right_margin = Cm(1.5)
sec.top_margin = Cm(2)
sec.bottom_margin = Cm(2)
sec.different_first_page_header_footer = True

# нумерация страниц в нижнем колонтитуле по центру
fp = sec.footer.paragraphs[0]
fp.alignment = WD_ALIGN_PARAGRAPH.CENTER
run = fp.add_run()
f1 = OxmlElement("w:fldChar"); f1.set(qn("w:fldCharType"), "begin")
it = OxmlElement("w:instrText"); it.set(qn("xml:space"), "preserve"); it.text = " PAGE "
f2 = OxmlElement("w:fldChar"); f2.set(qn("w:fldCharType"), "end")
run._r.append(f1); run._r.append(it); run._r.append(f2)
run.font.name = "Times New Roman"
run.font.size = Pt(12)

pending_break = [False]


def para(text="", align="justify", bold=False, indent=True, size=14,
         before=0, after=0, spacing=1.5, keep=False):
    p = doc.add_paragraph()
    pf = p.paragraph_format
    pf.line_spacing = spacing
    pf.space_before = Pt(before)
    pf.space_after = Pt(after)
    pf.first_line_indent = Cm(1.25) if indent else Cm(0)
    pf.alignment = {"justify": WD_ALIGN_PARAGRAPH.JUSTIFY,
                    "center": WD_ALIGN_PARAGRAPH.CENTER,
                    "left": WD_ALIGN_PARAGRAPH.LEFT,
                    "right": WD_ALIGN_PARAGRAPH.RIGHT}[align]
    pf.keep_with_next = keep
    if pending_break[0]:
        pf.page_break_before = True
        pending_break[0] = False
    r = p.add_run(text)
    r.bold = bold
    r.font.size = Pt(size)
    r.font.name = "Times New Roman"
    return p


# ---------- титульный лист ----------
para("", indent=False)
para(INSTITUTION, align="center", bold=True)
para(FACULTY, align="center")
para(CHAIR, align="center")
for _ in range(4):
    para("", indent=False)
para("КОРИ КУРСӢ", align="center", bold=True, size=16)
para(SUBJECT, align="center")
para("", indent=False)
para("Мавзӯъ:", align="center", bold=True)
para(TOPIC, align="center", bold=True)
for _ in range(4):
    para("", indent=False)

for line in ["Иҷрокунанда:",
             "донишҷӯи курси ______, гурӯҳи ______",
             "____________________________",
             "Роҳбар:",
             "____________________________"]:
    p = para(line, align="left", indent=False)
    p.paragraph_format.left_indent = Cm(8.0)

for _ in range(3):
    para("", indent=False)
para(CITY_YEAR, align="center")

# ---------- содержание ----------
pending_break[0] = True
para("МУНДАРИҶА", align="center", bold=True, after=12)

TOC_LABEL = {"МУҚАДДИМА": "МУҚАДДИМА", "ХУЛОСА": "ХУЛОСА",
             "РӮЙХАТИ АДАБИЁТ": "РӮЙХАТИ АДАБИЁТ", "ЗАМИМАҲО": "ЗАМИМАҲО"}
for lvl, title, pg in toc:
    p = doc.add_paragraph()
    pf = p.paragraph_format
    pf.line_spacing = 1.5
    pf.space_before = Pt(0)
    pf.space_after = Pt(0)
    pf.left_indent = Cm(0 if lvl == 1 else 0.75)
    pf.alignment = WD_ALIGN_PARAGRAPH.LEFT
    tabs = pf.tab_stops
    tabs.add_tab_stop(Cm(16.4), WD_TAB_ALIGNMENT.RIGHT, WD_TAB_LEADER.DOTS)
    r = p.add_run(title if lvl == 1 else title)
    r.bold = (lvl == 1)
    r.font.name = "Times New Roman"
    r.font.size = Pt(14)
    r2 = p.add_run("\t%d" % pg)
    r2.bold = (lvl == 1)
    r2.font.name = "Times New Roman"
    r2.font.size = Pt(14)

# ---------- основной текст ----------
pending_break[0] = True
bib_inserted = [False]

for bi, b in enumerate(blocks):
    kind = b[0]
    if kind == "pb":
        nxt = blocks[bi + 1][0] if bi + 1 < len(blocks) else None
        if nxt != "h1":
            pending_break[0] = True
        continue
    if kind == "h1":
        para(b[1], align="center", bold=True, indent=False, after=12, keep=True)
        if b[1].strip().upper().startswith("РӮЙХАТИ АДАБИЁТ"):
            for i, key in enumerate(order, 1):
                para("%d. %s" % (i, SOURCES[key]), align="justify")
            bib_inserted[0] = True
        continue
    if kind == "h2":
        para(b[1], align="left", bold=True, indent=True, before=12, after=6, keep=True)
        continue
    if kind == "cap":
        para(b[1], align="left", bold=True, indent=False, size=12, spacing=1.0,
             after=4, keep=True)
        continue
    if kind == "tbl":
        rows = b[1]
        ncol = max(len(r) for r in rows)
        widths, _ = table_widths(rows)
        p = doc.add_paragraph()
        p.paragraph_format.space_after = Pt(6)
        p.paragraph_format.line_spacing = 1.0
        if pending_break[0]:
            p.paragraph_format.page_break_before = True
            pending_break[0] = False
        t = doc.add_table(rows=len(rows), cols=ncol)
        t.style = "Table Grid"
        t.alignment = WD_TABLE_ALIGNMENT.CENTER
        t.autofit = False
        for ri, row in enumerate(rows):
            for ci in range(ncol):
                cell = t.cell(ri, ci)
                cell.width = Cm(widths[ci])
                txt = row[ci] if ci < len(row) else ""
                cp = cell.paragraphs[0]
                cp.paragraph_format.line_spacing = 1.0
                cp.paragraph_format.space_before = Pt(0)
                cp.paragraph_format.space_after = Pt(0)
                cp.paragraph_format.first_line_indent = Cm(0)
                cp.alignment = (WD_ALIGN_PARAGRAPH.CENTER if (ri == 0 or len(txt) <= 12)
                                else WD_ALIGN_PARAGRAPH.LEFT)
                cr = cp.add_run(txt)
                cr.font.size = Pt(12)
                cr.font.name = "Times New Roman"
                cr.bold = (ri == 0)
                cell.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
        if len(rows) > 1:
            trPr = t.rows[0]._tr.get_or_add_trPr()
            th = OxmlElement("w:tblHeader")
            trPr.append(th)
        continue
    if kind == "fig":
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.first_line_indent = Cm(0)
        p.paragraph_format.space_before = Pt(6)
        p.paragraph_format.space_after = Pt(3)
        p.paragraph_format.line_spacing = 1.0
        if pending_break[0]:
            p.paragraph_format.page_break_before = True
            pending_break[0] = False
        p.add_run().add_picture(b[1], width=Cm(15))
        cp = para(b[2], align="center", indent=False, size=12, spacing=1.0, after=6)
        continue
    if kind == "p":
        para(b[1], align="justify")

if not bib_inserted[0]:
    raise SystemExit("Библиография не вставлена")

doc.save(OUT)

chars = sum(len(b[1]) for b in blocks if b[0] in ("p", "cap"))
print("Файл:", OUT)
print("Блоков:", len(blocks), "| источников:", len(order))
print("Знаков в тексте (с пробелами):", chars)
print("Оценка страниц (текст):", total_pages)
print("Содержание:")
for lvl, title, pg in toc:
    print("  " * (lvl - 1), title[:70], "->", pg)
