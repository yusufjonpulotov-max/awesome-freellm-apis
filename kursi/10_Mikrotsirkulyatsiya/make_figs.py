# -*- coding: utf-8 -*-
"""Расмҳо барои кори курсӣ «Микроциркуляция»."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import os

plt.rcParams["font.family"] = "DejaVu Sans"
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "img")
os.makedirs(OUT, exist_ok=True)

# ---- Шакли 2.1: авторегулятсияи ҷараён ----
p = np.linspace(50, 190, 400)
flat = 50.0
low = flat * (1 - np.exp(-((p - 50) / 26.0)))
high = flat + 0.06 * np.maximum(p - 160, 0) ** 1.25
flow = np.where(p < 80, np.maximum(low, 20), np.where(p <= 160, flat, high))

pts_p = [60, 80, 100, 120, 140, 160, 180]
pts_f = [38, 48, 50, 50, 51, 52, 58]

fig, ax = plt.subplots(figsize=(7.2, 3.8), dpi=200)
ax.plot(p, flow, color="#2f6f9f", linewidth=1.9, label="Модели ҳисобшуда")
ax.plot(pts_p, pts_f, "o", color="#c0504d", markersize=5,
        label="Нуқтаҳои ҷадвали 2.1")
ax.axvspan(80, 160, color="#2f6f9f", alpha=0.07)
ax.set_xlabel("Фишори шарёнӣ, мм сим. сут.", fontsize=9)
ax.set_ylabel("Ҷараён, мл/100 г/дақ.", fontsize=9)
ax.set_ylim(20, 75)
ax.grid(linestyle=":", linewidth=0.5, alpha=0.6)
ax.legend(fontsize=8.5, frameon=False, loc="upper left")
ax.set_title("Авторегулятсияи ҷараёни хун дар микроциркуляция", fontsize=10)
fig.tight_layout()
fig.savefig(os.path.join(OUT, "shakl_2_1.png"), bbox_inches="tight")
plt.close(fig)

# ---- Шакли 3.1: муқоисаи «пеш» ва «баъд» ----
labels = ["Ҳисоби\nдуруст, %", "Вақти\nтаҳлил, дақ.", "Парокандагӣ, ± %", "Пуррагӣ, %"]
before = [63, 34, 12, 69]
after = [90, 22, 4, 100]
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
