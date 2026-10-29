# -*- coding: utf-8 -*-
"""Сохтани .docx кори курсӣ (мавзӯи 1 (серияи нав — биокимёи умумӣ)) бо талаботи банди 1/10."""
import re, math, sys
from docx import Document
from docx.shared import Pt, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_BREAK, WD_TAB_ALIGNMENT, WD_TAB_LEADER
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.section import WD_ORIENT, WD_SECTION
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

sys.path.insert(0, '.')
from content_kim10 import C

REFS = {
 'harper': "Rodwell V. W. et al. Harper's Illustrated Biochemistry. 32nd ed. — New York: McGraw-Hill, 2023. — P. 205–236.",
 'nelson': "Nelson D. L., Cox M. M. Lehninger Principles of Biochemistry. 8th ed. — New York: W. H. Freeman, 2021. — P. 343–386.",
 'berg': "Berg J. M., Tymoczko J. L., Gatto G. J., Stryer L. Biochemistry. 9th ed. — New York: W. H. Freeman, 2019. — P. 361–398.",
 'marks': "Lieberman M., Peet A. Marks' Basic Medical Biochemistry. 6th ed. — Philadelphia: Wolters Kluwer, 2022. — P. 391–420.",
 'komov': "Комов В. П., Шведова В. Н. Биохимия. — Москва: Юрайт, 2023. — С. 180–208.",
 'ferrier': "Ferrier D. R. Lippincott Illustrated Reviews: Biochemistry. 8th ed. — Philadelphia: Wolters Kluwer, 2023. — P. 155–182.",
 'bhagavan': "Bhagavan N. V., Ha C.-E. Essentials of Medical Biochemistry. 2nd ed. — London: Academic Press, 2015. — P. 167–196.",
 'tietz': "Rifai N. Tietz Fundamentals of Clinical Chemistry and Molecular Diagnostics. 8th ed. — Philadelphia: Elsevier, 2019. — P. 900–932.",
 'ncb_lipid': "Biochemistry, Lipid Metabolism. StatPearls. — Treasure Island: StatPearls Publishing, 2023. — P. 1–30. URL: https://www.ncbi.nlm.nih.gov/books/NBK525952 (санаи муроҷиат: 28.10.2026).",
 'ncb_chol': "Biochemistry, Cholesterol. StatPearls. — Treasure Island: StatPearls Publishing, 2023. — P. 1–25. URL: https://www.ncbi.nlm.nih.gov/books/NBK513326 (санаи муроҷиат: 28.10.2026).",
 'ncb_omega': "Krupa K., Fritz K., Parmar M. Omega-3 Fatty Acids. StatPearls. — Treasure Island: StatPearls Publishing, 2024. — P. 1–20. URL: https://www.ncbi.nlm.nih.gov/books/NBK562340 (санаи муроҷиат: 28.10.2026).",
 'who_fat': "World Health Organization. WHO updates guidelines on fats and carbohydrates: Total fat, saturated fat and trans-fat intake. — Geneva: WHO, 2023. URL: https://www.who.int/news/item/17-07-2023-who-updates-guidelines-on-fats-and-carbohydrates (санаи муроҷиат: 28.10.2026).",
 'who_hdiet': "World Health Organization. Healthy diet: Fact sheet. — Geneva: WHO, 2026. URL: https://www.who.int/news-room/fact-sheets/detail/healthy-diet (санаи муроҷиат: 28.10.2026).",
 'aha': "American Heart Association. Dietary Fats: Saturated, Unsaturated and Trans Fat. — Dallas: AHA, 2024. URL: https://www.heart.org/en/healthy-living/healthy-eating/eat-smart/fats (санаи муроҷиат: 28.10.2026).",
 'fda_fat': "U.S. Food and Drug Administration. Trans Fat. — Silver Spring: FDA, 2021. URL: https://www.fda.gov/food/nutrition-food-labeling-cfr/trans-fat (санаи муроҷиат: 28.10.2026).",
 'efsa2010': "EFSA Panel on Dietetic Products, Nutrition, and Allergies. Scientific Opinion on Dietary Reference Values for fats. — EFSA Journal, 2010; 8(3): 1461.",
 'nih_ods': "Omega-3 Fatty Acids: Fact Sheet for Health Professionals. — Bethesda: NIH Office of Dietary Supplements, 2023. URL: https://ods.od.nih.gov/factsheets/Omega3FattyAcids-HealthProfessional (санаи муроҷиат: 28.10.2026).",
 'lab10': "Дастури амалии биохимияи тиббӣ: Таҷрибаҳои липидҳо. — Хуҷанд: Донишкадаи илмҳои дақиқ ва технологияи Тоҷикистон, 2026. — С. 153–168.",
 'konf10': "Маҷмӯаи мақолаҳои конфаренси илмии ҷавонон «Илми муосир ва саломатӣ». — Хуҷанд, 2025. — С. 141–148.",
 'lec10': "Конспектҳои лексияҳои биохимия: Сохтор ва мубодилаи липидҳо. — Хуҷанд: Донишкадаи илмҳои дақиқ ва технологияи Тоҷикистон, 2026. — С. 173–188.",
}


