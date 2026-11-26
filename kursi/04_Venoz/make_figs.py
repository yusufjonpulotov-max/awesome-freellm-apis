import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["font.family"] = "DejaVu Sans"
OUT = "kursi/04_Venoz/img/"
os.makedirs(OUT, exist_ok=True)

# Шакли 2.1 — хати бозгашти венагӣ (қонуни Гайтон)
pra = [0, 1, 2, 3, 4, 5, 6, 7]
vr_norm = [7.0, 6.0, 5.0, 4.0, 3.0, 2.0, 1.0, 0.0]
vr_high = [9.0, 8.0, 7.0, 6.0, 5.0, 4.0, 3.0, 2.0]
vr_low = [4.0, 3.0, 2.0, 1.0, 0.0, 0.0, 0.0, 0.0]

fig, ax = plt.subplots(figsize=(7.0, 4.4), dpi=200)
ax.plot(pra, vr_norm, marker="o", color="#2f6f9f", linewidth=2,
        label="Ҳолати меъёрӣ (ФМС = 7 мм)")
ax.plot(pra, vr_high, marker="s", color="#3f8f5f", linewidth=2, linestyle="--",
        label="Ҳаҷми зиёд (ФМС = 9 мм)")
ax.plot(pra, vr_low, marker="^", color="#a34a4a", linewidth=2, linestyle=":",
        label="Ҳаҷми кам (ФМС = 4 мм)")
ax.axvline(2, color="#8a8a8a", linestyle=":", linewidth=1.2)
ax.annotate("нуқтаи корӣ\nФҲД = 2 мм", xy=(2, 5), xytext=(3.1, 6.3), fontsize=9,
            arrowprops=dict(arrowstyle="->", color="#8a8a8a", lw=1))
ax.set_xlabel("Фишори ҳуҷраи рост (ФҲД), мм сим. сут.", fontsize=11)
ax.set_ylabel("Бозгашти венагӣ, л/дақ.", fontsize=11)
ax.set_xlim(-0.4, 9.2)
ax.set_ylim(-0.6, 9.6)
ax.grid(alpha=0.25, linestyle=":")
ax.legend(fontsize=9, frameon=False, loc="upper right")
ax.spines[["top", "right"]].set_visible(False)
fig.tight_layout()
fig.savefig(OUT + "shakl_2_1.png")
plt.close(fig)

# Шакли 3.1 — муқоисаи ҳолати «пеш» ва «баъд»
mezon = ["Ҳисобҳои\nдуруст, %", "Вақти\nтаҳлил, дақ.", "Парокандагӣ,\n± %", "Пуррагии\nварақа, %"]
before = [60, 24, 8, 70]
after = [93, 16, 3, 100]
x = np.arange(len(mezon))
fig, ax = plt.subplots(figsize=(7.0, 4.2), dpi=200)
b1 = ax.bar(x - 0.2, before, width=0.38, label="Пеш", color="#a34a4a")
b2 = ax.bar(x + 0.2, after, width=0.38, label="Баъд", color="#2f6f9f")
for bs in (b1, b2):
    for b in bs:
        ax.text(b.get_x() + b.get_width() / 2, b.get_height() + 1.5, f"{int(b.get_height())}",
                ha="center", fontsize=9)
ax.set_xticks(x)
ax.set_xticklabels(mezon, fontsize=9.5)
ax.set_ylabel("Қимат", fontsize=11)
ax.set_ylim(0, 115)
ax.grid(axis="y", alpha=0.25, linestyle=":")
ax.legend(fontsize=10, frameon=False, loc="upper right")
ax.spines[["top", "right"]].set_visible(False)
fig.tight_layout()
fig.savefig(OUT + "shakl_3_1.png")
plt.close(fig)

print("OK")
