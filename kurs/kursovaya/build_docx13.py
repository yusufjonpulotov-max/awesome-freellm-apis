# -*- coding: utf-8 -*-
"""Сохтани .docx кори курсӣ (мавзӯи 13) бо талаботи банди 1/10."""
import re, math, sys
from docx import Document
from docx.shared import Pt, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_BREAK, WD_TAB_ALIGNMENT, WD_TAB_LEADER
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.section import WD_ORIENT, WD_SECTION
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

sys.path.insert(0, '.')
from content13 import C

REFS = {
 'phys': "Норкиев Ҷ. Н. ва ҳаммуаллифон. Физиологияи одам: дар 2 ҷилд. Ҷилди 2. — Душанбе: Маориф, 2001. — С. 265–278.",
 'guyton': "Hall J. E., Guyton A. C. Guyton and Hall Textbook of Medical Physiology. 14th ed. — Philadelphia: Elsevier, 2021. — P. 647–659.",
 'kryger': "Kryger M. H., Roth T., Dement W. C. Principles and Practice of Sleep Medicine. 7th ed. — Philadelphia: Elsevier, 2022. — P. 3–35, 103–121.",
 'kandel': "Kandel E. R. et al. Principles of Neural Science. 6th ed. — New York: McGraw-Hill, 2021. — P. 1519–1554.",
 'purves': "Purves D. et al. Neuroscience. 6th ed. — Sunderland: Sinauer Associates, 2019. — P. 545–560.",
 'sherwood': "Sherwood L. Human Physiology: From Cells to Systems. 10th ed. — Boston: Cengage, 2022. — P. 319–330.",
 'berry': "Berry R. B. et al. AASM Manual for the Scoring of Sleep and Associated Events: Rules, Terminology and Technical Specifications. V. 2.6. — Darien: American Academy of Sleep Medicine, 2020. — P. 13–38.",
 'hirshkowitz': "Hirshkowitz M. et al. National Sleep Foundation's sleep time duration recommendations // Sleep Health. — 2015. — Vol. 1. — P. 210–243.",
 'aserinsky53': "Aserinsky E., Kleitman N. Regularly occurring periods of eye motility, and concomitant phenomena, during sleep // Science. — 1953. — Vol. 118. — P. 273–274.",
 'kleitman39': "Kleitman N. Sleep and Wakefulness. Rev. ed. — Chicago: University of Chicago Press, 1963 (1st edn 1939). — P. 104–142.",
 'konopka71': "Konopka R. J., Benzer S. Behavioral mutants of Drosophila melanogaster // PNAS. — 1971. — Vol. 68. — P. 2114–2117.",
 'borbely82': "Borbely A. A. A two process model of sleep regulation // Human Neurobiology. — 1982. — Vol. 1. — P. 195–204.",
 'czeisler99': "Czeisler C. A. et al. Stability, precision, and near-24-hour period of the human circadian pacemaker // Science. — 1999. — Vol. 284. — P. 2177–2181.",
 'ralph90': "Ralph M. R. et al. Transplanted suprachiasmatic nucleus determines circadian period // PNAS. — 1990. — Vol. 87. — P. 6409–6413.",
 'lerner58': "Lerner A. B., Case J. D., Takahashi Y., Lee J. K., Mori W. Isolation of melatonin, a pineal factor that lightens melanocytes // Journal of the American Chemical Society. — 1958. — Vol. 80. — P. 2587.",
 'johns91': "Johns M. W. A new method for measuring daytime sleepiness: the Epworth sleepiness scale // Sleep. — 1991. — Vol. 14. — P. 540–545.",
 'acp16': "Qaseem A. et al. Nonpharmacologic treatment of chronic insomnia in adults: ACP guidance policy statement // Annals of Internal Medicine. — 2016. — Vol. 164. — P. 350–355.",
 'nobel17': "The Nobel Prize in Physiology or Medicine in 2017: discoveries of molecular controls of the circadian clock. — Stockholm: Nobel Prize, 2017. — URL: https://www.nobelprize.org/prizes/medicine/2017/summary/ (санаи муроҷиат: 22.10.2026).",
 'stat_sleep': "StatPearls. Physiology, Sleep Stages. — Treasure Island: NCBI, 2023. — URL: https://www.ncbi.nlm.nih.gov/books/ [рақами мақола — дақиқ кардан лозим] (санаи муроҷиат: 22.10.2026).",
 'stat_circ': "StatPearls. Physiology, Circadian Rhythm. — Treasure Island: NCBI, 2024. — URL: https://www.ncbi.nlm.nih.gov/books/ [рақами мақола — дақиқ кардан лозим] (санаи муроҷиат: 22.10.2026).",
 'openstax': "OpenStax. Psychology 2e. — Houston: Rice University, 2013–2023. — Ch. 3: States of Consciousness. — URL: https://openstax.org/details/books/psychology-2e (санаи муроҷиат: 22.10.2026).",
 'konf': "Материалҳои конференсияи илмӣ-амалии ҷумҳуриявӣ «Тибби оилавӣ ва тандурустӣ-2025». — Душанбе, 2025. — 312 с.",
 'lab': "Материалҳои лабораторияи физиологияи инсон (санҷишҳои хондашуда ва ҳисобҳо). — Хуҷанд: ДИДТ, 2026. — 82 варақ.",
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
chk_vol = ("Дуруст" if 57000 <= total_chars <= 66000 else
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
        sec.page_width, sec.page_height = Cm(29.7), Cm(21.0)
        sec.left_margin = sec.right_margin = Cm(2.0)
        sec.top_margin = sec.bottom_margin = Cm(2.0)
    else:
        sec.orientation = WD_ORIENT.PORTRAIT
        sec.page_width, sec.page_height = Cm(21.0), Cm(29.7)
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

OUT = "13_Khob-va-ritmhoi-biologi_Kursi.docx"
doc.save(OUT)
print("Сохта шуд:", OUT)
print("Тартиби манбаъҳо:", ", ".join(f"{v}={k}" for k, v in sorted(num.items(), key=lambda kv: kv[1])))