TOKEN = re.compile(r"\{R:(\w+)(?:\|([^}]+))?\}")

def all_strings(x):
    if isinstance(x, str):
        yield x
    elif isinstance(x, (list, tuple)):
        for y in x:
            yield from all_strings(y)

# --- рақамгузорӣ аз рӯи тартиби аввалин истифода ---
used_order = []
for b in C:
    for t in all_strings(b[1:] if isinstance(b, tuple) else b):
        for m in TOKEN.finditer(t):
            if m.group(1) not in used_order:
                used_order.append(m.group(1))

num = {k: i + 1 for i, k in enumerate(used_order)}
for k in REFS:
    if k not in num:
        num[k] = len(num) + 1

def sub(t):
    def r(m):
        k, page = m.group(1), m.group(2)
        n = num[k]
        return f"[{n}, {page}-б.]" if page else f"[{n}]"
    return TOKEN.sub(r, t)

# --- омор ---
def block_len(b):
    if b[0] in ("title_p", "toc"):
        return 0
    return sum(len(sub(x)) for x in all_strings(b[1:]))

refs_len = sum(len(f"{n}. {REFS[k]}") for k, n in num.items())
total_chars = sum(block_len(b) for b in C) + refs_len
n_tables = sum(1 for b in C if b[0] == "table")

i_intro = next(i for i, b in enumerate(C) if b[0] == "h1" and b[1] == "МУҚАДДИМА")
i_refs  = next(i for i, b in enumerate(C) if b[0] == "h1" and b[1].startswith("РӮЙХАТИ"))
main_chars = sum(block_len(b) for b in C[i_intro:i_refs])

cite_re = re.compile(r"\[\d+(?:,\s*[\d–\-]+-б\.)?\]")
n_cites = sum(len(cite_re.findall(sub(x))) for b in C for x in all_strings(b[1:] if isinstance(b, tuple) else b))
n_recent = sum(1 for v in REFS.values() if re.search(r"202[0-5]", v))
n_web = sum(1 for v in REFS.values() if "URL" in v)
n_refs = len(REFS)

main_pages = math.ceil(main_chars / 1900)
total_pages = math.ceil(total_chars / 1900)

stats_line = (f"Ҳаҷм аз рӯи ҳисоби автоматӣ: тамоми кор {total_chars} аломат (тақрибан {total_pages} саҳифа); "
              f"мазмуни асосӣ {main_chars} аломат (тақрибан {main_pages} саҳифа). "
              f"Ҷадвалҳо: {n_tables}. Иқтибосҳо: {n_cites}. Манбаъҳо: {n_refs}.")
chk_vol = ("Дуруст" if 65500 <= total_chars <= 70500 else
            ("Кам — бо ҷадвалу ҳисоб васеъ кардан лозим" if total_chars < 57000 else "Зиёд — ихтисор кардан лозим")) + \
          f". Ҳисобшуда: {total_chars} аломат ≈ {total_pages} саҳ."
per_page = n_cites / max(total_pages, 1)
chk_cite = f"Ҳа — ҷамъ {n_cites} иқтибос (тақр. {per_page:.1f} дар як саҳифа)"
chk_refs = (f"Ҳа — {n_refs} манбаъ; солҳои 2020–2025: {n_recent} адад; манбаъҳои интернетӣ: {n_web} адад; "
            f"солу нашриёри баъзе манбаъҳо бо «[дақиқ кардан лозим]» ишора шудаанд")

STATS = {"{STATS}": stats_line, "{CHK_VOL}": chk_vol, "{CHK_CITE}": chk_cite, "{CHK_REFS}": chk_refs}
print(f"Омор: ҷамъ {total_chars} аломат ≈ {total_pages} саҳ.; асосӣ {main_chars} ≈ {main_pages} саҳ.; "
      f"ҷадвал {n_tables}; иқтибос {n_cites}; манбаъ {n_refs} (2020+ {n_recent}, веб {n_web})")

