# -*- coding: utf-8 -*-
"""Расмҳо барои кори курсӣ «Гардиши хуни гурда ва танзими он»."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import os

plt.rcParams["font.family"] = "DejaVu Sans"
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "img")
os.makedirs(OUT, exist_ok=True)

# ---- Шакли 2.1: СФ вобаста ба фишори миёна ----
map_ = np.linspace(50, 210, 500)
gfr = np.where(map_ < 80, 20 + (map_ - 50) * 3.4,
               np.where(map_ <= 180, 122 + (map_ - 80) * 0.06,
                        128 + (map_ - 180) * 2.6))
fig, ax = plt.subplots(figsize=(7.2, 3.9), dpi=200)
ax.plot(map_, gfr, color="#2f6f9f", linewidth=2.0)
ax.axvspan(80, 180, color="#dbe7f0", alpha=0.7, lw=0)
ax.text(130, 100, "Ҳудуди ауторегулятсия", fontsize=8.5, ha="center",
        color="#2f4a63")
ax.axhline(125, color="#8a9aab", linewidth=0.8, linestyle=":")
for xv, yv in [(80, 122), (100, 125), (140, 126), (180, 128)]:
    ax.plot([xv], [yv], "o", color="#123a56", markersize=5)
    ax.annotate("%d" % yv, (xv, yv), textcoords="offset points", xytext=(0, 8),
                ha="center", fontsize=8)
ax.set_xlabel("Фишори миёнаи артериявӣ, мм", fontsize=9)
ax.set_ylabel("Суръати филтрасия, мл/дақ", fontsize=9)
ax.set_xlim(50, 210)
ax.set_ylim(0, 220)
ax.grid(linestyle=":", linewidth=0.5, alpha=0.6)
ax.set_title("Вобастагии суръати филтрасия аз фишор", fontsize=10)
fig.tight_layout()
fig.savefig(os.path.join(OUT, "shakl_2_1.png"), bbox_inches="tight")
plt.close(fig)

# ---- Шакли 3.1: муқоисаи «пеш» ва «баъд» ----
labels = ["Ҳисоби\nдуруст, %", "Вақти\nтаҳлил, дақ.", "Парокандагӣ, ± %",
          "Пуррагӣ, %", "Хатогиҳо, адад"]
before = [62, 43, 13, 72, 19]
after = [91, 28, 4, 100, 3]
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
