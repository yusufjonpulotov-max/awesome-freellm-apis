#!/usr/bin/env python3
"""
Се расми нақшавӣ барои лексияи «Камхуниҳои гемолитикии модарзодӣ».
Ҳосил: lectures/figures/*.svg
"""
import pathlib

OUT = pathlib.Path(__file__).parent / "figures"
OUT.mkdir(exist_ok=True)

FONT = "'Segoe UI','Noto Sans','PT Sans',Arial,sans-serif"

DEFS = """
<defs>
  <marker id="arw" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
    <path d="M0,0 L10,5 L0,10 z" fill="#0f6f8c"/>
  </marker>
  <marker id="arwR" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
    <path d="M0,0 L10,5 L0,10 z" fill="#a1202b"/>
  </marker>
  <style>
    .t { font-family:%(f)s; }
    .title { font:700 21px %(f)s; fill:#123b52; }
    .sub   { font:400 14px %(f)s; fill:#5b6b7c; }
    .bx    { fill:#eaf4f8; stroke:#0f6f8c; stroke-width:1.6; }
    .bxg   { fill:#eaf6f0; stroke:#1c6b4a; stroke-width:1.6; }
    .bxw   { fill:#fdf4e7; stroke:#a8571b; stroke-width:1.6; }
    .bxr   { fill:#fdeced; stroke:#a1202b; stroke-width:1.6; }
    .bxg2  { fill:#f3f6f9; stroke:#7b8ea3; stroke-width:1.6; }
    .h     { font:700 15px %(f)s; fill:#0d3a52; }
    .p     { font:400 12.8px %(f)s; fill:#23394b; }
    .s     { font:400 11.8px %(f)s; fill:#3d5566; }
    .lbl   { font:700 13px %(f)s; fill:#0f6f8c; }
    .lblr  { font:700 13px %(f)s; fill:#a1202b; }
    .flow  { stroke:#0f6f8c; stroke-width:1.8; fill:none; marker-end:url(#arw); }
    .flowr { stroke:#a1202b; stroke-width:1.8; fill:none; marker-end:url(#arwR); }
  </style>
</defs>
""" % {"f": FONT}


def box(x, y, w, h, cls, lines, hsize=15, psize=12.8, gap=None):
    """lines: [(text, class)]"""
    out = [f'<rect class="{cls}" x="{x}" y="{y}" width="{w}" height="{h}" rx="12"/>']
    gap = gap or 20
    cy = y + 26
    for text, klass in lines:
        out.append(f'<text class="{klass}" x="{x + w/2}" y="{cy}" text-anchor="middle">{text}</text>')
        cy += gap
    return "\n".join(out)


# ───────────────────────── РАСМИ 1: се механизми асосӣ ─────────────────────────
fig1 = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1080 760" width="1080" height="760" role="img" aria-label="Механизмҳои асосии камхуниҳои гемолитикии модарзодӣ">
{DEFS}
<rect width="1080" height="760" fill="#ffffff"/>
<text class="title" x="540" y="38" text-anchor="middle">Камхуниҳои гемолитикии модарзодӣ: се механизми асосӣ</text>
<text class="sub" x="540" y="62" text-anchor="middle">Нуқсон дар яке аз се система — мембрана, метаболизм (ферментҳо) ё гемоглобин — эритротситро ноустувор мекунад</text>

{box(30, 92, 320, 112, "bx", [("МЕМБРАНА ва СКЕЛЕТ", "h"), ("спектрин · анкирин · протеин 4.2 · band 3", "p"), ("нуқсон → сферотсит / эллиптотсит", "p")])}
{box(380, 92, 320, 112, "bx", [("ФЕРМЕНТҲО (метаболизм)", "h"), ("G6PD → NADPH ↓   ·   PK → ATP ↓", "p"), ("нуқсон → ҷисмҳои Heinz / дегидрататсия", "p")])}
{box(730, 92, 320, 112, "bx", [("ГЕМОГЛОБИН", "h"), ("миқдор → талассемия   ·   сифат → HbS", "p"), ("нуқсон → избытоки занҷирҳо", "p"), ("ё полимеризатсия", "p")])}

<path class="flow" d="M190,204 L190,250 Q190,268 208,268 L470,268"/>
<path class="flow" d="M540,204 L540,252"/>
<path class="flow" d="M890,204 L890,250 Q890,268 872,268 L610,268"/>

{box(360, 268, 360, 74, "bxw", [("ЭРИТРОТСИТИ НУҚСОНДОР", "h"), ("умри кӯтоҳ: аз 100–120 рӯз то 15–20 рӯз", "p")])}

<path class="flow" d="M470,342 L470,378 Q470,396 452,396 L300,396"/>
<path class="flow" d="M610,342 L610,378 Q610,396 628,396 L780,396"/>

