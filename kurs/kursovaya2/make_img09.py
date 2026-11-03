import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

plt.rcParams["font.family"] = "DejaVu Sans"
TEAL = "#0F766E"; ROSE = "#B91C5C"; AMBER = "#B45309"; SLATE = "#475569"
INK = "#1E293B"

# ===== 1.1: Ҳаворт — α-D-глюкопираноза бо карбони аномерӣ =====
fig, ax = plt.subplots(figsize=(8.8, 6.0), dpi=200)
fig.patch.set_facecolor("#F7FAF8"); ax.set_facecolor("#F7FAF8")
V = {"C1": (1.05, 0.45), "C2": (0.55, -0.42), "C3": (-0.55, -0.42),
     "C4": (-1.05, 0.45), "C5": (-0.55, 1.32), "O": (0.55, 1.32)}
ring = ["C1", "C2", "C3", "C4", "C5", "O", "C1"]
for a, b in zip(ring[:-1], ring[1:]):
    x1, y1 = V[a]; x2, y2 = V[b]
    if "O" in (a, b):
        ax.plot([x1, x2], [y1, y2], color=ROSE, lw=2.6)
    else:
        ax.plot([x1, x2], [y1, y2], color=INK, lw=2.4)
ax.plot(*V["O"], "o", ms=15, color="#FCE7F3", mec=ROSE, mew=1.6, zorder=5)
ax.text(V["O"][0], V["O"][1], "O", ha="center", va="center", fontsize=13, color=ROSE, zorder=6)
for k in ("C1", "C2", "C3", "C4", "C5"):
    x, y = V[k]
    ax.text(x * 1.14, y * 1.06, k, ha="center", va="center", fontsize=11, color=SLATE)
ax.add_patch(mpatches.Circle(V["C1"], 0.24, fill=False, ec=ROSE, lw=2.0, ls="--", zorder=4))
def bond(p, dx, dy, color=INK, lw=2.0):
    x, y = V[p] if isinstance(p, str) else p
    ax.plot([x, x + dx], [y, y + dy], color=color, lw=lw)
bond("C1", 0.42, -0.30, AMBER); ax.text(1.72, 0.02, "OH", fontsize=12, color=AMBER, ha="center", va="center")
bond("C1", 0.10, 0.46); ax.text(1.30, 1.02, "H", fontsize=10, color=SLATE, ha="center")
bond("C2", 0.0, -0.48, AMBER); ax.text(0.55, -1.08, "OH", fontsize=12, color=AMBER, ha="center")
bond("C3", -0.48, 0.24, AMBER); ax.text(-1.22, 0.82, "OH", fontsize=12, color=AMBER, ha="center")
bond("C4", 0.0, -0.48, AMBER); ax.text(-1.05, -0.92, "OH", fontsize=12, color=AMBER, ha="center")
bond("C5", -0.06, 0.50, TEAL); ax.text(-0.72, 2.02, r"CH$_2$OH", fontsize=12, color=TEAL, ha="center")
ax.annotate("карбони аномерӣ (C1)\nOH-и α ба поён", xy=(1.30, 0.62), xytext=(2.35, 1.60),
            fontsize=10.5, color=ROSE, ha="left",
            arrowprops=dict(arrowstyle="->", color=ROSE, lw=1.6))
ax.text(0.0, 2.62, "Ҳаворт: α-D-глюкопираноза", fontsize=13.5, color=INK,
        ha="center", weight="bold")
ax.text(0.0, -1.62, "О-глюкозидӣ: пайвасти C1–O дар байни ду ҳалқа",
        fontsize=10, color=SLATE, ha="center")
ax.set_xlim(-2.0, 4.6); ax.set_ylim(-1.9, 3.0)
ax.set_aspect("equal"); ax.axis("off")
plt.savefig("img09/shakli_1_1.png", dpi=200, facecolor="#F7FAF8", bbox_inches="tight")
plt.close()

# ===== 1.2: Дарахти таснифоти карбогидратҳо =====
fig, ax = plt.subplots(figsize=(9.2, 5.6), dpi=200)
fig.patch.set_facecolor("#FBF8F4"); ax.set_facecolor("#FBF8F4")
def box(x, y, w, h, title, sub, fc, ec):
    ax.add_patch(mpatches.FancyBboxPatch((x - w/2, y - h/2), w, h,
                 boxstyle="round,pad=0.02,rounding_size=0.06",
                 fc=fc, ec=ec, lw=1.8))
    ax.text(x, y + 0.13, title, ha="center", va="center", fontsize=11, color=INK, weight="bold")
    ax.text(x, y - 0.19, sub, ha="center", va="center", fontsize=9, color=SLATE)
box(0.0, 2.35, 3.6, 0.78, "КАРБОГИДРАТҲО", "C, H, O — формулаи умумии (CH₂O)n", "#E6F2EF", TEAL)
cols = [
    (-3.35, "Моносахаридҳо", "глюкоза, фруктоза,\nгалактоза, рибоза", "#FDF0F5", ROSE),
    (-1.10, "Дисахаридҳо", "сахароза, лактоза,\nмалтоза, изомалтоза", "#FEF6E7", AMBER),
    (1.18, "Полисахаридҳо", "нишондод, гликоген,\nцеллюлоза, файб", "#EEF4FB", "#1D4ED8"),
    (3.40, "Гликоконҷюғатҳо", "гликопротеин,\nгликолипид", "#F1F5F9", SLATE),
]
for x, t, s, fc, ec in cols:
    box(x, 0.55, 2.05, 1.06, t, s, fc, ec)
    ax.plot([x, x], [1.08, 1.95], color=ec, lw=1.6)
    ax.plot([x, 0.0], [1.95, 1.95], color=SLATE, lw=1.4)
