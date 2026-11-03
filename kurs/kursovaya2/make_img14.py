# -*- coding: utf-8 -*-
"""Расмҳои кори курсӣ М14 — Мубодилаи холестерин ва липопротеинҳо (5 PNG)."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import os

INK = "#1F2A44"; SLATE = "#64748B"; BLUE = "#1D4ED8"; TEAL = "#0F766E"
AMBER = "#B45309"; ROSE = "#BE185D"; BG = "#FBF8F4"
plt.rcParams["font.family"] = "DejaVu Sans"
os.makedirs("img14", exist_ok=True)

def arrow(ax, x1, y1, x2, y2, color, lw=2.2, style="-|>"):
    ax.annotate("", xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle=style, color=color, lw=lw,
                                mutation_scale=18))

def box(ax, x, y, w, h, txt, fc, ec, fs=9.2):
    ax.add_patch(mpatches.FancyBboxPatch((x - w/2, y - h/2), w, h,
                 boxstyle="round,pad=0.09", fc=fc, ec=ec, lw=2.0))
    ax.text(x, y, txt, ha="center", va="center", fontsize=fs, color=INK)

# ===== 1.1: Биосинтези холестерин (флоучарт, морпеч) =====
fig, ax = plt.subplots(figsize=(9.4, 7.8), dpi=200)
fig.patch.set_facecolor(BG); ax.set_facecolor(BG)
ax.text(0.0, 5.05, "Биосинтези холестерин аз ацетил-КоА", ha="center",
        fontsize=13.5, color=INK, weight="bold")
row1 = [("Ацетил-КоА", -3.6, "#EEF4FB", BLUE),
        ("Ацетоацетил-КоА", -1.2, "#EEF4FB", BLUE),
        ("HMG-CoA", 1.2, "#EEF4FB", BLUE)]
for txt, x, fc, ec in row1:
    box(ax, x, 4.5, 2.3, 0.78, txt, fc, ec, fs=9.4)
for xa, xb in [(-2.40, -2.35), (0.0, 0.05)]:
    arrow(ax, xa, 4.5, xb, 4.5, SLATE, lw=2.0)
arrow(ax, 1.2, 4.11, 1.2, 3.19, SLATE, lw=2.2)
ax.text(2.55, 3.62, "HMG-CoA редуктаза\n(қадами калидӣ)", ha="center",
        va="center", fontsize=9.4, color=AMBER, weight="bold")
box(ax, -0.75, 3.62, 2.05, 0.62, "статинҳо (манъ)", "#FEF2F2", ROSE, fs=9.0)
arrow(ax, 0.32, 3.62, 1.15, 3.62, ROSE, lw=2.0, style="-|>")
box(ax, 1.2, 2.8, 2.3, 0.78, "Мевалонат", "#FEF6E7", AMBER, fs=9.4)
arrow(ax, 1.2, 2.41, 1.2, 2.09, SLATE, lw=2.2)
row2 = [("Изопентенил-PP", 3.6), ("Фарнезил-PP", 1.2),
        ("Скуален", -1.2), ("Ланостерол", -3.6)]
for txt, x in row2:
    box(ax, x, 1.7, 2.3, 0.78, txt, "#E6F2EF", TEAL, fs=9.4)
for xa, xb in [(2.40, 2.35), (0.0, -0.05), (-2.40, -2.45)]:
    arrow(ax, xa, 1.7, xb, 1.7, SLATE, lw=2.0)
arrow(ax, -3.6, 1.31, -1.85, 0.55, SLATE, lw=2.2)
ax.text(-3.35, 1.02, "19 қадами ниҳоӣ", fontsize=9.0, color=SLATE)
box(ax, 0.0, 0.15, 3.3, 0.85, "ХОЛЕСТЕРИН (27 C)", "#FDF2F8", ROSE, fs=10.5)
ax.text(0.0, -0.52, "Нуздаҳ реаксияи ниҳоӣ: ланостерол → холестерин",
        ha="center", fontsize=9.6, color=SLATE)
ax.text(0.0, -0.92, "Хароҷот: 18 АТФ ва 12 NADPH барои як молекула",
        ha="center", fontsize=9.6, color=SLATE)
ax.set_xlim(-5.3, 5.3); ax.set_ylim(-1.15, 5.25)
ax.set_aspect("equal"); ax.axis("off")
plt.savefig("img14/shakli_1_1.png", dpi=200, facecolor=BG, bbox_inches="tight")
plt.close()

# ===== 2.1: Сохтори липопротеин =====
fig, ax = plt.subplots(figsize=(8.8, 7.0), dpi=200)
fig.patch.set_facecolor(BG); ax.set_facecolor(BG)
ax.text(0.0, 4.72, "Сохтори умумии зарраи липопротеин", ha="center",
        fontsize=13.5, color=INK, weight="bold")
ax.add_patch(mpatches.Circle((0, 1.9), 2.3, fc="#FEF6E7", ec=AMBER, lw=2.4))
ax.add_patch(mpatches.Circle((0, 1.9), 1.55, fc="#FDF2F8", ec=ROSE, lw=2.2))
ax.text(0, 2.14, "МАРКАЗ (ғализӣ)", ha="center", fontsize=10.5, color=ROSE,
        weight="bold")
ax.text(0, 1.60, "триглицеридҳо +\nэстерҳои холестерин", ha="center",
        fontsize=9.2, color=INK)
for ang in (45, 135, 225, 315):
    a = np.deg2rad(ang)
    ax.add_patch(mpatches.Circle((2.3*np.cos(a), 1.9+2.3*np.sin(a)), 0.17,
                 fc="#64748B", ec=INK, lw=1.2))
ax.text(0, 4.18, "аполипопротеинҳо", ha="center", fontsize=9.4, color=SLATE,
        weight="bold")
arrow(ax, -0.55, 4.02, -1.45, 3.66, SLATE, lw=1.8)
arrow(ax, 0.55, 4.02, 1.45, 3.66, SLATE, lw=1.8)
ax.text(4.0, 2.55, "фосфолипидҳо", fontsize=9.4, color=BLUE, weight="bold")
arrow(ax, 3.7, 2.45, 2.38, 2.05, BLUE, lw=1.8)
ax.text(-4.75, 0.55, "холестеринаи\nозод", fontsize=9.4, color=TEAL,
        weight="bold")
arrow(ax, -3.35, 0.72, -2.32, 1.52, TEAL, lw=1.8)
ax.text(0, -0.85, "Қабат берунӣ обдӯст аст — зарра дар хун устувор мемонад",
        ha="center", fontsize=10, color=INK, weight="bold")
ax.set_xlim(-5.0, 5.0); ax.set_ylim(-1.15, 4.95)
ax.set_aspect("equal"); ax.axis("off")
plt.savefig("img14/shakli_2_1.png", dpi=200, facecolor=BG, bbox_inches="tight")
plt.close()

# ===== 2.2: Роҳҳои экзоген ва эндоген =====
fig, ax = plt.subplots(figsize=(9.4, 6.8), dpi=200)
fig.patch.set_facecolor(BG); ax.set_facecolor(BG)
ax.text(0.0, 5.65, "Роҳҳои нақлиёти чарб: экзоген ва эндоген", ha="center",
        fontsize=13.5, color=INK, weight="bold")
ax.text(-3.3, 5.15, "РОҲИ ЭКЗОГЕН", ha="center", fontsize=10, color=ROSE,
        weight="bold")
ax.text(2.7, 5.15, "РОҲИ ЭНДОГЕН", ha="center", fontsize=10, color=BLUE,
        weight="bold")
left = ["Чарби хӯрок (рӯда)", "Хиломикронҳо", "Бофтаҳо (LPL)",
        "Боқимонда → ҷигар"]
right = ["Чарби дохилӣ (ҷигар)", "VLDL", "IDL → LDL", "Рецептори LDL"]
ys = [4.3, 3.2, 2.1, 1.0]
for txt, y in zip(left, ys):
    box(ax, -3.3, y, 2.6, 0.75, txt, "#FDF2F8", ROSE, fs=9.4)
for txt, y in zip(right, ys):
    box(ax, 2.7, y, 2.6, 0.75, txt, "#EEF4FB", BLUE, fs=9.4)
for y1, y2 in [(3.92, 3.58), (2.82, 2.48), (1.72, 1.38)]:
    arrow(ax, -3.3, y1, -3.3, y2, ROSE, lw=2.2)
    arrow(ax, 2.7, y1, 2.7, y2, BLUE, lw=2.2)
ax.text(0, 3.75, "ҳар ду — бо LPL", ha="center", fontsize=9.4, color=SLATE)
ax.text(0, 2.65, "триглицеридҳо мебуранд", ha="center", fontsize=9.4,
        color=SLATE)
ax.text(0, 1.55, "LDL — шакли ниҳоӣ", ha="center", fontsize=9.4,
        color=SLATE)
ax.text(-3.3, 0.42, "пас аз хӯрок", ha="center", fontsize=9.2, color=ROSE)
ax.text(2.7, 0.42, "дар вазъи гуруснагӣ", ha="center", fontsize=9.2,
        color=BLUE)
ax.set_xlim(-5.2, 5.2); ax.set_ylim(0.1, 5.9)
ax.axis("off")
plt.savefig("img14/shakli_2_2.png", dpi=200, facecolor=BG, bbox_inches="tight")
plt.close()

# ===== 3.1: Нақлиёти баръакси холестерин (HDL) =====
fig, ax = plt.subplots(figsize=(9.2, 6.4), dpi=200)
fig.patch.set_facecolor(BG); ax.set_facecolor(BG)
ax.text(0.0, 4.85, "Нақлиёти баръакси холестерин тавассути HDL",
        ha="center", fontsize=13, color=INK, weight="bold")
ax.add_patch(mpatches.Rectangle((-4.1, 1.5), 8.2, 1.7, fc="#FFF7ED",
             ec=SLATE, lw=1.3, hatch="///", alpha=0.75))
ax.text(-3.2, 3.42, "бофтаи берунӣ", fontsize=9.5, color=BLUE, ha="center")
ax.text(-4.0, 1.15, "хун", fontsize=9.5, color=TEAL, ha="center")
box(ax, -2.6, 2.35, 2.1, 0.7, "ҳуҷайра", "#EEF4FB", BLUE, fs=9.4)
box(ax, 2.9, 2.35, 1.9, 0.7, "ҷигар", "#FEF6E7", AMBER, fs=9.4)
box(ax, 0.2, 3.6, 2.5, 0.7, "HDL (апоA-I)", "#E6F2EF", TEAL, fs=9.6)
arrow(ax, -2.0, 2.72, -0.7, 3.25, BLUE, lw=2.4)
ax.text(-0.95, 2.80, "ABCA1 (хориҷи холестерин)", fontsize=8.8, color=BLUE,
        weight="bold", bbox=dict(fc=BG, ec="none", pad=2.0))
arrow(ax, 1.45, 3.6, 2.9, 2.72, TEAL, lw=2.4)
ax.text(2.35, 3.32, "SR-B1", fontsize=9.2, color=TEAL, weight="bold")
ax.text(0, 0.72, "LCAT: холестерин → эстер (дар марказ ҷой мегирад)",
        ha="center", fontsize=9.4, color=SLATE)
ax.text(0.0, 0.22, "Натиҷа: холестеринаи зиёди бофтаҳо ба ҷигар бармегардад",
        ha="center", fontsize=10.2, color=INK, weight="bold")
ax.set_xlim(-4.5, 4.5); ax.set_ylim(0.0, 4.65)
ax.axis("off")
plt.savefig("img14/shakli_3_1.png", dpi=200, facecolor=BG, bbox_inches="tight")
plt.close()

# ===== 4.1: Липид-профил — ҳадҳои меъёрӣ =====
fig, ax = plt.subplots(figsize=(9.2, 5.6), dpi=200)
fig.patch.set_facecolor(BG); ax.set_facecolor(BG)
ax.text(0.5, 0.93, "Ҳадҳои меъёрии липид-профил (мг/дл)", ha="center",
        fontsize=13.5, color=INK, weight="bold", transform=ax.transAxes)
labels = ["Умумӣ\n(<200)", "LDL\n(<100)", "HDL\n(>40; >50 занон)",
          "Триглицерид\n(<150)"]
lo = [200, 100, 40, 150]
colors = [TEAL, ROSE, BLUE, AMBER]
x = np.arange(len(labels))
b = ax.bar(x, lo, width=0.52, color=colors, alpha=0.88)
for bi, v in zip(b, lo):
    ax.text(bi.get_x() + bi.get_width()/2, v + 4, str(v), ha="center",
            fontsize=11.5, color=INK, weight="bold")
ax.set_xticks(x); ax.set_xticklabels(labels, fontsize=9.8, color=INK)
ax.set_ylim(0, 240)
ax.set_ylabel("мг/дл", fontsize=10, color=SLATE)
ax.spines[["top", "right"]].set_visible(False)
ax.text(0.5, -0.16, "Ҳадҳои меъёрӣ баъди 9–12 соат гуруснагӣ чен мешаванд",
        ha="center", fontsize=9.5, color=SLATE, transform=ax.transAxes)
plt.savefig("img14/shakli_4_1.png", dpi=200, facecolor=BG, bbox_inches="tight")
plt.close()

print("img14 ok: 5 PNG")
