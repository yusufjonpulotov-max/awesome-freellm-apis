# -*- coding: utf-8 -*-
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family'] = 'DejaVu Sans'
OUT = '/home/user/awesome-freellm-apis/kurs/metodichka-fiziologia/img_mf/'

# --- Расми 2.1: кривая роста (средние значения, по учебникам) ---
ages = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]
ht   = [51,75,86,94,100,107,114,121,127,132,137,142,148,154,160,166,170,173]
fig, ax = plt.subplots(figsize=(7.6,4.2))
ax.plot(ages, ht, 'o-', color='#1a5fb4', lw=2, ms=4)
ax.set_xlabel('Возраст, лет'); ax.set_ylabel('Длина тела, см')
ax.set_title('Динамика средней длины тела от рождения до 17 лет', fontsize=11)
ax.grid(True, ls=':', alpha=.6); ax.set_xlim(-0.5,17.5); ax.set_ylim(45,180)
ax.set_xticks(range(0,18,2))
for a,h in [(0,51),(1,75),(7,121),(14,160),(17,173)]:
    ax.annotate(f'{h}', (a,h), textcoords='offset points', xytext=(0,7), ha='center', fontsize=8)
fig.tight_layout(); fig.savefig(OUT+'rasmi_2_1.png', dpi=200); plt.close(fig)

# --- Расми 2.2: пропорции тела (доля головы от роста) ---
labels = ['Новорождённый\n(1/4)', '2 года\n(1/5)', '6 лет\n(1/6)', 'Взрослый\n(1/8)']
vals = [25.0, 20.0, 16.7, 12.5]
fig, ax = plt.subplots(figsize=(7.6,4.2))
bars = ax.bar(labels, vals, color=['#c01c28','#e66100','#26a269','#1a5fb4'], width=.6)
for b,v in zip(bars, vals):
    ax.annotate(f'{v:.1f}'.replace('.',','), (b.get_x()+b.get_width()/2, v),
                textcoords='offset points', xytext=(0,4), ha='center', fontsize=9)
ax.set_ylabel('Доля длины головы от роста, %')
ax.set_title('Изменение пропорций тела с возрастом', fontsize=11)
ax.grid(True, axis='y', ls=':', alpha=.6); ax.set_ylim(0,29)
fig.tight_layout(); fig.savefig(OUT+'rasmi_2_2.png', dpi=200); plt.close(fig)

# --- Расми 3.1: схема рефлекторной дуги ---
fig, ax = plt.subplots(figsize=(7.6,4.2))
ax.set_xlim(0,10); ax.set_ylim(0,5); ax.axis('off')
boxes = [(0.4,1.8,'РЕЦЕПТОР'), (3.7,3.0,'НЕРВНЫЙ ЦЕНТР\n(ЦНС)'), (7.2,1.8,'РАБОЧИЙ\nОРГАН')]
for x,y,t in boxes:
    ax.add_patch(plt.Rectangle((x,y), 2.2, 1.2, fc='#EDEDED', ec='k', lw=1.2))
    ax.text(x+1.1, y+0.6, t, ha='center', va='center', fontsize=9, fontweight='bold')
arrow_kw = dict(arrowstyle='->', lw=1.6, color='k')
ax.annotate('', xy=(3.7,3.6), xytext=(1.7,2.6), arrowprops=arrow_kw)
ax.text(2.3,3.35,'чувствительный\n(афферентный) путь', fontsize=8, ha='center')
ax.annotate('', xy=(7.2,2.6), xytext=(5.9,3.2), arrowprops=arrow_kw)
ax.text(6.6,3.35,'двигательный\n(эфферентный) путь', fontsize=8, ha='center')
ax.annotate('', xy=(9.6,3.4), xytext=(9.0,2.4), arrowprops=arrow_kw)
ax.text(9.25,3.55,'действие', fontsize=8, ha='center')
ax.text(5.0,0.6,'Рефлекторная дуга: рецептор → афферентный путь → нервный центр → эфферентный путь → рабочий орган',
        fontsize=8.5, ha='center', style='italic')
ax.set_title('Схема рефлекторной дуги', fontsize=11)
fig.tight_layout(); fig.savefig(OUT+'rasmi_3_1.png', dpi=200); plt.close(fig)
print('3 images ok')
