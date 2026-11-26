# -*- coding: utf-8 -*-
"""Расмҳо барои кори курсӣ «Мубодилаи моеъ байни капиллярҳо ва бофтаҳо»."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import os

plt.rcParams["font.family"] = "DejaVu Sans"
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "img")
os.makedirs(OUT, exist_ok=True)

# ---- Шакли 2.1: тавозуни холис дар тӯли капилляр ----
pos = np.arange(8)
share = [0, 14, 29, 43, 57, 71, 86, 100]
net = [13, 10, 7, 4, 1, -2, -5, -7]

fig, ax = plt.subplots(figsize=(7.2, 3.6), dpi=200)
colors = ["#2f6f9f" if v >= 0 else "#c0504d" for v in net]
ax.bar(pos, net, color=colors, width=0.62, edgecolor="#22303c", linewidth=0.6)
ax.axhline(0, color="#22303c", linewidth=1.0)
for x, v in zip(pos, net):
    ax.text(x, v + (0.6 if v >= 0 else -0.9), ("+%d" % v) if v >= 0 else str(v),
            ha="center", va="bottom" if v >= 0 else "top", fontsize=8.5)
ax.set_xticks(pos)
ax.set_xticklabels(["%d\n(%d %%)" % (i + 1, s) for i, s in enumerate(share)], fontsize=8)
ax.set_xlabel("Нуқтаи тӯли капилляр", fontsize=9)
ax.set_ylabel("Тавозуни холис, мм сим. сут.", fontsize=9)
ax.set_ylim(-11, 16)
ax.grid(axis="y", linestyle=":", linewidth=0.5, alpha=0.6)
ax.text(1.2, 12.2, "филтратсия", fontsize=9, color="#2f6f9f")
ax.text(5.6, -9.6, "реабсорбсия", fontsize=9, color="#c0504d")
ax.set_title("Тавозуни холис дар тӯли капилляр", fontsize=10)
fig.tight_layout()
fig.savefig(os.path.join(OUT, "shakl_2_1.png"), bbox_inches="tight")
plt.close(fig)

# ---- Шакли 3.1: муқоисаи «пеш» ва «баъд» ----
labels = ["Ҳисоби\nдуруст, %", "Вақти\nтаҳлил, дақ.", "Парокандагӣ, ± %", "Пуррагӣ, %"]
before = [58, 26, 9, 68]
after = [92, 17, 3, 100]

x = np.arange(len(labels))
w = 0.36
fig, ax = plt.subplots(figsize=(7.2, 3.6), dpi=200)
b1 = ax.bar(x - w / 2, before, w, label="Ҳолати «пеш»", color="#b7c6d1", edgecolor="#22303c", linewidth=0.6)
b2 = ax.bar(x + w / 2, after, w, label="Ҳолати «баъд»", color="#2f6f9f", edgecolor="#22303c", linewidth=0.6)
for bars in (b1, b2):
    for r in bars:
        ax.text(r.get_x() + r.get_width() / 2, r.get_height() + 1.5,
                "%d" % r.get_height(), ha="center", fontsize=8.5)
ax.set_xticks(x)
ax.set_xticklabels(labels, fontsize=8.5)
ax.set_ylabel("Қимат", fontsize=9)
ax.set_ylim(0, 132)
ax.grid(axis="y", linestyle=":", linewidth=0.5, alpha=0.6)
ax.legend(fontsize=8.5, frameon=False, loc="upper left")
ax.set_title("Муқоисаи нишондиҳандаҳои кор", fontsize=10)
fig.tight_layout()
fig.savefig(os.path.join(OUT, "shakl_3_1.png"), bbox_inches="tight")
plt.close(fig)

print("OK")
