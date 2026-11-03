# -*- coding: utf-8 -*-
# Расмҳои М12 «Занҷири нафас ва фосфорилатсияи оксидшавӣ» — matplotlib, Agg, dpi=200
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

plt.rcParams["font.family"] = "DejaVu Sans"
INK, SLATE = "#1F2937", "#64748B"
TEAL, BLUE, AMBER, ROSE, GREEN = "#0F766E", "#1D4ED8", "#B45309", "#BE185D", "#15803D"

def arrow(ax, x1, y1, x2, y2, c=SLATE, lw=1.8):
    ax.annotate("", xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle="-|>", color=c, lw=lw))

# ===== 1.1: Схемаи занҷири нафас (пардохтии мембрана) =====
fig, ax = plt.subplots(figsize=(11.0, 5.8), dpi=200)
fig.patch.set_facecolor("#F7FAF8"); ax.set_facecolor("#F7FAF8")
ax.text(0.0, 5.15, "Занҷири нафас дар мембранаи дохилии митохондрия",
        fontsize=13.5, ha="center", color=INK, weight="bold")
# мембрана
ax.add_patch(mpatches.Rectangle((-6.0, 1.15), 12.0, 1.5, fc="#FFF7ED",
             ec=SLATE, lw=1.4, hatch="///", alpha=0.85))
ax.text(-5.75, 1.9, "мембранаи дохилӣ", fontsize=8.5, color=SLATE, va="center", rotation=90)
ax.text(5.75, 1.9, "", fontsize=8.5, color=SLATE)
ax.text(0.0, 4.45, "фазои байнимембранӣ (протонҳои зиёд)", fontsize=9.5,
        ha="center", color=BLUE)
ax.text(0.0, 0.35, "митрикс (протонҳои кам)", fontsize=9.5, ha="center", color=TEAL)
def cx(x, t, s, ec, fc):
    ax.add_patch(mpatches.FancyBboxPatch((x-1.05, 1.45), 2.1, 0.95,
                 boxstyle="round,pad=0.03,rounding_size=0.08", fc=fc, ec=ec, lw=2.0))
    ax.text(x, 1.98, t, ha="center", fontsize=10, color=INK, weight="bold")
    ax.text(x, 1.66, s, ha="center", fontsize=7.8, color=SLATE)
cx(-4.2, "I", "NADH-убихинон\nредуктаза", TEAL, "#E6F2EF")
cx(-1.4, "II", "Сукцинат-\nдегидрогеназа", SLATE, "#F1F5F9")
cx(1.4, "III", "Убихинон-цитохром c\nредуктаза", AMBER, "#FEF6E7")
cx(4.2, "IV", "Цитохром c\nоксидаза", ROSE, "#FDF0F5")
# CoQ and cyt c
ax.add_patch(mpatches.FancyBboxPatch((-3.25, 0.62), 1.6, 0.55,
             boxstyle="round,pad=0.02,rounding_size=0.08", fc="#F0FDF4", ec=GREEN, lw=1.7))
ax.text(-2.45, 0.89, "CoQ", ha="center", fontsize=9, color=INK, weight="bold")
ax.add_patch(mpatches.FancyBboxPatch((2.6, 0.62), 1.7, 0.55,
             boxstyle="round,pad=0.02,rounding_size=0.08", fc="#F0FDF4", ec=GREEN, lw=1.7))
ax.text(3.45, 0.89, "цитохром c", ha="center", fontsize=8.6, color=INK, weight="bold")
# electron arrows inside
arrow(ax, -3.15, 1.92, -2.1, 1.05, GREEN)
arrow(ax, -0.35, 1.05, 0.42, 1.05, GREEN)
arrow(ax, 2.15, 1.05, 2.85, 1.05, GREEN)
arrow(ax, 4.2, 0.62, 4.2, 0.62)
arrow(ax, 4.28, 1.15, 4.28, 1.15)
# O2
ax.add_patch(mpatches.FancyBboxPatch((5.75, 0.6), 1.15, 0.6,
             boxstyle="round,pad=0.02,rounding_size=0.08", fc="#EEF4FB", ec=BLUE, lw=1.8))
ax.text(6.32, 0.9, "O2 → H2O", ha="center", fontsize=9, color=INK, weight="bold")
arrow(ax, 4.85, 1.6, 5.8, 0.95, BLUE)
# NADH / FADH2 inputs
ax.add_patch(mpatches.FancyBboxPatch((-5.35, 3.35), 2.3, 0.55,
             boxstyle="round,pad=0.02,rounding_size=0.08", fc="#EEF4FB", ec=BLUE, lw=1.7))
