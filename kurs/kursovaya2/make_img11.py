# -*- coding: utf-8 -*-
# Расмҳои М11 «Гликолиз ва цикли Кребс» — matplotlib, Agg, dpi=200
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

plt.rcParams["font.family"] = "DejaVu Sans"
INK, SLATE = "#1F2937", "#64748B"
TEAL, BLUE, AMBER, ROSE, GREEN = "#0F766E", "#1D4ED8", "#B45309", "#BE185D", "#15803D"

def box(ax, x, y, w, h, t, s, fc, ec, ts=10, ss=8.2):
    ax.add_patch(mpatches.FancyBboxPatch((x - w/2, y - h/2), w, h,
                 boxstyle="round,pad=0.03,rounding_size=0.1", fc=fc, ec=ec, lw=1.8))
    ax.text(x, y + h*0.14, t, ha="center", va="center", fontsize=ts, color=INK, weight="bold")
    ax.text(x, y - h*0.24, s, ha="center", va="center", fontsize=ss, color=SLATE)

def arrow(ax, x1, y1, x2, y2, c=SLATE):
    ax.annotate("", xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle="-|>", color=c, lw=1.8))

# ===== 1.1: Тартиби 10 қадами гликолиз (flowchart-и ду устун) =====
fig, ax = plt.subplots(figsize=(10.5, 6.6), dpi=200)
fig.patch.set_facecolor("#F7FAF8"); ax.set_facecolor("#F7FAF8")
ax.text(0.0, 7.45, "Тартиби даҳ қадами гликолиз", fontsize=14, ha="center",
        color=INK, weight="bold")
ax.text(-2.75, 6.75, "Марҳилаи тайёркунӣ (қадамҳои 1–5)", fontsize=10.5,
        ha="center", color=AMBER, weight="bold")
ax.text(2.75, 6.75, "Марҳилаи ҷамъбаст (қадамҳои 6–10)", fontsize=10.5,
        ha="center", color=BLUE, weight="bold")
s1 = [("Глюкоза", "–1 ATP  (қ.1)"),
      ("Глюкоза-6-фосфат", "изомераза  (қ.2)"),
      ("Фруктоза-6-фосфат", "–1 ATP  (қ.3, PFK-1)"),
      ("Фруктоза-1,6-дифосфат", "алдолаза  (қ.4)"),
      ("Г-3-Ф  × 2", "изомеразаи триоза  (қ.5)")]
s2 = [("1,3-Бифосфоглицерат ×2", "+2 NADH  (қ.6)"),
      ("3-Фосфоглицерат ×2", "+2 ATP  (қ.7)"),
      ("2-Фосфоглицерат ×2", "мутаза  (қ.8)"),
      ("Фосфоенолпируват ×2", "энолаза  (қ.9)"),
      ("Пируват ×2", "+2 ATP  (қ.10)")]
ys = [5.9, 4.55, 3.2, 1.85, 0.5]
for (t, s), y in zip(s1, ys):
    box(ax, -2.75, y, 4.5, 0.98, t, s, "#FEF6E7", AMBER, ts=9.6, ss=8.0)
    if y != ys[-1]:
        arrow(ax, -2.75, y - 0.49, -2.75, y - 0.96, AMBER)
for (t, s), y in zip(s2, ys):
    box(ax, 2.75, y, 4.5, 0.98, t, s, "#EEF4FB", BLUE, ts=9.6, ss=8.0)
    if y != ys[-1]:
        arrow(ax, 2.75, y - 0.49, 2.75, y - 0.96, BLUE)
arrow(ax, -0.48, 0.5, 0.48, 0.5, GREEN)
ax.text(0.0, 0.78, "× 2", fontsize=9.5, ha="center", color=GREEN, weight="bold")
ax.text(0.0, -0.65, "Ҳамагии соф: 2 ATP  +  2 NADH  аз  1 молекулаи глюкоза",
        ha="center", fontsize=11, color=INK, weight="bold")
ax.set_xlim(-5.6, 5.6); ax.set_ylim(-1.1, 7.8)
ax.axis("off")
plt.savefig("img11/shakli_1_1.png", dpi=200, facecolor="#F7FAF8", bbox_inches="tight")
plt.close()

