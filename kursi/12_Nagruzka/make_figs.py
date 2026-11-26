# -*- coding: utf-8 -*-
"""Расмҳо барои кори курсӣ «Танзими гардиши хун ҳангоми кори ҷисмонӣ»."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import os

plt.rcParams["font.family"] = "DejaVu Sans"
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "img")
os.makedirs(OUT, exist_ok=True)

# ---- Шакли 2.1: ҳаҷми дақиқавӣ ва истеъмоли оксиген аз шиддат ----
w = np.linspace(0, 300, 300)
q = 5.0 + 0.043 * w + 0.00005 * w ** 2
vo2 = 250 + 9.6 * w + 0.0035 * w ** 2

fig, ax = plt.subplots(figsize=(7.2, 3.9), dpi=200)
ax.plot(w, q, color="#2f6f9f", linewidth=1.9, label="Ҳаҷми дақиқавӣ, л/дақ")
ax.set_xlabel("Қувваи корӣ, Вт", fontsize=9)
ax.set_ylabel("Ҳаҷми дақиқавӣ, л/дақ", fontsize=9, color="#2f6f9f")
ax.tick_params(axis="y", labelcolor="#2f6f9f")
ax.grid(linestyle=":", linewidth=0.5, alpha=0.6)

ax2 = ax.twinx()
ax2.plot(w, vo2, color="#c0504d", linewidth=1.7, linestyle="--",
         label="Истеъмоли оксиген, мл/дақ")
ax2.set_ylabel("Истеъмоли оксиген, мл/дақ", fontsize=9, color="#c0504d")
ax2.tick_params(axis="y", labelcolor="#c0504d")

pts = [0, 100, 200, 300]
ax.plot(pts, [5.0, 9.5, 14.0, 21.1], "o", color="#123a56", markersize=5)
lines = ax.get_lines()[:1] + ax2.get_lines()[:1]
ax.legend(lines, [l.get_label() for l in lines], fontsize=8.5, frameon=False,
          loc="upper left")
ax.set_title("Динамикаи нишондиҳандаҳо ҳангоми афзоиши шиддати кор", fontsize=10)
fig.tight_layout()
fig.savefig(os.path.join(OUT, "shakl_2_1.png"), bbox_inches="tight")
plt.close(fig)

# ---- Шакли 3.1: муқоисаи «пеш» ва «баъд» ----
labels = ["Ҳисоби\nдуруст, %", "Вақти\nтаҳлил, дақ.", "Парокандагӣ, ± %",
          "Пуррагӣ, %", "Хатогиҳо, адад"]
before = [64, 41, 12, 70, 18]
after = [91, 27, 4, 100, 3]
x = np.arange(len(labels))
wd = 0.36
fig, ax = plt.subplots(figsize=(7.2, 3.8), dpi=200)
b1 = ax.bar(x - wd / 2, before, wd, label="Ҳолати «пеш»", color="#b7c6d1",
            edgecolor="#22303c", linewidth=0.6)
b2 = ax.bar(x + wd / 2, after, wd, label="Ҳолати «баъд»", color="#2f6f9f",
            edgecolor="#22303c", linewidth=0.6)
for bars in (b1, b2):
    for rr in bars:
        ax.text(rr.get_x() + rr.get_width() / 2, rr.get_height() + 1.6,
                "%d" % rr.get_height(), ha="center", fontsize=8.5)
ax.set_xticks(x)
ax.set_xticklabels(labels, fontsize=8.5)
ax.set_ylabel("Қимат", fontsize=9)
ax.set_ylim(0, 118)
ax.grid(axis="y", linestyle=":", linewidth=0.5, alpha=0.6)
ax.legend(fontsize=8.5, frameon=False, loc="upper left")
ax.set_title("Муқоисаи нишондиҳандаҳо дар ду ҳолати кор", fontsize=10)
fig.tight_layout()
fig.savefig(os.path.join(OUT, "shakl_3_1.png"), bbox_inches="tight")
plt.close(fig)

print("OK")
