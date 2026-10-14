#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Cor dos estados de componente, achada por busca de família de cor.

A primeira versão usava janelas de coordenada escolhidas a olho na folha
de contato, que está reduzida: as janelas caíram no lugar errado e três
delas nem existiam na imagem. Aqui nada depende de posição. Para cada
pergunta, o script varre a tela inteira atrás de uma família de cor
(vermelho, navy, laranja, cinza médio) e devolve o valor exato mais
frequente, com a área que ele ocupa.
"""
import os
from collections import Counter
from PIL import Image

CAP = '../../../case-sulamerica/materiais/fluxo-atual'
def hexa(c): return '#%02x%02x%02x' % c[:3]

FAMILIAS = {
    'vermelho':   lambda r, g, b: r - g > 35 and r - b > 35 and r > 100,
    'navy':       lambda r, g, b: b > 60 and b - r > 45 and b > g and r < 90,
    'navy-texto': lambda r, g, b: b - r > 25 and b > 70 and r < 140,
    'laranja':    lambda r, g, b: r > 180 and 40 < g < 160 and b < 90,
    'cinza-medio':lambda r, g, b: abs(r-g) < 10 and abs(g-b) < 10 and 150 < r < 225,
    'azul-link':  lambda r, g, b: b > 120 and b - r > 60 and g > r,
}

PERGUNTAS = [
    ('preenchimento do botão desabilitado', '22.png', 'cinza-medio'),
    ('preenchimento do botão navy',          '6.png', 'navy'),
    ('texto de erro',                       '32.png', 'vermelho'),
    ('radio marcado',                       '15.png', 'laranja'),
    ('borda do card selecionado',           '21.png', 'laranja'),
    ('círculo do ícone de clipe',           '22.png', 'navy-texto'),
    ('ícone de categoria',                   '7.png', 'navy-texto'),
    ('título da nav bar',                   '14.png', 'navy-texto'),
]

TOKENS = {
    '#f05223': 'brand-primary', '#001c5c': 'brand-secondary', '#c80505': 'feedback-error',
    '#ef9928': 'feedback-alert', '#04843f': 'feedback-success', '#313333': 'text-primary',
    '#6c6e6e': 'text-secondary', '#949595': 'text-disabled', '#1355b4': 'text-link',
    '#f3f4f4': 'surface-on-body', '#1769e0': 'brand-tertiary-1', '#fc9c26': 'brand-tertiary-2',
}

def perto(h):
    rgb = tuple(int(h[i:i+2], 16) for i in (1, 3, 5))
    melhor, dist = None, 1e9
    for t, rot in TOKENS.items():
        trgb = tuple(int(t[i:i+2], 16) for i in (1, 3, 5))
        d = sum((rgb[i] - trgb[i]) ** 2 for i in range(3)) ** 0.5
        if d < dist: dist, melhor = d, (t, rot)
    if dist < 3:   return 'IGUAL ao token %s (%s)' % (melhor[0], melhor[1])
    if dist < 50:  return 'perto de %s (%s), distância %.0f' % (melhor[0], melhor[1], dist)
    return 'sem token equivalente (mais próximo %s, distância %.0f)' % (melhor[0], dist)

print('%-34s %-9s %-9s %8s  %s' % ('estado', 'tela', 'medido', 'px', 'contra o sistema da web'))
for nome, arq, fam in PERGUNTAS:
    im = Image.open(os.path.join(CAP, arq)).convert('RGB')
    f = FAMILIAS[fam]
    c = Counter(p for p in (im.get_flattened_data() if hasattr(im,'get_flattened_data') else im.getdata()) if f(*p[:3]))
    if not c:
        print('%-34s %-9s %s' % (nome, arq, 'família %s não encontrada' % fam)); continue
    k, n = c.most_common(1)[0]
    if n < 500:
        print('%-34s %-9s %-9s %8d  amostra insuficiente, não reportar' % (nome, arq, hexa(k), n)); continue
    print('%-34s %-9s %-9s %8d  %s' % (nome, arq, hexa(k), n, perto(hexa(k))))