{box(60, 396, 420, 128, "bxg", [("ЭКСТРАВАСКУЛЯРӢ (сипурз, ҷигар)", "h"), ("фагоцитоз · «бозёфти сипурз»", "p"), ("спленомегалия · сферотситҳо", "p"), ("≈ 90 % ҳолатҳо", "s")])}
{box(600, 396, 420, 128, "bxr", [("ИНТРАВАСКУЛЯРӢ (дар дохили рагҳо)", "h"), ("комплемент · механикӣ · оксидантҳо", "p"), ("гемоглобинемия · гемоглобинурия", "p"), ("гаптоглобин ↓↓↓   ·   ≈ 10 % ҳолатҳо", "s")])}

<path class="flow" d="M270,524 L270,560 Q270,578 288,578 L470,578"/>
<path class="flow" d="M810,524 L810,560 Q810,578 792,578 L610,578"/>
{box(360, 578, 360, 66, "bxg2", [("КАМХУНӢ + ГЕМОЛИЗ", "h"), ("ретикулотситоз (ҷуброн)", "p")])}

<path class="flow" d="M470,644 L470,672 Q470,690 452,690 L330,690"/>
<path class="flow" d="M610,644 L610,672 Q610,690 628,690 L750,690"/>
{box(70, 690, 380, 58, "bxg2", [("КЛИНИКА: зардӣ · спленомегалия · сангҳои талхадон", "p")])}
{box(630, 690, 380, 58, "bxg2", [("ЛАБОРАТОРИЯ: билирубин · LDH · ретикулотситҳо ↑", "p")])}
</svg>
'''

# ───────────────────── РАСМИ 2: скелети мембрана ─────────────────────
fig2 = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1080 620" width="1080" height="620" role="img" aria-label="Скелети мембранаи эритротсит">
{DEFS}
<rect width="1080" height="620" fill="#ffffff"/>
<text class="title" x="540" y="36" text-anchor="middle">Скелети мембранаи эритротсит: пайвандҳои вертикалӣ ва уфуқӣ</text>
<text class="sub" x="540" y="60" text-anchor="middle">Вертикалӣ (анкирин/band 3) вайрон шавад → сферотсит · Уфуқӣ (спектрин–актин) вайрон шавад → эллиптотсит</text>

<!-- липидии дуқабат -->
<rect x="60" y="96" width="960" height="20" rx="10" fill="#cfe3ee" stroke="#7ba6bf"/>
<text class="s" x="60" y="90">дуқабати липидӣ (фосфолипидҳо, холестерол)</text>

<!-- band 3 -->
<rect x="300" y="96" width="86" height="84" rx="10" fill="#0f6f8c" opacity="0.85"/>
<text class="s" x="343" y="200" text-anchor="middle" fill="#0d3a52"><tspan font-weight="700">band 3 (AE1)</tspan></text>
<rect x="700" y="96" width="86" height="84" rx="10" fill="#0f6f8c" opacity="0.55"/>
<text class="s" x="743" y="200" text-anchor="middle" fill="#0d3a52"><tspan font-weight="700">band 3</tspan></text>

<!-- анкирин -->
<rect x="316" y="210" width="54" height="60" rx="10" fill="#a8571b" opacity="0.9"/>
<text class="h" x="343" y="292" text-anchor="middle" fill="#a8571b">анкирин</text>

<!-- 4.2 -->
<rect x="392" y="216" width="48" height="48" rx="10" fill="#7b8ea3"/>
<text class="h" x="416" y="292" text-anchor="middle" fill="#4a6070">4.2</text>

<!-- спектрин -->
<line x1="343" y1="300" x2="343" y2="380" stroke="#1c6b4a" stroke-width="8" stroke-linecap="round"/>
<line x1="343" y1="380" x2="560" y2="380" stroke="#1c6b4a" stroke-width="8" stroke-linecap="round"/>
<line x1="560" y1="380" x2="560" y2="300" stroke="#1c6b4a" stroke-width="8" stroke-linecap="round"/>
<line x1="560" y1="380" x2="780" y2="380" stroke="#1c6b4a" stroke-width="8" stroke-linecap="round"/>
<line x1="780" y1="380" x2="780" y2="300" stroke="#1c6b4a" stroke-width="8" stroke-linecap="round"/>
<line x1="780" y1="300" x2="780" y2="230" stroke="#1c6b4a" stroke-width="6" stroke-dasharray="8 6" stroke-linecap="round"/>
<text class="h" x="455" y="410" text-anchor="middle" fill="#1c6b4a">α- ва β-спектрин (тетрамер)</text>

<!-- актин -->
<circle cx="560" cy="380" r="16" fill="#1c6b4a"/>
<text class="s" x="560" y="430" text-anchor="middle" fill="#1c6b4a">актин · аддуцин · тропомиозин (пайванди уфуқӣ)</text>

<!-- 4.1R -->
<rect x="762" y="228" width="46" height="46" rx="10" fill="#7b8ea3"/>
<text class="h" x="785" y="292" text-anchor="middle" fill="#4a6070">4.1R</text>

<!-- гликофорин C -->
<rect x="820" y="96" width="70" height="70" rx="10" fill="#3f7f9c" opacity="0.7"/>
<text class="s" x="855" y="186" text-anchor="middle" fill="#0d3a52"><tspan font-weight="700">гликофорин C</tspan></text>

<!-- тирҳои шарҳ -->
<path class="flow" d="M343,300 L343,214"/>
<text class="lbl" x="120" y="252">ПАЙВАНДИ ВЕРТИКАЛӢ:</text>
<text class="s" x="120" y="272">band 3 ← 4.2 ← анкирин ← спектрин</text>
{box(60, 470, 420, 116, "bxr", [("Нуқсони пайванди ВЕРТИКАЛӢ", "h"), ("талафи везикулҳо ва липидҳо", "p"), ("сатҳ/ҳаҷм ↓ → СФЕРОТСИТ", "p"), ("MCHC ↑ (> 360 г/л) · osmotic fragility +", "s")], gap=22)}
{box(600, 470, 420, 116, "bxw", [("Нуқсони пайванди УФУҚӢ", "h"), ("ҳуҷайра робитаро гум мекунад", "p"), ("шакли эллипс → ЭЛЛИПТОТСИТ", "p"), ("EMA-binding муқаррарӣ", "s")], gap=22)}
</svg>
'''

