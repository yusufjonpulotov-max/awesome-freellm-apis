import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import os

os.makedirs("kursi/01_Hajmi-zarbavi/img", exist_ok=True)

plt.rcParams["font.family"] = "DejaVu Sans"

# Шакли 2.1 — дақиқавии дил дар чор ҳолат
holat = ["Оромӣ", "Машқи\nмӯътадил", "Ортостаз", "Машқ дар\n65-солагӣ"]
qiymat = [5.6, 14.7, 6.1, 9.2]

fig, ax = plt.subplots(figsize=(7.0, 4.2), dpi=200)
bars = ax.bar(holat, qiymat, color=["#4a7ba7", "#a34a4a", "#6d8b74", "#9a8a56"], width=0.55)
for b, v in zip(bars, qiymat):
    ax.text(b.get_x() + b.get_width() / 2, v + 0.25, f"{v:.1f}", ha="center", va="bottom", fontsize=11)
ax.set_ylabel("Дақиқавии дил, л/мин", fontsize=11)
ax.set_ylim(0, 17)
ax.axhline(5.6, color="grey", linestyle="--", linewidth=1)
ax.text(0.42, 5.9, "сатҳи оромӣ", fontsize=9, color="grey", ha="left")
ax.spines[["top", "right"]].set_visible(False)
ax.tick_params(labelsize=10)
fig.tight_layout()
fig.savefig("kursi/01_Hajmi-zarbavi/img/shakl_2_1.png")
plt.close(fig)

# Шакли 3.1 — муқоисаи пеш ва баъд
mezon = ["Ҳиссаи\nхатоҳо, %", "Вақти\nченкунӣ, дақ.", "Парокандагӣ,\n± %", "Пуррагии\nварақа, %"]
peh = [33, 23, 9, 62]
bad = [8, 16, 4, 100]

import numpy as np
x = np.arange(len(mezon))
fig, ax = plt.subplots(figsize=(7.0, 4.2), dpi=200)
b1 = ax.bar(x - 0.2, peh, width=0.38, label="Пеш", color="#a34a4a")
b2 = ax.bar(x + 0.2, bad, width=0.38, label="Баъд", color="#4a7ba7")
for bs in (b1, b2):
    for b in bs:
        ax.text(b.get_x() + b.get_width() / 2, b.get_height() + 1.5, f"{int(b.get_height())}",
                ha="center", va="bottom", fontsize=10)
ax.set_xticks(x)
ax.set_xticklabels(mezon, fontsize=10)
ax.set_ylabel("Қимат", fontsize=11)
ax.set_ylim(0, 115)
ax.legend(fontsize=10, frameon=False, loc="upper left")
ax.spines[["top", "right"]].set_visible(False)
fig.tight_layout()
fig.savefig("kursi/01_Hajmi-zarbavi/img/shakl_3_1.png")
plt.close(fig)
print("figures ok")
