# -*- coding: utf-8 -*-
"""Расмҳо барои кори курсӣ «Гардиши хуни ҷигар ва танзими он»."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import os

plt.rcParams["font.family"] = "DejaVu Sans"
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "img")
os.makedirs(OUT, exist_ok=True)

# ---- Шакли 2.1: тақсими фишор дар гардиши ҷигар ----
fig, ax = plt.subplots(figsize=(7.2, 3.9), dpi=200)
ax.plot([0, 1], [90, 10], color="#2f6f9f", linewidth=2.4, label="Артерияи ҷигар")
ax.plot([1, 2], [10, 9], color="#c0504d", linewidth=2.4, linestyle="--",
        label="Венаи дарвоза")
ax.plot([2, 3], [9, 1], color="#4b7f52", linewidth=2.4, linestyle="-.",
        label="Синусоидҳо ва венаи ҷигар")
for xv, yv, tx in [(0, 90, "90"), (1, 10, "10"), (2, 9, "9"), (3, 1, "1")]:
    ax.plot([xv], [yv], "o", color="#123a56", markersize=5)
    ax.annotate(tx, (xv, yv), textcoords="offset points", xytext=(0, 9),
                ha="center", fontsize=8.5)
ax.set_xticks([0, 1, 2, 3])
ax.set_xticklabels(["Артерия", "Венаи дарвоза", "Синусоидҳо", "Венаи ҷигар"],
                   fontsize=8.5)
ax.set_ylabel("Фишор, мм", fontsize=9)
ax.set_ylim(0, 100)
ax.grid(linestyle=":", linewidth=0.5, alpha=0.6)
ax.legend(fontsize=8.5, frameon=False, loc="upper right")
ax.set_title("Тақсими фишор дар тӯли гардиши хуни ҷигар", fontsize=10)
fig.tight_layout()
fig.savefig(os.path.join(OUT, "shakl_2_1.png"), bbox_inches="tight")
plt.close(fig)

# ---- Шакли 3.1: муқоисаи «пеш» ва «баъд» ----
labels = ["Ҳисоби\nдуруст, %", "Вақти\nтаҳлил, дақ.", "Парокандагӣ, ± %",
          "Пуррагӣ, %", "Хатогиҳо, адад"]
before = [63, 42, 12, 71, 20]
after = [92, 27, 4, 100, 3]
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
