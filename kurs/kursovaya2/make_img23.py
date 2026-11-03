# -*- coding: utf-8 -*-
"""Расмҳои М23: сохтори FFA/триглитсерид, бета-оксидшавӣ, CPT-шаттл+кетогенез, нақшаи ташхис, машқи амалӣ."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Rectangle, Ellipse, Wedge
import numpy as np, os

plt.rcParams["font.family"] = "DejaVu Sans"
BG = "#FBF8F4"
OUT = "img23"
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

# ---------- 1.1 Сохтори кислотаҳои чарб ва триглитсерид ----------
fig, ax = plt.subplots(figsize=(10.4, 6.6))
ax.set_xlim(0, 12); ax.set_ylim(0, 8); ax.axis("off")
ax.add_patch(Rectangle((0, 0), 12, 8, facecolor=BG, edgecolor="none"))
# триглитсерид
box(ax, 4.2, 6.0, 3.6, 1.3, "ТРИГЛИТСЕРИД\n(глитсерол + 3 кислота)", fc="#FDEBD3", ec="#B9770E", fs=9.6, bold=True)
box(ax, 0.5, 3.9, 2.7, 1.2, "Кислотаи чарб 1\n(палмитат C16:0)", fc="#FFF3DE", ec="#B9770E", fs=8.4)
box(ax, 4.6, 3.9, 2.7, 1.2, "Кислотаи чарб 2\n(олеат C18:1)", fc="#FFF3DE", ec="#B9770E", fs=8.4)
box(ax, 8.7, 3.9, 2.8, 1.2, "Кислотаи чарб 3\n(линолат C18:2)", fc="#FFF3DE", ec="#B9770E", fs=8.4)
arr(ax, (5.3, 6.0), (1.9, 5.1)); arr(ax, (6.0, 6.0), (6.0, 5.1)); arr(ax, (6.7, 6.0), (10.0, 5.1))
ax.text(2.2, 5.45, "липолиз", fontsize=8.4, color="#7A4A12")
# сохтори кислота
box(ax, 0.6, 0.6, 5.0, 2.5, "", fc="#EAF3FB", ec="#1F4E79", lw=2)
ax.text(3.1, 2.7, "СОХТОРИ УМУМӢ", fontsize=10.5, ha="center", color="#1F4E79", fontweight="bold")
ax.text(3.1, 2.05, "CH₃—(CH₂)ₙ—COOH", fontsize=11, ha="center", color="#1F4E79")
ax.text(3.1, 1.35, "Метил ← занҷираи карбонӣ → карбоксил", fontsize=9, ha="center")
ax.text(3.1, 0.9, "Сергидроген: бе C=C · Бисёрпайваст: бо C=C", fontsize=9, ha="center")
box(ax, 6.4, 0.6, 5.1, 2.5, "", fc="#FFF8E1", ec="#B9770E", lw=2)
ax.text(8.95, 2.7, "ЗАХИРА ВА ЭНЕРГИЯ", fontsize=10.5, ha="center", color="#7A4A12", fontweight="bold")
ax.text(8.95, 2.05, "1 г чарб ≈ 9 ккал", fontsize=10.5, ha="center")
ax.text(8.95, 1.35, "Гликоген: 1 рӯз · Чарб: чанд моҳ", fontsize=9, ha="center")
ax.text(8.95, 0.9, "Нақлиёт бо албумин дар хун", fontsize=9, ha="center")
ax.set_title("Сохтори кислотаҳои чарб ва триглитсерид ҳамчун захира", fontsize=13, pad=14)
save(fig, "shakli_1_1")

# ---------- 1.2 Чор марҳилаи бета-оксидшавӣ ----------
fig, ax = plt.subplots(figsize=(10.6, 7.0))
ax.set_xlim(0, 12); ax.set_ylim(0, 8.4); ax.axis("off")
ax.add_patch(Rectangle((0, 0), 12, 8.4, facecolor=BG, edgecolor="none"))
cx, cy, R = 4.9, 4.05, 2.15
box(ax, 0.4, 7.1, 3.4, 1.05, "Вуруд: ацил-КоА\n(аз CPT-шаттл)", fc="#FDEBD3", ec="#B9770E", fs=8.6)
arr(ax, (2.6, 7.1), (4.1, 6.75))
# ҳалқаи марҳилаҳо
phases = [
    (90,  "1. ОКСИДШАВӢ", "Ацил-КоАДГ (FAD)", "#B9770E"),
    (0,   "2. ГИДРАТАТСИЯ", "Эноил-КоА гидратаза", "#1F4E79"),
    (270, "3. ОКСИДШАВӢ", "β-гидроксиАКДГ (NAD⁺)", "#1B5E20"),
    (180, "4. ТИОЛИЗ", "β-кетотиолаза + HS-КоА", "#9C1F1F"),
]
for ang, title, enz, col in phases:
    a = np.deg2rad(ang)
    x, y = cx + R*1.42*np.cos(a), cy + R*1.08*np.sin(a)
    box(ax, x-1.5, y-0.52, 3.0, 1.04, f"{title}\n{enz}", fc="#FFFFFF", ec=col, fs=8.2, bold=True)
    ax.add_patch(Wedge((cx, cy), 0.62, ang-40, ang+40, fc=col, alpha=0.85, ec="none"))
ax.text(cx, cy, "Ҳар давр\nC₂↓", ha="center", va="center", fontsize=10, fontweight="bold",
        color="#333333", zorder=6, bbox=dict(fc=BG, ec="none", pad=2))
# маҳсулот
box(ax, 8.4, 6.4, 3.2, 1.1, "FADH₂ ва NADH\n→ занҷири нақлиёти электрон", fc="#E8F1F8", ec="#1F4E79", fs=8.4)
box(ax, 8.4, 4.6, 3.2, 1.1, "Ацетил-КоА\n→ Кребс ё кетогенез", fc="#E8F5E9", ec="#1B5E20", fs=8.6, bold=True)
arr(ax, (7.6, 6.35), (8.4, 6.85), label="", ly=0)
arr(ax, (7.4, 4.4), (8.4, 5.0), label="", ly=0)
box(ax, 0.4, 0.45, 3.6, 1.0, "Палмитат C16 → 7 давр →\n8 ацетил-КоА ≈ 106 ATP", fc="#FFF3DE", ec="#B9770E", fs=8.6, bold=True)
arr(ax, (2.2, 1.45), (3.3, 2.9), label="", ly=0, color="#B9770E")
ax.text(9.9, 2.4, "Кислотаҳои тоқ →\nпропионил-КоА →\nсукцинил-КоА", fontsize=8.4, ha="center", color="#444444")
ax.set_title("Чор марҳилаи бета-оксидшавӣ: ҳар давр як ҷуфти карбон мебарад", fontsize=12.6, pad=14)
save(fig, "shakli_1_2")

# ---------- 2.1 CPT-шаттл ва кетогенез ----------
fig, ax = plt.subplots(figsize=(10.8, 7.0))
ax.set_xlim(0, 12); ax.set_ylim(0, 8.4); ax.axis("off")
ax.add_patch(Rectangle((0, 0), 12, 8.4, facecolor=BG, edgecolor="none"))
# шаттл
box(ax, 0.4, 5.6, 2.6, 1.2, "Ацил-КоА\n(ситоплазма)", fc="#FDEBD3", ec="#B9770E", fs=8.8)
box(ax, 3.6, 5.6, 2.3, 1.2, "CPT1\n+ карнитин", fc="#E8F1F8", ec="#1F4E79", fs=9, bold=True)
box(ax, 6.5, 5.6, 2.3, 1.2, "Ацил-карнитин\nмембрана", fc="#FFFFFF", ec="#1F4E79", fs=8.6)
box(ax, 9.4, 5.6, 2.2, 1.2, "CPT2\n→ ацил-КоА", fc="#E8F1F8", ec="#1F4E79", fs=9, bold=True)
arr(ax, (3.0, 6.2), (3.6, 6.2)); arr(ax, (5.9, 6.2), (6.5, 6.2)); arr(ax, (8.8, 6.2), (9.4, 6.2))
ax.text(10.55, 7.05, "Митохондрия →", fontsize=8.6, color="#444444", ha="center")
box(ax, 6.5, 4.0, 5.1, 0.95, "Матрикс: бета-оксидшавӣ → ацетил-КоА", fc="#E8F5E9", ec="#1B5E20", fs=9.4, bold=True)
arr(ax, (10.5, 5.6), (10.5, 4.95))
box(ax, 0.4, 4.0, 3.6, 0.95, "Малонил-КоА — манъкунандаи CPT1", fc="#F6D8D8", ec="#9C1F1F", fs=8.8)
arr(ax, (4.7, 4.95), (4.7, 5.6), color="#9C1F1F", ls="--")
# кетогенез
box(ax, 0.6, 2.3, 2.3, 1.05, "2 ацетил-КоА\nтиолаза", fc="#FFF3DE", ec="#B9770E", fs=8.4)
box(ax, 3.5, 2.3, 2.5, 1.05, "Ацетоацетил-КоА\n+ ацетили 3", fc="#FFF3DE", ec="#B9770E", fs=8.2)
box(ax, 6.6, 2.3, 2.4, 1.05, "HMG-КоА\n(синтаза)", fc="#FFFFFF", ec="#1F4E79", fs=8.8, bold=True)
box(ax, 9.6, 2.3, 2.0, 1.05, "ЛИАЗА\nацетоацетат", fc="#E8F5E9", ec="#1B5E20", fs=8.6, bold=True)
arr(ax, (2.9, 2.8), (3.5, 2.8)); arr(ax, (6.0, 2.8), (6.6, 2.8)); arr(ax, (9.0, 2.8), (9.6, 2.8))
box(ax, 3.5, 0.6, 2.5, 1.0, "β-гидроксибутират\n(NADH)", fc="#E8F1F8", ec="#1F4E79", fs=8.4)
box(ax, 6.6, 0.6, 2.4, 1.0, "Ацетон\n(нафас)", fc="#F6D8D8", ec="#9C1F1F", fs=8.4)
arr(ax, (10.3, 2.3), (9.1, 1.6), label="ДГ", ly=0.28, fs=8)
arr(ax, (10.0, 2.3), (7.95, 1.65), label="декарбоксил.", ly=-0.3, fs=8)
ax.set_title("CPT-шаттл ба матрикс ва кетогенез дар ҷигар (HMG-КоА)", fontsize=12.6, pad=14)
save(fig, "shakli_2_1")

# ---------- 3.1 Нақшаи ташхиси гипогликемияи гипокетотикӣ ----------
fig, ax = plt.subplots(figsize=(10.4, 7.2))
ax.set_xlim(0, 12); ax.set_ylim(0, 8.6); ax.axis("off")
ax.add_patch(Rectangle((0, 0), 12, 8.6, facecolor=BG, edgecolor="none"))
box(ax, 3.4, 7.3, 5.2, 1.0, "Кӯдак: гуруснагӣ → летаргия, ташнагӣ\nё скрининги навзодӣ", fc="#FDEBD3", ec="#B9770E", fs=9, bold=True)
box(ax, 3.4, 5.8, 5.2, 1.0, "Глюкозаи хун ↓ + кетонҳои пешоб (−)\nГИПОГЛИКЕМИЯИ ГИПОКЕТОТИКӢ", fc="#FFFFFF", ec="#9C1F1F", fs=9, bold=True)
arr(ax, (6.0, 7.3), (6.0, 6.8))
box(ax, 0.5, 4.2, 3.3, 1.1, "Асильно-карнитин ↑\n(тандем-МС, хуни хушк)", fc="#E8F1F8", ec="#1F4E79", fs=8.6)
box(ax, 4.35, 4.2, 3.3, 1.1, "Кислотаҳои дикарбонатии пешоб ↑\n(C6–C10, тест-и фарқӣ)", fc="#E8F1F8", ec="#1F4E79", fs=8.4)
box(ax, 8.2, 4.2, 3.3, 1.1, "Карнитини умумӣ ↓ / ацил ↓\n(CPT1: рақами нормалӣ)", fc="#E8F1F8", ec="#1F4E79", fs=8.4)
arr(ax, (4.6, 5.8), (2.2, 5.3)); arr(ax, (6.0, 5.8), (6.0, 5.3)); arr(ax, (7.4, 5.8), (9.8, 5.3))
box(ax, 0.5, 2.5, 3.3, 1.15, "МУТАТСИЯ ACADM\nc.985A>G\n→ МСAD тасдиқ", fc="#E8F5E9", ec="#1B5E20", fs=8.6, bold=True)
box(ax, 4.35, 2.5, 3.3, 1.15, "Ферменти CPT2 ↓\nдар лимфотситҳо\n→ CPT II тасдиқ", fc="#E8F5E9", ec="#1B5E20", fs=8.6, bold=True)
box(ax, 8.2, 2.5, 3.3, 1.15, "Фаъолияти CPT1A\n(1–5% боқимонда)\n→ CPT1A тасдиқ", fc="#E8F5E9", ec="#1B5E20", fs=8.6, bold=True)
arr(ax, (2.1, 4.2), (2.1, 3.65)); arr(ax, (6.0, 4.2), (6.0, 3.65)); arr(ax, (9.85, 4.2), (9.85, 3.65))
box(ax, 2.6, 0.6, 6.8, 1.15, "ДАРМОН: хӯроки мунтазам · машқи вазнин манъ ·\nдар крисис глюкозаи варидӣ + назорати кетон", fc="#FFF3DE", ec="#B9770E", fs=9, bold=True)
arr(ax, (6.0, 2.5), (6.0, 1.75))
ax.set_title("Нақшаи ташхиси гипогликемияи гипокетотикӣ (FAOD)", fontsize=12.6, pad=14)
save(fig, "shakli_3_1")

# ---------- 4.1 Машғулияти амалӣ: панели кетон ----------
fig, ax = plt.subplots(figsize=(10.4, 6.8))
ax.set_xlim(0, 12); ax.set_ylim(0, 8); ax.axis("off")
ax.add_patch(Rectangle((0, 0), 12, 8, facecolor=BG, edgecolor="none"))
box(ax, 0.4, 6.3, 3.5, 1.2, "ҚАДАМИ 1\nПарҳези шабона\n(8–12 соат, об иҷозат)", fc="#FDEBD3", ec="#B9770E", fs=8.8, bold=True)
box(ax, 4.25, 6.3, 3.5, 1.2, "ҚАДАМИ 2\nНамунаи хун аз банана\n(сабоғи асептикӣ)", fc="#E8F1F8", ec="#1F4E79", fs=8.8, bold=True)
box(ax, 8.1, 6.3, 3.5, 1.2, "ҚАДАМИ 3\nГлюкометри кетонӣ\n(бета-гидроксибутират)", fc="#E8F5E9", ec="#1B5E20", fs=8.6, bold=True)
arr(ax, (3.9, 6.9), (4.25, 6.9)); arr(ax, (7.75, 6.9), (8.1, 6.9))
box(ax, 0.4, 4.4, 5.6, 1.3, "Ҷадвали натиҷа (mmol/л):\n0.0–0.5 нормалӣ · 0.6–1.5 гуруснагӣ ·\n1.6–3.0 кетози муътадил · >3.0 кетоаз", fc="#FFFFFF", ec="#444444", fs=8.8)
box(ax, 6.4, 4.4, 5.2, 1.3, "Фарқи DKA (ёдоварӣ):\nглюкоза >250 mg/dL + pH <7.3 +\nкетон >3.0 → фаврӣ!", fc="#F6D8D8", ec="#9C1F1F", fs=8.8, bold=True)
# диаграммаи содаи ададӣ
cats = ["Гуруснагӣ\n(кӯтоҳ)", "Гуруснагӣ\n(дароз)", "Диетаи\nкетонӣ", "DKA"]
vals = [0.3, 2.5, 1.8, 8.0]
cols = ["#1B5E20", "#B9770E", "#1F4E79", "#9C1F1F"]
for i, (c, v, cc) in enumerate(zip(cats, vals, cols)):
    h = v / 8.0 * 2.2
    ax.add_patch(Rectangle((0.9 + i*2.7, 1.1), 1.7, h, fc=cc, alpha=0.85, ec="none"))
    ax.text(1.75 + i*2.7, 1.15 + h + 0.12, f"{v}", fontsize=9.6, ha="center", fontweight="bold", color=cc)
    ax.text(1.75 + i*2.7, 0.55, c, fontsize=7.8, ha="center", va="top")
ax.text(6.0, 3.65, "Бета-гидроксибутират, mmol/л — ададҳои намунавӣ", fontsize=9.4, ha="center", color="#444444")
ax.set_title("Машғулияти амалӣ: ченкунии кетон ва фарқи кетоаз", fontsize=12.6, pad=14)
save(fig, "shakli_4_1")

print("ВАЙТ: ҳамаи 5 расм сохта шуданд")
