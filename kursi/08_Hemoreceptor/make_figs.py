# -*- coding: utf-8 -*-
"""Расмҳо барои кори курсӣ «Рефлексҳои хеморесепторӣ»."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import os

plt.rcParams["font.family"] = "DejaVu Sans"
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "img")
os.makedirs(OUT, exist_ok=True)

# ---- Шакли 2.1: вентилятсия вобаста ба CO₂ ----
pco2 = np.linspace(25, 58, 300)
ve_norm = 3.0 + 0.35 * np.exp(0.075 * (pco2 - 40)) * 7.0
ve_low = ve_norm * (1 + 0.42 * np.exp(-((pco2 - 40) ** 2) / 900))

fig, ax = plt.subplots(figsize=(7.2, 3.8), dpi=200)
ax.plot(pco2, ve_norm, color="#2f6f9f", linewidth=1.9, label="PaO₂ 100 мм")
ax.plot(pco2, ve_low, color="#c0504d", linewidth=1.9, linestyle="--",
        label="PaO₂ 60 мм")
ax.axvline(40, color="#7a8794", linewidth=0.9, linestyle=":")
ax.axhline(7.0, color="#7a8794", linewidth=0.9, linestyle=":")
ax.annotate("меъёр", xy=(40, 7.0), xytext=(30, 14),
            fontsize=8.5, arrowprops=dict(arrowstyle="->", color="#7a8794"))
ax.set_xlabel("PaCO₂, мм сим. сут.", fontsize=9)
ax.set_ylabel("Вентилятсия, л/дақ.", fontsize=9)
ax.set_ylim(0, 30)
ax.grid(linestyle=":", linewidth=0.5, alpha=0.6)
ax.legend(fontsize=8.5, frameon=False, loc="upper left")
ax.set_title("Вентилятсияи шуш вобаста ба CO₂ ва оксиген", fontsize=10)
fig.tight_layout()
fig.savefig(os.path.join(OUT, "shakl_2_1.png"), bbox_inches="tight")
plt.close(fig)

# ---- Шакли 3.1: муқоисаи «пеш» ва «баъд» ----
labels = ["Ҳисоби\nдуруст, %", "Вақти\nтаҳлил, дақ.", "Парокандагӣ, ± %", "Пуррагӣ, %"]
before = [64, 32, 11, 68]
after = [91, 20, 4, 100]
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
