# -*- coding: utf-8 -*-
# Расмҳои М25: биосинтези сафедаҳо ва коди генетикӣ
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle, Rectangle, Ellipse
import numpy as np, os

plt.rcParams['font.family'] = 'DejaVu Sans'
BG, FB, AC, GB = '#fffaf0', '#b45309', '#1d4ed8', '#166534'
os.makedirs('img25', exist_ok=True)

def box(ax, x, y, w, h, t, fc='#fff', ec=FB, fs=9, bold=False):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle='round,pad=0.02',
                 fc=fc, ec=ec, lw=1.4))
    ax.text(x + w/2, y + h/2, t, ha='center', va='center', fontsize=fs,
            fontweight='bold' if bold else 'normal', wrap=True)

def arrow(ax, x1, y1, x2, y2, c=FB, ls='-'):
    ax.add_patch(FancyArrowPatch((x1, y1), (x2, y2), arrowstyle='-|>',
                 mutation_scale=14, color=c, lw=1.6, linestyle=ls))

# ---------- 1_1: Коди генетикӣ ----------
fig, ax = plt.subplots(figsize=(9.2, 5.4)); ax.set_xlim(0, 10); ax.set_ylim(0, 6); ax.axis('off')
ax.add_patch(FancyBboxPatch((0.15, 0.15), 9.7, 5.7, boxstyle='round,pad=0.03', fc=BG, ec=FB, lw=2))
ax.text(5, 5.55, 'Коди генетикӣ: аз тройка то аминокислота', ha='center', fontsize=13, fontweight='bold', color=FB)
ax.text(0.45, 4.85, 'mRNA:', fontsize=10, fontweight='bold')
codons = [('AUG', GB), ('GCA', AC), ('UUC', '#7c3aed'), ('UAA', '#b91c1c')]
labels = ['Мет (оғоз)', 'Алан', 'Фен', 'STOP']
for i, (cd, cc) in enumerate(codons):
    x = 1.6 + i * 2.1
    box(ax, x, 4.35, 1.5, 0.62, cd, fc='#fff', ec=cc, fs=11, bold=True)
    ax.text(x + 0.75, 4.05, labels[i], ha='center', fontsize=8, color=cc)
for i in range(4):
    x = 1.6 + i * 2.1 + 0.75
    arrow(ax, x, 4.3, x, 3.5, c='#92400e')
box(ax, 1.2, 2.6, 8.0, 0.85, 'Занҷираи пептидӣ: Мет — Алан — Фен — (қатъ)', fc='#fef3c7', ec=GB, fs=10, bold=True)
box(ax, 0.5, 0.5, 4.4, 1.6, '64 кодон = 61 маънёдор + 3 STOP\n61 кодон ← 20 аминокислота\nҲаммаъноӣ: дар ҷои 3-юм (wobble)', fc='#fff', ec=AC, fs=9)
box(ax, 5.1, 0.5, 4.4, 1.6, 'AUG — оғоз (Мет)\nUAA, UAG, UGA — оҳир\nМитохондрия: UGA = Триптофан', fc='#fff', ec=GB, fs=9)
plt.tight_layout(); plt.savefig('img25/shakli_1_1.png', dpi=200); plt.close()

