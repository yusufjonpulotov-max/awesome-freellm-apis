import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

plt.rcParams["font.family"] = "DejaVu Sans"
TEAL = "#0F766E"; ROSE = "#B91C5C"; AMBER = "#B45309"; SLATE = "#475569"
BLUE = "#1D4ED8"; INK = "#1E293B"

# ===== 1.1: Дарахти таснифоти липидҳо =====
fig, ax = plt.subplots(figsize=(9.2, 5.6), dpi=200)
fig.patch.set_facecolor("#F7FAF8"); ax.set_facecolor("#F7FAF8")
def box(x, y, w, h, title, sub, fc, ec):
    ax.add_patch(mpatches.FancyBboxPatch((x - w/2, y - h/2), w, h,
                 boxstyle="round,pad=0.02,rounding_size=0.06",
                 fc=fc, ec=ec, lw=1.8))
    ax.text(x, y + 0.14, title, ha="center", va="center", fontsize=10.5, color=INK, weight="bold")
    ax.text(x, y - 0.20, sub, ha="center", va="center", fontsize=8.6, color=SLATE)
box(0.0, 2.35, 4.0, 0.78, "ЛИПИДҲО", "дар об ҳалнашаванда: C, H, O (+ P, N)", "#E6F2EF", TEAL)
cols = [
    (-3.30, "Чарбҳои сода", "триглицеридҳо\n(захираи энергия)", "#FEF6E7", AMBER),
    (-1.10, "Фосфолипидҳо", "лецитин,\nсфингомиелин", "#EEF4FB", BLUE),
    (1.10, "Стеролҳо", "холестерин\n(мембрана, гормон)", "#FDF0F5", ROSE),
    (3.30, "Гликолипидҳо", "ганглиозидҳо\n(системаи асаб)", "#F1F5F9", SLATE),
]
for x, t, s, fc, ec in cols:
    box(x, 0.55, 2.0, 1.06, t, s, fc, ec)
    ax.plot([x, x], [1.08, 1.95], color=ec, lw=1.6)
    ax.plot([x, 0.0], [1.95, 1.95], color=SLATE, lw=1.4)
ax.text(0.0, -0.85, "Асоси гурӯҳҳо: кислотаҳои чарбӣ ва пайвасти онҳо бо спирт, фосфор ва азот",
        ha="center", fontsize=10, color=SLATE)
ax.set_xlim(-4.8, 4.8); ax.set_ylim(-1.15, 2.95)
ax.axis("off")
plt.savefig("img10/shakli_1_1.png", dpi=200, facecolor="#F7FAF8", bbox_inches="tight")
plt.close()

# ===== 1.2: Сохтори триглицерид (схемаи молекула) =====
fig, ax = plt.subplots(figsize=(10.2, 6.0), dpi=200)
fig.patch.set_facecolor("#FBF8F4"); ax.set_facecolor("#FBF8F4")
# глицерол
gx, gy = 0.0, 0.0
ax.add_patch(mpatches.FancyBboxPatch((gx-1.15, gy-1.15), 2.3, 2.3,
             boxstyle="round,pad=0.03,rounding_size=0.1", fc="#E6F2EF", ec=TEAL, lw=2.2))
ax.text(gx, gy+0.22, "ГЛИЦЕРОЛ", ha="center", fontsize=12.5, color=INK, weight="bold")
ax.text(gx, gy-0.38, "се гурӯҳи OH", ha="center", fontsize=9.5, color=SLATE)
# се кислотаи чарбӣ
fas = [(-4.1, 2.6, "Кислотаи чарбии 1\n(мас. палмитат C16:0)", AMBER, "#FEF6E7"),
       (-4.1, 0.0, "Кислотаи чарбии 2\n(мас. олеат C18:1)", BLUE, "#EEF4FB"),
       (-4.1, -2.6, "Кислотаи чарбии 3\n(мас. линоленат C18:3)", ROSE, "#FDF0F5")]
for x, y, t, ec, fc in fas:
    ax.add_patch(mpatches.FancyBboxPatch((x-1.5, y-0.62), 3.0, 1.24,
                 boxstyle="round,pad=0.03,rounding_size=0.1", fc=fc, ec=ec, lw=2.0))
    ax.text(x, y, t, ha="center", va="center", fontsize=9.8, color=INK)
    ax.annotate("", xy=(gx-1.2, gy+y/2.6), xytext=(x+1.55, y),
                arrowprops=dict(arrowstyle="-|>", color=ec, lw=2.2))
    ax.text((x+gx-1.2)/2 - 0.15, y + 0.48, "пайвасти эфирӣ", fontsize=8.6, color=ec, ha="center")
# натиҷа: триглицерид
ax.add_patch(mpatches.FancyBboxPatch((2.75, -1.05), 3.3, 2.1,
             boxstyle="round,pad=0.03,rounding_size=0.1", fc="#FEF6E7", ec=AMBER, lw=2.2))
