# -*- coding: utf-8 -*-
# Расмҳои М26: даври мочавина ва мубодилаи азот
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Ellipse
import numpy as np, os

plt.rcParams['font.family'] = 'DejaVu Sans'
BG, FB, AC, GB = '#fffaf0', '#b45309', '#1d4ed8', '#166534'
os.makedirs('img26', exist_ok=True)

def box(ax, x, y, w, h, t, fc='#fff', ec=FB, fs=9, bold=False):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle='round,pad=0.02',
                 fc=fc, ec=ec, lw=1.4))
    ax.text(x + w/2, y + h/2, t, ha='center', va='center', fontsize=fs,
            fontweight='bold' if bold else 'normal', wrap=True)

def arrow(ax, x1, y1, x2, y2, c=FB, ls='-'):
    ax.add_patch(FancyArrowPatch((x1, y1), (x2, y2), arrowstyle='-|>',
                 mutation_scale=14, color=c, lw=1.6, linestyle=ls))

# ---------- 1_1: Трансаминатсия ----------
fig, ax = plt.subplots(figsize=(9.2, 5.4)); ax.set_xlim(0, 10); ax.set_ylim(0, 6); ax.axis('off')
ax.add_patch(FancyBboxPatch((0.15, 0.15), 9.7, 5.7, boxstyle='round,pad=0.03', fc=BG, ec=FB, lw=2))
ax.text(5, 5.55, 'Трансаминатсия: АСТ ва АЛТ', ha='center', fontsize=13, fontweight='bold', color=FB)
box(ax, 0.5, 4.0, 2.6, 0.9, 'Глутамат\n(азотдо дар)', fc='#dbeafe', ec=AC, fs=10, bold=True)
box(ax, 3.5, 4.0, 2.6, 0.9, 'Альфа-кетокислота', fc='#dcfce7', ec=GB, fs=10, bold=True)
arrow(ax, 3.1, 4.45, 3.5, 4.45, c='#92400e')
arrow(ax, 3.5, 3.9, 3.1, 3.9, c='#92400e')
box(ax, 0.5, 2.7, 5.6, 0.9, 'Ферментҳо: АСТ (Глутамат+ОАА → Асп)  |  АЛТ (Глутамат+Пируват → Алан)', fc='#fff', ec=FB, fs=9.2)
box(ax, 6.5, 4.0, 3.0, 0.9, 'Кофермент: PLP (B6)\nмеханизми Шифф-асос', fc='#fef9c3', ec='#a16207', fs=9.5, bold=True)
arrow(ax, 6.5, 4.45, 6.1, 4.45, c='#92400e')
box(ax, 0.5, 0.6, 4.4, 1.7, 'АСТ:\n• дар ҷигар ва дил\n• маркери осеби дил ва ҷигар', fc='#fff', ec=AC, fs=9.3)
box(ax, 5.1, 0.6, 4.4, 1.7, 'АЛТ:\n• хоси ҷигар\n• маркери осеби ҷигар (гепатит)', fc='#fff', ec=GB, fs=9.3)
plt.tight_layout(); plt.savefig('img26/shakli_1_1.png', dpi=200); plt.close()

# ---------- 1_2: Аммиак — манбаъҳо ва нақлиёт ----------
fig, ax = plt.subplots(figsize=(9.4, 5.6)); ax.set_xlim(0, 10); ax.set_ylim(0, 6.2); ax.axis('off')
ax.add_patch(FancyBboxPatch((0.15, 0.15), 9.7, 5.9, boxstyle='round,pad=0.03', fc=BG, ec=FB, lw=2))
ax.text(5, 5.8, 'Аммиак: манбаъҳо ва нақлиёти ба ҷигар', ha='center', fontsize=13, fontweight='bold', color=FB)
srcs = [('Деаминатсияи оксидӣ\n(ГДГ, ҷигар)', '#dbeafe', AC),
        ('Рӯшнаҳо (уреаза)\nмочавина → NH3', '#dcfce7', GB),
        ('Мушак (AMR + NH3)', '#fef9c3', '#a16207'),
        ('Мағз (глутаминаза)', '#f3e8ff', '#7c3aed')]
