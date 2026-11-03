# -*- coding: utf-8 -*-
"""Расмҳои М20: сохтори гем, роҳи 8-марҳила, мубодилаи оҳан, фарқи камхуниҳо, нақшаи панели оҳан."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyBboxPatch, FancyArrowPatch, Rectangle
import numpy as np, os

plt.rcParams["font.family"] = "DejaVu Sans"
BG = "#FBF8F4"
OUT = "img20"
os.makedirs(OUT, exist_ok=True)

def save(fig, name):
    fig.savefig(f"{OUT}/{name}.png", dpi=200, bbox_inches="tight", facecolor=BG)
    plt.close(fig)
    print(name, "ok")

# ---------- 1.1 Сохтори гем ----------
fig, ax = plt.subplots(figsize=(8.2, 6.2))
ax.set_xlim(0, 10); ax.set_ylim(0, 7.6); ax.axis("off")
ax.add_patch(Rectangle((0, 0), 10, 7.6, facecolor=BG, edgecolor="none"))
ang = np.linspace(0, 2*np.pi, 4, endpoint=False) + np.pi/4
ring_xy = [(5 + 2.1*np.cos(a), 3.9 + 1.75*np.sin(a)) for a in ang]
for i, (x, y) in enumerate(ring_xy):
    ax.add_patch(Circle((x, y), 0.78, facecolor="#F3D9B0", edgecolor="#7A4A12", lw=2.2, zorder=3))
    ax.text(x, y, f"N", ha="center", va="center", fontsize=13, color="#7A4A12", zorder=4, fontweight="bold")
for i in range(4):
    x1, y1 = ring_xy[i]; x2, y2 = ring_xy[(i + 1) % 4]
    ax.plot([x1, x2], [y1, y2], color="#7A4A12", lw=2.0, zorder=2)
    mx, my = (x1 + x2) / 2, (y1 + y2) / 2
    ax.add_patch(Circle((mx, my), 0.14, facecolor="#7A4A12", edgecolor="none", zorder=3))
    ax.text(mx + 0.22, my + 0.2, "CH", fontsize=8.5, color="#5A3A0A", zorder=3)
ax.add_patch(Circle((5, 3.9), 0.95, facecolor="#C7D8EA", edgecolor="#1F4E79", lw=2.6, zorder=5))
ax.text(5, 3.9, "Fe$^{2+}$", ha="center", va="center", fontsize=15, fontweight="bold", color="#1F4E79", zorder=6)
labels = ["метил", "винил", "пропионат", "метил"]
side_xy = [(5 + 3.6*np.cos(a), 3.9 + 3.0*np.sin(a)) for a in (ang + 0.4)]
for (x, y), lb in zip(side_xy, labels):
    ax.text(x, y, lb, fontsize=11, color="#8A4B0F", ha="center",
            bbox=dict(boxstyle="round,pad=0.3", fc="#FFE9C9", ec="#C98A3D"))
ax.set_title("Сохтори гем: ҳалқаи порфирин, пулҳои метин ва оҳани марказӣ", fontsize=13, pad=14)
save(fig, "shakli_1_1")

# ---------- 1.2 Роҳи ҳаштмарҳила (сохтори морпуст) ----------
fig, ax = plt.subplots(figsize=(10.6, 6.8))
ax.set_xlim(0, 12); ax.set_ylim(0, 8); ax.axis("off")
ax.add_patch(Rectangle((0, 0), 12, 8, facecolor=BG, edgecolor="none"))
# 3 bands: mito / cyto / mito
ax.add_patch(FancyBboxPatch((0.15, 5.7), 11.7, 2.0, boxstyle="round,pad=0.1", fc="#FDEBD3", ec="#B9770E", lw=2))
ax.add_patch(FancyBboxPatch((0.15, 3.5), 11.7, 2.0, boxstyle="round,pad=0.1", fc="#E8F1F8", ec="#1F4E79", lw=2))
ax.add_patch(FancyBboxPatch((0.15, 0.55), 11.7, 2.2, boxstyle="round,pad=0.1", fc="#FDEBD3", ec="#B9770E", lw=2))
ax.text(0.45, 7.32, "МИТОХОНДРИЯ", fontsize=11, color="#B9770E", fontweight="bold")
ax.text(6.1, 5.18, "ЦИТОПЛАЗМА", fontsize=11, color="#1F4E79", fontweight="bold", ha="center")
ax.text(6.1, 2.38, "МИТОХОНДРИЯ", fontsize=11, color="#B9770E", fontweight="bold", ha="center")
def node(x, y, w, h, txt, fc="#FFFFFF", ec="#444444", fs=8.4):
    b = FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.07", fc=fc, ec=ec, lw=1.7)
    ax.add_patch(b)
    ax.text(x + w/2, y + h/2, txt, ha="center", va="center", fontsize=fs, zorder=5)
def harrow(x1, y1, x2, y2, label="", ly=0.3, fs=8.0, color="#333333"):
    a = FancyArrowPatch((x1, y1), (x2, y2), arrowstyle="-|>", mutation_scale=14, color=color, lw=1.7, zorder=4)
    ax.add_patch(a)
    if label:
        ax.text((x1 + x2)/2, (y1 + y2)/2 + ly, label, ha="center", fontsize=fs, color=color)
# band 1: gly + succCoA -> ALA
node(1.2, 6.1, 3.6, 0.95, "Глицин + сукцинил-КоА", fc="#FFF3DE", ec="#B9770E")
node(8.9, 6.1, 1.7, 0.95, "ALA", fc="#FFE9C9", ec="#B9770E", fs=9)
harrow(4.8, 6.575, 8.9, 6.575, "ALA-синтаза (PLP), марҳилаи 1", ly=0.32)
a = FancyArrowPatch((9.75, 6.1), (9.75, 4.85), arrowstyle="-|>", mutation_scale=14, color="#1F4E79", lw=1.8)
ax.add_patch(a)
ax.text(10.0, 5.45, "ба цитоплазма", fontsize=8.2, color="#1F4E79")
# band 2 (рост ба чап): ALA -> PBG -> HMB -> УПГ III -> КПГ III
node(8.9, 3.9, 1.7, 0.95, "ALA", fc="#DCE9F5", ec="#1F4E79", fs=9)
node(6.7, 3.9, 1.8, 0.95, "Порфобилиноген", fc="#DCE9F5", ec="#1F4E79", fs=8.2)
node(4.6, 3.9, 1.7, 0.95, "HMB", fc="#DCE9F5", ec="#1F4E79", fs=9)
node(2.3, 3.9, 1.9, 0.95, "Уропорфириноген III", fc="#DCE9F5", ec="#1F4E79", fs=8.2)
node(0.2, 3.9, 1.75, 0.95, "Копропорфириноген III", fc="#DCE9F5", ec="#1F4E79", fs=7.0)
harrow(8.9, 4.375, 8.5, 4.375, "ALA-дегидратаза (Zn), 2", ly=-0.42)
harrow(6.7, 4.375, 6.3, 4.375, "PBG-деаминаза, 3", ly=-0.42)
harrow(4.6, 4.375, 4.2, 4.375, "синтаза III, 4", ly=-0.42)
harrow(2.3, 4.375, 1.95, 4.375, "декарбоксилаза, 5", ly=-0.42)
a = FancyArrowPatch((1.05, 3.9), (1.05, 1.95), arrowstyle="-|>", mutation_scale=14, color="#B9770E", lw=1.8)
ax.add_patch(a)
ax.text(1.35, 3.15, "ба митохондрия", fontsize=8.2, color="#B9770E")
# band 3: КПГ III -> ППГ IX -> ПП IX -> ГЕМ
node(0.35, 1.0, 1.9, 0.95, "Копропорфириноген III", fc="#FFF3DE", ec="#B9770E", fs=7.8)
node(2.75, 1.0, 2.1, 0.95, "Протопорфириноген IX", fc="#FFF3DE", ec="#B9770E", fs=8.2)
node(5.35, 1.0, 1.9, 0.95, "Протопорфирин IX", fc="#FFF3DE", ec="#B9770E", fs=8.2)
node(8.0, 1.0, 2.3, 0.95, "ГЕМ (Fe$^{2+}$)", fc="#F6D8D8", ec="#9C1F1F", fs=10.5)
harrow(2.25, 1.475, 2.75, 1.475, "оксидаза, 6", ly=0.35, fs=7.8)
harrow(4.85, 1.475, 5.35, 1.475, "оксидаза, 7", ly=0.35, fs=7.8)
harrow(7.25, 1.475, 8.0, 1.475, "феррокелатаза + Fe$^{2+}$, 8", ly=0.35, fs=7.8)
ax.set_title("Роҳи ҳаштмарҳилаи синтези гем: байни митохондрия ва цитоплазма", fontsize=12.5, pad=14)
save(fig, "shakli_1_2")

# ---------- 2.1 Ҷабби оҳан ва гепсидин ----------
fig, ax = plt.subplots(figsize=(9.2, 6.6))
ax.set_xlim(0, 12); ax.set_ylim(0, 8.4); ax.axis("off")
ax.add_patch(Rectangle((0, 0), 12, 8.4, facecolor=BG, edgecolor="none"))
ent = FancyBboxPatch((2.6, 2.6), 4.2, 4.4, boxstyle="round,pad=0.12", fc="#EAF3EA", ec="#2E7D32", lw=2.2)
ax.add_patch(ent)
ax.text(4.7, 6.65, "ЭНТЕРОСИТ", fontsize=11.5, color="#2E7D32", fontweight="bold", ha="center")
ax.text(1.15, 5.2, "Рӯда", fontsize=10.5, color="#555555", ha="center")
ax.text(1.15, 4.75, "Fe$^{3+}$ дар ғизо", fontsize=9.5, color="#555555", ha="center")
ax.add_patch(Circle((2.6, 5.6), 0.16, fc="#8A4B0F", ec="none"))
ax.text(2.72, 5.95, "Dcytb: Fe$^{3+}$ → Fe$^{2+}$", fontsize=9, color="#1B5E20")
ax.add_patch(FancyArrowPatch((1.6, 5.2), (2.75, 5.0), arrowstyle="-|>", mutation_scale=15, color="#1B5E20", lw=1.8))
ax.text(3.05, 4.98, "DMT1", fontsize=9, color="#1B5E20")
ax.add_patch(Circle((5.4, 5.6), 0.62, fc="#F6D8B0", ec="#8A4B0F", lw=1.8))
ax.text(5.4, 5.6, "Ферритин", ha="center", va="center", fontsize=8.6)
ax.add_patch(FancyArrowPatch((3.6, 5.05), (4.85, 5.45), arrowstyle="-|>", mutation_scale=13, color="#8A4B0F", lw=1.6))
ax.text(3.75, 5.6, "захира", fontsize=8.2, color="#8A4B0F")
ax.add_patch(FancyArrowPatch((5.4, 4.6), (5.4, 3.3), arrowstyle="-|>", mutation_scale=15, color="#1B5E20", lw=1.9))
ax.text(5.62, 3.95, "Ферропортин", fontsize=9.4, color="#1B5E20")
liv = FancyBboxPatch((8.0, 5.2), 3.4, 2.4, boxstyle="round,pad=0.12", fc="#FDEBD3", ec="#B9770E", lw=2.2)
ax.add_patch(liv)
ax.text(9.7, 7.2, "ҶИГАР", fontsize=11.5, color="#B9770E", fontweight="bold", ha="center")
ax.add_patch(Circle((9.7, 6.3), 0.72, fc="#F3C6C6", ec="#9C1F1F", lw=2))
ax.text(9.7, 6.3, "Гепсидин", ha="center", va="center", fontsize=9.6, color="#9C1F1F")
ax.text(9.7, 5.42, "IL-6 ↑", fontsize=9, color="#9C1F1F", ha="center")
ax.add_patch(FancyArrowPatch((9.0, 5.55), (6.1, 3.6), arrowstyle="-|>", mutation_scale=15,
                             color="#9C1F1F", lw=2.0, linestyle="--"))
ax.text(7.9, 4.25, "блоки бароӣ", fontsize=9, color="#9C1F1F", rotation=27)
bl = FancyBboxPatch((3.0, 0.45), 6.6, 1.35, boxstyle="round,pad=0.12", fc="#E8F1F8", ec="#1F4E79", lw=2.2)
ax.add_patch(bl)
ax.text(6.3, 1.35, "ХУН", fontsize=11, color="#1F4E79", fontweight="bold", ha="center")
ax.add_patch(Circle((4.5, 0.95), 0.55, fc="#C7D8EA", ec="#1F4E79", lw=1.8))
ax.text(4.5, 0.95, "Трансферрин\n(2×Fe$^{3+}$)", ha="center", va="center", fontsize=8.4)
ax.text(7.4, 0.95, "→ мӯҳри сурх", fontsize=9.4, color="#1F4E79")
ax.add_patch(FancyArrowPatch((5.4, 3.3), (4.9, 1.9), arrowstyle="-|>", mutation_scale=15, color="#1B5E20", lw=1.9))
ax.text(6.9, 2.6, "церулоплазмин / гефестин: Fe$^{2+}$ → Fe$^{3+}$", fontsize=8.6, color="#555555")
ax.set_title("Ҷабби оҳан: Dcytb, DMT1, ферропортин ва блоки гепсидин", fontsize=12.5, pad=14)
save(fig, "shakli_2_1")

# ---------- 3.1 Фарқи камхуниҳо ----------
fig, ax = plt.subplots(figsize=(8.6, 6.4))
ax.set_facecolor(BG)
pts = [
 ("Камхунии темирнокӣ", 72, 12, "#1B5E20"),
 ("Камхунии музмин", 86, 150, "#B9770E"),
 ("Сидеробластикӣ", 74, 200, "#9C1F1F"),
 ("Талассемия", 68, 120, "#6A1B9A"),
 ("Камии B12", 112, 90, "#1F4E79"),
 ("Камии фолат", 108, 110, "#00695C"),
]
for name, mcv, ferr, c in pts:
    ax.scatter(mcv, ferr, s=210, color=c, edgecolor="#333333", lw=1.2, zorder=3)
    ax.annotate(name, (mcv, ferr), textcoords="offset points", xytext=(9, 8),
                fontsize=9.5, color=c)
ax.axvline(80, color="#888888", lw=1.4, linestyle="--")
ax.axvline(100, color="#888888", lw=1.4, linestyle="--")
ax.axhline(30, color="#888888", lw=1.4, linestyle=":")
ax.axhline(300, color="#888888", lw=1.4, linestyle=":")
ax.set_xlim(55, 130); ax.set_ylim(0, 320)
ax.set_xlabel("MCV, фЛ", fontsize=11)
ax.set_ylabel("Ферритин, мкг/л", fontsize=11)
ax.grid(alpha=0.25)
ax.text(60, 300, "микроситик", fontsize=9.5, color="#666666")
ax.text(84, 300, "нормоситик", fontsize=9.5, color="#666666")
ax.text(104, 300, "макроситик", fontsize=9.5, color="#666666")
ax.set_title("Фарқи камхуниҳо: MCV ва ферритин", fontsize=13, pad=14)
save(fig, "shakli_3_1")

# ---------- 4.1 Нақшаи панели оҳан ----------
fig, ax = plt.subplots(figsize=(9.4, 6.8))
ax.set_xlim(0, 12); ax.set_ylim(0, 8.6); ax.axis("off")
ax.add_patch(Rectangle((0, 0), 12, 8.6, facecolor=BG, edgecolor="none"))
def fnode(x, y, w, h, txt, fc="#FFFFFF", ec="#444444", fs=9.5):
    b = FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.1", fc=fc, ec=ec, lw=2)
    ax.add_patch(b)
    ax.text(x + w/2, y + h/2, txt, ha="center", va="center", fontsize=fs, zorder=5)
def farrow(p1, p2, label="", lx=0, ly=0, fs=8.6, color="#333333"):
    a = FancyArrowPatch(p1, p2, arrowstyle="-|>", mutation_scale=15, color=color, lw=1.8)
    ax.add_patch(a)
    if label:
        mx, my = (p1[0]+p2[0])/2 + lx, (p1[1]+p2[1])/2 + ly
        ax.text(mx, my, label, fontsize=fs, color=color, ha="center")
fnode(4.2, 7.0, 3.6, 1.1, "Панели оҳан:\nферритин, оҳан, TIBC, ҳиссат", fc="#FDEBD3", ec="#B9770E", fs=9)
fnode(0.6, 4.6, 3.3, 1.3, "Ферритин < 30 мкг/л\n→ камхунии темирнокӣ", fc="#E8F5E9", ec="#1B5E20")
fnode(4.4, 4.6, 3.3, 1.3, "Ферритин ≥ 100 ва\nҳиссат < 20 фоиз\n→ илтиҳоб", fc="#FFF8E1", ec="#B9770E", fs=9)
fnode(8.3, 4.6, 3.3, 1.3, "Ферритин > 300 ва\nҳиссат > 45 фоиз\n→ фароғат", fc="#FDE7E7", ec="#9C1F1F", fs=9)
fnode(0.6, 1.6, 3.3, 1.3, "MCV < 80:\nмикроситик\n(талассемия, сурб)", fc="#F3E5F5", ec="#6A1B9A", fs=9)
fnode(4.4, 1.6, 3.3, 1.3, "MCV > 100:\nB12, MMA, фолат,\nгомосистеин", fc="#E0F2F1", ec="#00695C", fs=9)
fnode(8.3, 1.6, 3.3, 1.3, "Гаптоглобин < 25, LDH ↑,\nретикулосит > 2,5 фоиз\n→ ҳамолиз", fc="#E3F2FD", ec="#1F4E79", fs=9)
farrow((5.2, 7.0), (2.25, 5.9), "қадами 1", ly=0.25)
farrow((6.0, 7.0), (6.05, 5.9), "қадами 2")
farrow((6.9, 7.0), (9.95, 5.9), "қадами 3")
farrow((2.25, 4.6), (2.25, 2.9), "MCV")
farrow((6.05, 4.6), (6.05, 2.9), "MCV")
farrow((9.95, 4.6), (9.95, 2.9), "ҳамолиз?", color="#1F4E79")
ax.set_title("Нақшаи ҳисобии панели оҳан барои машғулияти амалӣ", fontsize=12.5, pad=14)
save(fig, "shakli_4_1")
print("img20: 5 rasm tayor")
