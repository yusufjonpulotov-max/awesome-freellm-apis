# -*- coding: utf-8 -*-
"""Расмҳои кори курсӣ М13 — Мубодилаи об ва минералҳо (5 PNG)."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import os

INK = "#1F2A44"; SLATE = "#64748B"; BLUE = "#1D4ED8"; TEAL = "#0F766E"
AMBER = "#B45309"; ROSE = "#BE185D"; BG = "#FBF8F4"
plt.rcParams["font.family"] = "DejaVu Sans"
os.makedirs("img13", exist_ok=True)

def arrow(ax, x1, y1, x2, y2, color, lw=2.2):
    ax.annotate("", xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle="-|>", color=color, lw=lw,
                                mutation_scale=18))

# ===== 1.1: Тақсими оби организм (қоидаи 60–40–20) =====
fig, ax = plt.subplots(figsize=(9.2, 5.4), dpi=200)
fig.patch.set_facecolor(BG); ax.set_facecolor(BG)
ax.text(0.5, 0.93, "Тақсими оби организм: қоидаи 60–40–20", ha="center",
        fontsize=13.5, color=INK, weight="bold", transform=ax.transAxes)
bars = [
    ("Оби умумӣ — 60% (42 л)", 60, "#0F766E"),
    ("Оби байнихуҷайравӣ — 40% (28 л), 2/3 аз умумӣ", 40, "#1D4ED8"),
    ("Оби байниҳуҷайравӣ — 20% (14 л), 1/3 аз умумӣ", 20, "#B45309"),
    ("Моеъи интерстициал — 15% (10,5 л), 3/4 аз байниҳуҷайравӣ", 15, "#BE185D"),
    ("Плазмаи хун — 5% (3,5 л), 1/4 аз байниҳуҷайравӣ", 5, "#6D28D9"),
]
y = 3.7
for name, val, color in bars:
    ax.barh(y, val, height=0.52, color=color, alpha=0.88)
    ax.text(62.5, y, name, va="center", ha="left", fontsize=9.6, color=INK,
            weight="bold")
    y -= 1.0
ax.set_xlim(0, 60); ax.set_ylim(-1.3, 5.0)
ax.axis("off")
ax.text(0.5, 0.035, "Ҳиссаи об дар вазни бадани марди 70-килограммӣ (фоиз ва литр)",
        ha="center", fontsize=9.5, color=SLATE, transform=ax.transAxes)
plt.savefig("img13/shakli_1_1.png", dpi=200, facecolor=BG, bbox_inches="tight")
plt.close()

# ===== 2.1: Ҷойгиршавии ионҳо ECF/ICF =====
fig, ax = plt.subplots(figsize=(9.2, 5.6), dpi=200)
fig.patch.set_facecolor(BG); ax.set_facecolor(BG)
ax.text(0.5, 0.94, "Ҷойгиршавии ионҳо: байниҳуҷайравӣ ва байнихуҷайравӣ",
        ha="center", fontsize=13.5, color=INK, weight="bold", transform=ax.transAxes)
ions = ["Na+", "K+", "Cl−", "HCO3−"]
ecf = [142, 4.2, 106, 24]
icf = [14, 150, 4, 10]
x = np.arange(len(ions)); w = 0.36
b1 = ax.bar(x - w/2, ecf, w, color=BLUE, alpha=0.9, label="Плазма (ECF)")
b2 = ax.bar(x + w/2, icf, w, color=AMBER, alpha=0.9, label="Дохили ҳуҷайра (ICF)")
for b in b1:
    ax.text(b.get_x() + b.get_width()/2, b.get_height() + 3,
            f"{b.get_height():g}", ha="center", fontsize=9.5, color=BLUE,
            weight="bold")
for b in b2:
    ax.text(b.get_x() + b.get_width()/2, b.get_height() + 3,
            f"{b.get_height():g}", ha="center", fontsize=9.5, color=AMBER,
            weight="bold")
ax.set_xticks(x); ax.set_xticklabels(ions, fontsize=11.5, color=INK)
ax.set_ylabel("ммол/л", fontsize=10, color=SLATE)
ax.set_ylim(0, 200)
ax.spines[["top", "right"]].set_visible(False)
ax.legend(frameon=False, fontsize=10, loc="upper right", bbox_to_anchor=(1.0, 0.88))
ax.text(0.5, -0.13, "Фарқи калони Na+ ва K+ бо помпаи натрий-калий нигоҳ дошта мешавад",
        ha="center", fontsize=9.5, color=SLATE, transform=ax.transAxes)
plt.savefig("img13/shakli_2_1.png", dpi=200, facecolor=BG, bbox_inches="tight")
plt.close()

# ===== 3.1: Вазопрессин ва AQP2 =====
fig, ax = plt.subplots(figsize=(8.8, 6.8), dpi=200)
fig.patch.set_facecolor(BG); ax.set_facecolor(BG)
ax.text(0.0, 4.72, "Вазопрессин ва аквапорин-2 дар лояи ҷамъоварии гурда",
        ha="center", fontsize=13, color=INK, weight="bold")
# membrane band
ax.add_patch(mpatches.Rectangle((-4.0, 2.05), 8.0, 1.0, fc="#FFF7ED",
             ec=SLATE, lw=1.3, hatch="///", alpha=0.85))
ax.text(-3.9, 2.55, "мембрана", fontsize=8.5, color=SLATE, va="center",
        rotation=90)
ax.text(0.9, 4.45, "пешоби таркибӣ (лумен)", ha="center", fontsize=9.5, color=BLUE)
ax.text(0.0, 1.32, "хун (базолатералӣ)", ha="center", fontsize=9.5, color=TEAL)
# AQP channels in membrane
for cx, lab in [(-2.2, "AQP2"), (0.0, "AQP2"), (2.2, "AQP2")]:
    ax.add_patch(mpatches.Ellipse((cx, 2.55), 0.85, 0.62, fc="#E6F2EF",
                 ec=TEAL, lw=2.0))
    ax.text(cx, 2.55, lab, ha="center", va="center", fontsize=7.6, color=INK,
            weight="bold")
# ADH arrow from blood to receptor
arrow(ax, -3.3, 1.55, -3.3, 2.28, TEAL, lw=2.4)
ax.text(-4.0, 1.7, "вазопрессин", fontsize=9.5, color=TEAL, weight="bold")
ax.add_patch(mpatches.Ellipse((-3.3, 2.42), 0.7, 0.5, fc="#FDF2F8",
             ec=ROSE, lw=1.8))
ax.text(-3.3, 2.42, "V2", ha="center", va="center", fontsize=8.2, color=INK,
        weight="bold")
# cAMP cascade arrow inside cell
arrow(ax, -3.0, 2.9, -2.5, 3.2, AMBER, lw=2.0)
ax.text(-4.05, 3.62, "cAMP → PKA", fontsize=9, color=AMBER, weight="bold")
# vesicle fusion
ax.add_patch(mpatches.Ellipse((-1.3, 3.32), 1.5, 0.62, fc="#E6F2EF", ec=TEAL,
             lw=1.8, linestyle="--"))
ax.text(-1.3, 3.32, "везикулаи AQP2", ha="center", va="center", fontsize=7.8,
        color=SLATE)
arrow(ax, -0.95, 3.05, -0.55, 2.9, TEAL, lw=1.8)
# water movement
for wx in (-2.2, 0.0, 2.2):
    arrow(ax, wx, 3.42, wx, 2.95, BLUE, lw=2.6)
ax.text(2.75, 3.35, "об", fontsize=10.5, color=BLUE, weight="bold")
arrow(ax, 1.1, 2.45, 3.3, 1.6, BLUE, lw=2.6)
ax.text(2.5, 1.9, "об ба хун", fontsize=9, color=BLUE, weight="bold")
ax.text(0.0, 0.55, "Натиҷа: пешоб ғализ мешавад, об нигоҳ дошта мешавад",
        ha="center", fontsize=10.5, color=INK, weight="bold")
ax.set_xlim(-4.6, 4.6); ax.set_ylim(0.3, 5.0)
ax.axis("off")
plt.savefig("img13/shakli_3_1.png", dpi=200, facecolor=BG, bbox_inches="tight")
plt.close()

# ===== 3.2: Занҷири RAAS (flowchart) =====
fig, ax = plt.subplots(figsize=(9.4, 6.6), dpi=200)
fig.patch.set_facecolor(BG); ax.set_facecolor(BG)
ax.text(0.0, 4.72, "Системаи ренин-ангиотензин-альдостерон", ha="center",
        fontsize=13.5, color=INK, weight="bold")
boxes = [
    ("Камшавии фишори хун\nва хунравии гурда", (-3.4, 3.85), 2.5, 0.85, "#FDF2F8", ROSE),
    ("Ренин\n(юкстагломеруларӣ)", (-3.5, 2.65), 2.4, 0.95, "#EEF4FB", BLUE),
    ("Ангиотензиноген →\nАнгиотензин I (ҷигар)", (0.05, 2.65), 2.7, 0.95, "#EEF4FB", BLUE),
    ("Ангиотензин II\n(ACE, шуш)", (3.25, 2.65), 2.3, 0.95, "#FEF6E7", AMBER),
    ("Альдостерон (пӯсти болоии\nгурдаи ҳойла)", (3.25, 1.35), 2.3, 0.95, "#E6F2EF", TEAL),
    ("Na+ ва об нигоҳ\nдошта мешаванд", (0.2, 1.35), 2.7, 0.95, "#E6F2EF", TEAL),
    ("Фишор ва ҳаҷми хун\nбармегарданд", (-3.2, 1.35), 2.6, 0.95, "#E6F2EF", TEAL),
]
for txt, (bx, by), bw, bh, fc, ec in boxes:
    ax.add_patch(mpatches.FancyBboxPatch((bx - bw/2, by - bh/2), bw, bh,
                 boxstyle="round,pad=0.09", fc=fc, ec=ec, lw=2.0))
    ax.text(bx, by, txt, ha="center", va="center", fontsize=8.8, color=INK)
arrow(ax, -3.4, 3.42, -3.4, 3.16, ROSE, lw=2.2)
arrow(ax, -2.3, 2.65, -1.3, 2.65, BLUE, lw=2.2)
arrow(ax, 1.4, 2.65, 2.1, 2.65, BLUE, lw=2.2)
arrow(ax, 3.25, 2.15, 3.25, 1.86, AMBER, lw=2.2)
arrow(ax, 1.68, 1.35, 1.1, 1.35, TEAL, lw=2.2)
arrow(ax, -1.2, 1.35, -1.85, 1.35, TEAL, lw=2.2)
ax.text(0.0, 0.55, "Ангиотензин II рагҳоро тор мекунад ва ташнӯро меорад",
        ha="center", fontsize=9.8, color=SLATE)
ax.set_xlim(-5.3, 4.8); ax.set_ylim(0.75, 4.6)
ax.axis("off")
plt.savefig("img13/shakli_3_2.png", dpi=200, facecolor=BG, bbox_inches="tight")
plt.close()

# ===== 4.1: ЭКГ дар вазъҳои калий =====
fig, ax = plt.subplots(figsize=(9.4, 6.4), dpi=200)
fig.patch.set_facecolor(BG); ax.set_facecolor(BG)
ax.text(0.5, 0.94, "Тағйироти ЭКГ дар вазъҳои калий", ha="center",
        fontsize=13.5, color=INK, weight="bold", transform=ax.transAxes)
t = np.linspace(0, 6, 1200)

def beat(y0, amp=1.0, peak=1.0, qrs_w=0.16, u=0.0, p_amp=1.0):
    y = 0.02 * np.sin(t * 6.3)
    qrs = amp * np.exp(-((t - 1.0) ** 2) / (2 * qrs_w ** 2)) * 1.55 * peak
    tw = np.exp(-((t - 1.55) ** 2) / (2 * 0.16 ** 2)) * 0.55 * peak
    pw = np.exp(-((t - 0.45) ** 2) / (2 * 0.07 ** 2)) * 0.22 * p_amp
    uw = np.exp(-((t - 2.05) ** 2) / (2 * 0.09 ** 2)) * 0.22 * u
    return y0 + y + pw + qrs + tw + uw

rows = [
    ("Гипокалcия (K < 3,5): U-мӯҷа, T паст", beat(6.6, peak=0.55, u=1.9),
     BLUE),
    ("Меъёр (K 3,5–5,1)", beat(4.4), TEAL),
    ("Гиперкалиемия (K > 5,5): T-баланд,\nQRS васеъ", beat(2.2, peak=1.7,
     qrs_w=0.34, p_amp=0.25), ROSE),
]
for i, (lab, y, color) in enumerate(rows):
    off = 6.6 - i * 2.2
    ax.plot(t, y, color=color, lw=1.9)
    ax.text(6.15, off + 0.72, lab, fontsize=9.6, color=color, weight="bold",
            ha="right")
ax.axhline(8.8, color=SLATE, lw=0.7, alpha=0.4)
ax.axhline(6.6, color=SLATE, lw=0.7, alpha=0.4)
ax.axhline(4.4, color=SLATE, lw=0.7, alpha=0.4)
ax.axhline(2.2, color=SLATE, lw=0.7, alpha=0.4)
ax.set_xlim(0, 6.2); ax.set_ylim(1.2, 9.5)
ax.axis("off")
ax.text(0.5, 0.015, "Афзоиши калий: T баланд → P паст → QRS васеъ → аритмия",
        ha="center", fontsize=9.5, color=SLATE, transform=ax.transAxes)
plt.savefig("img13/shakli_4_1.png", dpi=200, facecolor=BG, bbox_inches="tight")
plt.close()

print("img13 ok: 5 PNG")
