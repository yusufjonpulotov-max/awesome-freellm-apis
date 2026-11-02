# -*- coding: utf-8 -*-
"""Расмҳои М24: сохтори липопротеин, нақлиёти экзоген/эндоген, синтези холестерин, нақшаи ташхис, панели липидӣ."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Rectangle, Circle, Ellipse
import numpy as np, os

plt.rcParams["font.family"] = "DejaVu Sans"
BG = "#FBF8F4"
OUT = "img24"
os.makedirs(OUT, exist_ok=True)

def save(fig, name):
    fig.savefig(f"{OUT}/{name}.png", dpi=200, bbox_inches="tight", facecolor=BG)
    plt.close(fig)
    print(name, "ok")

def box(ax, x, y, w, h, txt, fc="#FFFFFF", ec="#444444", fs=9.0, bold=False, lw=1.8):
    b = FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.1", fc=fc, ec=ec, lw=lw)
    ax.add_patch(b)
    ax.text(x + w/2, y + h/2, txt, ha="center", va="center", fontsize=fs, zorder=5,
            fontweight=("bold" if bold else "normal"))

def arr(ax, p1, p2, color="#333333", lw=1.8, ls="-", label="", ly=0.22, fs=8.4):
    a = FancyArrowPatch(p1, p2, arrowstyle="-|>", mutation_scale=14, color=color, lw=lw, linestyle=ls)
    ax.add_patch(a)
    if label:
        ax.text((p1[0]+p2[0])/2, (p1[1]+p2[1])/2 + ly, label, fontsize=fs, color=color, ha="center")

# ---------- 1.1 Сохтори липопротеин ва панҷ класс ----------
fig, ax = plt.subplots(figsize=(10.4, 6.8))
ax.set_xlim(0, 12); ax.set_ylim(0, 8.2); ax.axis("off")
ax.add_patch(Rectangle((0, 0), 12, 8.2, facecolor=BG, edgecolor="none"))
# липопротеин
cx, cy = 3.4, 5.6
ax.add_patch(Circle((cx, cy), 2.05, fc="#FDEBD3", ec="#B9770E", lw=2.4))
ax.add_patch(Circle((cx, cy), 1.28, fc="#FFF8E1", ec="#B9770E", lw=1.8))
ax.text(cx, cy, "Ядра:\nTG + эфири\nхолестерин", ha="center", va="center", fontsize=8.6, color="#7A4A12")
ax.text(cx, cy + 1.72, "Қабат: фосфолипид + холестери озод", ha="center", fontsize=8.2, color="#7A4A12",
        bbox=dict(fc=BG, ec="none", pad=1.5))
ax.text(cx, cy + 2.38, "Аполипопротеинҳо", ha="center", fontsize=9.2, color="#7A4A12", fontweight="bold")
for ang in (30, 100, 150, 250, 320):
    a = np.deg2rad(ang)
    ax.add_patch(Circle((cx + 1.68*np.cos(a), cy + 1.68*np.sin(a)), 0.17, fc="#9C1F1F", ec="none"))
# 5 класс — андоза зуд кам мешавад
sizes = [1.15, 0.95, 0.75, 0.62, 0.5]
names = ["Хиломикрон\n<0.95", "VLDL\n0.95–1.006", "IDL\n1.006–1.019", "LDL\n1.019–1.063", "HDL\n1.063–1.21"]
cols = ["#B9770E", "#1F4E79", "#6B3FA0", "#9C1F1F", "#1B5E20"]
for i, (s, n, c) in enumerate(zip(sizes, names, cols)):
    x = 6.5 + i * 1.12
    ax.add_patch(Circle((x, 6.4), s * 0.52, fc="#FFFFFF", ec=c, lw=2))
    ax.text(x, 5.05, n, ha="center", fontsize=7.2, color=c)
ax.text(9.35, 7.55, "Панҷ класс — зич меафзояд", fontsize=10, ha="center", color="#444444", fontweight="bold")
box(ax, 6.6, 1.4, 5.0, 3.0, "", fc="#EAF3FB", ec="#1F4E79", lw=2)
ax.text(9.1, 3.95, "ЗАХИРА ВА ЭНЕРГИЯ", fontsize=10.5, ha="center", color="#1F4E79", fontweight="bold")
ax.text(9.1, 3.15, "Хиломикрон: 85–90% TG", fontsize=9.2, ha="center")
ax.text(9.1, 2.55, "LDL: 50% холестерин", fontsize=9.2, ha="center")
ax.text(9.1, 1.95, "HDL: 50% сафеда", fontsize=9.2, ha="center")
box(ax, 0.5, 1.4, 5.4, 1.0, "Апои асосӣ: apoB-48 (хиломикрон) · apoB-100 (VLDL/LDL) · apoA-I (HDL)", fc="#FFF3DE", ec="#B9770E", fs=8.6)
ax.set_title("Сохтори липопротеин ва панҷ класси зичӣ", fontsize=13, pad=14)
save(fig, "shakli_1_1")

# ---------- 1.2 Нақлиёти экзогенӣ ва эндогенӣ ----------
fig, ax = plt.subplots(figsize=(10.8, 7.0))
ax.set_xlim(0, 12); ax.set_ylim(0, 8.4); ax.axis("off")
ax.add_patch(Rectangle((0, 0), 12, 8.4, facecolor=BG, edgecolor="none"))
# экзоген
box(ax, 0.4, 6.7, 5.4, 1.2, "РОҲИ ЭЗОГЕНӢ (ғиза)\nРӯда → хиломикрон (apoB-48)", fc="#FDEBD3", ec="#B9770E", fs=9.4, bold=True)
box(ax, 6.6, 6.7, 5.0, 1.2, "РОҲИ ЭНДОГЕНӢ (ҷигар)\nҶигар → VLDL (apoB-100)", fc="#E8F1F8", ec="#1F4E79", fs=9.4, bold=True)
box(ax, 0.4, 4.6, 5.4, 1.3, "LPL (+apoC-II)\nTG → кислотаҳои чарб\nбарои мушак ва бофтаи чарбӣ", fc="#FFF3DE", ec="#B9770E", fs=8.6)
box(ax, 6.6, 4.6, 5.0, 1.3, "LPL ва липазаи ҷигарӣ\nVLDL → IDL → LDL", fc="#EAF3FB", ec="#1F4E79", fs=8.8)
arr(ax, (3.1, 6.7), (3.1, 5.9)); arr(ax, (9.1, 6.7), (9.1, 5.9))
box(ax, 0.4, 2.6, 5.4, 1.2, "Боқимондаи хиломикрон (apoE)\n→ ба ҷигар (LDLR/LRP)", fc="#FFFFFF", ec="#B9770E", fs=8.6)
box(ax, 6.6, 2.6, 5.0, 1.2, "LDL (холестерин)\n→ ба бофтаҳо тавассути LDLR", fc="#FFFFFF", ec="#1F4E79", fs=8.8)
arr(ax, (3.1, 4.6), (3.1, 3.8)); arr(ax, (9.1, 4.6), (9.1, 3.8))
box(ax, 0.4, 0.7, 5.4, 1.2, "Ҳалқаи фидбек: холестерин\nсинтезро саркунӣ мекунад", fc="#E8F5E9", ec="#1B5E20", fs=8.8)
box(ax, 6.6, 0.7, 5.0, 1.2, "OxLDL → scavenger-рецептор\n→ ҳуҷайраи каф (атеросклероз)", fc="#F6D8D8", ec="#9C1F1F", fs=8.8)
arr(ax, (3.1, 2.6), (3.1, 1.9)); arr(ax, (9.1, 2.6), (9.1, 1.9))
ax.set_title("Нақлиёти липидҳо: роҳи экзогенӣ ва эндогенӣ", fontsize=12.6, pad=14)
save(fig, "shakli_1_2")

# ---------- 2.1 Синтези холестерин ва SREBP ----------
fig, ax = plt.subplots(figsize=(10.6, 7.0))
ax.set_xlim(0, 12); ax.set_ylim(0, 8.4); ax.axis("off")
ax.add_patch(Rectangle((0, 0), 12, 8.4, facecolor=BG, edgecolor="none"))
box(ax, 0.4, 6.9, 2.6, 1.0, "Ацетил-КоА\n(ситоплазма)", fc="#FDEBD3", ec="#B9770E", fs=8.8)
box(ax, 3.6, 6.9, 2.6, 1.0, "Ацетоацетил-КоА\n(тиолаза)", fc="#FFF3DE", ec="#B9770E", fs=8.4)
box(ax, 6.8, 6.9, 2.6, 1.0, "HMG-КоА\n(синтаза)", fc="#FFF3DE", ec="#B9770E", fs=8.8)
box(ax, 9.8, 6.9, 1.8, 1.0, "Мевалонат", fc="#E8F5E9", ec="#1B5E20", fs=9, bold=True)
arr(ax, (3.0, 7.4), (3.6, 7.4)); arr(ax, (6.2, 7.4), (6.8, 7.4)); arr(ax, (9.4, 7.4), (9.8, 7.4))
box(ax, 8.55, 5.3, 3.2, 0.95, "СТАТИН — ингибитори\nHMG-CoA редуктаза", fc="#F6D8D8", ec="#9C1F1F", fs=8.8, bold=True)
ax.text(10.15, 6.45, "қадами нишон", fontsize=8.2, ha="center", color="#9C1F1F")
arr(ax, (10.15, 6.3), (10.4, 6.9), color="#9C1F1F", ls="--")
box(ax, 3.0, 5.3, 2.6, 0.95, "Изопентил-пирофосфат\n(C5, ×6)", fc="#FFFFFF", ec="#1F4E79", fs=8.4)
box(ax, 0.4, 5.3, 2.2, 0.95, "Сквален\n(C30)", fc="#FFFFFF", ec="#1F4E79", fs=9)
arr(ax, (3.0, 5.77), (2.6, 5.77))
box(ax, 3.0, 3.6, 2.6, 0.95, "Ланостерол\n(сикл пӯшида)", fc="#FFFFFF", ec="#1F4E79", fs=8.8)
arr(ax, (1.5, 5.3), (3.6, 4.55))
box(ax, 6.4, 3.6, 3.0, 0.95, "ХОЛЕСТЕРИН\n(19 қадам аз ланостерол)", fc="#E8F5E9", ec="#1B5E20", fs=9.2, bold=True)
arr(ax, (5.6, 4.07), (6.4, 4.07))
box(ax, 10.0, 3.6, 1.6, 0.95, "Кислотаи\nсафровӣ", fc="#FFF3DE", ec="#B9770E", fs=8.4)
arr(ax, (9.4, 4.07), (10.0, 4.07))
box(ax, 0.4, 1.3, 5.2, 1.3, "Танзими SREBP-Scap-Insig:\nкамии холестерин → Голҷӣ → генҳо фаъол\nзичии холестерин → боздор (Insig)", fc="#EAF3FB", ec="#1F4E79", fs=8.6)
box(ax, 6.4, 1.3, 5.2, 1.3, "Манбаи холестерин:\nэндогенӣ 800–1200 mg/рӯз (ҷигар)\nэкзогенӣ 300–700 mg/рӯз (ғиза)", fc="#FFF8E1", ec="#B9770E", fs=8.6)
ax.set_title("Синтези холестерин: қадами нишон ва танзими SREBP", fontsize=12.6, pad=14)
save(fig, "shakli_2_1")

# ---------- 3.1 Нақшаи ташхиси дислипидемия ----------
fig, ax = plt.subplots(figsize=(10.4, 7.2))
ax.set_xlim(0, 12); ax.set_ylim(0, 8.6); ax.axis("off")
ax.add_patch(Rectangle((0, 0), 12, 8.6, facecolor=BG, edgecolor="none"))
box(ax, 3.3, 7.3, 5.4, 1.0, "Панели липидӣ: TC · LDL-C · HDL-C · TG\n(гуруснагии 9–12 соат)", fc="#FDEBD3", ec="#B9770E", fs=9, bold=True)
box(ax, 3.3, 5.9, 5.4, 1.0, "LDL-C ≥190 mg/dL\nГУМОНИ ГИПЕРХОЛЕСТЕРИНЕМИЯИ ОИЛАВӢ (FH)", fc="#FFFFFF", ec="#9C1F1F", fs=8.8, bold=True)
arr(ax, (6.0, 7.3), (6.0, 6.9))
box(ax, 0.5, 4.2, 3.4, 1.15, "Ген-тест:\nLDLR · APOB · PCSK9\n(LDLRAP1 — рецессивӣ)", fc="#E8F1F8", ec="#1F4E79", fs=8.6)
box(ax, 4.35, 4.2, 3.3, 1.15, "TG ≥880 mg/dL\nГУМОНИ НУҚСИ LPL\n(плазмаи ширин)", fc="#E8F1F8", ec="#1F4E79", fs=8.6)
box(ax, 8.3, 4.2, 3.3, 1.15, "HDL-и кам + TG-и баланд\nСЕМЕНИИ МЕТАБОЛИКӢ, диабет,\nгипотиреоз (TSH)", fc="#E8F1F8", ec="#1F4E79", fs=8.4)
arr(ax, (4.5, 5.9), (2.2, 5.35)); arr(ax, (6.0, 5.9), (6.0, 5.35)); arr(ax, (7.5, 5.9), (9.95, 5.35))
box(ax, 0.5, 2.5, 3.4, 1.15, "FH тасдиқ\nстатин + PCSK9-ингибитор\ncascade-тест ба оила", fc="#E8F5E9", ec="#1B5E20", fs=8.6, bold=True)
box(ax, 4.35, 2.5, 3.3, 1.15, "LPL-нуқс тасдиқ\nпарҳези чарби кам,\nfish oil — МАНЪ", fc="#E8F5E9", ec="#1B5E20", fs=8.6, bold=True)
box(ax, 8.3, 2.5, 3.3, 1.15, "Дармуни сабаб:\nгормонҳо, қанд,\nуслоби зиндагӣ", fc="#E8F5E9", ec="#1B5E20", fs=8.6, bold=True)
arr(ax, (2.2, 4.2), (2.2, 3.65)); arr(ax, (6.0, 4.2), (6.0, 3.65)); arr(ax, (9.95, 4.2), (9.95, 3.65))
box(ax, 2.4, 0.7, 7.2, 1.1, "Friedewald: LDL = TC − HDL − TG/5 (mg/dL, TG<400)\nНон-HDL = TC − HDL — apoB-липопротеинҳои ҳама", fc="#FFF3DE", ec="#B9770E", fs=8.8, bold=True)
arr(ax, (6.0, 2.5), (6.0, 1.8))
ax.set_title("Нақшаи ташхиси дислипидемия", fontsize=12.6, pad=14)
save(fig, "shakli_3_1")

# ---------- 4.1 Машғулияти амалӣ: панели липидӣ ----------
fig, ax = plt.subplots(figsize=(10.4, 6.8))
ax.set_xlim(0, 12); ax.set_ylim(0, 8); ax.axis("off")
ax.add_patch(Rectangle((0, 0), 12, 8, facecolor=BG, edgecolor="none"))
box(ax, 0.4, 6.3, 3.5, 1.2, "ҚАДАМИ 1\nГуруснагии 9–12 соат\n(об иҷозат)", fc="#FDEBD3", ec="#B9770E", fs=8.8, bold=True)
box(ax, 4.25, 6.3, 3.5, 1.2, "ҚАДАМИ 2\nНамунаи хун\nTC · HDL · TG", fc="#E8F1F8", ec="#1F4E79", fs=8.8, bold=True)
box(ax, 8.1, 6.3, 3.5, 1.2, "ҚАДАМИ 3\nFriedewald:\nLDL = TC − HDL − TG/5", fc="#E8F5E9", ec="#1B5E20", fs=8.6, bold=True)
arr(ax, (3.9, 6.9), (4.25, 6.9)); arr(ax, (7.75, 6.9), (8.1, 6.9))
box(ax, 0.4, 4.4, 5.6, 1.3, "Меъёрҳо (mg/dL):\nTC <200 · LDL <100 · HDL >40/50 ·\nTG <150 · non-HDL <130", fc="#FFFFFF", ec="#444444", fs=8.8)
box(ax, 6.4, 4.4, 5.2, 1.3, "Ҳушдор:\nLDL ≥190 → FH · TG ≥880 → LPL-нуқс ·\nTG ≥500 → панкреатит", fc="#F6D8D8", ec="#9C1F1F", fs=8.8, bold=True)
# диаграммаи меъёрҳо
cats = ["TC", "LDL", "HDL", "TG"]
vals = [200, 100, 50, 150]
cols = ["#B9770E", "#9C1F1F", "#1B5E20", "#1F4E79"]
mx = 240
for i, (c, v, cc) in enumerate(zip(cats, vals, cols)):
    h = v / mx * 2.0
    ax.add_patch(Rectangle((1.1 + i*2.7, 1.15), 1.5, h, fc=cc, alpha=0.85, ec="none"))
    ax.text(1.85 + i*2.7, 1.2 + h + 0.12, f"<{v}" if c != "HDL" else f">{v}", fontsize=9.6,
            ha="center", fontweight="bold", color=cc)
    ax.text(1.85 + i*2.7, 0.55, c + "\nmg/dL", fontsize=7.8, ha="center", va="top")
ax.text(6.0, 3.85, "Ҳадҳои меъёрии панели липидӣ — ададҳои намунавӣ", fontsize=9.4, ha="center", color="#444444")
ax.set_title("Машғулияти амалӣ: панели липидӣ ва ҳисоби Friedewald", fontsize=12.6, pad=14)
save(fig, "shakli_4_1")

print("ВАЙТ: ҳамаи 5 расм сохта шуданд")