for i, (t, fc, ec) in enumerate(srcs):
    box(ax, 0.4 + (i % 2) * 3.2, 4.1 - (i // 2) * 1.35, 2.9, 1.05, t, fc=fc, ec=ec, fs=8.8, bold=True)
    arrow(ax, 0.4 + (i % 2) * 3.2 + 1.45, 4.05 - (i // 2) * 1.35, 0.4 + (i % 2) * 3.2 + 1.45, 3.6 - (i // 2) * 1.35, c='#92400e')
box(ax, 0.4, 1.6, 6.1, 1.0, 'Нақлиёт: Глутамин (ҳама бофтаҳо) ва Аланин (мушак → ҷигар)', fc='#fff', ec=FB, fs=9.5, bold=True)
arrow(ax, 3.4, 1.55, 3.4, 1.25, c='#92400e')
box(ax, 0.4, 0.3, 6.1, 0.9, 'Ҷигар: аммиак → даври мочавина → мочавина → гурда', fc='#fee2e2', ec='#b91c1c', fs=10, bold=True)
box(ax, 6.8, 1.6, 2.7, 2.55, 'Глутамин-синтетаза:\nГлутамат + NH3 + ATP →\n→ Глутамин\n\nГлутаминаза:\nГлутамин → глутамат + NH3', fc='#fff', ec=AC, fs=9)
plt.tight_layout(); plt.savefig('img26/shakli_1_2.png', dpi=200); plt.close()

# ---------- 2_1: Даври мочавина ----------
fig, ax = plt.subplots(figsize=(9.4, 6.0)); ax.set_xlim(0, 10); ax.set_ylim(0, 6.4); ax.axis('off')
ax.add_patch(FancyBboxPatch((0.15, 0.15), 9.7, 6.1, boxstyle='round,pad=0.03', fc=BG, ec=FB, lw=2))
ax.text(5, 6.02, 'Даври мочавина: 5 марҳила дар ҷигар', ha='center', fontsize=13, fontweight='bold', color=FB)
steps = [('1. CPS1\nNH3+CO2+2ATP → карбамоил-фосфат\n(активатор: NAG)', '#dbeafe', AC),
         ('2. OTC\n+ орнитин → цитруллин', '#dcfce7', GB),
         ('3. ASS1\n+ аспартат+ATP → аргининосукцинат', '#fef9c3', '#a16207'),
         ('4. ASL\n→ аргинин + фумарат', '#f3e8ff', '#7c3aed'),
         ('5. Аргиназа\n→ мочавина + орнитин', '#fee2e2', '#b91c1c')]
for i, (t, fc, ec) in enumerate(steps):
    x = 0.4 + (i % 3) * 3.25; y = 4.35 - (i // 3) * 1.9
    box(ax, x, y, 2.95, 1.45, t, fc=fc, ec=ec, fs=8.6, bold=True)
    if i % 3 < 2 and i < 4:
        arrow(ax, x + 2.95, y + 0.72, x + 3.25, y + 0.72, c='#92400e')
    if i % 3 == 2 and i < 4:
        arrow(ax, x + 1.4, y, x + 0.4, y - 0.42, c='#92400e')
box(ax, 3.6, 0.3, 5.9, 1.3, 'Мочавина ба хун → гурда → пешоб\nОрнитин ба митохондрия бармегардад (ORNT1)\nҲар мочавина: 4 ATP сарф мешавад', fc='#fff', ec=FB, fs=9.3)
box(ax, 0.4, 0.3, 3.0, 1.3, 'Митохондрия:\n1-2\n\nЦитоплазма:\n3-5', fc='#dcfce7', ec=GB, fs=9.5, bold=True)
plt.tight_layout(); plt.savefig('img26/shakli_2_1.png', dpi=200); plt.close()

# ---------- 3_1: Нуқсҳои маврсӣ ----------
fig, ax = plt.subplots(figsize=(9.4, 5.8)); ax.set_xlim(0, 10); ax.set_ylim(0, 6.2); ax.axis('off')
ax.add_patch(FancyBboxPatch((0.15, 0.15), 9.7, 5.9, boxstyle='round,pad=0.03', fc=BG, ec=FB, lw=2))
ax.text(5, 5.75, 'Нуқсҳои даври мочавина (UCD) ва нишонаҳо', ha='center', fontsize=13, fontweight='bold', color=FB)
box(ax, 3.4, 4.6, 3.2, 0.8, 'Гипераммониемия', fc='#fee2e2', ec='#b91c1c', fs=11, bold=True)
kids = [('OTC-нуқс\nX-linked\nоротоват ↑', '#dbeafe', AC), ('CPS1-нуқс\nрецессивӣ\nцитруллин ↓', '#dcfce7', GB),
        ('Цитруллинемия\nASS1\nцитруллин ↑↑', '#fef9c3', '#a16207'), ('Аргининемия\nАргиназа\nаргинин ↑↑', '#f3e8ff', '#7c3aed'),
        ('HHH / цитрин\nнақлиёт\nорнитин ↑', '#e0e7ff', '#4f46e5')]
for i, (t, fc, ec) in enumerate(kids):
    x = 0.45 + i * 1.95
    arrow(ax, 5.0, 4.55, x + 0.85, 3.6, c='#92400e')
    box(ax, x, 2.75, 1.7, 0.9, t, fc=fc, ec=ec, fs=8.2, bold=True)
dis = [('Навзод: > 100 мкмол/л\nКалонсол: > 50 мкмол/л', '#fee2e2', '#b91c1c'),
       ('Энцефалопатия: 200–500 мкмол/л\nосеби мағз', '#dbeafe', AC),
       ('Дармон: бензоат, фенилацетат,\nпарҳез, диализ', '#dcfce7', GB)]
for i, (t, fc, ec) in enumerate(dis):
    box(ax, 0.45 + i * 3.25, 0.6, 3.0, 1.25, t, fc=fc, ec=ec, fs=8.8)
    arrow(ax, 0.45 + i * 3.25 + 1.5, 2.7, 0.45 + i * 3.25 + 1.5, 1.9, c='#92400e', ls=':')
plt.tight_layout(); plt.savefig('img26/shakli_3_1.png', dpi=200); plt.close()

# ---------- 4_1: Машғулияти амалӣ ----------
fig, ax = plt.subplots(figsize=(9.2, 5.4)); ax.set_xlim(0, 10); ax.set_ylim(0, 6); ax.axis('off')
ax.add_patch(FancyBboxPatch((0.15, 0.15), 9.7, 5.7, boxstyle='round,pad=0.03', fc=BG, ec=FB, lw=2))
ax.text(5, 5.55, 'Машғулияти амалӣ: аммиак ва карбамид', ha='center', fontsize=13, fontweight='bold', color=FB)
steps = [('1. Гирифтани намуна\n(хуни венавӣ)', '#dbeafe', AC),
         ('2. Тести аммиак\n(< 50 мкмол/л)', '#dcfce7', GB),
         ('3. Тести карбамид\n(2.5–7.5 ммол/л)', '#fef9c3', '#a16207'),
         ('4. Аминокислотаҳо\n(цитруллин, аргинин)', '#f3e8ff', '#7c3aed'),
         ('5. Гузориш\n(ҷадвал ва ташхис)', '#fee2e2', '#b91c1c')]
for i, (t, fc, ec) in enumerate(steps):
    x = 0.5 + (i % 3) * 3.25; y = 3.35 - (i // 3) * 1.75
    box(ax, x, y, 2.95, 1.3, t, fc=fc, ec=ec, fs=9, bold=True)
    if i % 3 < 2 and i < 4:
        arrow(ax, x + 2.95, y + 0.65, x + 3.25, y + 0.65, c='#92400e')
    if i % 3 == 2 and i < 4:
        arrow(ax, x + 1.4, y, x + 0.8, y - 0.45, c='#92400e')
box(ax, 0.5, 0.35, 9.0, 0.95, 'Меъёр: NH3 < 50 мкмол/л | карбамид 2.5–7.5 ммол/л | цитруллин 12–55 мкмол/л', fc='#fff', ec=FB, fs=10, bold=True)
plt.tight_layout(); plt.savefig('img26/shakli_4_1.png', dpi=200); plt.close()
print('OK: 5 images')
