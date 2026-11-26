# -*- coding: utf-8 -*-
"""Расмҳо барои кори курсӣ «Танзими гуморалии гардиши хун»."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import os

plt.rcParams["font.family"] = "DejaVu Sans"
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "img")
os.makedirs(OUT, exist_ok=True)

# ---- Шакли 2.1: доза-таъсири адреналин ----
d = np.linspace(0, 0.5, 400)
map_ = 90 - 12 * np.exp(-((d - 0.03) ** 2) / (2 * 0.025 ** 2)) + 95 * d ** 1.6
res = 100 - 30 * np.exp(-((d - 0.03) ** 2) / (2 * 0.03 ** 2)) + 190 * d ** 1.8

pts_d = [0, 0.02, 0.05, 0.10, 0.20, 0.50]
pts_map = [90, 86, 90, 100, 116, 132]

fig, ax = plt.subplots(figsize=(7.2, 3.9), dpi=200)
ax.plot(d, map_, color="#2f6f9f", linewidth=1.9, label="Фишори миёна, мм")
ax.plot(d, res, color="#c0504d", linewidth=1.7, linestyle="--",
        label="Муқовимат, %")
ax.plot(pts_d, pts_map, "o", color="#2f6f9f", markersize=5)
ax.set_xlabel("Миқдори адреналин, мкг/кг/дақ.", fontsize=9)
ax.set_ylabel("Қимат", fontsize=9)
ax.grid(linestyle=":", linewidth=0.5, alpha=0.6)
ax.legend(fontsize=8.5, frameon=False, loc="upper left")
ax.set_title("Таъсири адреналин вобаста ба миқдор", fontsize=10)
fig.tight_layout()
fig.savefig(os.path.join(OUT, "shakl_2_1.png"), bbox_inches="tight")
plt.close(fig)

# ---- Шакли 3.1: муқоисаи «пеш» ва «баъд» ----
labels = ["Ҳисоби\nдуруст, %", "Вақти\nтаҳлил, дақ.", "Парокандагӣ, ± %", "Пуррагӣ, %"]
before = [61, 33, 13, 67]
after = [89, 21, 4, 100]
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