# ===== 1.2: Комплекси ПДК =====
fig, ax = plt.subplots(figsize=(10.2, 5.6), dpi=200)
fig.patch.set_facecolor("#FBF8F4"); ax.set_facecolor("#FBF8F4")
ax.text(0.0, 3.15, "Комплекси пируватдегидрогеназа (ПДК)", fontsize=14,
        ha="center", color=INK, weight="bold")
ax.add_patch(mpatches.FancyBboxPatch((-3.4, -0.15), 6.8, 2.5,
             boxstyle="round,pad=0.05,rounding_size=0.15", fc="#E6F2EF", ec=TEAL, lw=2.2))
box(ax, -2.35, 1.15, 2.15, 1.0, "E1", "декарбоксилаза", "#F1F5F9", TEAL, ts=11, ss=7.6)
box(ax, 0.0, 1.15, 2.15, 1.0, "E2", "ацилтрансфераза", "#F1F5F9", TEAL, ts=11, ss=7.2)
box(ax, 2.35, 1.15, 2.15, 1.0, "E3", "дегидрогеназа", "#F1F5F9", TEAL, ts=11, ss=7.6)
arrow(ax, -1.28, 1.15, -1.06, 1.15, TEAL)
arrow(ax, 1.06, 1.15, 1.28, 1.15, TEAL)
box(ax, -5.15, 1.15, 2.6, 1.0, "Пируват", "аз цитоплазма", "#FDF0F5", ROSE, ts=10.5, ss=8.2)
arrow(ax, -3.82, 1.15, -3.1, 1.15, ROSE)
box(ax, 5.35, 2.0, 2.7, 0.85, "Ацетил-КоА", "ба даври Кребс", "#FEF6E7", AMBER, ts=10, ss=8.0)
box(ax, 5.35, 1.0, 2.7, 0.85, "CO2", "", "#F1F5F9", SLATE, ts=10, ss=8.0)
box(ax, 5.35, 0.0, 2.7, 0.85, "NADH", "2 молекула", "#EEF4FB", BLUE, ts=10, ss=8.0)
arrow(ax, 3.1, 1.5, 3.95, 2.0, AMBER)
arrow(ax, 3.1, 1.15, 3.95, 1.05, SLATE)
arrow(ax, 3.1, 0.85, 3.95, 0.1, BLUE)
box(ax, 0.0, -1.25, 8.6, 0.95, "Панҷ кофактар: TPP (B1), кислотаи липоевӣ, CoA (B5), FAD (B2), NAD (B3)",
    "Танзим: киназаи ПДК — маҳдудкунӣ; фосфатаза ва инсулин — фаъолкунӣ", "#FFF7ED", GREEN, ts=9.8, ss=8.6)
ax.text(0.0, -2.35, "Натиҷа: пируват + CoA + NAD → ацетил-КоА + CO2 + NADH",
        ha="center", fontsize=10.5, color=SLATE)
ax.set_xlim(-7.0, 7.1); ax.set_ylim(-2.8, 3.7)
ax.axis("off")
plt.savefig("img11/shakli_1_2.png", dpi=200, facecolor="#FBF8F4", bbox_inches="tight")
plt.close()

# ===== 2.1: Схемаи даврии даври Кребс =====
fig, ax = plt.subplots(figsize=(9.6, 8.2), dpi=200)
fig.patch.set_facecolor("#FBF8F4"); ax.set_facecolor("#FBF8F4")
ax.text(0.0, 4.9, "Даври Кребс (даври кислотаҳои трикарбонӣ)", fontsize=13.5,
        ha="center", color=INK, weight="bold")
import numpy as np
nodes = [
    ("Цитрат", AMBER, "#FEF6E7"),
    ("Изоцитрат", BLUE, "#EEF4FB"),
    ("α-Кетоглутарат", BLUE, "#EEF4FB"),
    ("Сукцинил-КоА", GREEN, "#F0FDF4"),
    ("Сукцинат", GREEN, "#F0FDF4"),
    ("Фумарат", ROSE, "#FDF0F5"),
    ("Малат", ROSE, "#FDF0F5"),
    ("Оксалоацетат", TEAL, "#E6F2EF"),
]
R = 3.05
pos = []
for i, (t, ec, fc) in enumerate(nodes):
    ang = np.pi/2 - i * 2*np.pi/8
    x, y = R*np.cos(ang)*1.25, R*np.sin(ang)*0.92
    pos.append((x, y))
    ax.add_patch(mpatches.FancyBboxPatch((x-1.05, y-0.42), 2.1, 0.84,
                 boxstyle="round,pad=0.03,rounding_size=0.08", fc=fc, ec=ec, lw=1.8))
    ax.text(x, y, t, ha="center", va="center", fontsize=9.2, color=INK, weight="bold")
