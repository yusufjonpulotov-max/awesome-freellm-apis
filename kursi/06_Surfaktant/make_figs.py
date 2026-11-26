# -*- coding: utf-8 -*-
"""Расмҳо барои кори курсӣ «Сурфактанти шуш»."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import os

plt.rcParams["font.family"] = "DejaVu Sans"
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "img")
os.makedirs(OUT, exist_ok=True)

# ---- Шакли 2.1: фишор вобаста ба радиус ----
r = np.array([40, 50, 60, 70, 80, 100, 110, 120], dtype=float)  # мкм
p_no = 2 * 50 / (r * 1e-4) / 980          # см сутуни об, T = 50 доимӣ
t_sur = np.array([8, 10, 13, 17, 22, 32, 37, 42], dtype=float)
p_sur = 2 * t_sur / (r * 1e-4) / 980

fig, ax = plt.subplots(figsize=(7.2, 3.7), dpi=200)
ax.plot(r, p_no, marker="o", color="#c0504d", linewidth=1.8, markersize=4.5,
        label="Бе сурфактант (T = 50 доимӣ)")
ax.plot(r, p_sur, marker="s", color="#2f6f9f", linewidth=1.8, markersize=4.5,
        label="Бо сурфактант (T тағйирёбанда)")
ax.set_xlabel("Радиуси алвеола, мкм", fontsize=9)
ax.set_ylabel("Фишори алвеолӣ, см сутуни об", fontsize=9)
ax.grid(linestyle=":", linewidth=0.5, alpha=0.6)
ax.legend(fontsize=8, frameon=False, loc="upper right")
ax.set_title("Вобастагии фишори алвеолӣ аз радиус", fontsize=10)
ax.set_ylim(0, 28)
fig.tight_layout()
fig.savefig(os.path.join(OUT, "shakl_2_1.png"), bbox_inches="tight")
plt.close(fig)

# ---- Шакли 3.1: муқоисаи «пеш» ва «баъд» ----
labels = ["Ҳисоби\nдуруст, %", "Вақти\nтаҳлил, дақ.", "Парокандагӣ, ± %", "Пуррагӣ, %"]
before = [58, 25, 8, 72]
after = [92, 17, 3, 100]
x = np.arange(len(labels))
w = 0.36
fig, ax = plt.subplots(figsize=(7.2, 3.7), dpi=200)
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
