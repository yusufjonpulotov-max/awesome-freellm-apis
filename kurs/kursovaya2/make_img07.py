import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np

plt.rcParams["font.family"] = "DejaVu Sans"
C_BG   = "#F4F9F1"; C_BOX = "#E8F0DD"; C_EDGE = "#4A7043"
C_A    = "#D9E8F5"; C_AE  = "#2E5F8A"
C_B    = "#FBE9D9"; C_BE  = "#B45F1D"
C_C    = "#EFE3F5"; C_CE  = "#6B3FA0"

def box(ax, x, y, w, h, txt, fc, ec, fs=9.5, weight="normal"):
    b = FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.02,rounding_size=0.035",
                       fc=fc, ec=ec, lw=1.6)
    ax.add_patch(b)
    ax.text(x + w/2, y + h/2, txt, ha="center", va="center", fontsize=fs,
            weight=weight, color="#1A1A1A", wrap=True)

def arrow(ax, x1, y1, x2, y2, color, style="-|>", lw=1.8, ls="-"):
    a = FancyArrowPatch((x1, y1), (x2, y2), arrowstyle=style, mutation_scale=16,
                        color=color, lw=lw, linestyle=ls)
    ax.add_patch(a)

# ============ 1.1 Синфи гормонҳо (ситонаи се-шоха) ============
fig, ax = plt.subplots(figsize=(9.2, 5.2), dpi=200)
ax.set_xlim(0, 1); ax.set_ylim(0, 1); ax.axis("off")
fig.patch.set_facecolor(C_BG); ax.set_facecolor(C_BG)
box(ax, 0.32, 0.83, 0.36, 0.12, "ГОРМОНҲО\n(пайвироҳи сигнали химиявӣ)", C_EDGE, C_EDGE, 11, "bold")
box(ax, 0.02, 0.46, 0.29, 0.16, "Пептидӣ ва сафедавӣ\nинсулин, глюкагон,\nACTH, TSH, гормони рушд", C_A, C_AE)
box(ax, 0.355, 0.46, 0.29, 0.16, "Стероидӣ\nкортизол, алдостерон,\nэстрадиол, тестостерон", C_B, C_BE)
box(ax, 0.69, 0.46, 0.29, 0.16, "Аминокислотагӣ\nT3, T4 (тирозин+йод),\nадреналин, норадреналин", C_C, C_CE)
for x0 in (0.165, 0.5, 0.835):
    arrow(ax, 0.5, 0.815, x0, 0.635, C_EDGE)
box(ax, 0.02, 0.13, 0.29, 0.17, "Ресептор:\nмембранаӣ\n(cAMP, PKA)", "#FFFFFF", C_AE)
box(ax, 0.355, 0.13, 0.29, 0.17, "Ресептор:\nдохили ҳуҷайравӣ\n(гени мубодила)", "#FFFFFF", C_BE)
box(ax, 0.69, 0.13, 0.29, 0.17, "Ресептор:\nдохилӣ ё мембранаӣ\n(мубодила ↑)", "#FFFFFF", C_CE)
arrow(ax, 0.165, 0.44, 0.165, 0.31, C_AE)
arrow(ax, 0.5, 0.44, 0.5, 0.31, C_BE)
arrow(ax, 0.835, 0.44, 0.835, 0.31, C_CE)
ax.text(0.5, 0.035, "Синфи гормон механизми амал ва суръати таъсирро муайян мекунад",
        ha="center", fontsize=9, style="italic", color="#333333")
plt.savefig("img07/shakli_1_1.png", dpi=200, facecolor=C_BG, bbox_inches="tight")
plt.close()

# ============ 1.2 Оси HPA ============
fig, ax = plt.subplots(figsize=(9.2, 5.6), dpi=200)
ax.set_xlim(0, 1); ax.set_ylim(0, 1); ax.axis("off")
fig.patch.set_facecolor(C_BG); ax.set_facecolor(C_BG)
box(ax, 0.34, 0.82, 0.32, 0.12, "ГИПОТАЛАМУС\nCRH (кортикотропин-озодкунанда)", C_A, C_AE, 9.5, "bold")
box(ax, 0.34, 0.50, 0.32, 0.12, "ГИПОФИЗИ ПЕШ\nACTH (адренокортикотропин)", C_B, C_BE, 9.5, "bold")
box(ax, 0.34, 0.18, 0.32, 0.12, "ҚИШРИ ҒАДУДИ АДРЕНАЛ\n(зонаи фасцикулата ~75%)", C_C, C_CE, 9.5, "bold")
box(ax, 0.73, 0.18, 0.25, 0.12, "КОРТИЗОЛ\nглюконеогенез,\nлиполиз, протеолиз", "#FFFFFF", C_EDGE, 9)
arrow(ax, 0.5, 0.80, 0.5, 0.64, C_AE)
ax.text(0.515, 0.725, "CRH", fontsize=9, color=C_AE, weight="bold")
arrow(ax, 0.5, 0.48, 0.5, 0.32, C_BE)
ax.text(0.515, 0.405, "ACTH", fontsize=9, color=C_BE, weight="bold")
arrow(ax, 0.67, 0.24, 0.72, 0.24, C_CE)
ax.text(0.86, 0.085, "гликемия ↑", fontsize=9.5, color="#333333")
arrow(ax, 0.855, 0.165, 0.855, 0.115, C_CE)
ax.plot([0.73, 0.13], [0.24, 0.24], color=C_CE, lw=1.5)
ax.plot([0.13, 0.13], [0.24, 0.88], color=C_EDGE, lw=1.5, linestyle="--")
arrow(ax, 0.13, 0.88, 0.325, 0.88, C_EDGE, ls="--", lw=1.5)
arrow(ax, 0.13, 0.60, 0.325, 0.60, C_EDGE, ls="--", lw=1.5)
ax.text(0.045, 0.48, "танзими бозгаштии\nманфӣ (кортизол)", fontsize=8.5, color="#333333", style="italic")
plt.savefig("img07/shakli_1_2.png", dpi=200, facecolor=C_BG, bbox_inches="tight")
plt.close()

