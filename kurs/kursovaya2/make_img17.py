# -*- coding: utf-8 -*-
"""Расмҳои кори курсӣ М17 — Кислотаҳои сафравӣ ва азот (5 PNG)."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import os

INK = "#1F2A44"; SLATE = "#64748B"; BLUE = "#1D4ED8"; TEAL = "#0F766E"
AMBER = "#B45309"; ROSE = "#BE185D"; PURPLE = "#6D28D9"; BG = "#FBF8F4"
plt.rcParams["font.family"] = "DejaVu Sans"
os.makedirs("img17", exist_ok=True)

def arrow(ax, x1, y1, x2, y2, color, lw=2.2, rad=0.0):
    ax.annotate("", xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle="-|>", color=color, lw=lw,
                                mutation_scale=18,
                                connectionstyle=f"arc3,rad={rad}"))

def box(ax, x, y, w, h, txt, fc, ec, fs=9.2):
    ax.add_patch(mpatches.FancyBboxPatch((x - w/2, y - h/2), w, h,
                 boxstyle="round,pad=0.09", fc=fc, ec=ec, lw=2.0))
    ax.text(x, y, txt, ha="center", va="center", fontsize=fs, color=INK)

# ===== 1.1: Сохтори нуклеотид =====
fig, ax = plt.subplots(figsize=(8.8, 7.0), dpi=200)
fig.patch.set_facecolor(BG); ax.set_facecolor(BG)
ax.text(0.0, 4.55, "Сохтори нуклеотид: асос, қанд ва фосфат", ha="center",
        fontsize=13.5, color=INK, weight="bold")
box(ax, 0, 3.35, 3.1, 0.95, "Асоси азотӣ\n(пурин ё пиримидин)", "#FDF2F8",
    ROSE, fs=10)
box(ax, 0, 1.7, 2.5, 0.95, "Қанд (рибоза ё\nдеоксирибоза)", "#EEF4FB", BLUE,
    fs=9.6)
arrow(ax, 0, 2.87, 0, 2.18, SLATE, lw=2.2)
ax.text(0.42, 2.55, "N-гликозидӣ", fontsize=8.6, color=SLATE)
box(ax, -2.6, 0.25, 2.6, 0.9, "Фосфат\n(1–3 гурӯҳ)", "#FEF6E7", AMBER, fs=9.6)
arrow(ax, -1.3, 0.4, -1.15, 1.35, SLATE, lw=2.2)
ax.text(-2.95, 0.95, "эфирӣ", fontsize=8.6, color=SLATE)
box(ax, 2.6, 0.25, 2.6, 0.9, "5'-фосфодиэфир →\nзанҷири полинуклеотид",
    "#E6F2EF", TEAL, fs=8.6)
ax.text(0, -0.95, "Нуклеозид = асос + қанд   |   Нуклеотид = нуклеозид + фосфат",
        ha="center", fontsize=9.8, color=INK, weight="bold")
ax.text(0, -1.7, "ДНК: деоксирибоза, тимин   |   РНК: рибоза, урацил",
        ha="center", fontsize=9.6, color=SLATE)
ax.set_xlim(-4.4, 4.4); ax.set_ylim(-2.0, 4.8)
ax.set_aspect("equal"); ax.axis("off")
plt.savefig("img17/shakli_1_1.png", dpi=200, facecolor=BG,
            bbox_inches="tight")
plt.close()

# ===== 1.2: Синтези пурин (PRPP → ИМФ) =====
fig, ax = plt.subplots(figsize=(9.4, 6.2), dpi=200)
fig.patch.set_facecolor(BG); ax.set_facecolor(BG)
ax.text(0.0, 4.75, "Синтези пуринҳо: аз PRPP то ИМФ", ha="center",
        fontsize=13.5, color=INK, weight="bold")
box(ax, -3.4, 4.0, 2.3, 0.75, "Рибоза-5-фосфат", "#EEF4FB", BLUE, fs=8.8)
box(ax, -1.1, 4.0, 1.8, 0.75, "PRPP", "#EEF4FB", BLUE, fs=9.5)
box(ax, 1.35, 4.0, 2.4, 0.75, "PRPP-амидотрансфераза", "#FEF6E7", AMBER,
    fs=8.2)
box(ax, 3.55, 4.0, 1.7, 0.75, "ИМФ", "#FDF2F8", ROSE, fs=10.5)
arrow(ax, -2.2, 4.0, -2.02, 4.0, SLATE, lw=2.0)
arrow(ax, -0.2, 4.0, 0.13, 4.0, SLATE, lw=2.0)
arrow(ax, 2.57, 4.0, 2.68, 4.0, SLATE, lw=2.0)
ax.text(0.0, 2.95, "Фидбеки манъӣ: АМФ ва ГМФ", ha="center", fontsize=9.6,
        color=AMBER, weight="bold")
arrow(ax, 1.35, 3.62, 0.6, 3.3, AMBER, lw=1.8)
box(ax, -3.4, 2.2, 2.4, 0.8, "Манбаъҳо: глутамин,\nглицин, аспартат,\nCO2, C1-воҳидҳо",
    "#E6F2EF", TEAL, fs=8.2)
arrow(ax, -2.15, 2.45, -0.6, 3.85, TEAL, lw=1.8)
box(ax, 1.0, 2.2, 2.2, 0.8, "ИМФ → АМФ\nИМФ → ГМФ", "#FDF2F8", ROSE, fs=8.8)
arrow(ax, 3.55, 3.62, 2.15, 2.62, ROSE, lw=1.8)
box(ax, -3.4, 0.8, 2.4, 0.8, "Роҳи қутқодӣ:\nAPRT, HGPRT", "#EEF4FB", BLUE,
    fs=8.8)
arrow(ax, -3.0, 1.22, 0.55, 1.95, BLUE, lw=1.8)
ax.text(-1.3, 1.82, "асосҳои озод", fontsize=8.4, color=BLUE, weight="bold")
ax.text(0.0, -0.1, "Ҷой: ҷигар  |  Ферменти калидӣ: PRPP-амидотрансфераза",
        ha="center", fontsize=9.8, color=INK, weight="bold")
ax.set_xlim(-5.3, 5.3); ax.set_ylim(-0.35, 5.0)
ax.axis("off")
plt.savefig("img17/shakli_1_2.png", dpi=200, facecolor=BG,
            bbox_inches="tight")
plt.close()

# ===== 2.1: Таҷзияи пурин =====
fig, ax = plt.subplots(figsize=(9.4, 6.4), dpi=200)
fig.patch.set_facecolor(BG); ax.set_facecolor(BG)
ax.text(0.0, 5.0, "Роҳи таҷзияи пуринҳо то кислотаи урик", ha="center",
        fontsize=13.5, color=INK, weight="bold")
left = ["АМФ", "ИМФ → инозин", "Гипоксантин", "Ксантин",
        "Кислотаи урик"]
right = ["ГМФ → гуанозин", "Гуанин", "Ксантин", "Кислотаи урик", "Хориҷшавӣ"]
ys = [4.3, 3.4, 2.5, 1.6, 0.7]
for txt, y in zip(left, ys):
    box(ax, -3.2, y, 2.6, 0.68, txt, "#FDF2F8", ROSE, fs=9.0)
for txt, y in zip(right, ys):
    box(ax, 2.9, y, 2.7, 0.68, txt, "#EEF4FB", BLUE, fs=9.0)
for y1, y2 in [(3.96, 3.74), (3.06, 2.84), (2.16, 1.94), (1.26, 1.04)]:
    arrow(ax, -3.2, y1, -3.2, y2, SLATE, lw=2.0)
    arrow(ax, 2.9, y1, 2.9, y2, SLATE, lw=2.0)
ax.text(0.0, 2.5, "ксантиноксидаза", ha="center", fontsize=9.4,
        color=ROSE, weight="bold")
arrow(ax, -1.85, 2.5, 1.5, 2.5, ROSE, lw=2.2)
ax.text(0.0, 0.25, "Одам урикароз надорад → кислотаи урик маҳсули ниҳоӣ аст",
        ha="center", fontsize=9.8, color=INK, weight="bold")
ax.set_xlim(-5.2, 5.2); ax.set_ylim(0.05, 5.35)
ax.axis("off")
plt.savefig("img17/shakli_2_1.png", dpi=200, facecolor=BG,
            bbox_inches="tight")
plt.close()

# ===== 3.1: Сатҳи урат ва хатар =====
fig, ax = plt.subplots(figsize=(9.2, 5.6), dpi=200)
fig.patch.set_facecolor(BG); ax.set_facecolor(BG)
labels = ["Меъёр\n(мардон)", "Мақсади\nтабобат", "Ҳадди\nҳалшавӣ",
          "Хатари\nбаланд", "Ҳамлаи\nшадид"]
vals = [5.3, 6.0, 6.8, 9.0, 12.0]
colors = [TEAL, BLUE, AMBER, ROSE, PURPLE]
x = np.arange(len(labels))
b = ax.bar(x, vals, width=0.55, color=colors, alpha=0.88)
labs = ["5,3", "6,0", "6,8", "9,0", "12+"]
for bi, v, lb in zip(b, vals, labs):
    ax.text(bi.get_x() + bi.get_width()/2, v + 0.25, lb, ha="center",
            fontsize=11, color=INK, weight="bold")
ax.set_xticks(x); ax.set_xticklabels(labels, fontsize=9.4, color=INK)
ax.set_ylim(0, 13.5)
ax.set_ylabel("мг/дл", fontsize=10, color=SLATE)
ax.spines[["top", "right"]].set_visible(False)
ax.text(0.5, 0.96, "Кислотаи урик: ҳадҳои ададӣ ва хатар", ha="center",
        va="top", fontsize=13.5, color=INK, weight="bold",
        transform=ax.transAxes)
plt.savefig("img17/shakli_3_1.png", dpi=200, facecolor=BG,
            bbox_inches="tight")
plt.close()

# ===== 4.1: Давраи уреа =====
fig, ax = plt.subplots(figsize=(9.4, 7.6), dpi=200)
fig.patch.set_facecolor(BG); ax.set_facecolor(BG)
ax.text(0.0, 6.95, "Давраи уреа: ҷой ва ферментҳо", ha="center",
        fontsize=13.5, color=INK, weight="bold")
ax.add_patch(mpatches.Rectangle((-4.9, 3.5), 4.8, 3.2, fill=True,
             fc="#FEF6E7", ec=AMBER, lw=2.2))
ax.text(-2.5, 6.42, "МИТОХОНДРИЯ", ha="center", fontsize=9.6,
        color=AMBER, weight="bold")
ax.add_patch(mpatches.Rectangle((0.3, 3.5), 4.6, 3.2, fill=True,
             fc="#E6F2EF", ec=TEAL, lw=2.2))
ax.text(2.6, 6.42, "ЦИТОЗОЛ", ha="center", fontsize=9.6, color=TEAL,
        weight="bold")
box(ax, -3.8, 5.95, 2.0, 0.8, "CPS1\n(N-ацетилглутамат)", "#FEF6E7", AMBER,
    fs=8.0)
box(ax, -1.4, 5.95, 1.7, 0.8, "OTC", "#FEF6E7", AMBER, fs=9.0)
arrow(ax, -2.77, 5.95, -2.28, 5.95, SLATE, lw=2.0)
box(ax, 2.6, 5.95, 2.3, 0.8, "Аргининосукцинат-\nсинтетаза (ASS1)",
    "#E6F2EF", TEAL, fs=7.8)
box(ax, 2.6, 4.75, 2.3, 0.74, "Аргининосукцинат-\nлиаза (ASL)",
    "#E6F2EF", TEAL, fs=7.8)
arrow(ax, 2.6, 5.52, 2.6, 5.14, SLATE, lw=2.0)
box(ax, 2.6, 3.95, 2.0, 0.62, "Аргиназа", "#E6F2EF", TEAL, fs=8.6)
arrow(ax, 2.6, 4.35, 2.6, 4.28, SLATE, lw=2.0)
arrow(ax, -0.52, 5.95, 1.42, 5.95, SLATE, lw=2.2)
ax.text(0.42, 6.22, "цитруллин", fontsize=8.2, color=SLATE, ha="center",
        weight="bold")
arrow(ax, 1.62, 3.98, -1.05, 5.35, BLUE, lw=2.0, rad=-0.5)
ax.text(-0.25, 3.95, "орнитин бармегардад", fontsize=8.2, color=BLUE,
        ha="center", weight="bold")
box(ax, -3.1, 2.35, 3.6, 0.78, "Аммиак (аз кислотаҳои аминок ва рӯда)",
    "#FDF2F8", ROSE, fs=8.4)
arrow(ax, -3.7, 2.77, -3.8, 5.52, ROSE, lw=2.0)
box(ax, 1.0, 2.0, 3.0, 0.74, "Уреа → гурда → пешоб", "#FDF2F8", ROSE, fs=9.2)
arrow(ax, 2.35, 3.62, 1.75, 2.4, ROSE, lw=2.2)
ax.text(2.95, 3.0, "уреа", fontsize=8.8, color=ROSE, weight="bold")
ax.text(0.0, 0.95, "Ҳар давр: 2 азот + CO2 → уреа (10–20 г дар рӯз)",
        ha="center", fontsize=9.8, color=INK, weight="bold")
ax.set_xlim(-5.5, 5.5); ax.set_ylim(0.7, 7.35)
ax.axis("off")
plt.savefig("img17/shakli_4_1.png", dpi=200, facecolor=BG,
            bbox_inches="tight")
plt.close()

print("img17 ok: 5 PNG")
