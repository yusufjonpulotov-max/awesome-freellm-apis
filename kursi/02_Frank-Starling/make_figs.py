import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["font.family"] = "DejaVu Sans"
OUT = "kursi/02_Frank-Starling/img/"

# Шакли 2.1 — қонуни Франк–Старлинг: ҲЗ вобаста ба ҲОД
edv = [90, 100, 110, 120, 130, 140, 150, 160]
sv_norm = [55, 65, 75, 85, 92, 97, 99, 97]
sv_hf = [45, 50, 55, 58, 60, 61, 61, 59]

fig, ax = plt.subplots(figsize=(7.0, 4.4), dpi=200)
ax.plot(edv, sv_norm, marker="o", color="#2f6f9f", linewidth=2, label="Дили солим")
ax.plot(edv, sv_hf, marker="s", color="#a34a4a", linewidth=2, linestyle="--", label="Иллати дил")
ax.axvspan(115, 140, color="#2f6f9f", alpha=0.07)
ax.text(127, 52, "ҳудуди муфид", fontsize=9, color="#2f6f9f", ha="center")
ax.set_xlabel("Ҳаҷми охири диастолӣ (ҲОД), мл", fontsize=11)
ax.set_ylabel("Ҳаҷми зарбавӣ (ҲЗ), мл", fontsize=11)
ax.set_xlim(85, 165)
ax.set_ylim(30, 110)
ax.grid(alpha=0.25, linestyle=":")
ax.legend(fontsize=10, frameon=False, loc="lower right")
ax.spines[["top", "right"]].set_visible(False)
fig.tight_layout()
fig.savefig(OUT + "shakl_2_1.png")
plt.close(fig)

# Шакли 3.1 — муқоисаи пеш ва баъд
mezon = ["Ҳисобҳои\nдуруст, %", "Вақти таҳлил,\nдақ.", "Парокандагӣ,\n± %", "Пуррагии\nҷадвал, %"]
before = [62, 25, 8, 70]
after = [94, 17, 3, 100]
x = np.arange(len(mezon))
fig, ax = plt.subplots(figsize=(7.0, 4.2), dpi=200)
b1 = ax.bar(x - 0.2, before, width=0.38, label="Пеш", color="#a34a4a")
b2 = ax.bar(x + 0.2, after, width=0.38, label="Баъд", color="#2f6f9f")
for bs in (b1, b2):
    for b in bs:
        ax.text(b.get_x() + b.get_width() / 2, b.get_height() + 1.5, f"{int(b.get_height())}",
                ha="center", va="bottom", fontsize=10)
ax.set_xticks(x)
ax.set_xticklabels(mezon, fontsize=10)
ax.set_ylabel("Қимат", fontsize=11)
ax.set_ylim(0, 115)
ax.legend(fontsize=10, frameon=False)
ax.spines[["top", "right"]].set_visible(False)
fig.tight_layout()
fig.savefig(OUT + "shakl_3_1.png")
plt.close(fig)
print("ok")
