# -*- coding: utf-8 -*-
"""Расмҳо барои кори курсӣ «Гардиши хуни пӯст ва танзими ҳарорати бадан»."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import os

plt.rcParams["font.family"] = "DejaVu Sans"
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "img")
os.makedirs(OUT, exist_ok=True)

# ---- Шакли 2.1: ҷараёни пӯст аз ҳарорати муҳит ----
t = np.linspace(5, 40, 400)
q = 50 + 3.0 * (t - 5) ** 1.9
fig, ax = plt.subplots(figsize=(7.2, 3.9), dpi=200)
ax.plot(t, q, color="#2f6f9f", linewidth=2.0)
ax.axvspan(20, 30, color="#dbe7f0", alpha=0.8, lw=0)
ax.text(25, 2500, "Ҳудуди\nмуътадил", fontsize=8.5, ha="center", color="#2f4a63")
for xv, yv in [(5, 50), (15, 150), (22, 250), (32, 1500), (38, 3000)]:
    ax.plot([xv], [yv], "o", color="#123a56", markersize=5)
    ax.annotate("%d" % yv, (xv, yv), textcoords="offset points", xytext=(0, 8),
                ha="center", fontsize=8)
ax.set_xlabel("Ҳарорати муҳит, °С", fontsize=9)
ax.set_ylabel("Ҷараёни пӯст, мл/дақ", fontsize=9)
ax.set_xlim(5, 40)
ax.set_ylim(0, 3400)
ax.grid(linestyle=":", linewidth=0.5, alpha=0.6)
ax.set_title("Ҷараёни хуни пӯст вобаста ба ҳарорати муҳит", fontsize=10)
fig.tight_layout()
fig.savefig(os.path.join(OUT, "shakl_2_1.png"), bbox_inches="tight")
plt.close(fig)

# ---- Шакли 3.1: муқоисаи «пеш» ва «баъд» ----
labels = ["Ҳисоби\nдуруст, %", "Вақти\nтаҳлил, дақ.", "Парокандагӣ, ± %",
          "Пуррагӣ, %", "Хатогиҳо, адад"]
before = [61, 44, 14, 69, 22]
after = [90, 30, 4, 100, 3]
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
