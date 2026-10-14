#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Ancora a escala px->pt das capturas e mede as margens de conteúdo.

As capturas foram redimensionadas: 739x1600 não é resolução de aparelho.
Aqui eu testo a hipótese de iPhone 13/14 (390x844pt) e confiro contra
medidas que a plataforma fixa: margem lateral e barra de status.
"""
import glob, os
from collections import Counter
from PIL import Image

CAPTURAS = '../../../case-sulamerica/materiais/fluxo-atual'

def branco(c, tol=8):
    return all(v >= 255 - tol for v in c[:3])

arqs = sorted(glob.glob(os.path.join(CAPTURAS, '*.png')))
print('capturas:', len(arqs))

dims = Counter(Image.open(a).size for a in arqs)
print('\n=== dimensões ===')
for (w, h), n in dims.most_common():
    print('   %4d x %-5d  %2d arquivo(s)' % (w, h, n))

L = 739.0
for pt_w, aparelho in [(390, 'iPhone 13/14/16'), (375, 'iPhone SE/8'), (393, 'iPhone 14 Pro'), (430, 'iPhone 15 Pro Max')]:
    print('   %-18s %3dpt -> %.4f px/pt' % (aparelho, pt_w, L / pt_w))

print('\n=== margem esquerda do conteúdo (px) ===')
margens = Counter()
for a in arqs:
    im = Image.open(a).convert('RGB')
    w, h = im.size
    if w != 739:
        continue
    px = im.load()
    # varre a faixa central vertical, longe de header e rodapé
    for y in range(int(h * 0.30), int(h * 0.75), 2):
        for x in range(0, 120):
            if not branco(px[x, y]):
                margens[x] += 1
                break
for x, n in margens.most_common(8):
    print('   x=%-4d %5d linhas   -> %.1f pt (a 1,8949 px/pt)' % (x, n, x / 1.8949))