for i in range(8):
    x1, y1 = pos[i]
    x2, y2 = pos[(i+1) % 8]
    dx, dy = x2-x1, y2-y1
    L = (dx**2 + dy**2) ** 0.5
    ax.annotate("", xy=(x2 - dx/L*1.15, y2 - dy/L*0.5), xytext=(x1 + dx/L*1.15, y1 + dy/L*0.5),
                arrowprops=dict(arrowstyle="-|>", color=SLATE, lw=1.7))
ax.text(0.0, 0.0, "Донаки\nмубодила", ha="center", fontsize=11.5, color=TEAL, weight="bold")
box(ax, 0.0, 3.85, 2.9, 0.85, "Ацетил-КоА", "аз комплекси ПДК", "#FFF7ED", AMBER, ts=10, ss=8.2)
arrow(ax, 0.0, 3.42, 0.0, 2.9, AMBER)
lab = ["(қ.1) –КоА", "(қ.2)", "(қ.3) NADH+CO2", "(қ.4) NADH+CO2",
       "(қ.5) GTP", "(қ.6) FADH2", "(қ.7) +H2O", "(қ.8) NADH"]
mid = []
for i in range(8):
    x1, y1 = pos[i]; x2, y2 = pos[(i+1) % 8]
    mid.append(((x1+x2)/2*1.16, (y1+y2)/2*1.3))
for (mx, my), t in zip(mid, lab):
    ax.text(mx, my, t, fontsize=8.0, ha="center", va="center", color=SLATE)
ax.text(0.0, -4.35, "Дар ҳар давр: 3 NADH + 1 FADH2 + 1 GTP + 2 CO2",
        ha="center", fontsize=11, color=INK, weight="bold")
ax.set_xlim(-4.9, 4.9); ax.set_ylim(-4.8, 4.6)
ax.axis("off")
plt.savefig("img11/shakli_2_1.png", dpi=200, facecolor="#FBF8F4", bbox_inches="tight")
plt.close()

# ===== 3.1: Муқоисаи ҳосили ATP =====
fig, ax = plt.subplots(figsize=(9.8, 5.2), dpi=200)
fig.patch.set_facecolor("#F7FAF8"); ax.set_facecolor("#F7FAF8")
cats = ["Анаэробӣ\n(бе оксиген)", "Гликолиз\n(соф ATP)", "ПДК\n(NADH)", "Кребс\n(GTP)",
        "Оксидшавии\nкоферментҳо", "Ҳамагии\nаэробӣ"]
vals = [2, 2, 5, 2, 23, 32]
cols = [SLATE, AMBER, ROSE, GREEN, BLUE, TEAL]
bars = ax.bar(cats, vals, color=cols, width=0.62, edgecolor="white")
for b, v in zip(bars, vals):
    ax.text(b.get_x() + b.get_width()/2, v + 0.6, str(v), ha="center",
            fontsize=11, color=INK, weight="bold")
ax.axhline(2, color=SLATE, ls="--", lw=1.2, alpha=0.6)
ax.text(4.62, 3.0, "сатҳи анаэробӣ: 2", fontsize=8.6, color=SLATE)
ax.set_ylim(0, 37)
ax.set_ylabel("Молекулаи ATP аз 1 глюкоза", fontsize=10, color=INK)
ax.set_title("Ҳосили энергиядории роҳҳои мубодилаи глюкоза", fontsize=13.5,
             color=INK, weight="bold", pad=12)
ax.tick_params(axis="x", labelsize=8.6)
ax.grid(axis="y", alpha=0.25)
ax.set_axisbelow(True)
plt.savefig("img11/shakli_3_1.png", dpi=200, facecolor="#F7FAF8", bbox_inches="tight")
plt.close()
print("img11 ok: 4 PNG")