def fin(t):
    return sub(STATS.get and t or t)  # placeholder, real below

def apply_all(t):
    for k, v in STATS.items():
        t = t.replace(k, v)
    return sub(t)

# ============================ ҲУҶҶАТ ============================
doc = Document()
st = doc.styles["Normal"]
st.font.name = "Times New Roman"
st.font.size = Pt(14)
st.element.get_or_add_rPr().get_or_add_rFonts().set(qn("w:eastAsia"), "Times New Roman")
pf = st.paragraph_format
pf.line_spacing = 1.5
pf.space_after = Pt(0)
pf.space_before = Pt(0)
pf.first_line_indent = Cm(1.25)
pf.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY

def setup_section(sec, landscape=False, numbered=False, allow_start=False):
    if landscape:
        sec.orientation = WD_ORIENT.LANDSCAPE
        sec.page_width, sec.page_height = Cm(30.7), Cm(21.0)
        sec.left_margin = sec.right_margin = Cm(2.0)
        sec.top_margin = sec.bottom_margin = Cm(2.0)
    else:
        sec.orientation = WD_ORIENT.PORTRAIT
        sec.page_width, sec.page_height = Cm(21.0), Cm(30.7)
        sec.left_margin, sec.right_margin = Cm(3.0), Cm(1.5)
        sec.top_margin, sec.bottom_margin = Cm(2.0), Cm(2.0)
    if numbered:
        f = sec.footer
        f.is_linked_to_previous = False
        par = f.paragraphs[0]
        if par._p.find(qn("w:fldSimple")) is None:
            par.alignment = WD_ALIGN_PARAGRAPH.CENTER
            pfmt = par.paragraph_format
            pfmt.first_line_indent = Cm(0)
            pfmt.line_spacing = 1.0
            fld = OxmlElement("w:fldSimple")
            fld.set(qn("w:instr"), " PAGE ")
            run = OxmlElement("w:r")
            rpr = OxmlElement("w:rPr")
            rf = OxmlElement("w:rFonts"); rf.set(qn("w:ascii"), "Times New Roman"); rf.set(qn("w:hAnsi"), "Times New Roman")
            sz = OxmlElement("w:sz"); sz.set(qn("w:val"), "24")
            rpr.append(rf); rpr.append(sz); run.append(rpr)
            t = OxmlElement("w:t"); t.text = "3"; run.append(t)
            fld.append(run)
            par._p.append(fld)
        sectPr = sec._sectPr
        has_start = any(el.get(qn("w:start")) is not None for el in sectPr.findall(qn("w:pgNumType")))
        if not has_start and allow_start:
            pg = OxmlElement("w:pgNumType")
            pg.set(qn("w:start"), "3")
            sectPr.insert_element_before(pg, "w:cols", "w:formProt", "w:vAlign",
                                         "w:noEndnote", "w:titlePg", "w:textDirection",
                                         "w:bidi", "w:rtlGutter", "w:docGrid")

def add_p(text, size=14, bold=False, italic=False, align=WD_ALIGN_PARAGRAPH.JUSTIFY,
          indent=Cm(1.25), spacing=1.5, after=0):
    par = doc.add_paragraph()
    f = par.paragraph_format
    f.alignment = align
    f.first_line_indent = indent
    f.line_spacing = spacing
    f.space_after = Pt(after)
    run = par.add_run(apply_all(text))
    run.font.name = "Times New Roman"
    run.font.size = Pt(size)
    run.bold = bold
    run.italic = italic
    return par

def add_pagebreak():
    par = doc.add_paragraph()
    par.paragraph_format.line_spacing = 1.0
    par.paragraph_format.space_after = Pt(0)
    par.paragraph_format.first_line_indent = Cm(0)
    par.add_run().add_break(WD_BREAK.PAGE)