# ───────────────────── РАСМИ 3: занҷираи патогенези HbS ─────────────────────
fig3 = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1160 800" width="1160" height="800" role="img" aria-label="Патогенези камхунии ҳуҷайраҳои досма">
{DEFS}
<rect width="1160" height="800" fill="#ffffff"/>
<text class="title" x="560" y="34" text-anchor="middle">Патогенези камхунии ҳуҷайраҳои досма: аз мутация то криз</text>
<text class="sub" x="560" y="58" text-anchor="middle">Занҷираро аз боло ба поён хонед; триггерҳо дар тарафи чап, нуқтаҳои таъсири табобат дар тарафи рост</text>

{box(330, 78, 460, 58, "bx", [("Мутацияи HBB: кодони 6, Glu → Val (HbS)", "h")], gap=0)}

<path class="flow" d="M560,136 L560,166"/>
{box(330, 166, 460, 58, "bx", [("Дезоксигенатсия (гипоксия, асидоз, дегидрататсия)", "h")], gap=0)}

<path class="flow" d="M560,224 L560,254"/>
{box(330, 254, 460, 92, "bxw", [("ПОЛИМЕРИЗАТСИЯ: валини β ба ҷайби гидрофобии", "h"), ("молекулаи ҳамсоя мепайвандад", "p"), ("→ фибриллҳои HbS", "p")], gap=22)}

<path class="flow" d="M560,346 L560,376"/>
{box(330, 376, 460, 74, "bxr", [("Ҳуҷайра шакли ДОСМА мегирад", "h"), ("деформатсияпазирӣ ↓", "p")], gap=22)}

<path class="flow" d="M560,450 L560,480"/>
{box(330, 480, 460, 74, "bxr", [("Дегидрататсия: Ca²⁺ ↑ → канали Gardos", "h"), ("K⁺ ва об берун → MCHC ↑", "p")], gap=22)}

<path class="flowr" d="M790,517 Q910,517 910,420 Q910,340 795,330"/>
<text class="lblr" x="915" y="440">ҳалқаи пороқ:</text>
<text class="s" x="915" y="458">MCHC ↑ → полимеризатсия</text>
<text class="s" x="915" y="474">боз ҳам тезтар мешавад</text>

<path class="flow" d="M560,554 L560,586"/>
{box(180, 586, 340, 150, "bxg", [("ВАСООККЛЮЗИЯ", "h"), ("часпакӣ: P-selectin, VCAM-1,", "p"), ("ICAM-1; лейкотситҳо", "p"), ("→ ишемия, гипоксия, некроз", "p"), ("→ КРИЗҲОИ ДАРД (VOC),", "p"), ("ACS, инсулт", "p")], gap=21)}
{box(600, 586, 340, 150, "bxg", [("ГЕМОЛИЗ", "h"), ("Hb ва аргиназаи озод → NO ↓", "p"), ("→ вазоконстриксия,", "p"), ("гипертензияи пулмоналӣ,", "p"), ("ҳиперкоагулятсия", "p"), ("→ приапизм, захмҳои пои", "p")], gap=21)}

<path class="flow" d="M250,586 L250,560"/>
<text class="lbl" x="40" y="540">ТРИГГЕРҲО:</text>
<text class="s" x="40" y="558">сироят, табларза,</text>
<text class="s" x="40" y="574">дегидрататсия, сармо,</text>
<text class="s" x="40" y="590">стресс, баландӣ, асидоз</text>
<path class="flow" d="M980,586 L980,560"/>
<text class="lbl" x="1000" y="540">ТАБОБАТ:</text>
<text class="s" x="1000" y="558">hydroxyurea (HbF ↑),</text>
<text class="s" x="1000" y="574">трансфузия, HSCT,</text>
<text class="s" x="1000" y="590">терапияи генетикӣ</text>
</svg>
'''

for name, svg in [("01-se-mekhanizm.svg", fig1), ("02-skelet-membrana.svg", fig2), ("03-patogenez-hbs.svg", fig3)]:
    (OUT / name).write_text(svg, encoding="utf-8")
    print("навишта шуд:", OUT / name)