ax.text(-4.2, 3.62, "NADH", ha="center", fontsize=9.5, color=INK, weight="bold")
arrow(ax, -4.2, 3.32, -4.2, 2.45, BLUE)
ax.add_patch(mpatches.FancyBboxPatch((-2.6, 3.35), 2.4, 0.55,
             boxstyle="round,pad=0.02,rounding_size=0.08", fc="#FDF0F5", ec=ROSE, lw=1.7))
ax.text(-1.4, 3.62, "FADH2", ha="center", fontsize=9.5, color=INK, weight="bold")
arrow(ax, -1.4, 3.32, -1.4, 2.45, ROSE)
# proton pumps
for x, n in [(-4.2, "4H+"), (1.4, "4H+"), (4.2, "2H+")]:
    arrow(ax, x, 2.42, x, 3.7, AMBER, lw=2.2)
    ax.text(x + 0.28, 3.05, n, fontsize=9, color=AMBER, weight="bold")
ax.text(-1.4, 2.9, "0H+", fontsize=9, color=SLATE)
ax.text(0.0, -0.65, "Ҷамъ: 10 протон аз NADH  •  6 протон аз FADH2  •  шаш протон аз комплексҳои III ва IV",
        ha="center", fontsize=10, color=SLATE)
ax.set_xlim(-6.6, 7.3); ax.set_ylim(-1.0, 5.6)
ax.axis("off")
plt.savefig("img12/shakli_1_1.png", dpi=200, facecolor="#F7FAF8", bbox_inches="tight")
plt.close()

# ===== 1.2: АТФ-синтетаза =====
fig, ax = plt.subplots(figsize=(8.6, 6.6), dpi=200)
fig.patch.set_facecolor("#FBF8F4"); ax.set_facecolor("#FBF8F4")
ax.text(0.0, 4.7, "АТФ-синтетаза (F0F1-ATPase)", fontsize=13.5,
        ha="center", color=INK, weight="bold")
ax.text(0.0, 4.2, "фазои байнимембранӣ", fontsize=9.5, ha="center", color=BLUE)
ax.add_patch(mpatches.Rectangle((-3.6, 1.6), 7.2, 1.15, fc="#FFF7ED",
             ec=SLATE, lw=1.3, hatch="///", alpha=0.85))
ax.text(-3.45, 2.17, "мембрана", fontsize=8.3, color=SLATE, va="center", rotation=90)
ax.text(0.0, -0.05, "митрикс", fontsize=9.5, ha="center", color=TEAL)
# stator
ax.add_patch(mpatches.Rectangle((-1.15, 1.6), 0.4, 2.5, fc="#EEF4FB", ec=SLATE, lw=1.5))
ax.text(-3.15, 3.42, "статор (b)", fontsize=8.5, color=SLATE)
# F1 head
ax.add_patch(mpatches.Ellipse((0.45, 3.15), 3.1, 1.55, fc="#E6F2EF", ec=TEAL, lw=2.2))
ax.text(0.45, 3.15, "F1", ha="center", fontsize=13, color=INK, weight="bold")
ax.text(0.45, 2.72, "6 зержазира: α3β3", ha="center", fontsize=8.0, color=SLATE)
# rotor shaft
ax.add_patch(mpatches.Rectangle((0.32, 1.55), 0.26, 1.55, fc="#FEF6E7", ec=AMBER, lw=1.8))
ax.text(1.62, 1.82, "суменк (γ)", fontsize=8.5, color=SLATE)
# c-ring
ax.add_patch(mpatches.Ellipse((0.45, 2.17), 2.0, 0.85, fc="#FEF6E7", ec=AMBER, lw=2.2))
ax.text(0.45, 2.17, "F0 — ҳалқаи c", ha="center", fontsize=9.2, color=INK, weight="bold")
# proton flow
arrow(ax, -2.3, 3.9, -0.55, 2.35, BLUE, lw=2.4)
ax.text(-2.95, 4.12, "H+", fontsize=11, color=BLUE, weight="bold")
arrow(ax, 1.45, 2.35, 3.1, 3.9, BLUE, lw=2.4)
ax.text(3.0, 3.72, "4H+ → 1 ATP", fontsize=9.5, color=BLUE, weight="bold")
ax.text(0.45, 1.15, "гардиши ротор: 3 ATP дар ҳар гардиши пурра",
        ha="center", fontsize=10, color=INK, weight="bold")
ax.text(0.45, 0.62, "Механизми гардиши Бойер–Уолкер (Нобел 1997)",
        ha="center", fontsize=9.3, color=SLATE)