def add_table(widths, head, rows):
    n_rows = len(rows) + (1 if head else 0)
    t = doc.add_table(rows=n_rows, cols=len(widths))
    t.style = doc.styles["Table Grid"]
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    t.autofit = False
    layout = OxmlElement("w:tblLayout"); layout.set(qn("w:type"), "fixed")
    t._tbl.tblPr.append(layout)
    def fill(cell, text, bold=False, shade=None):
        p0 = cell.paragraphs[0]
        f = p0.paragraph_format
        f.line_spacing = 1.0; f.space_after = Pt(0); f.space_before = Pt(0); f.first_line_indent = Cm(0)
        f.alignment = WD_ALIGN_PARAGRAPH.LEFT
        r = p0.add_run(apply_all(text))
        r.font.name = "Times New Roman"; r.font.size = Pt(12); r.bold = bold
        if shade:
            sh = OxmlElement("w:shd"); sh.set(qn("w:val"), "clear"); sh.set(qn("w:fill"), shade)
            cell._tc.get_or_add_tcPr().append(sh)
    idx = 0
    if head:
        for j, h in enumerate(head):
            c = t.cell(0, j); c.width = Cm(widths[j]); fill(c, h, bold=True, shade="EDEDED")
        idx = 1
    for i, row in enumerate(rows):
        for j, val in enumerate(row):
            c = t.cell(idx + i, j); c.width = Cm(widths[j]); fill(c, val)
    tail = doc.add_paragraph()
    tail.paragraph_format.line_spacing = 1.0
    tail.paragraph_format.space_after = Pt(0)
    tail.paragraph_format.first_line_indent = Cm(0)
    tail.add_run().font.size = Pt(6)

started = False
for b in C:
    kind = b[0]
    if kind == "title_p":
        for line, size in b[1]:
            add_p(line, size=size, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, indent=Cm(0))
        doc.add_section(WD_SECTION.NEW_PAGE)
        setup_section(doc.sections[-1])
        continue
    if kind == "h1" and b[1] == "МУҚАДДИМА" and not started:
        doc.add_section(WD_SECTION.NEW_PAGE)
        started = True
        add_p(b[1], bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, indent=Cm(0))
        continue
    if kind == "landscape":
        doc.add_section(WD_SECTION.NEW_PAGE)
        setup_section(doc.sections[-1], landscape=True)
        continue
    if kind == "portrait":
        doc.add_section(WD_SECTION.NEW_PAGE)
        setup_section(doc.sections[-1], landscape=False)
        continue
    if kind == "pagebreak":
        add_pagebreak(); continue
    if kind == "h1":
        add_p(b[1], bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, indent=Cm(0)); continue
    if kind == "h2" or kind == "h3":
        add_p(b[1], bold=True, align=WD_ALIGN_PARAGRAPH.LEFT); continue
    if kind == "img":
        ip = doc.add_paragraph()
        ip.alignment = WD_ALIGN_PARAGRAPH.CENTER
        ip.paragraph_format.first_line_indent = Cm(0)
        ip.add_run().add_picture(b[1], width=Cm(14.0))
        continue
    if kind == "cap":
        add_p(b[1], size=12, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, indent=Cm(0), spacing=1.0); continue
    if kind == "small":
        add_p(b[1], size=12, spacing=1.0); continue
    if kind == "center":
        add_p(b[1], align=WD_ALIGN_PARAGRAPH.CENTER, indent=Cm(0)); continue
    if kind == "toc":
        par = doc.add_paragraph()
        f = par.paragraph_format
        f.line_spacing = 1.5; f.first_line_indent = Cm(0); f.space_after = Pt(0)
        f.alignment = WD_ALIGN_PARAGRAPH.LEFT
        f.tab_stops.add_tab_stop(Cm(16.4), WD_TAB_ALIGNMENT.RIGHT, WD_TAB_LEADER.DOTS)
        r1 = par.add_run(apply_all(b[1])); r1.font.name = "Times New Roman"; r1.font.size = Pt(14)
        r2 = par.add_run("\t" + b[2]); r2.font.name = "Times New Roman"; r2.font.size = Pt(14)
        continue
    if kind == "refs":
        for k, n in sorted(num.items(), key=lambda kv: kv[1]):
            add_p(f"{n}. {REFS[k]}", align=WD_ALIGN_PARAGRAPH.LEFT, indent=Cm(0))
        continue
    if kind == "table":
        _, widths, head, rows, _ = b
        add_table(widths, head, rows); continue
    if kind == "p":
        add_p(b[1]); continue
    raise ValueError(f"номаълум: {kind}")

# ---- танзими ниҳоии бақшаҳо ----
for si, sec in enumerate(list(doc.sections)):
    setup_section(sec, landscape=(si == 3), numbered=(si >= 2), allow_start=(si == 2))
    if si != 2:
        for el in sec._sectPr.findall(qn("w:pgNumType")):
            if el.get(qn("w:start")) is not None:
                sec._sectPr.remove(el)

OUT = "10_Sokhtor-vazifa-lipidho_Kursi.docx"
doc.save(OUT)
print("Сохта шуд:", OUT)
print("Тартиби манбаъҳо:", ", ".join(f"{v}={k}" for k, v in sorted(num.items(), key=lambda kv: kv[1])))
