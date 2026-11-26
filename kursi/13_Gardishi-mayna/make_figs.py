# -*- coding: utf-8 -*-
"""Расмҳо барои кори курсӣ «Гардиши хуни майна ва танзими он»."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import os

plt.rcParams["font.family"] = "DejaVu Sans"
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "img")
os.makedirs(OUT, exist_ok=True)

# ---- Шакли 2.1: қайчии ауторегулятсия ----
map_ = np.linspace(30, 200, 500)
cbf = np.where(map_ < 60, 25 + (map_ - 30) * 0.833,
               np.where(map_ <= 150, 50 + (map_ - 60) * 0.045,
                        56 + (map_ - 150) * 0.58))

fig, ax = plt.subplots(figsize=(7.2, 3.9), dpi=200)
ax.plot(map_, cbf, color="#2f6f9f", linewidth=2.0)
ax.axvspan(60, 150, color="#dbe7f0", alpha=0.7, lw=0)
ax.axhline(50, color="#8a9aab", linewidth=0.8, linestyle=":")
ax.text(105, 46, "Ҳудуди ауторегулятсия", fontsize=8.5, ha="center",
        color="#2f4a63")
ax.plot([60, 90, 120, 150], [50, 52, 54, 56], "o", color="#123a56", markersize=5)
for xv, yv in [(60, 50), (90, 52), (120, 54), (150, 56)]:
    ax.annotate("%d" % yv, (xv, yv), textcoords="offset points", xytext=(0, 8),
                ha="center", fontsize=8)
ax.set_xlabel("Фишори миёнаи артериявӣ, мм", fontsize=9)
ax.set_ylabel("Ҷараён, мл/100 г/дақ", fontsize=9)
ax.set_xlim(30, 200)
ax.set_ylim(0, 100)
ax.grid(linestyle=":", linewidth=0.5, alpha=0.6)
ax.set_title("Қайчии ауторегулятсияи гардиши хуни майна", fontsize=10)
fig.tight_layout()
fig.savefig(os.path.join(OUT, "shakl_2_1.png"), bbox_inches="tight")
plt.close(fig)

# ---- Шакли 3.1: муқоисаи «пеш» ва «баъд» ----
labels = ["Ҳисоби\nдуруст, %", "Вақти\nтаҳлил, дақ.", "Парокандагӣ, ± %",
          "Пуррагӣ, %", "Хатогиҳо, адад"]
before = [60, 45, 14, 68, 21]
after = [90, 29, 4, 100, 3]
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
ax.set_ylim(0, 116)
ax.grid(axis="y", linestyle=":", linewidth=0.5, alpha=0.6)
ax.legend(fontsize=8.5, frameon=False, loc="upper left")
ax.set_title("Муқоисаи нишондиҳандаҳо дар ду ҳолати кор", fontsize=10)
fig.tight_layout()
fig.savefig(os.path.join(OUT, "shakl_3_1.png"), bbox_inches="tight")
plt.close(fig)

print("OK")
