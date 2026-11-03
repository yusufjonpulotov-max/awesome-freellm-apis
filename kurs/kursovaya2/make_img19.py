# -*- coding: utf-8 -*-
"""Расмҳои кори курсӣ М19 — Биохимияи мушак (5 PNG)."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import os

INK = "#1F2A44"; SLATE = "#64748B"; BLUE = "#1D4ED8"; TEAL = "#0F766E"
AMBER = "#B45309"; ROSE = "#BE185D"; PURPLE = "#6D28D9"; BG = "#FBF8F4"
plt.rcParams["font.family"] = "DejaVu Sans"
os.makedirs("img19", exist_ok=True)

def arrow(ax, x1, y1, x2, y2, color, lw=2.2):
    ax.annotate("", xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle="-|>", color=color, lw=lw,
                                mutation_scale=18))

def box(ax, x, y, w, h, txt, fc, ec, fs=9.0):
    ax.add_patch(mpatches.FancyBboxPatch((x - w/2, y - h/2), w, h,
                 boxstyle="round,pad=0.09", fc=fc, ec=ec, lw=2.0))
    ax.text(x, y, txt, ha="center", va="center", fontsize=fs, color=INK)

# ===== 1.1: Саркомер =====
fig, ax = plt.subplots(figsize=(9.6, 5.6), dpi=200)
fig.patch.set_facecolor(BG); ax.set_facecolor(BG)
ax.text(0.0, 3.15, "Саркомер ва зонаҳои он", ha="center", fontsize=13.5,
        color=INK, weight="bold")
ax.add_patch(mpatches.Rectangle((1.15, 0.7), 0.22, 2.0, fc=ROSE,
             ec="none"))
ax.add_patch(mpatches.Rectangle((8.63, 0.7), 0.22, 2.0, fc=ROSE,
             ec="none"))
ax.text(1.26, 0.42, "хати Z", ha="center", fontsize=9.4, color=ROSE,
        weight="bold")
ax.text(8.74, 0.42, "хати Z", ha="center", fontsize=9.4, color=ROSE,
        weight="bold")
# филаменти ғафс (миозин) — мияна
ax.add_patch(mpatches.Rectangle((3.2, 1.45), 3.6, 0.5, fc=BLUE,
             ec="none", alpha=0.85))
ax.text(5.0, 1.7, "филаменти ғафс (миозин)", ha="center", va="center",
        fontsize=9.2, color="white", weight="bold")
# филаменти назук (актин) — аз ҳар тараф
for x0, x1 in [(1.37, 3.6), (6.4, 8.63)]:
    ax.add_patch(mpatches.Rectangle((x0, 1.56), x1 - x0, 0.28,
                 fc=TEAL, ec="none", alpha=0.9))
ax.text(2.4, 2.12, "актин (филаменти назук)", ha="center", fontsize=9.2,
        color=TEAL, weight="bold")
# зонаҳо
ax.annotate("", xy=(3.2, 3.0), xytext=(6.8, 3.0),
            arrowprops=dict(arrowstyle="<->", color=AMBER, lw=2.2))
ax.text(5.0, 3.18, "зонаи А", ha="center", fontsize=9.8, color=AMBER,
        weight="bold")
ax.annotate("", xy=(1.37, 2.55), xytext=(3.2, 2.55),
            arrowprops=dict(arrowstyle="<->", color=PURPLE, lw=2.2))
ax.text(2.25, 2.75, "зонаи I", ha="center", fontsize=9.8, color=PURPLE,
        weight="bold")
ax.annotate("", xy=(6.8, 2.55), xytext=(8.63, 2.55),
            arrowprops=dict(arrowstyle="<->", color=PURPLE, lw=2.2))
ax.text(7.7, 2.75, "зонаи I", ha="center", fontsize=9.8, color=PURPLE,
        weight="bold")
ax.text(5.0, 0.95, "Қискарш: зонаи I кӯтоҳ мешавад, зонаи А доимист",
        ha="center", fontsize=10.2, color=INK, weight="bold")
ax.add_patch(mpatches.Rectangle((1.26, 0.18), 7.59, 0.0, fc="none"))
ax.text(5.0, 0.1, "Саркомер = фосилаи байни ду хати Z", ha="center",
        fontsize=9.6, color=SLATE)
ax.set_xlim(0.6, 9.4); ax.set_ylim(-0.15, 3.6)
ax.axis("off")
plt.savefig("img19/shakli_1_1.png", dpi=200, facecolor=BG,
            bbox_inches="tight")
plt.close()

# ===== 1.2: Филаменти назук =====
fig, ax = plt.subplots(figsize=(9.6, 4.6), dpi=200)
fig.patch.set_facecolor(BG); ax.set_facecolor(BG)
ax.text(0.0, 1.95, "Филаменти назук: актин, тропомиозин ва тропонин",
        ha="center", fontsize=13.5, color=INK, weight="bold")
# занҷири актин — доираҳо
for i in range(14):
    ax.add_patch(mpatches.Circle((1.0 + i * 0.6, 0.9), 0.22, fc=TEAL,
                 ec="white", lw=1.5))
ax.text(4.9, 0.35, "занҷири F-актин", ha="center", fontsize=9.6,
        color=TEAL, weight="bold")
# тропомиозин — хати дароз
ax.plot([0.9, 8.9], [1.35, 1.35], color=AMBER, lw=4.5,
        solid_capstyle="round")
ax.text(4.9, 1.62, "тропомиозин (пӯшони ҷойҳои миозин)", ha="center",
        fontsize=9.6, color=AMBER, weight="bold")
# тропонин — се нуқта
for xx in [2.2, 4.6, 7.0]:
    ax.add_patch(mpatches.Circle((xx, 1.35), 0.17, fc=ROSE,
                 ec="white", lw=1.5))
ax.text(2.2, 0.12, "тропонин T", ha="center", fontsize=8.8, color=ROSE)
ax.text(4.6, 0.12, "тропонин C — пайвасти калсий", ha="center",
        fontsize=8.8, color=ROSE)
ax.text(7.0, 0.12, "тропонин I", ha="center", fontsize=8.8, color=ROSE)
ax.text(0.0, -0.55, "Калсий ба тропонин C мепайвастад → пӯшон боз мешавад",
        ha="center", fontsize=10.0, color=INK, weight="bold")
ax.set_xlim(-0.3, 10.1); ax.set_ylim(-0.85, 2.3)
ax.axis("off")
plt.savefig("img19/shakli_1_2.png", dpi=200, facecolor=BG,
            bbox_inches="tight")
plt.close()

# ===== 2.1: Роҳи калсий =====
fig, ax = plt.subplots(figsize=(9.6, 6.2), dpi=200)
fig.patch.set_facecolor(BG); ax.set_facecolor(BG)
ax.text(0.0, 4.7, "Роҳи калсий: аз импулс то қискарш", ha="center",
        fontsize=13.5, color=INK, weight="bold")
box(ax, -3.4, 4.0, 2.7, 0.8, "Пайвасти\nнерв-мушак", "#EEF4FB", BLUE,
    fs=9.0)
box(ax, -0.4, 4.0, 2.5, 0.8, "Импулс дар\nлӯлачаҳои T", "#E6F2EF",
    TEAL, fs=9.0)
box(ax, 2.7, 4.0, 2.6, 0.8, "Рецептори\nрианодин кушода", "#FEF6E7",
    AMBER, fs=9.0)
arrow(ax, -2.05, 4.0, -1.67, 4.0, SLATE)
arrow(ax, 0.87, 4.0, 1.38, 4.0, SLATE)
box(ax, 0.9, 2.6, 3.2, 0.9, "Калсий аз тор берун\n→ тропонин C",
    "#FDF2F8", ROSE, fs=9.2)
arrow(ax, 2.7, 3.58, 1.7, 3.08, SLATE)
box(ax, -2.9, 2.6, 2.6, 0.8, "Ҷойҳои миозин\nкушода мешаванд",
    "#FDF2F8", ROSE, fs=8.8)
arrow(ax, -0.72, 2.6, -1.58, 2.6, SLATE)
box(ax, -2.9, 1.1, 2.6, 0.8, "Давраи пайвастҳо\n→ қискарш", "#E6F2EF",
    TEAL, fs=9.0)
arrow(ax, -2.9, 2.18, -2.9, 1.53, SLATE)
box(ax, 2.4, 1.1, 3.2, 0.9, "Помпаи SERCA:\nкалсий бармегардад", "#EEF4FB",
    BLUE, fs=9.0)
arrow(ax, 1.4, 1.1, 0.78, 1.1, SLATE)
box(ax, 0.0, -0.3, 3.4, 0.8, "Оромии мушак", "#F5F3FF", PURPLE, fs=9.4)
arrow(ax, -1.5, 0.68, -0.8, 0.13, SLATE)
arrow(ax, 2.4, 0.63, 0.9, 0.13, SLATE)
ax.text(0.0, -1.25, "Ҳамон помпаи SERCA АТФ-ро мегирад", ha="center",
        fontsize=10.0, color=INK, weight="bold")
ax.set_xlim(-5.2, 5.2); ax.set_ylim(-1.6, 5.1)
ax.axis("off")
plt.savefig("img19/shakli_2_1.png", dpi=200, facecolor=BG,
            bbox_inches="tight")
plt.close()

# ===== 3.1: Динамикаи CK =====
fig, ax = plt.subplots(figsize=(9.4, 5.6), dpi=200)
fig.patch.set_facecolor(BG); ax.set_facecolor(BG)
t = np.linspace(0, 120, 300)
rise = np.where(t < 2, 200, 200 + 7800 * np.tanh((t - 2) / 22))
decay = np.where(t > 48, 8000 * np.exp(-(t - 48) / 52) + 200, rise)
y = np.where(t > 48, decay, rise)
ax.plot(t, y, color=ROSE, lw=3.2)
ax.fill_between(t, 0, y, color=ROSE, alpha=0.12)
ax.axhline(200, color=SLATE, lw=1.6, ls="--")
ax.text(112, 320, "меъёр 200", ha="right", fontsize=9.2, color=SLATE)
ax.axhline(1000, color=AMBER, lw=1.6, ls="--")
ax.text(112, 1130, "ҳадди ташхис ×5", ha="right", fontsize=9.2,
        color=AMBER)
ax.axvline(48, color=BLUE, lw=1.6, ls=":")
ax.text(49, 7600, "қулла: 1–5 рӯз", fontsize=9.4, color=BLUE,
        weight="bold")
ax.annotate("t½ = 36 соат", xy=(84, 2600), xytext=(88, 4700),
            fontsize=9.6, color=INK,
            arrowprops=dict(arrowstyle="-|>", color=INK, lw=1.8))
ax.set_xlabel("Соатҳо баъди осеб", fontsize=10, color=SLATE)
ax.set_ylabel("Креатинкиназа, воҳид/л", fontsize=10, color=SLATE)
ax.set_xlim(0, 120); ax.set_ylim(0, 9000)
ax.spines[["top", "right"]].set_visible(False)
ax.text(0.5, 0.96, "Динамикаи креатинкиназа баъди осеби мушак",
        ha="center", va="top", fontsize=13.5, color=INK, weight="bold",
        transform=ax.transAxes)
plt.savefig("img19/shakli_3_1.png", dpi=200, facecolor=BG,
            bbox_inches="tight")
plt.close()

# ===== 4.1: Навъҳои наёлҳо =====
fig, ax = plt.subplots(figsize=(9.4, 5.8), dpi=200)
fig.patch.set_facecolor(BG); ax.set_facecolor(BG)
groups = ["Навъи I", "Навъи IIa", "Навъи IIb"]
speed = [3, 7, 10]
fatig = [2, 5, 9]
myo = [9, 6, 2]
x = np.arange(3)
w = 0.24
b1 = ax.bar(x - w, speed, w, label="Суръати қискарш", color=BLUE,
            alpha=0.88)
b2 = ax.bar(x, fatig, w, label="Хастагӣ", color=ROSE, alpha=0.88)
b3 = ax.bar(x + w, myo, w, label="Миоглобин", color=TEAL, alpha=0.88)
for bars in (b1, b2, b3):
    for bi in bars:
        ax.text(bi.get_x() + bi.get_width()/2, bi.get_height() + 0.15,
                f"{int(bi.get_height())}", ha="center", fontsize=9.2,
                color=INK, weight="bold")
ax.set_xticks(x); ax.set_xticklabels(groups, fontsize=10.5, color=INK)
ax.set_ylim(0, 11.5)
ax.set_ylabel("Баҳои муқоисавӣ (0–10)", fontsize=10, color=SLATE)
ax.legend(fontsize=9.2, frameon=False, loc="upper left")
ax.spines[["top", "right"]].set_visible(False)
ax.set_title("Муқоисаи навъҳои наёлҳои скелетӣ", fontsize=13.5,
             color=INK, weight="bold", pad=14)
plt.savefig("img19/shakli_4_1.png", dpi=200, facecolor=BG,
            bbox_inches="tight")
plt.close()

print("img19 ok: 5 PNG")