ax.set_xlim(-4.3, 5.2); ax.set_ylim(0.15, 5.1)
ax.axis("off")
plt.savefig("img12/shakli_1_2.png", dpi=200, facecolor="#FBF8F4", bbox_inches="tight")
plt.close()

# ===== 2.1: Ҷудокунандагон ва гармӣ =====
fig, ax = plt.subplots(figsize=(9.6, 5.6), dpi=200)
fig.patch.set_facecolor("#FBF8F4"); ax.set_facecolor("#FBF8F4")
ax.text(0.0, 4.55, "Ҷудокунанда: ҷои ATP гармӣ мегирад", fontsize=13.5,
        ha="center", color=INK, weight="bold")
ax.text(0.0, 4.05, "фазои байнимембранӣ", fontsize=9.3, ha="center", color=BLUE)
ax.add_patch(mpatches.Rectangle((-4.6, 1.5), 9.2, 1.2, fc="#FFF7ED",
             ec=SLATE, lw=1.3, hatch="///", alpha=0.85))
ax.text(-4.45, 2.1, "мембрана", fontsize=8.3, color=SLATE, va="center", rotation=90)
ax.text(0.0, 0.15, "митрикс", fontsize=9.3, ha="center", color=TEAL)
# ATP synthase blocked
ax.add_patch(mpatches.Ellipse((2.6, 2.55), 1.9, 1.1, fc="#F1F5F9", ec=SLATE, lw=2.0))
ax.text(2.6, 2.55, "АТФ-синтетаза", ha="center", fontsize=8.4, color=SLATE, weight="bold")
ax.text(2.6, 2.2, "кор намекунад", ha="center", fontsize=7.6, color=ROSE)
# UCP1 channel
ax.add_patch(mpatches.FancyBboxPatch((-1.15, 1.75), 2.3, 0.7,
             boxstyle="round,pad=0.02,rounding_size=0.08", fc="#FDF0F5", ec=ROSE, lw=2.2))
ax.text(0.0, 2.1, "Термогенин (UCP1)", ha="center", fontsize=9.0, color=INK, weight="bold")
# protons
arrow(ax, -3.3, 3.6, -0.7, 2.15, ROSE, lw=2.6)
ax.text(-3.05, 3.5, "H+", fontsize=12, color=ROSE, weight="bold")
arrow(ax, 0.75, 2.15, 3.3, 3.6, ROSE, lw=2.6)
ax.text(2.85, 3.42, "гармӣ (43°C)", fontsize=9.6, color=ROSE, weight="bold")
ax.text(-4.45, 0.75, "Энергияи градиент ба гармӣ табдил мешавад", fontsize=10, color=SLATE)
ax.text(-4.45, 0.25, "2,4-динитрофенол ҳамон механизми хатардор дорад", fontsize=10, color=SLATE)
ax.set_xlim(-5.3, 5.3); ax.set_ylim(-0.35, 5.0)
ax.axis("off")
plt.savefig("img12/shakli_2_1.png", dpi=200, facecolor="#FBF8F4", bbox_inches="tight")
plt.close()

# ===== 3.1: Тақсими ҳиссаи ATP (донут) =====
fig, ax = plt.subplots(figsize=(8.8, 5.4), dpi=200)
fig.patch.set_facecolor("#F7FAF8"); ax.set_facecolor("#F7FAF8")
labels = ["Оксидшавии NADH — 25 ATP", "Оксидшавии FADH2 — 3 ATP", "Фосфорилатсияи субстратӣ — 4 ATP"]
vals = [25, 3, 4]
cols = [TEAL, AMBER, BLUE]
wedges, _, autot = ax.pie(vals, colors=cols, startangle=90,
        wedgeprops=dict(width=0.42, edgecolor="white"), autopct="%1.0f%%",
        pctdistance=0.79, textprops=dict(color="white", fontsize=11, weight="bold"))
ax.legend(wedges, labels, loc="center left", bbox_to_anchor=(0.97, 0.5),
          fontsize=9.5, frameon=False)
ax.text(0, 0, "32 ATP\nаз 1 глюкоза", ha="center", va="center",
        fontsize=12.5, color=INK, weight="bold")
ax.set_title("Ҳиссаи манбаъҳои ATP-и аэробӣ", fontsize=13.5, color=INK,
             weight="bold", pad=14)
plt.savefig("img12/shakli_3_1.png", dpi=200, facecolor="#F7FAF8",
            bbox_inches="tight")
plt.close()
print("img12 ok: 4 PNG")
