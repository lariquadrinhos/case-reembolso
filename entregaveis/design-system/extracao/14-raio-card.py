#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Raio do card de contorno, medido pelo perfil do canto.

O ajuste de curva do `07` não convergiu: a borda tem 1pt e o
redimensionamento a espalhou por três pixels misturados com branco, então
não havia contraste para o mínimo quadrático achar o raio.

O perfil resolve sem ajuste nenhum. Para cada linha a partir do topo do
card, onde começa a tinta alaranjada. A coordenada cai enquanto a curva
avança e trava quando chega na lateral reta. O número de linhas até
travar é o raio, e a distância horizontal percorrida tem que dar o mesmo
valor: são os dois catetos do mesmo quarto de círculo.
"""
import os
from PIL import Image

CAP = '../../../case-sulamerica/materiais/fluxo-atual'
ESCALA = 739.0 / 393
alar = lambda p: p[0] - p[2] > 30 and p[0] > 150

im = Image.open(os.path.join(CAP, '14.png')).convert('RGB')
px = im.load()

perfil = []
for y in range(450, 520):
    xs = [x for x in range(25, 130) if alar(px[x, y])]
    if xs: perfil.append((y, min(xs)))

topo_y, topo_x = perfil[0]
lateral = min(x for _, x in perfil)
trava_y = next(y for y, x in perfil if x == lateral)

r_vert = trava_y - topo_y
r_horiz = topo_x - lateral
print('topo do card em y=%d, tinta começa em x=%d' % (topo_y, topo_x))
print('lateral reta em x=%d, alcançada em y=%d' % (lateral, trava_y))
print()
print('raio pela vertical:   %2d px  ->  %.1f pt' % (r_vert, r_vert / ESCALA))
print('raio pela horizontal: %2d px  ->  %.1f pt' % (r_horiz, r_horiz / ESCALA))
if abs(r_vert - r_horiz) <= 2:
    r = (r_vert + r_horiz) / 2.0
    print('\nos dois catetos concordam, então é quarto de círculo.')
    print('raio = %.1f px  ->  **%.1f pt**' % (r, r / ESCALA))
else:
    print('\ncatetos discordam: não é quarto de círculo simples, não reportar')