# ============ 2.1 Контр-танзими гликемия ============
fig, ax = plt.subplots(figsize=(9.2, 5.6), dpi=200)
ax.set_xlim(0, 1); ax.set_ylim(0, 1); ax.axis("off")
fig.patch.set_facecolor(C_BG); ax.set_facecolor(C_BG)
box(ax, 0.36, 0.84, 0.28, 0.10, "ГЛИКЕМИЯ\n(сатҳи глюкозаи хун)", C_EDGE, C_EDGE, 10.5, "bold")
box(ax, 0.03, 0.52, 0.27, 0.14, "ИНСУЛИН: β-ҳуҷайра,\nGLUT4 ба мембрана,\nглюкоза → ҳуҷайра", "#DCEFE0", "#2F6B3F")
box(ax, 0.355, 0.52, 0.29, 0.14, "ГЛЮКАГОН: α-ҳуҷайра,\nгликогенолиз ва\nглюконеогенез дар ҷигар", C_B, C_BE)
box(ax, 0.70, 0.52, 0.27, 0.14, "КОРТИЗОЛ + АДРЕНАЛИН\nстресс, глюконеогенез\nва гликогенолиз", C_C, C_CE)
arrow(ax, 0.165, 0.65, 0.40, 0.84, "#2F6B3F")
arrow(ax, 0.50, 0.64, 0.50, 0.82, C_BE)
arrow(ax, 0.835, 0.65, 0.61, 0.84, C_CE)
box(ax, 0.09, 0.13, 0.82, 0.20, "ҲАМРОҲАМДӢ:\nқарши ҳамдигар — инсулин ↔ глюкагон;\nҳамроҳамдӣ — кортизол + адреналин ↔ глюкагон → ҷамъбасти гликемия",
    "#FFFFFF", C_EDGE, 9.5)
arrow(ax, 0.165, 0.50, 0.30, 0.35, "#2F6B3F", ls="-")
arrow(ax, 0.50, 0.50, 0.50, 0.35, C_BE)
arrow(ax, 0.835, 0.50, 0.70, 0.35, C_CE)
ax.text(0.5, 0.045, "Дар диабет ин мутаносиб вайрон мешавад — гликемия устуворӣ гум мекунад",
        ha="center", fontsize=9, style="italic", color="#333333")
plt.savefig("img07/shakli_2_1.png", dpi=200, facecolor=C_BG, bbox_inches="tight")
plt.close()

# ============ 3.1 Профили гликемияи рӯзона ============
fig, ax = plt.subplots(figsize=(9.2, 4.9), dpi=200)
fig.patch.set_facecolor("#FBFCF7"); ax.set_facecolor("#FBFCF7")
t = np.linspace(0, 24, 481)
def profile(meals, base=5.2, k=1.0):
    g = np.full_like(t, base)
    for (tm, amp, w) in meals:
        g += amp * np.exp(-((t - tm) ** 2) / (2 * w ** 2))
    return g
meals_pre  = [(8, 3.9, 1.1), (13, 4.2, 1.3), (16.5, 2.1, 0.9), (20, 3.4, 1.2)]
meals_post = [(8, 2.2, 0.9), (13, 2.6, 1.0), (16.5, 0.9, 0.7), (20, 1.9, 0.9)]
ax.axhspan(3.9, 7.8, color="#E4F0E0", zorder=0, label="Ҳудуди меъёр (3,9–7,8 ммол/л)")
ax.axhline(7.8, color="#B45F1D", lw=1.4, ls="--")
ax.plot(t, profile(meals_pre),  color="#B45F1D", lw=2.4, label="Пеш аз тадбир (қулла: 9,4)")
ax.plot(t, profile(meals_post), color="#2F6B3F", lw=2.4, label="Баъди тадбир (қулла: 7,2)")
for tm, lbl in [(8, "субҳ"), (13, "нисфирӯз"), (16.5, "зоҳирхӯрӣ"), (20, "шом")]:
    ax.axvline(tm, color="#9AA79A", lw=0.9, ls=":")
    ax.text(tm, 2.85, lbl, ha="center", fontsize=8.2, color="#556455")
ax.set_xlim(6.5, 22.5); ax.set_ylim(2.5, 10.2)
ax.set_xticks(range(7, 23, 2)); ax.set_xticklabels([f"{h}:00" for h in range(7, 23, 2)], fontsize=9)
ax.set_ylabel("Гликемия, ммол/л", fontsize=10)
ax.set_xlabel("Вақти шабонарӯз", fontsize=10)
ax.grid(color="#DDE5D8", lw=0.6)
ax.legend(loc="upper right", fontsize=9, framealpha=0.95)
for s in ("top", "right"):
    ax.spines[s].set_visible(False)
plt.savefig("img07/shakli_3_1.png", dpi=200, facecolor="#FBFCF7", bbox_inches="tight")
plt.close()
print("4 PNG ok")