# ---------- 1_2: tRNA cloverleaf ----------
fig, ax = plt.subplots(figsize=(9.2, 6.0)); ax.set_xlim(0, 10); ax.set_ylim(0, 6.4); ax.axis('off')
ax.add_patch(FancyBboxPatch((0.15, 0.15), 9.7, 6.1, boxstyle='round,pad=0.03', fc=BG, ec=FB, lw=2))
ax.text(5, 6.02, 'tRNA: баргборак ва аминоасилшавӣ', ha='center', fontsize=13, fontweight='bold', color=FB)
cx = 2.55
ax.add_patch(Circle((cx, 5.15), 0.38, fc='#fff', ec=GB, lw=1.8))
ax.text(cx, 5.15, 'АК', ha='center', va='center', fontsize=9.5, fontweight='bold', color=GB)
arrow(ax, cx, 4.75, cx, 4.42, c='#92400e')
ax.add_patch(Ellipse((cx, 4.05), 1.15, 0.75, fc='#fee2e2', ec='#b91c1c', lw=1.5))
ax.text(cx, 4.05, "3'-CCA", ha='center', va='center', fontsize=8.5, fontweight='bold', color='#b91c1c')
ax.plot([cx, cx], [3.65, 3.1], color='#92400e', lw=1.4)
ax.add_patch(Ellipse((cx - 1.25, 2.75), 1.45, 0.8, fc='#dbeafe', ec=AC, lw=1.5))
ax.text(cx - 1.25, 2.75, 'Бозӯи D', ha='center', va='center', fontsize=8.5, color=AC)
ax.add_patch(Ellipse((cx + 1.25, 2.75), 1.45, 0.8, fc='#dcfce7', ec=GB, lw=1.5))
ax.text(cx + 1.25, 2.75, 'Бозӯи T', ha='center', va='center', fontsize=8.5, color=GB)
ax.plot([cx, cx], [2.3, 2.0], color='#92400e', lw=1.4)
ax.add_patch(Ellipse((cx, 1.62), 1.5, 0.8, fc='#fef9c3', ec='#a16207', lw=1.5))
ax.text(cx, 1.62, 'Антикодон', ha='center', va='center', fontsize=8, color='#a16207')
box(ax, 0.5, 0.3, 4.3, 0.85, 'АК + ATP + tRNA → аминоасил-AMP + PPi', fc='#fff', ec=AC, fs=8.3)
box(ax, 5.3, 4.45, 4.25, 1.25, 'Аминоасил-tRNA: АК бо пайвасти эфирӣ\nба охири 3′-CCA пайваст аст', fc='#fff', ec=GB, fs=9.3)
box(ax, 5.3, 2.75, 4.25, 1.45, 'Аминоасил-tRNA-синтетаза:\n20 навъ — ҳар АК ферменти хос дорад;\ndурустӣ бо таҳрири таҳрирӣ таъмин мешавад', fc='#fff', ec=AC, fs=9.3)
box(ax, 5.3, 1.0, 4.25, 1.5, 'Антикодон бо кодони mRNA\nпайвасти комплементарӣ дорад;\nпуркунии tRNA аз синтетаза', fc='#fff', ec='#a16207', fs=9.3)
plt.tight_layout(); plt.savefig('img25/shakli_1_2.png', dpi=200); plt.close()

# ---------- 2_1: Рибосома A/P/E ----------
fig, ax = plt.subplots(figsize=(9.2, 6.0)); ax.set_xlim(0, 10); ax.set_ylim(0, 6.4); ax.axis('off')
ax.add_patch(FancyBboxPatch((0.15, 0.15), 9.7, 6.1, boxstyle='round,pad=0.03', fc=BG, ec=FB, lw=2))
ax.text(5, 6.02, 'Рибосомаи 80S: ҷойҳои A, P, E ва элонгатсия', ha='center', fontsize=13, fontweight='bold', color=FB)
box(ax, 2.0, 4.6, 6.0, 1.05, 'Субчестораи калон 60S\n(пептидилтрансфераза — rRNA, рибозим)', fc='#dbeafe', ec=AC, fs=10, bold=True)
sites = [('A\nаминоасил-tRNA', 2.35, AC), ('P\nпептидил-tRNA', 4.2, GB), ('E\ntRNA-и холӣ', 6.05, '#b91c1c')]
for t, x, cc in sites:
    box(ax, x, 3.55, 1.6, 0.85, t, fc='#fff', ec=cc, fs=8.6, bold=True)
box(ax, 2.6, 2.65, 4.8, 0.62, 'Субчестораи хурд 40S', fc='#dcfce7', ec=GB, fs=9.5, bold=True)
ax.plot([1.1, 8.9], [2.38, 2.38], color='#92400e', lw=3)
ax.text(0.5, 2.32, 'mRNA', fontsize=9, fontweight='bold', color='#92400e')
for x in (3.15, 5.0, 6.85):
    ax.plot([x, x], [2.30, 2.46], color='#92400e', lw=2)
box(ax, 0.5, 0.4, 4.4, 1.6, 'Даври элонгатсия:\n1. eEF1A + GTP → tRNA ба ҷои A\n2. Пайвасти пептидӣ (A → P)', fc='#fff', ec=AC, fs=9)
box(ax, 5.1, 0.4, 4.4, 1.6, '3. eEF2 + GTP → транслокация\n4. tRNA-и холӣ аз ҷои E мебарояд\nҲар кодон ~2 молекула GTP сарф мешавад', fc='#fff', ec=GB, fs=9)
plt.tight_layout(); plt.savefig('img25/shakli_2_1.png', dpi=200); plt.close()

