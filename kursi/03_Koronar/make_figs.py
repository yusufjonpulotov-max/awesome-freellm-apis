import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["font.family"] = "DejaVu Sans"
OUT = "kursi/03_Koronar/img/"
os.makedirs(OUT, exist_ok=True)

# Шакли 2.1 — авторегулятсияи ҷараёни хуни коронарӣ
map_ = [40, 50, 60, 80, 100, 120, 140, 160, 180]
flow = [26, 41, 55, 61, 64, 65, 64, 70, 88]

fig, ax = plt.subplots(figsize=(7.0, 4.4), dpi=200)
ax.plot(map_, flow, marker="o", color="#2f6f9f", linewidth=2, label="Ҷараён")
ax.axvspan(60, 140, color="#2f6f9f", alpha=0.08)
ax.text(100, 30, "ҳудуди авторегулятсия", fontsize=9, color="#2f6f9f", ha="center")
ax.axvline(60, color="#8a8a8a", linestyle=":", linewidth=1.2)
ax.axvline(140, color="#8a8a8a", linestyle=":", linewidth=1.2)
ax.annotate("нуқтаи поёнӣ\n60 мм", xy=(60, 55), xytext=(48, 76), fontsize=9,
            arrowprops=dict(arrowstyle="->", color="#8a8a8a", lw=1))
ax.annotate("нуқтаи болоӣ\n140 мм", xy=(140, 64), xytext=(146, 44), fontsize=9,
            arrowprops=dict(arrowstyle="->", color="#8a8a8a", lw=1))
ax.set_xlabel("Фишори миёнаи шарёнӣ, мм сим. сут.", fontsize=11)
ax.set_ylabel("Ҷараёни хун, мл/дақ. ба 100 г", fontsize=11)
ax.set_xlim(35, 185)
ax.set_ylim(15, 100)
ax.grid(alpha=0.25, linestyle=":")
ax.spines[["top", "right"]].set_visible(False)
fig.tight_layout()
fig.savefig(OUT + "shakl_2_1.png")
plt.close(fig)

# Шакли 3.1 — муқоисаи ҳолати «пеш» ва «баъд»
mezon = ["Ҳисобҳои\nдуруст, %", "Вақти\nтаҳлил, дақ.", "Парокандагӣ,\n± %", "Пуррагии\nварақа, %"]
before = [58, 22, 9, 65]
after = [92, 15, 4, 100]
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
