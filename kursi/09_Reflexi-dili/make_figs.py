# -*- coding: utf-8 -*-
"""Расмҳо барои кори курсӣ «Рефлексҳои дилӣ»."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import os

plt.rcParams["font.family"] = "DejaVu Sans"
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "img")
os.makedirs(OUT, exist_ok=True)

# ---- Шакли 2.1: набз вобаста ба ҳаҷми хун ----
v = np.linspace(0, 35, 300)
hr = 68 + 16 * (1 - np.exp(-0.15 * v))
pts_v = [0, 5, 10, 15, 20, 25, 30, 35]
pts_hr = [68, 74, 80, 84, 86, 87, 88, 88]

fig, ax = plt.subplots(figsize=(7.2, 3.8), dpi=200)
ax.plot(v, hr, color="#2f6f9f", linewidth=1.9, label="Модели ҳисобшуда")
ax.plot(pts_v, pts_hr, "o", color="#c0504d", markersize=5,
        label="Нуқтаҳои ҷадвали 2.1")
ax.set_xlabel("Тағйири ҳаҷми хун, %", fontsize=9)
ax.set_ylabel("Набз, зарба/дақ.", fontsize=9)
ax.set_ylim(60, 92)
ax.grid(linestyle=":", linewidth=0.5, alpha=0.6)
ax.legend(fontsize=8.5, frameon=False, loc="lower right")
ax.set_title("Таъсири пуршавии атриумҳо ба набз", fontsize=10)
fig.tight_layout()
fig.savefig(os.path.join(OUT, "shakl_2_1.png"), bbox_inches="tight")
plt.close(fig)

# ---- Шакли 3.1: муқоисаи «пеш» ва «баъд» ----
labels = ["Ҳисоби\nдуруст, %", "Вақти\nтаҳлил, дақ.", "Парокандагӣ, ± %", "Пуррагӣ, %"]
before = [66, 31, 10, 71]
after = [92, 21, 3, 100]
x = np.arange(len(labels))
w = 0.36
fig, ax = plt.subplots(figsize=(7.2, 3.8), dpi=200)
b1 = ax.bar(x - w / 2, before, w, label="Ҳолати «пеш»", color="#b7c6d1",
            edgecolor="#22303c", linewidth=0.6)
b2 = ax.bar(x + w / 2, after, w, label="Ҳолати «баъд»", color="#2f6f9f",
            edgecolor="#22303c", linewidth=0.6)
for bars in (b1, b2):
    for rr in bars:
        ax.text(rr.get_x() + rr.get_width() / 2, rr.get_height() + 1.5,
                "%d" % rr.get_height(), ha="center", fontsize=8.5)
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