# ---------- 3_1: Мутатсияҳо ва бемориҳо ----------
fig, ax = plt.subplots(figsize=(9.4, 5.8)); ax.set_xlim(0, 10); ax.set_ylim(0, 6.2); ax.axis('off')
ax.add_patch(FancyBboxPatch((0.15, 0.15), 9.7, 5.9, boxstyle='round,pad=0.03', fc=BG, ec=FB, lw=2))
ax.text(5, 5.75, 'Мутатсияҳо ва бемориҳои маврисӣ', ha='center', fontsize=13, fontweight='bold', color=FB)
box(ax, 3.4, 4.6, 3.2, 0.8, 'Мутатсия дар ген', fc='#fee2e2', ec='#b91c1c', fs=11, bold=True)
kids = [('Синонимӣ\nбетоғйир', '#dcfce7', GB), ('Мисенс\nHbS', '#fef9c3', '#a16207'),
        ('Nonsense\nDMD', '#fee2e2', '#b91c1c'), ('Frameshift\nТалассемия', '#e0e7ff', AC),
        ('Splice\nHbE', '#f3e8ff', '#7c3aed')]
for i, (t, fc, ec) in enumerate(kids):
    x = 0.45 + i * 1.95
    arrow(ax, 5.0, 4.55, x + 0.85, 3.6, c='#92400e')
    box(ax, x, 2.75, 1.7, 0.85, t, fc=fc, ec=ec, fs=8.5, bold=True)
dis = [('DMD — дистрофин, Xp21,\nCK то 100×, қоидаи фрейм', '#fee2e2', '#b91c1c'),
       ('Бета-талассемия — HBB, 11p15.4,\nHbA₂ > 4%, MCV < 79 fL', '#dbeafe', AC),
       ('OI — COL1A1/COL1A2, глисин,\nустухони шикаст, бисфосфонат', '#dcfce7', GB)]
for i, (t, fc, ec) in enumerate(dis):
    box(ax, 0.45 + i * 3.25, 0.9, 3.0, 1.25, t, fc=fc, ec=ec, fs=8.5)
    arrow(ax, 0.45 + i * 3.25 + 1.5, 2.7, 0.45 + i * 3.25 + 1.5, 2.2, c='#92400e', ls=':')
plt.tight_layout(); plt.savefig('img25/shakli_3_1.png', dpi=200); plt.close()

# ---------- 4_1: Машғулияти амалӣ ----------
fig, ax = plt.subplots(figsize=(9.2, 5.4)); ax.set_xlim(0, 10); ax.set_ylim(0, 6); ax.axis('off')
ax.add_patch(FancyBboxPatch((0.15, 0.15), 9.7, 5.7, boxstyle='round,pad=0.03', fc=BG, ec=FB, lw=2))
ax.text(5, 5.55, 'Машғулияти амалӣ: тарҷума ва мутатсия', ha='center', fontsize=13, fontweight='bold', color=FB)
steps = [('1. mRNA-и мисол\n(AUG-GCA-UUC-UAA)', '#dbeafe', AC),
         ('2. Тарҷума: занҷираи АК\nМет-Алан-Фен-STOP', '#dcfce7', GB),
         ('3. Мутатсия: GCA→GAA\nМисенс: Алан→Глу', '#fef9c3', '#a16207'),
         ('4. Мутатсия: UUC→UAA\nNonsense: сафед кӯтоҳ', '#fee2e2', '#b91c1c'),
         ('5. Гузориш:\nҷадвал ва хулоса', '#f3e8ff', '#7c3aed')]
for i, (t, fc, ec) in enumerate(steps):
    x = 0.5 + (i % 3) * 3.25; y = 3.35 - (i // 3) * 1.75
    box(ax, x, y, 2.95, 1.3, t, fc=fc, ec=ec, fs=9, bold=True)
    if i % 3 < 2 and i < 4:
        arrow(ax, x + 2.95, y + 0.65, x + 3.25, y + 0.65, c='#92400e')
    if i % 3 == 2 and i < 4:
        arrow(ax, x + 1.4, y, x + 0.8, y - 0.45, c='#92400e')
box(ax, 0.5, 0.35, 9.0, 0.95, 'Меъёр: CK 26–192 U/L | HbA₂ 2–3% | HbF < 1% | MCV 80–100 fL', fc='#fff', ec=FB, fs=10, bold=True)
plt.tight_layout(); plt.savefig('img25/shakli_4_1.png', dpi=200); plt.close()
print('OK: 5 images')
