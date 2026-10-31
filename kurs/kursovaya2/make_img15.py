# -*- coding: utf-8 -*-
"""Расмҳои кори курсӣ М15 — Витаминҳо (4 PNG)."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import os

INK = "#1F2A44"; SLATE = "#64748B"; BLUE = "#1D4ED8"; TEAL = "#0F766E"
AMBER = "#B45309"; ROSE = "#BE185D"; PURPLE = "#6D28D9"; BG = "#FBF8F4"
plt.rcParams["font.family"] = "DejaVu Sans"
os.makedirs("img15", exist_ok=True)

def arrow(ax, x1, y1, x2, y2, color, lw=2.2):
    ax.annotate("", xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle="-|>", color=color, lw=lw,
                                mutation_scale=18))

def box(ax, x, y, w, h, txt, fc, ec, fs=9.2):
    ax.add_patch(mpatches.FancyBboxPatch((x - w/2, y - h/2), w, h,
                 boxstyle="round,pad=0.09", fc=fc, ec=ec, lw=2.0))
    ax.text(x, y, txt, ha="center", va="center", fontsize=fs, color=INK)

# ===== 1.1: Дарахти таснифоти витаминҳо =====
fig, ax = plt.subplots(figsize=(9.4, 6.4), dpi=200)
fig.patch.set_facecolor(BG); ax.set_facecolor(BG)
ax.text(0.0, 5.05, "Таснифоти витаминҳо", ha="center", fontsize=13.5,
        color=INK, weight="bold")
box(ax, 0.0, 4.4, 3.0, 0.72, "ВИТАМИНҲО (13)", "#EEF4FB", BLUE, fs=10.5)
box(ax, -2.4, 3.2, 2.9, 0.72, "Ҳалкунандаи об", "#E6F2EF", TEAL, fs=10.2)
box(ax, 2.4, 3.2, 2.9, 0.72, "Ҷаррӣ", "#FEF6E7", AMBER, fs=10.2)
arrow(ax, -0.9, 4.04, -1.9, 3.56, SLATE, lw=2.2)
arrow(ax, 0.9, 4.04, 1.9, 3.56, SLATE, lw=2.2)
ax.text(-2.4, 2.62, "B1, B2, PP, B6,\nфолат, B12, C", ha="center",
        fontsize=10, color=INK, weight="bold")
ax.text(2.4, 2.62, "A, D, E, K", ha="center", fontsize=10, color=INK,
        weight="bold")
ax.text(-2.4, 1.92, "захираи кам —\nба пешоб мераванд", ha="center",
        fontsize=9.2, color=SLATE)
ax.text(2.4, 1.92, "дар ҷигар ва бофтаи\nчарб захира мешаванд",
        ha="center", fontsize=9.2, color=SLATE)
ax.text(0.0, 1.1, "Гурӯҳи B асосан кофермент аст; витаминаи D",
        ha="center", fontsize=9.6, color=SLATE)
ax.text(0.0, 0.68, "нақши гормонӣ дорад", ha="center", fontsize=9.6,
        color=SLATE)
ax.set_xlim(-4.9, 4.9); ax.set_ylim(0.4, 5.3)
ax.axis("off")
plt.savefig("img15/shakli_1_1.png", dpi=200, facecolor=BG,
            bbox_inches="tight")
plt.close()

# ===== 2.1: Трансаминатсия бо PLP =====
fig, ax = plt.subplots(figsize=(9.4, 5.2), dpi=200)
fig.patch.set_facecolor(BG); ax.set_facecolor(BG)
ax.text(0.0, 3.6, "Реаксияи трансаминатсия бо иштироки PLP", ha="center",
        fontsize=13.5, color=INK, weight="bold")
box(ax, -3.0, 2.5, 2.6, 0.8, "Аминокислота 1", "#EEF4FB", BLUE)
box(ax, 3.0, 2.5, 2.6, 0.8, "Альфа-кетоглутарат", "#FDF2F8", ROSE, fs=8.8)
box(ax, -3.0, 0.9, 2.6, 0.8, "Альфа-кето кислота", "#E6F2EF", TEAL, fs=8.8)
box(ax, 3.0, 0.9, 2.6, 0.8, "Глутамат", "#FEF6E7", AMBER)
box(ax, 0.0, 1.7, 2.3, 0.85, "Трансаминаза\n+ PLP", "#EDE9FE", PURPLE,
    fs=9.6)
arrow(ax, -1.65, 2.35, -1.1, 1.9, SLATE, lw=2.2)
arrow(ax, 1.65, 2.35, 1.1, 1.9, SLATE, lw=2.2)
arrow(ax, -1.1, 1.5, -1.65, 1.05, SLATE, lw=2.2)
arrow(ax, 1.1, 1.5, 1.65, 1.05, SLATE, lw=2.2)
ax.text(-4.05, 0.15, "гурӯҳи NH2 мегузарад", ha="center", fontsize=9.2,
        color=BLUE, weight="bold")
ax.text(4.15, 0.15, "азот ба уреа мерасад", ha="center", fontsize=9.2,
        color=ROSE, weight="bold")
ax.set_xlim(-5.2, 5.2); ax.set_ylim(-0.25, 3.85)
ax.axis("off")
plt.savefig("img15/shakli_2_1.png", dpi=200, facecolor=BG,
            bbox_inches="tight")
plt.close()

# ===== 3.1: Витамин D — пӯст, ҷигар, гурда =====
fig, ax = plt.subplots(figsize=(9.4, 5.6), dpi=200)
fig.patch.set_facecolor(BG); ax.set_facecolor(BG)
ax.text(0.0, 4.55, "Мубодилаи витамини D: се марҳила", ha="center",
        fontsize=13.5, color=INK, weight="bold")
box(ax, -3.5, 3.4, 2.5, 0.85, "ПӮСТ\n7-ДХК + нур", "#FEF6E7", AMBER, fs=9.2)
box(ax, 0.0, 3.4, 2.5, 0.85, "ҶИГАР\n25-гидроксилаза", "#E6F2EF", TEAL,
    fs=9.2)
box(ax, 3.5, 3.4, 2.5, 0.85, "ГУРДА\n1-альфа-гидроксилаза", "#EEF4FB",
    BLUE, fs=8.8)
arrow(ax, -2.2, 3.4, -1.3, 3.4, SLATE, lw=2.2)
arrow(ax, 1.3, 3.4, 2.2, 3.4, SLATE, lw=2.2)
ax.text(-1.75, 3.62, "холекалсиферол (D3)", ha="center", fontsize=8.2,
        color=SLATE)
ax.text(1.75, 3.62, "25-OH-D", ha="center", fontsize=8.2, color=SLATE)
box(ax, 0.0, 1.85, 3.4, 0.85, "КАЛЦИТРИОЛ — 1,25(OH)2D3", "#FDF2F8", ROSE,
    fs=9.6)
arrow(ax, 3.5, 2.95, 1.75, 2.25, SLATE, lw=2.2)
box(ax, -2.6, 0.65, 2.2, 0.75, "рӯда:\nҷабби калсий", "#FFF7ED", SLATE,
    fs=8.8)
box(ax, 0.0, 0.65, 2.2, 0.75, "устухон:\nминералҳо", "#FFF7ED", SLATE,
    fs=8.8)
box(ax, 2.6, 0.65, 2.2, 0.75, "гурда:\nбозчамъи калсий", "#FFF7ED", SLATE,
    fs=8.8)
arrow(ax, -1.0, 1.42, -2.2, 1.05, SLATE, lw=1.9)
arrow(ax, 0.0, 1.42, 0.0, 1.05, SLATE, lw=1.9)
arrow(ax, 1.0, 1.42, 2.2, 1.05, SLATE, lw=1.9)
ax.text(0.0, -0.2, "Ками D: рахит (кӯдакон) ва остеомаляция (калонсолон)",
        ha="center", fontsize=9.6, color=INK, weight="bold")
ax.set_xlim(-5.2, 5.2); ax.set_ylim(-0.5, 4.75)
ax.axis("off")
plt.savefig("img15/shakli_3_1.png", dpi=200, facecolor=BG,
            bbox_inches="tight")
plt.close()

# ===== 4.1: Ҳадҳои рӯзона (мг/рӯз) =====
fig, ax = plt.subplots(figsize=(9.2, 5.4), dpi=200)
fig.patch.set_facecolor(BG); ax.set_facecolor(BG)
ax.text(0.5, 0.985, "Ҳадҳои рӯзонаи баъзе витаминҳо (мг/рӯз)", ha="center",
        va="top", fontsize=13.5, color=INK, weight="bold",
        transform=ax.transAxes)
names = ["C", "PP", "E", "B6", "B2", "B1"]
vals = [90, 16, 15, 1.7, 1.3, 1.2]
colors = [ROSE, PURPLE, TEAL, BLUE, AMBER, SLATE]
y = np.arange(len(names))[::-1]
b = ax.barh(y, vals, height=0.55, color=colors, alpha=0.88)
for bi, v in zip(b, vals):
    lab = f"{v:g}"
    ax.text(v + 1.6, bi.get_y() + bi.get_height()/2, lab, va="center",
            fontsize=11, color=INK, weight="bold")
ax.set_yticks(y)
ax.set_yticklabels([f"Витамини {n}" for n in names], fontsize=10, color=INK)
ax.set_xlim(0, 104)
ax.set_ylim(-0.6, 5.95)
ax.set_xlabel("мг/рӯз", fontsize=10, color=SLATE)
ax.spines[["top", "right"]].set_visible(False)
ax.text(0.5, -0.14, "Фолат, B12, A, D ва K бо микрограмм ё воҳид чен мешаванд",
        ha="center", fontsize=9.5, color=SLATE, transform=ax.transAxes)
plt.savefig("img15/shakli_4_1.png", dpi=200, facecolor=BG,
            bbox_inches="tight")
plt.close()

print("img15 ok: 4 PNG")
