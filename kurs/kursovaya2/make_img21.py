# -*- coding: utf-8 -*-
"""Расмҳои М21: PLP-механизм, роҳи ғизо→АК, давраи уреа, ALT/AST-диаграмма, нақшаи ташхис."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyBboxPatch, FancyArrowPatch, Rectangle
import numpy as np, os

plt.rcParams["font.family"] = "DejaVu Sans"
BG = "#FBF8F4"
OUT = "img21"
os.makedirs(OUT, exist_ok=True)

def save(fig, name):
    fig.savefig(f"{OUT}/{name}.png", dpi=200, bbox_inches="tight", facecolor=BG)
    plt.close(fig)
    print(name, "ok")

# ---------- 1.1 Механизми PLP ----------
fig, ax = plt.subplots(figsize=(9.6, 6.4))
ax.set_xlim(0, 12); ax.set_ylim(0, 8); ax.axis("off")
ax.add_patch(Rectangle((0, 0), 12, 8, facecolor=BG, edgecolor="none"))
ax.text(6, 7.4, "Марҳилаи 1: PLP амино мегирад", fontsize=12, ha="center", color="#7A4A12", fontweight="bold")
ax.add_patch(FancyBboxPatch((0.7, 4.3), 3.3, 1.5, boxstyle="round,pad=0.1", fc="#FFE9C9", ec="#B9770E", lw=2))
ax.text(2.35, 5.05, "Аминокислота\n(R-CH-NH₂)", ha="center", va="center", fontsize=10)
ax.add_patch(FancyBboxPatch((4.9, 4.3), 2.6, 1.5, boxstyle="round,pad=0.1", fc="#F3D9B0", ec="#7A4A12", lw=2))
ax.text(6.2, 5.05, "PLP\n(алдегид-шакл)", ha="center", va="center", fontsize=10, fontweight="bold")
ax.add_patch(FancyBboxPatch((8.4, 4.3), 2.9, 1.5, boxstyle="round,pad=0.1", fc="#DCE9F5", ec="#1F4E79", lw=2))
ax.text(9.85, 5.05, "Кето-кислота\n(R-C=O)", ha="center", va="center", fontsize=10)
ax.add_patch(FancyArrowPatch((4.0, 5.05), (4.9, 5.05), arrowstyle="-|>", mutation_scale=16, color="#7A4A12", lw=2))
ax.add_patch(FancyArrowPatch((7.5, 5.05), (8.4, 5.05), arrowstyle="-|>", mutation_scale=16, color="#7A4A12", lw=2))
ax.text(4.45, 5.35, "-NH₂", fontsize=9, ha="center", color="#7A4A12")
ax.text(7.95, 5.35, "-NH₂", fontsize=9, ha="center", color="#7A4A12")
ax.text(6, 2.9, "Марҳилаи 2: PMP амино медиҳад", fontsize=12, ha="center", color="#1F4E79", fontweight="bold")
ax.add_patch(FancyBboxPatch((4.9, 0.7), 2.6, 1.5, boxstyle="round,pad=0.1", fc="#C7D8EA", ec="#1F4E79", lw=2))
ax.text(6.2, 1.45, "PMP\n(амин-шакл)", ha="center", va="center", fontsize=10, fontweight="bold")
ax.add_patch(FancyBboxPatch((0.7, 0.7), 3.3, 1.5, boxstyle="round,pad=0.1", fc="#E8F1F8", ec="#1F4E79", lw=2))
ax.text(2.35, 1.45, "α-Кетоглутарат", ha="center", va="center", fontsize=10)
ax.add_patch(FancyBboxPatch((8.4, 0.7), 2.9, 1.5, boxstyle="round,pad=0.1", fc="#F6D8D8", ec="#9C1F1F", lw=2))
ax.text(9.85, 1.45, "Глутамат", ha="center", va="center", fontsize=10)
ax.add_patch(FancyArrowPatch((4.0, 1.45), (4.9, 1.45), arrowstyle="-|>", mutation_scale=16, color="#1F4E79", lw=2))
ax.add_patch(FancyArrowPatch((7.5, 1.45), (8.4, 1.45), arrowstyle="-|>", mutation_scale=16, color="#1F4E79", lw=2))
ax.text(4.45, 1.75, "+NH₂", fontsize=9, ha="center", color="#1F4E79")
ax.text(7.95, 1.75, "+NH₂", fontsize=9, ha="center", color="#1F4E79")
ax.add_patch(FancyArrowPatch((6.2, 4.3), (6.2, 2.2), arrowstyle="-|>", mutation_scale=16, color="#444444", lw=2.2, linestyle="--"))
ax.text(6.55, 3.25, "PLP → PMP → PLP", fontsize=10.5, color="#444444")
save(fig, "shakli_1_1")

# ---------- 1.2 Роҳи ғизо → АК ----------
fig, ax = plt.subplots(figsize=(10.2, 6.2))
ax.set_xlim(0, 12); ax.set_ylim(0, 7.6); ax.axis("off")
ax.add_patch(Rectangle((0, 0), 12, 7.6, facecolor=BG, edgecolor="none"))
def fnode(x, y, w, h, txt, fc="#FFFFFF", ec="#444444", fs=9.2):
    b = FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.1", fc=fc, ec=ec, lw=2)
    ax.add_patch(b)
    ax.text(x + w/2, y + h/2, txt, ha="center", va="center", fontsize=fs, zorder=5)
def farrow(p1, p2, label="", ly=0.28, fs=8.4, color="#333333"):
    a = FancyArrowPatch(p1, p2, arrowstyle="-|>", mutation_scale=15, color=color, lw=1.8)
    ax.add_patch(a)
    if label:
        ax.text((p1[0]+p2[0])/2, (p1[1]+p2[1])/2 + ly, label, fontsize=fs, color=color, ha="center")
fnode(0.4, 5.6, 2.7, 1.2, "Сафедаи ғизо\n(100 г/рӯз)", fc="#FFF3DE", ec="#B9770E")
fnode(4.0, 5.6, 2.9, 1.2, "Пепсин, pH 1,5–2\n→ пептидҳо", fc="#FFE9C9", ec="#B9770E", fs=8.8)
fnode(8.0, 5.6, 3.4, 1.2, "Трипсин, химотрипсин\n(ошкунак) → АК", fc="#E8F1F8", ec="#1F4E79", fs=8.6)
farrow((3.1, 6.2), (4.0, 6.2), "меъда")
farrow((6.9, 6.2), (8.0, 6.2), "рӯда")
fnode(4.6, 3.2, 3.2, 1.2, "ХАЗИНАИ АК\n(≈100 г)", fc="#F6D8D8", ec="#9C1F1F", fs=10)
farrow((9.7, 5.6), (7.4, 4.4), "ҷабб дар энтеросит", ly=0.3)
fnode(0.6, 0.6, 3.1, 1.2, "Синтези сафеда", fc="#E8F5E9", ec="#1B5E20")
fnode(4.6, 0.6, 3.2, 1.2, "Азот → уреа\n(трансаминатсия)", fc="#FFF8E1", ec="#B9770E", fs=8.8)
fnode(8.8, 0.6, 2.7, 1.2, "Скелет → энергия\n(Кребс)", fc="#E3F2FD", ec="#1F4E79", fs=8.8)
farrow((5.4, 3.2), (2.4, 1.8), "")
farrow((6.2, 3.2), (6.2, 1.8), "")
farrow((7.2, 3.2), (9.9, 1.8), "")
ax.set_title("Аз сафедаи ғизо то хазинаи аминокислотаҳо ва се роҳи истифода", fontsize=12.5, pad=14)
save(fig, "shakli_1_2")

# ---------- 2.1 Давраи уреа ----------
fig, ax = plt.subplots(figsize=(10.4, 7.0))
ax.set_xlim(0, 12); ax.set_ylim(0, 8.4); ax.axis("off")
ax.add_patch(Rectangle((0, 0), 12, 8.4, facecolor=BG, edgecolor="none"))
mito = FancyBboxPatch((0.2, 4.9), 11.6, 3.2, boxstyle="round,pad=0.1", fc="#FDEBD3", ec="#B9770E", lw=2)
cyto = FancyBboxPatch((0.2, 0.3), 11.6, 3.9, boxstyle="round,pad=0.1", fc="#E8F1F8", ec="#1F4E79", lw=2)
ax.add_patch(mito); ax.add_patch(cyto)
ax.text(0.55, 7.75, "МИТОХОНДРИЯ", fontsize=11, color="#B9770E", fontweight="bold")
ax.text(6.2, 3.95, "СИТОПЛАЗМА", fontsize=11, color="#1F4E79", fontweight="bold", ha="center")
def node(x, y, w, h, txt, fc="#FFFFFF", ec="#444444", fs=8.6):
    b = FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.07", fc=fc, ec=ec, lw=1.7)
    ax.add_patch(b)
    ax.text(x + w/2, y + h/2, txt, ha="center", va="center", fontsize=fs, zorder=5)
def harrow(x1, y1, x2, y2, label="", ly=0.3, fs=8.0, color="#333333"):
    a = FancyArrowPatch((x1, y1), (x2, y2), arrowstyle="-|>", mutation_scale=14, color=color, lw=1.8, zorder=4)
    ax.add_patch(a)
    if label:
        ax.text((x1 + x2)/2, (y1 + y2)/2 + ly, label, ha="center", fontsize=fs, color=color)
node(0.6, 6.0, 3.2, 1.3, "CO₂ + NH₄⁺ + 2ATP\n→ Карбамоилфосфат", fc="#FFF3DE", ec="#B9770E", fs=8.2)
ax.text(2.2, 5.75, "CPS1 (марҳ. 1) ← NAG", fontsize=8, color="#9C1F1F", ha="center")
node(5.6, 6.0, 2.6, 1.3, "Карбамоилфосфат +\nОрнитин → Ситруллин", fc="#FFE9C9", ec="#B9770E", fs=8.0)
ax.text(6.9, 5.75, "OTC (марҳ. 2)", fontsize=8, color="#9C1F1F", ha="center")
a = FancyArrowPatch((8.2, 6.65), (8.2, 3.4), arrowstyle="-|>", mutation_scale=14, color="#1F4E79", lw=1.8)
ax.add_patch(a)
ax.text(8.5, 5.0, "ба ситоплазма", fontsize=8, color="#1F4E79")
node(7.4, 2.3, 3.6, 1.3, "Ситруллин + Аспартат →\nАргининсукцинат  [ASS1, 3]", fc="#DCE9F5", ec="#1F4E79", fs=8.0)
node(3.6, 2.3, 3.0, 1.3, "→ Аргинин + Фумарат\n[ASL, 4]", fc="#DCE9F5", ec="#1F4E79", fs=8.4)
node(0.4, 2.3, 2.6, 1.3, "→ УРЕА + Орнитин\n[ARG1, 5]", fc="#F6D8D8", ec="#9C1F1F", fs=8.6)
harrow(7.4, 2.95, 6.6, 2.95, "")
harrow(3.6, 2.95, 3.0, 2.95, "")
a = FancyArrowPatch((1.7, 3.6), (1.7, 5.5), arrowstyle="-|>", mutation_scale=14, color="#B9770E", lw=1.8)
ax.add_patch(a)
ax.text(1.15, 4.55, "орнитин\nбармегардад", fontsize=7.6, color="#B9770E", ha="center")
ax.text(5.0, 0.55, "Фумарат → давраи Кребс  |  Аспартат ← AST (аз глутамат + ОАА)", fontsize=8.6, color="#555555", ha="center")
ax.set_title("Давраи уреа: 2 марҳила дар митохондрия, 3 дар ситоплазма", fontsize=12.5, pad=14)
save(fig, "shakli_2_1")

# ---------- 3.1 ALT/AST дар бемориҳо ----------
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10.8, 5.6), facecolor=BG)
diseases = ["Солим", "Вайрусии\nшадид", "Спиртӣ", "Фиброз"]
alt = [25, 3500, 120, 90]
ast = [20, 2200, 280, 130]
x = np.arange(len(diseases)); w = 0.38
ax1.bar(x - w/2, alt, w, label="ALT", color="#1F4E79")
ax1.bar(x + w/2, ast, w, label="AST", color="#B9770E")
ax1.set_yscale("log")
ax1.set_xticks(x); ax1.set_xticklabels(diseases, fontsize=9)
ax1.set_ylabel("Е/л (лог.)", fontsize=10)
ax1.set_title("Сатҳи ALT ва AST", fontsize=11.5)
ax1.legend(); ax1.grid(axis="y", alpha=0.3)
ratios = [20/25, 2200/3500, 280/120, 130/90]
bars = ax2.bar(diseases, ratios, color=["#888888", "#1B5E20", "#9C1F1F", "#B9770E"])
ax2.axhline(1.0, color="#555555", ls="--", lw=1.2)
ax2.axhline(2.0, color="#9C1F1F", ls="--", lw=1.2)
ax2.text(3.4, 1.05, "DeRitis = 1", fontsize=8.5, color="#555555")
ax2.text(3.4, 2.05, "DeRitis = 2", fontsize=8.5, color="#9C1F1F")
ax2.set_ylabel("AST / ALT", fontsize=10)
ax2.set_title("Нисбати DeRitis", fontsize=11.5)
ax2.grid(axis="y", alpha=0.3)
fig.suptitle("ALT, AST ва нисбати DeRitis дар бемориҳои ҷигар", fontsize=13)
fig.tight_layout(rect=[0, 0, 1, 0.93])
save(fig, "shakli_3_1")

# ---------- 4.1 Нақшаи ташхис ----------
fig, ax = plt.subplots(figsize=(9.6, 7.2))
ax.set_xlim(0, 12); ax.set_ylim(0, 9.2); ax.axis("off")
ax.add_patch(Rectangle((0, 0), 12, 9.2, facecolor=BG, edgecolor="none"))
def fnode(x, y, w, h, txt, fc="#FFFFFF", ec="#444444", fs=9.0):
    b = FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.1", fc=fc, ec=ec, lw=2)
    ax.add_patch(b)
    ax.text(x + w/2, y + h/2, txt, ha="center", va="center", fontsize=fs, zorder=5)
def farrow(p1, p2, label="", lx=0, ly=0.26, fs=8.4, color="#333333"):
    a = FancyArrowPatch(p1, p2, arrowstyle="-|>", mutation_scale=15, color=color, lw=1.8)
    ax.add_patch(a)
    if label:
        ax.text((p1[0]+p2[0])/2 + lx, (p1[1]+p2[1])/2 + ly, label, fontsize=fs, color=color, ha="center")
fnode(3.8, 7.7, 4.4, 1.1, "Гумон: гипераммониемия\n(летаргия, қай, энсефалопатия)", fc="#FDEBD3", ec="#B9770E", fs=8.8)
fnode(0.5, 5.3, 3.3, 1.3, "Аммиак > 100 (навзод)\nё > 50 (калонсол)\n→ тасдиқ", fc="#F6D8D8", ec="#9C1F1F", fs=8.6)
fnode(4.4, 5.3, 3.3, 1.3, "Кислотаи оротик-и пешоб ↑\n→ нуқси OTC", fc="#E8F1F8", ec="#1F4E79", fs=8.6)
fnode(8.4, 5.3, 3.2, 1.3, "Аммиак нормалӣ\n→ панели ҷигар (ALT/AST)", fc="#E8F5E9", ec="#1B5E20", fs=8.4)
fnode(1.6, 2.6, 3.0, 1.3, "АК-и плазма\n(тандем-МС)\n→ MSUD, PKU", fc="#F3E5F5", ec="#6A1B9A", fs=8.6)
fnode(5.6, 2.6, 3.0, 1.3, "Нисбати Фишер ↑\n+ аллоизолейцин\n→ MSUD", fc="#E0F2F1", ec="#00695C", fs=8.6)
fnode(9.0, 2.6, 2.6, 1.3, "Phe/Tyr ↑\n→ PKU", fc="#FFF8E1", ec="#B9770E", fs=8.8)
fnode(3.5, 0.4, 5.0, 1.1, "Даво: азотсбёр (фенилбутират), калория, диализ", fc="#FFFFFF", ec="#555555", fs=9)
farrow((5.0, 7.7), (2.15, 6.6), "қадами 1", ly=0.22)
farrow((6.0, 7.7), (6.05, 6.6), "қадами 2")
farrow((7.0, 7.7), (10.0, 6.6), "қадами 3")
farrow((2.15, 5.3), (2.9, 3.9), "UCD?")
farrow((6.05, 5.3), (6.8, 3.9), "ACM?")
farrow((9.95, 5.3), (10.2, 3.9), "Phe?")
farrow((5.2, 2.6), (6.0, 1.5), "даво")
ax.set_title("Нақшаи ташхиси гипераммониемия ва аминокислотаметиё", fontsize=12.5, pad=14)
save(fig, "shakli_4_1")
print("img21: 5 rasm tayor")
