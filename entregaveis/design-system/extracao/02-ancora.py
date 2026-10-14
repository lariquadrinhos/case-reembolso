#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Ancora a escala px->pt das capturas.

Três medidas independentes, todas de elementos que o iOS fixa e o app não
controla. Se as três apontarem para a mesma escala, a régua está posta.
"""
import glob, os
from collections import Counter
from PIL import Image

CAPTURAS = '../../../case-sulamerica/materiais/fluxo-atual'
arqs = [a for a in sorted(glob.glob(os.path.join(CAPTURAS, '*.png')))
        if Image.open(a).size == (739, 1600)]

CANDIDATOS = [
    (390, 844, 47, 'iPhone 13 / 14 (notch)'),
    (393, 852, 54, 'iPhone 14 Pro / 15 / 16 (Dynamic Island)'),
    (402, 874, 54, 'iPhone 16 Pro'),
    (430, 932, 54, 'iPhone 15 Pro Max'),
]

# medida 1: divisor abaixo da barra de navegação
div = Counter()
for a in arqs:
    px = Image.open(a).convert('RGB').load()
    for y in range(120, 260):
        if sum(1 for x in range(20, 719) if sum(px[x, y][:3]) < 735) > 699 * 0.92:
            div[y] += 1
            break
divisor, n_div = div.most_common(1)[0]

# medida 2: altura de caixa dos dígitos do relógio
alt = Counter()
for a in arqs:
    px = Image.open(a).convert('RGB').load()
    ys = [y for y in range(0, 110) for x in range(70, 210) if sum(px[x, y][:3]) < 430]
    if ys and 15 < max(ys) - min(ys) < 40:
        alt[max(ys) - min(ys) + 1] += 1
cap, n_cap = alt.most_common(1)[0]

print('medidas brutas: divisor y=%d (%d telas) · cap do relógio %dpx (%d telas) · altura 1600px'
      % (divisor, n_div, cap, n_cap))
print('\n%-42s %-9s %-11s %-11s %s' % ('hipótese', 'px/pt', 'altura', 'divisor', 'cap 12,1pt'))
for w_pt, h_pt, sb, nome in CANDIDATOS:
    e = 739.0 / w_pt
    print('%-42s %.4f    %4.0fpt %-4s %5.1fpx %-3s %4.1fpx %s'
          % (nome, e, 1600 / e, 'ok' if abs(1600 / e - h_pt) < 4 else '~',
             (sb + 44) * e, 'ok' if abs((sb + 44) * e - divisor) < 3 else '~',
             12.1 * e, 'ok' if abs(12.1 * e - cap) < 1.5 else '~'))

ESCALA = 739.0 / 393
print('\n=== margens de conteúdo, medidas por tela (a %.4f px/pt) ===' % ESCALA)
def borda_esq(a, y0, y1):
    im = Image.open(a).convert('RGB'); px = im.load()
    cont = Counter()
    for y in range(y0, y1, 2):
        for x in range(0, 150):
            if not all(v >= 248 for v in px[x, y][:3]):
                cont[x] += 1
                break
    return cont
agg = Counter()
for a in arqs:
    for x, n in borda_esq(a, 400, 1300).items():
        agg[x] += n
for x, n in agg.most_common(6):
    print('   x=%-4d %5d linhas  ->  %5.2f pt' % (x, n, x / ESCALA))
