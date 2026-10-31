# -*- coding: utf-8 -*-
"""Расмҳои кори курсӣ М16 — Мубодилаи пигментҳо (5 PNG)."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import os

INK = "#1F2A44"; SLATE = "#64748B"; BLUE = "#1D4ED8"; TEAL = "#0F766E"
AMBER = "#B45309"; ROSE = "#BE185D"; PURPLE = "#6D28D9"; BG = "#FBF8F4"
plt.rcParams["font.family"] = "DejaVu Sans"
os.makedirs("img16", exist_ok=True)

def arrow(ax, x1, y1, x2, y2, color, lw=2.2):
    ax.annotate("", xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle="-|>", color=color, lw=lw,
                                mutation_scale=18))

def box(ax, x, y, w, h, txt, fc, ec, fs=9.2):
    ax.add_patch(mpatches.FancyBboxPatch((x - w/2, y - h/2), w, h,
                 boxstyle="round,pad=0.09", fc=fc, ec=ec, lw=2.0))
    ax.text(x, y, txt, ha="center", va="center", fontsize=fs, color=INK)

# ===== 1.1: Сохтори гем =====
fig, ax = plt.subplots(figsize=(8.8, 7.2), dpi=200)
fig.patch.set_facecolor(BG); ax.set_facecolor(BG)
ax.text(0.0, 4.55, "Сохтори гем: ҳалқаи порфирин ва оҳан", ha="center",
        fontsize=13.5, color=INK, weight="bold")
# чор ҳалқаи пирролӣ
for ang, (cx, cy) in zip((45, 135, 225, 315),
                         ((1.45, 1.45), (-1.45, 1.45), (-1.45, -1.45), (1.45, -1.45))):
    ax.add_patch(mpatches.Circle((cx, cy), 0.85, fc="#E6F2EF", ec=TEAL,
                 lw=2.2))
    ax.text(cx, cy, "N", ha="center", va="center", fontsize=12,
            color=TEAL, weight="bold")
ax.add_patch(mpatches.Circle((0, 0), 0.95, fc="#FEF3C7", ec=AMBER, lw=2.4))
ax.text(0, 0, "Fe2+", ha="center", va="center", fontsize=13, color=INK,
        weight="bold")
# пайвастҳои метинӣ
for (x1, y1, x2, y2) in [(1.05, 2.15, -1.05, 2.15), (-2.15, 1.05, -2.15, -1.05),
                         (-1.05, -2.15, 1.05, -2.15), (2.15, -1.05, 2.15, 1.05)]:
    ax.plot([x1, x2], [y1, y2], color=SLATE, lw=2.2)
ax.text(0, 2.55, "пайвастҳои метинӣ", ha="center", fontsize=9.4, color=SLATE)
# гурӯҳҳои бокӣ
for (x, y, t) in [(0, -2.85, "гурӯҳҳои бокӣ: метил, винил, пропионат")]:
    ax.text(x, y, t, ha="center", fontsize=9.6, color=SLATE)
ax.text(0, -3.5, "Протопорфирини IX + Fe2+ = ГЕМ", ha="center", fontsize=11,
        color=INK, weight="bold")
ax.set_xlim(-3.6, 3.6); ax.set_ylim(-3.85, 4.8)
ax.set_aspect("equal"); ax.axis("off")
plt.savefig("img16/shakli_1_1.png", dpi=200, facecolor=BG,
            bbox_inches="tight")
plt.close()

# ===== 1.2: Синтези гем ва порфириҳо =====
fig, ax = plt.subplots(figsize=(9.4, 6.2), dpi=200)
fig.patch.set_facecolor(BG); ax.set_facecolor(BG)
ax.text(0.0, 4.75, "Роҳи синтези гем ва порфириҳо", ha="center",
        fontsize=13.5, color=INK, weight="bold")
box(ax, -3.4, 4.0, 2.5, 0.75, "Глицин + сукцинил-КоА", "#EEF4FB", BLUE,
    fs=8.6)
box(ax, -1.15, 4.0, 1.9, 0.75, "ALA", "#EEF4FB", BLUE)
box(ax, 1.15, 4.0, 2.1, 0.75, "Порфобилиноген", "#E6F2EF", TEAL, fs=9.2)
box(ax, 3.4, 4.0, 2.1, 0.75, "Уропорфириноген III", "#E6F2EF", TEAL, fs=8.4)
arrow(ax, -2.1, 4.0, -1.75, 4.0, SLATE, lw=2.0)
arrow(ax, -0.2, 4.0, 0.15, 4.0, SLATE, lw=2.0)
arrow(ax, 2.2, 4.0, 2.55, 4.0, SLATE, lw=2.0)
ax.text(-1.95, 4.42, "ALA-синтаза", ha="center", fontsize=8.2, color=BLUE,
        weight="bold")
box(ax, -3.4, 2.6, 2.4, 0.75, "Копропорфириноген III", "#FEF6E7", AMBER,
    fs=8.4)
box(ax, -1.15, 2.6, 2.2, 0.75, "Протопорфирини IX", "#FEF6E7", AMBER, fs=9.0)
box(ax, 1.3, 2.6, 2.1, 0.75, "ГЕМ", "#FDF2F8", ROSE, fs=10.5)
arrow(ax, -2.15, 2.6, -1.75, 2.6, SLATE, lw=2.0)
arrow(ax, -0.0, 2.6, 0.35, 2.6, SLATE, lw=2.2)
ax.text(0.18, 3.02, "феррокелатаза + Fe2+", ha="center", fontsize=8.2,
        color=ROSE, weight="bold")
ax.text(1.3, 2.0, "сурб: манъи ALA-дегидратаза ва феррокелатаза",
        ha="center", fontsize=8.6, color=ROSE)
box(ax, -3.4, 1.0, 2.4, 0.8, "Порфирияи ҳамла", "#FEF2F2", ROSE, fs=9.2)
arrow(ax, -3.0, 3.62, -3.25, 1.42, SLATE, lw=1.8)
ax.text(-3.55, 2.35, "ками ферментҳо", fontsize=8.4, color=ROSE,
        weight="bold")
ax.text(0.0, 0.25, "Танзим: гем — фидбеки манъӣ барои ALA-синтаза",
        ha="center", fontsize=9.8, color=INK, weight="bold")
ax.set_xlim(-5.3, 5.3); ax.set_ylim(0.0, 5.0)
ax.axis("off")
plt.savefig("img16/shakli_1_2.png", dpi=200, facecolor=BG,
            bbox_inches="tight")
plt.close()

# ===== 2.1: Роҳи билирубин =====
fig, ax = plt.subplots(figsize=(9.4, 6.8), dpi=200)
fig.patch.set_facecolor(BG); ax.set_facecolor(BG)
ax.text(0.0, 5.55, "Роҳи мубодилаи билирубин", ha="center", fontsize=13.5,
        color=INK, weight="bold")
left = ["Эритросит (120 рӯз)", "Гем", "Биливердин (сабз)",
        "Билирубин (сурх)", "Ҳамроҳи албумин дар хун"]
right = ["Ҷигар: ҷабб ва UGT1A1", "Конюгатсия (диглюкуронид)",
         "Нӯҷа", "Рӯда: уробилиноген", "Стеркобилин + пешоб"]
ys = [4.7, 3.75, 2.8, 1.85, 0.9]
for txt, y in zip(left, ys):
    box(ax, -3.3, y, 2.7, 0.72, txt, "#FDF2F8", ROSE, fs=8.8)
for txt, y in zip(right, ys):
    box(ax, 3.0, y, 2.8, 0.72, txt, "#EEF4FB", BLUE, fs=8.8)
for y1, y2 in [(4.34, 4.11), (3.39, 3.16), (2.44, 2.21), (1.49, 1.26)]:
    arrow(ax, -3.3, y1, -3.3, y2, SLATE, lw=2.0)
    arrow(ax, 3.0, y1, 3.0, y2, SLATE, lw=2.0)
arrow(ax, -1.9, 0.9, 1.55, 4.6, TEAL, lw=2.2)
ax.text(-0.2, 2.6, "гардиши\nэнтерогепатикӣ", ha="center", fontsize=8.8,
        color=TEAL, weight="bold")
ax.text(0, 0.28, "Ҳар рӯз: 250–300 мг билирубин (4 мг/кг)", ha="center",
        fontsize=9.8, color=INK, weight="bold")
ax.set_xlim(-5.3, 5.3); ax.set_ylim(0.05, 5.8)
ax.axis("off")
plt.savefig("img16/shakli_2_1.png", dpi=200, facecolor=BG,
            bbox_inches="tight")
plt.close()

# ===== 3.1: Фарқи се зардак =====
fig, ax = plt.subplots(figsize=(9.4, 6.4), dpi=200)
fig.patch.set_facecolor(BG); ax.set_facecolor(BG)
ax.text(0.0, 4.85, "Фарқи се намуди зардак", ha="center", fontsize=13.5,
        color=INK, weight="bold")
cols = [(-3.2, "Гемолитикӣ", ROSE, "#FDF2F8"),
        (0.0, "Паренхимавӣ", AMBER, "#FEF6E7"),
        (3.2, "Мешообӣ", BLUE, "#EEF4FB")]
for x, name, ec, fc in cols:
    box(ax, x, 4.1, 2.5, 0.7, name, fc, ec, fs=10)
rows = [
    ("Ғайримустоқим", ["зиёд", "зиёд", "меъёр"], 3.25),
    ("Мустоқим", ["меъёр", "зиёд", "зиёд"], 2.6),
    ("Ранги нӯҷа", ["торик", "меъёр", "сафед"], 1.95),
    ("Пешоб: билирубин", ["не", "ҳа", "ҳа"], 1.3),
    ("Уробилиноген", ["зиёд", "ҳа", "кам"], 0.65),
]
for label, vals, y in rows:
    ax.text(-4.85, y, label, ha="left", fontsize=9.4, color=INK,
            weight="bold")
    for (x, _, _, _), v in zip(cols, vals):
        c = TEAL if v in ("меъёр", "не") else ROSE
        ax.text(x, y, v, ha="center", fontsize=9.6, color=c, weight="bold")
    ax.plot([-5.0, 4.6], [y - 0.3, y - 0.3], color="#E2E8F0", lw=1.0)
ax.set_xlim(-5.1, 4.7); ax.set_ylim(0.35, 5.15)
ax.axis("off")
plt.savefig("img16/shakli_3_1.png", dpi=200, facecolor=BG,
            bbox_inches="tight")
plt.close()

# ===== 4.1: Ҳадҳои билирубин =====
fig, ax = plt.subplots(figsize=(9.2, 5.4), dpi=200)
fig.patch.set_facecolor(BG); ax.set_facecolor(BG)
labels = ["Умумӣ\n(меъёр)", "Мустоқим\n(меъёр)", "Зардак\n(ҳад)",
          "Навзод\n(физиологӣ)", "Хатари мағз"]
vals = [1.2, 0.3, 2.5, 5.5, 25]
colors = [TEAL, BLUE, AMBER, PURPLE, ROSE]
x = np.arange(len(labels))
b = ax.bar(x, vals, width=0.55, color=colors, alpha=0.88)
labs = ["1,2", "0,3", "2,5", "5,5", "25"]
for bi, v, lb in zip(b, vals, labs):
    ax.text(bi.get_x() + bi.get_width()/2, v + 0.5, lb, ha="center",
            fontsize=11, color=INK, weight="bold")
ax.set_xticks(x); ax.set_xticklabels(labels, fontsize=9.6, color=INK)
ax.set_ylim(0, 28)
ax.set_ylabel("мг/дл", fontsize=10, color=SLATE)
ax.spines[["top", "right"]].set_visible(False)
ax.text(0.5, 0.96, "Ҳадҳои меъёрии билирубин (мг/дл)", ha="center",
        va="top", fontsize=13.5, color=INK, weight="bold",
        transform=ax.transAxes)
plt.savefig("img16/shakli_4_1.png", dpi=200, facecolor=BG,
            bbox_inches="tight")
plt.close()

print("img16 ok: 5 PNG")