ax.text(4.4, 0.35, "ТРИГЛИЦЕРИД", ha="center", fontsize=12.5, color=INK, weight="bold")
ax.text(4.4, -0.42, "глисерол +\n3 кислотаи чарбӣ", ha="center", fontsize=9.2, color=SLATE)
ax.text(0.0, 3.45, "Сохтори молекулаи триглицерид", fontsize=13.5, color=INK,
        ha="center", weight="bold")
ax.text(0.0, -3.45, "Пайвасти эфирӣ: гурӯҳи OH-и глицерол бо гурӯҳи COOH-и кислотаи чарбӣ",
        ha="center", fontsize=10, color=SLATE)
ax.set_xlim(-6.1, 6.4); ax.set_ylim(-3.8, 3.9)
ax.axis("off")
plt.savefig("img10/shakli_1_2.png", dpi=200, facecolor="#FBF8F4", bbox_inches="tight")
plt.close()

# ===== 2.1: Flowchart ҳазм → ҷабб → нақлиёт =====
fig, ax = plt.subplots(figsize=(9.0, 6.2), dpi=200)
fig.patch.set_facecolor("#F7FAF8"); ax.set_facecolor("#F7FAF8")
steps = [
    ("ДАҲОН", "ҳазми механикӣ; чарб ҳамчун қатраҳои калон", "#EEF4FB", BLUE),
    ("РӮДАИ ДУВОЗДАҲАНГУШТА", "кислотаҳои зардобӣ: эмулгатсия → қатраҳои хурд", "#FEF6E7", AMBER),
    ("РӮДАИ БОРИК", "липазаи панкреатӣ → глицерол + кислотаҳои чарбӣ", "#FDF0F5", ROSE),
    ("ҲУҶАЙРАИ ЭПТЕЛИЙ", "мицелла → реэстерификатсия → хиломикрон", "#F1F5F9", SLATE),
    ("ЛИМФА → ХУН → БОФТАҲО", "липопротеинлипаза: кислотаи чарбӣ ба мушак ва бофтаи чарб", "#E6F2EF", TEAL),
]
x, w, h = 0.0, 6.6, 0.86
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
ax.text(0.0, 5.45, "Роҳи ҳазм ва ҷабби липидҳо", fontsize=13.5, color=INK,
        ha="center", weight="bold")
ax.text(4.9, 1.12, "нақлиёт тавассути лимфа\nмегузарад", fontsize=8.6,
        color=SLATE, ha="center")
ax.set_xlim(-4.8, 4.8); ax.set_ylim(-0.85, 5.8)
ax.axis("off")
plt.savefig("img10/shakli_2_1.png", dpi=200, facecolor="#F7FAF8", bbox_inches="tight")
plt.close()

# ===== 3.1: Диаграммаи рацион — пеш/баъд/меъёр (аз Ҷадвали 3.3) =====
fig, axes = plt.subplots(1, 3, figsize=(10.4, 4.6), dpi=200)
fig.patch.set_facecolor("#FBF8F4")
panels = [
    ("Чарби умумӣ, % энергия", 38, 29, 30, 50),
    ("Чарби сатурӣ, % энергия", 14, 9, 10, 18),
    ("Моҳӣ, маротиба дар ҳафта", 1, 2, None, 3.5),
]
for ax, (t, v0, v1, target, ymax) in zip(axes, panels):
    ax.set_facecolor("#FBF8F4")
    xs = [0, 1]
    bars = ax.bar(xs, [v0, v1], width=0.56, color=[SLATE, AMBER], zorder=3)
    for b, v in zip(bars, (v0, v1)):
        ax.text(b.get_x() + b.get_width()/2, v + ymax*0.03, str(v),
                ha="center", fontsize=10.5, color=INK)
    if target is not None:
        ax.axhline(target, color=ROSE, lw=1.8, ls="--", zorder=4)
        ax.text(1.42, target, f"WHO: {target}", fontsize=9.5, color=ROSE,
                va="center", ha="left")
    else:
        ax.text(0.5, ymax*0.86, "тавсия: 2 маротиба", fontsize=9.5, color=ROSE, ha="center")
    ax.set_xticks(xs); ax.set_xticklabels(["Пеш", "Баъд"], fontsize=10.5)
    ax.set_ylim(0, ymax)
    ax.set_title(t, fontsize=10.5, color=INK)
    ax.grid(axis="y", color="#E2DDD2", lw=0.6, zorder=0)
    for s_ in ("top", "right"):
        ax.spines[s_].set_visible(False)
fig.suptitle("Нишондиҳандаҳои рацион пеш ва баъди тадбир (Ҷадвали 3.3)",
             fontsize=12.5, color=INK, weight="bold", y=1.0)
fig.tight_layout(rect=(0, 0, 1, 0.96))
plt.savefig("img10/shakli_3_1.png", dpi=200, facecolor="#FBF8F4", bbox_inches="tight")
plt.close()
print("img10 ok: 4 PNG")