ax.plot([0.0, 0.0], [1.95, 1.95], color=SLATE, lw=1.4)
ax.text(0.0, -0.85, "Моносахарид — воҳиди сохторӣ; дигарҳо бо пайвасти O-гликозидӣ сохта мешаванд",
        ha="center", fontsize=10, color=SLATE)
ax.set_xlim(-4.8, 4.8); ax.set_ylim(-1.15, 2.95)
ax.axis("off")
plt.savefig("img09/shakli_1_2.png", dpi=200, facecolor="#FBF8F4", bbox_inches="tight")
plt.close()

# ===== 2.1: Flowchart ҳазм → ҷабб =====
fig, ax = plt.subplots(figsize=(9.0, 6.2), dpi=200)
fig.patch.set_facecolor("#F7FAF8"); ax.set_facecolor("#F7FAF8")
steps = [
    ("ДАҲОН", "нишондод + амилазаи шира → декстрин, малтоза", "#EEF4FB", "#1D4ED8"),
    ("МЕЪДА", "пайваст мешавад, ҳазм мустақар мешавад (pH-и кислота)", "#F1F5F9", SLATE),
    ("РӮДАИ БОРИК", "амилазаи панкреатӣ + дисахаридазаҳои хӯроак\n→ глюкоза, галактоза, фруктоза", "#FEF6E7", AMBER),
    ("ҲУҶАЙРАҲОИ ЭПТЕЛИЙ", "SGLT1: глюкоза/галактоза + 2Na⁺ (фаъол)\nGLUT5: фруктоза (тессел)", "#FDF0F5", ROSE),
    ("ХУН → ҶИГАР", "GLUT2 ба капилляр мебарад; сипас ба бофтаҳо", "#E6F2EF", TEAL),
]
x, w, h = 0.0, 6.4, 0.86
y = 4.55
for i, (t, s, fc, ec) in enumerate(steps):
    ax.add_patch(mpatches.FancyBboxPatch((x - w/2, y - h/2), w, h,
                 boxstyle="round,pad=0.02,rounding_size=0.08",
                 fc=fc, ec=ec, lw=1.9))
    ax.text(x, y + 0.20, t, ha="center", va="center", fontsize=11, color=INK, weight="bold")
    ax.text(x, y - 0.21, s, ha="center", va="center", fontsize=8.6, color=SLATE)
    if i < len(steps) - 1:
        ax.annotate("", xy=(x, y - h/2 - 0.34), xytext=(x, y - h/2 - 0.04),
                    arrowprops=dict(arrowstyle="-|>", color=ec, lw=2.2))
    y -= 1.20
ax.text(0.0, 5.45, "Роҳи ҳазм ва ҷабби карбогидратҳо", fontsize=13.5, color=INK,
        ha="center", weight="bold")
ax.text(4.85, 1.12, "нақлиётчиҳо дар мембранаи\nмиқдори рӯда ҷой доранд", fontsize=8.6,
        color=ROSE, ha="center")
ax.set_xlim(-4.6, 4.6); ax.set_ylim(-0.85, 5.8)
ax.axis("off")
plt.savefig("img09/shakli_2_1.png", dpi=200, facecolor="#F7FAF8", bbox_inches="tight")
plt.close()

# ===== 3.1: Диаграммаи рацион — пеш/баъд/меъёр (аз Ҷадвали 3.3) =====
fig, axes = plt.subplots(1, 3, figsize=(10.4, 4.6), dpi=200)
fig.patch.set_facecolor("#FBF8F4")
panels = [
    ("Файб, г/рӯз", 14, 26, 25, 34),
    ("Мева ва сабзавот, г/рӯз", 240, 420, 400, 540),
    ("Ғаллаи пурра, г/рӯз", 30, 120, None, 160),
]
for ax, (t, v0, v1, target, ymax) in zip(axes, panels):
    ax.set_facecolor("#FBF8F4")
    xs = [0, 1]
    bars = ax.bar(xs, [v0, v1], width=0.56, color=[SLATE, AMBER], zorder=3)
    for b, v in zip(bars, (v0, v1)):
        ax.text(b.get_x() + b.get_width()/2, v + ymax*0.02, str(v),
                ha="center", fontsize=10.5, color=INK)
    if target is not None:
        ax.axhline(target, color=ROSE, lw=1.8, ls="--", zorder=4)
        ax.text(1.42, target, f"WHO: {target}", fontsize=9.5, color=ROSE,
                va="center", ha="left")
    else:
        ax.text(0.5, ymax*0.86, "меъёр: манбаи асосӣ", fontsize=9.5, color=ROSE, ha="center")
    ax.set_xticks(xs); ax.set_xticklabels(["Пеш", "Баъд"], fontsize=10.5)
    ax.set_ylim(0, ymax)
    ax.set_title(t, fontsize=10.5, color=INK)
    ax.grid(axis="y", color="#E2DDD2", lw=0.6, zorder=0)
    for s_ in ("top", "right"):
        ax.spines[s_].set_visible(False)
fig.suptitle("Нишондиҳандаҳои рацион пеш ва баъди тадбир (Ҷадвали 3.3)",
             fontsize=12.5, color=INK, weight="bold", y=1.0)
fig.tight_layout(rect=(0, 0, 1, 0.96))
plt.savefig("img09/shakli_3_1.png", dpi=200, facecolor="#FBF8F4", bbox_inches="tight")
plt.close()
print("img09 ok: 4 PNG")
