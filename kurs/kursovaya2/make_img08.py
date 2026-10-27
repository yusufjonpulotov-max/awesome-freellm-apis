import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["font.family"] = "DejaVu Sans"
TEAL = "#0F766E"; ROSE = "#B91C5C"; AMBER = "#B45309"; SLATE = "#475569"

# ===== 1.1: Michaelis-Menten гипербола =====
fig, ax = plt.subplots(figsize=(8.8, 5.2), dpi=200)
fig.patch.set_facecolor("#F7FAF8"); ax.set_facecolor("#F7FAF8")
S = np.linspace(0, 10, 400); Km, Vm = 2.0, 8.0
v = Vm * S / (Km + S)
ax.plot(S, v, color=TEAL, lw=2.6, label="v = Vmax·[S]/(Km+[S])")
ax.axhline(Vm, color=SLATE, lw=1.3, ls="--")
ax.text(7.4, Vm + 0.15, "Vmax = 8", fontsize=10, color=SLATE)
ax.plot([Km, Km], [0, Vm/2], color=ROSE, lw=1.2, ls=":")
ax.plot([0, Km], [Vm/2, Vm/2], color=ROSE, lw=1.2, ls=":")
ax.plot([Km], [Vm/2], "o", ms=7, color=ROSE)
ax.annotate("Km: [S] дар нисфи Vmax", xy=(Km, Vm/2), xytext=(3.4, 2.4),
            fontsize=10, color=ROSE, arrowprops=dict(arrowstyle="->", color=ROSE, lw=1.4))
ax.annotate("суръати ибтидоӣ:\nхатӣ", xy=(0.55, 1.55), xytext=(0.45, 3.7),
            fontsize=9, color=AMBER, arrowprops=dict(arrowstyle="->", color=AMBER, lw=1.3))
ax.text(8.35, 4.15, "суръати\nнасишавӣ:\nсифрӣ", fontsize=9, color=SLATE, ha="center")
ax.set_xlim(0, 10); ax.set_ylim(0, 9.4)
ax.set_xlabel("Консентратсияи субстрат [S], ммол/л", fontsize=10)
ax.set_ylabel("Суръати реаксия v, U/L", fontsize=10)
ax.grid(color="#D9E2DD", lw=0.6)
ax.legend(loc="lower right", fontsize=9.5, framealpha=0.95)
for s_ in ("top", "right"):
    ax.spines[s_].set_visible(False)
plt.savefig("img08/shakli_1_1.png", dpi=200, facecolor="#F7FAF8", bbox_inches="tight")
plt.close()

# ===== 1.2: Лайнвивер–Бёрк, 3 хат =====
fig, ax = plt.subplots(figsize=(8.8, 5.6), dpi=200)
fig.patch.set_facecolor("#FBF8F4"); ax.set_facecolor("#FBF8F4")
x = np.linspace(-0.6, 1.6, 200)
Vm2 = 8.0; Km2 = 2.0
y0 = (Km2/Vm2) * x + 1/Vm2                      # бе ингибитор
yc = (Km2/Vm2 * 2.2) * x + 1/Vm2                # рақобатӣ
yn = (Km2/Vm2 * 2.2) * x + 2.2/Vm2              # ғайрирақобатӣ
ax.plot(x, y0, color=TEAL, lw=2.4, label="бе ингибитор")
ax.plot(x, yc, color=ROSE, lw=2.4, ls="--", label="манъи рақобатӣ")
ax.plot(x, yn, color=AMBER, lw=2.4, ls="-.", label="манъи ғайрирақобатӣ")
ax.axhline(0, color="#94A3B8", lw=1.0); ax.axvline(0, color="#94A3B8", lw=1.0)
ax.annotate("қатъи Y: 1/Vmax\n(як ҷо — рақобатӣ)", xy=(0, 1/Vm2), xytext=(0.55, 0.32),
            fontsize=9, color=ROSE, arrowprops=dict(arrowstyle="->", color=ROSE, lw=1.3))
ax.annotate("қатъи X: −1/Km\n(як ҷо — ғайрирақобатӣ)", xy=(-1/Km2, 0), xytext=(-0.62, 0.44),
            fontsize=9, color=AMBER, arrowprops=dict(arrowstyle="->", color=AMBER, lw=1.3))
ax.set_xlim(-0.7, 1.7); ax.set_ylim(0, 0.62)
ax.set_xlabel("1/[S], 1/(ммол/л)", fontsize=10)
ax.set_ylabel("1/v, 1/(U/L)", fontsize=10)
ax.grid(color="#EADFD2", lw=0.6)
ax.legend(loc="upper right", fontsize=9.5, framealpha=0.95)
for s_ in ("top", "right"):
    ax.spines[s_].set_visible(False)
plt.savefig("img08/shakli_1_2.png", dpi=200, facecolor="#FBF8F4", bbox_inches="tight")
plt.close()

# ===== 2.1: Flowchart ташхиси ферментӣ =====
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
def box(ax, x, y, w, h, txt, fc, ec, fs=9.5, weight="normal"):
    b = FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.02,rounding_size=0.04",
                       fc=fc, ec=ec, lw=1.6)
    ax.add_patch(b)
    ax.text(x + w/2, y + h/2, txt, ha="center", va="center", fontsize=fs,
            weight=weight, color="#1F2937")

