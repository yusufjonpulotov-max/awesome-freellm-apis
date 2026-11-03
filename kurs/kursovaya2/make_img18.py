# -*- coding: utf-8 -*-
"""Расмҳои кори курсӣ М18 — Биохимияи гурда (5 PNG)."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import os

INK = "#1F2A44"; SLATE = "#64748B"; BLUE = "#1D4ED8"; TEAL = "#0F766E"
AMBER = "#B45309"; ROSE = "#BE185D"; PURPLE = "#6D28D9"; BG = "#FBF8F4"
plt.rcParams["font.family"] = "DejaVu Sans"
os.makedirs("img18", exist_ok=True)

def arrow(ax, x1, y1, x2, y2, color, lw=2.2, rad=0.0):
    ax.annotate("", xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle="-|>", color=color, lw=lw,
                                mutation_scale=18,
                                connectionstyle=f"arc3,rad={rad}"))

def box(ax, x, y, w, h, txt, fc, ec, fs=9.2):
    ax.add_patch(mpatches.FancyBboxPatch((x - w/2, y - h/2), w, h,
                 boxstyle="round,pad=0.09", fc=fc, ec=ec, lw=2.0))
    ax.text(x, y, txt, ha="center", va="center", fontsize=fs, color=INK)

# ===== 1.1: Нефрон =====
fig, ax = plt.subplots(figsize=(9.2, 7.2), dpi=200)
fig.patch.set_facecolor(BG); ax.set_facecolor(BG)
ax.text(0.0, 6.3, "Нефрон: қисмҳо ва вазифаҳо", ha="center", fontsize=13.5,
        color=INK, weight="bold")
box(ax, -3.3, 5.4, 2.9, 0.95, "ГЛОМЕРУЛ\n+ капсулаи Боуман\n(суперфилтратсия)",
    "#FDF2F8", ROSE, fs=8.8)
box(ax, 0.0, 5.4, 2.7, 0.8, "Лӯлаи проксималӣ\n(реабсорбсияи калон)",
    "#EEF4FB", BLUE, fs=8.8)
arrow(ax, -1.85, 5.4, -1.36, 5.4, SLATE, lw=2.2)
box(ax, -3.3, 3.9, 2.7, 0.85, "Ҳалқаи Ҳенле\nфурудо (об)", "#FEF6E7",
    AMBER, fs=8.8)
box(ax, 0.0, 3.9, 2.7, 0.85, "Ҳалқаи Ҳенле\nболо (NaCl)", "#FEF6E7",
    AMBER, fs=8.8)
arrow(ax, 0.0, 5.0, -0.02, 4.35, SLATE, lw=2.2)
arrow(ax, -1.93, 3.9, -1.38, 3.9, SLATE, lw=2.2)
box(ax, -3.3, 2.5, 2.7, 0.85, "Лӯлаи дисталӣ\n(танзими ионҳо)", "#E6F2EF",
    TEAL, fs=8.8)
arrow(ax, 0.0, 3.45, 0.02, 2.95, SLATE, lw=2.2)
arrow(ax, 0.0, 2.5, -1.9, 2.5, SLATE, lw=2.0)
box(ax, -3.3, 1.2, 3.4, 0.9, "ЛӮЛАИ ҶАМЪОВАР\n(об ва pH; аквапорин-2)",
    "#F5F3FF", PURPLE, fs=9.0)
arrow(ax, -3.3, 2.05, -3.3, 1.68, SLATE, lw=2.2)
box(ax, 2.9, 1.2, 2.3, 0.9, "Пешоби ниҳоӣ\n1–2 л/рӯз", "#FDF2F8", ROSE,
    fs=9.4)
arrow(ax, -1.55, 1.2, 1.7, 1.2, ROSE, lw=2.2)
ax.text(0.0, 0.15, "180 л суперфилтрат → 1–2 л пешоб (реабсорбсия >99%)",
        ha="center", fontsize=9.8, color=INK, weight="bold")
ax.set_xlim(-5.4, 5.4); ax.set_ylim(-0.15, 6.7)
ax.axis("off")
plt.savefig("img18/shakli_1_1.png", dpi=200, facecolor=BG,
            bbox_inches="tight")
plt.close()

# ===== 1.2: РААС =====
fig, ax = plt.subplots(figsize=(9.4, 6.2), dpi=200)
fig.patch.set_facecolor(BG); ax.set_facecolor(BG)
ax.text(0.0, 4.95, "РААС: аз ренин то алдостерон", ha="center",
        fontsize=13.5, color=INK, weight="bold")
box(ax, -3.5, 4.2, 2.6, 0.8, "Гурда: дастгоҳи\nҳамсоя → ренин",
    "#EEF4FB", BLUE, fs=8.8)
box(ax, -0.6, 4.2, 2.2, 0.8, "Ангиотензиноген →\nАнгиотензин I",
    "#E6F2EF", TEAL, fs=8.6)
box(ax, 2.4, 4.2, 1.9, 0.8, "АСЕ (шиш)\n→ AT II", "#FEF6E7", AMBER,
    fs=8.8)
arrow(ax, -2.2, 4.2, -1.72, 4.2, SLATE, lw=2.2)
arrow(ax, 0.52, 4.2, 1.43, 4.2, SLATE, lw=2.2)
box(ax, 0.0, 2.6, 3.4, 0.9, "AT II: танги рагҳо\n+ фишор меафзояд",
    "#FDF2F8", ROSE, fs=9.2)
arrow(ax, 2.4, 3.8, 1.0, 3.1, SLATE, lw=2.2)
box(ax, -3.5, 2.6, 2.8, 0.9, "Алдостерон\n(ғадуди уҳрубар)", "#FDF2F8",
    ROSE, fs=9.2)
arrow(ax, -1.7, 2.6, -2.1, 2.6, SLATE, lw=2.2)
box(ax, -3.5, 1.0, 3.0, 0.9, "Лӯлаи дисталӣ:\nNa↑ бармегардад, K↓ хориҷ",
    "#E6F2EF", TEAL, fs=8.6)
arrow(ax, -3.5, 2.13, -3.5, 1.48, SLATE, lw=2.2)
box(ax, 0.6, 1.0, 3.0, 0.9, "Об ҳамроҳи Na\n→ ҳаҷм ва фишор ↑",
    "#FEF6E7", AMBER, fs=8.8)
arrow(ax, -1.95, 1.0, -1.13, 1.0, SLATE, lw=2.2)
ax.text(0.0, -0.05, "Доруҳои АСЕ-ингибитор: AT II кам → фишор мекӯҳонад",
        ha="center", fontsize=9.8, color=INK, weight="bold")
ax.set_xlim(-5.4, 5.4); ax.set_ylim(-0.35, 5.35)
ax.axis("off")
plt.savefig("img18/shakli_1_2.png", dpi=200, facecolor=BG,
            bbox_inches="tight")
plt.close()

# ===== 2.1: Реабсорбсия 180→1.5 =====
fig, ax = plt.subplots(figsize=(9.4, 5.8), dpi=200)
fig.patch.set_facecolor(BG); ax.set_facecolor(BG)
ax.text(0.0, 4.55, "Аз 180 л суперфилтрат то 1,5 л пешоб", ha="center",
        fontsize=13.5, color=INK, weight="bold")
labels = ["Суперфилтрат", "Проксималӣ", "Ҳалқаи Ҳенле", "Дисталӣ",
          "Ҷамъовар", "Пешоб"]
vals = [180, 54, 18, 6, 3, 1.5]
colors = [ROSE, BLUE, AMBER, TEAL, PURPLE, SLATE]
x = np.arange(len(labels))
b = ax.bar(x, vals, width=0.55, color=colors, alpha=0.88)
labs = ["180", "54", "18", "6", "3", "1,5"]
for bi, v, lb in zip(b, vals, labs):
    ax.text(bi.get_x() + bi.get_width()/2, v + 3.5, lb, ha="center",
            fontsize=11, color=INK, weight="bold")
ax.set_xticks(x); ax.set_xticklabels(labels, fontsize=9.4, color=INK)
ax.set_ylim(0, 200)
ax.set_ylabel("л дар рӯз", fontsize=10, color=SLATE)
ax.spines[["top", "right"]].set_visible(False)
ax.text(0.5, 0.96, "Реабсорбсияи об дар қисмҳои нефрон", ha="center",
        va="top", fontsize=13.5, color=INK, weight="bold",
        transform=ax.transAxes)
plt.savefig("img18/shakli_2_1.png", dpi=200, facecolor=BG,
            bbox_inches="tight")
plt.close()

# ===== 3.1: Намудҳои санг =====
fig, ax = plt.subplots(figsize=(8.6, 6.4), dpi=200)
fig.patch.set_facecolor(BG); ax.set_facecolor(BG)
ax.text(0.0, 3.4, "Намудҳои сангҳои гурда (%)", ha="center", fontsize=13.5,
        color=INK, weight="bold")
sizes = [80, 9, 8, 3]
labels2 = ["Оксалати\nкалсий 80%", "Урат 9%", "Струвит 8%",
           "Цистин 3%"]
colors2 = [BLUE, AMBER, TEAL, ROSE]
wedges, _ = ax.pie(sizes, colors=colors2, startangle=90,
                   wedgeprops=dict(width=0.42, edgecolor=BG, linewidth=2))
ax.text(0, 0, "Сангҳои\nгурда", ha="center", va="center", fontsize=11,
        color=INK, weight="bold")
for w_, lb, c in zip(wedges, labels2, colors2):
    ang = (w_.theta2 + w_.theta1) / 2
    xx = 1.5 * np.cos(np.deg2rad(ang))
    yy = 1.5 * np.sin(np.deg2rad(ang))
    ha = "left" if xx > 0.15 else ("right" if xx < -0.15 else "center")
    ax.text(xx, yy, lb, ha=ha, va="center", fontsize=9.6, color=c,
            weight="bold",
            bbox=dict(boxstyle="round,pad=0.25", fc="white", ec="none",
                      alpha=0.9))
ax.text(0, -1.75, "pH: оксалат — 5,0–6,5  |  урат — кислата  |  фосфат — ишқор",
        ha="center", fontsize=9.6, color=SLATE)
ax.set_xlim(-1.9, 1.9); ax.set_ylim(-1.95, 3.7)
ax.set_aspect("equal"); ax.axis("off")
plt.savefig("img18/shakli_3_1.png", dpi=200, facecolor=BG,
            bbox_inches="tight")
plt.close()

# ===== 4.1: Марҳилаҳои CKD =====
fig, ax = plt.subplots(figsize=(9.2, 5.6), dpi=200)
fig.patch.set_facecolor(BG); ax.set_facecolor(BG)
labels3 = ["G1", "G2", "G3a", "G3b", "G4", "G5"]
vals3 = [105, 75, 52, 37, 22, 10]
colors3 = [TEAL, BLUE, AMBER, AMBER, ROSE, PURPLE]
x = np.arange(len(labels3))
b = ax.bar(x, vals3, width=0.55, color=colors3, alpha=0.88)
labs3 = ["≥90", "60–89", "45–59", "30–44", "15–29", "<15"]
for bi, v, lb in zip(b, vals3, labs3):
    ax.text(bi.get_x() + bi.get_width()/2, v + 2, lb, ha="center",
            fontsize=10.5, color=INK, weight="bold")
ax.set_xticks(x); ax.set_xticklabels(labels3, fontsize=10, color=INK)
ax.set_ylim(0, 125)
ax.set_ylabel("GFR, мл/мин/1.73 м²", fontsize=10, color=SLATE)
ax.spines[["top", "right"]].set_visible(False)
ax.text(0.5, 0.96, "Марҳилаҳои бемории муҷтами гурда (G1–G5)", ha="center",
        va="top", fontsize=13.5, color=INK, weight="bold",
        transform=ax.transAxes)
plt.savefig("img18/shakli_4_1.png", dpi=200, facecolor=BG,
            bbox_inches="tight")
plt.close()

print("img18 ok: 5 PNG")