def arrow(ax, x1, y1, x2, y2, color, lw=1.8, ls="-"):
    a = FancyArrowPatch((x1, y1), (x2, y2), arrowstyle="-|>", mutation_scale=15,
                        color=color, lw=lw, linestyle=ls)
    ax.add_patch(a)

fig, ax = plt.subplots(figsize=(9.4, 5.8), dpi=200)
ax.set_xlim(0, 1); ax.set_ylim(0, 1); ax.axis("off")
fig.patch.set_facecolor("#F5F6F8"); ax.set_facecolor("#F5F6F8")
box(ax, 0.345, 0.855, 0.31, 0.105, "ГИРИФТАНИ НАМУНА\n(варақаи сабт: вақт, дору, ҳолат)", "#E2E8F0", SLATE, 9.3, "bold")
box(ax, 0.345, 0.66, 0.31, 0.105, "НАЗОРАТИ НАМУНА\n(ҳемолиз? липемия? зудкорӣ?)", "#FCE7F3", ROSE, 9.3)
box(ax, 0.345, 0.465, 0.31, 0.105, "ТАҲЛИЛИ КИНЕТИКӢ\n(37°C, pH-и стандарӣ, U/L)", "#CCFBF1", TEAL, 9.3, "bold")
box(ax, 0.345, 0.27, 0.31, 0.105, "МУҚОИСА БО МЕЪЁР\n(дараҷаи афзоиш, × ULN)", "#FEF3C7", AMBER, 9.3)
box(ax, 0.345, 0.075, 0.31, 0.105, "ТАФСИРИ КЛИНИКӢ\n(гурӯҳи осеб, динамика)", "#EDE9FE", "#6D28D9", 9.3, "bold")
for y1, y2 in [(0.852, 0.768), (0.657, 0.573), (0.462, 0.378), (0.267, 0.183)]:
    arrow(ax, 0.5, y1, 0.5, y2, SLATE)
box(ax, 0.735, 0.66, 0.245, 0.105, "НАМУНАИ НАВ\n(қабули дубора)", "#FCE7F3", ROSE, 9)
arrow(ax, 0.658, 0.7125, 0.732, 0.7125, ROSE, ls="--")
box(ax, 0.005, 0.27, 0.285, 0.105, "ИЗОФЕРМЕНТ Ё МАРКЕРИ ИЛОВА\n(CK-MB, тропонин, GGT)", "#F1F5F9", SLATE, 8.8)
arrow(ax, 0.292, 0.3225, 0.342, 0.3225, SLATE)
box(ax, 0.735, 0.075, 0.245, 0.105, "НАЗОРАТИ ДИНАМИКА\n(ҳар 2–3 рӯз)", "#EDE9FE", "#6D28D9", 8.8)
arrow(ax, 0.658, 0.1275, 0.732, 0.1275, "#6D28D9", ls="--")
ax.text(0.5, 0.018, "Ҳар марҳила дар варақаи сабт сабт мешавад — ин асоси сифати таҳлил аст",
        ha="center", fontsize=9, style="italic", color="#4B5563")
plt.savefig("img08/shakli_2_1.png", dpi=200, facecolor="#F5F6F8", bbox_inches="tight")
plt.close()

# ===== 3.1: Динамикаи ALT =====
fig, ax = plt.subplots(figsize=(8.8, 5.0), dpi=200)
fig.patch.set_facecolor("#FBFCF8"); ax.set_facecolor("#FBFCF8")
weeks = np.array([0, 2, 4, 8])
alt = np.array([245, 118, 68, 39])
ax.axhspan(0, 56, color="#E6F4EA", zorder=0, label="Меъёри ALT (то 56 U/L)")
ax.axhline(56, color=TEAL, lw=1.4, ls="--")
ax.plot(weeks, alt, color=ROSE, lw=2.5, marker="o", ms=7,
        mfc="#FFFFFF", mec=ROSE, mew=2, label="ALT дар давоми табобат")
for w_, a_ in zip(weeks, alt):
    ax.annotate(f"{a_}", xy=(w_, a_), xytext=(w_ + 0.13, a_ + 7),
                fontsize=9.5, color=ROSE, weight="bold")
ax.annotate("4,4× меъёр:\nафзоиши аз 2 то 5", xy=(0.05, 243), xytext=(1.7, 226),
            fontsize=9, color=SLATE, arrowprops=dict(arrowstyle="->", color=SLATE, lw=1.2))
ax.annotate("0,7× меъёр: мутаносиб", xy=(8, 39), xytext=(5.0, 88),
            fontsize=9, color=TEAL, arrowprops=dict(arrowstyle="->", color=TEAL, lw=1.2))
ax.set_xlim(-0.4, 8.9); ax.set_ylim(0, 280)
ax.set_xticks([0, 2, 4, 6, 8])
ax.set_xticklabels(["ҳафтаи 0", "ҳафтаи 2", "ҳафтаи 4", "ҳафтаи 6", "ҳафтаи 8"], fontsize=9.5)
ax.set_ylabel("ALT, U/L", fontsize=10)
ax.grid(color="#E2E8DF", lw=0.6)
ax.legend(loc="upper right", fontsize=9.5, framealpha=0.95)
for s_ in ("top", "right"):
    ax.spines[s_].set_visible(False)
plt.savefig("img08/shakli_3_1.png", dpi=200, facecolor="#FBFCF8", bbox_inches="tight")
plt.close()
print("4 PNG ok")
