#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Corpo do título de tela, medido só onde existe título de tela.

A tentativa do 05 varria uma janela fixa logo abaixo do divisor e deu
desvio de 4,09px, porque nem toda tela abre com título: a janela pegava
ora o título, ora um card, ora um campo. Aqui a lista de telas é
explícita, e cada uma foi conferida na captura antes de entrar.

Cap/em = 0,70 (Figtree).
"""
import os
from PIL import Image

CAP = '../../../case-sulamerica/materiais/fluxo-atual'
ESCALA, CAP_EM = 739.0 / 393, 0.70

# telas cujo primeiro bloco de texto abaixo do divisor é o título da tela
TELAS = [
    ('14.png', 'Atenção!'),
    ('15.png', 'Dados do procedimento'),
    ('19.png', 'Selecione o tipo de documento'),
    ('20.png', 'Selecione o tipo de documento'),
    ('22.png', 'Anexar documentos'),
    ('24.png', 'Anexar documentos'),
    ('25.png', 'Resumo da solicitação'),
    ('9.png',  'Prévia de Consulta Médica'),
    ('5.png',  'Selecione uma opção:'),
    ('7.png',  'Qual categoria de Prévia'),
    ('13.png', 'Sessão Psicologia ou Psiquiatria'),
]

def primeira_banda(px, y0, y1, x0=25, x1=715, lim=140):
    dens = [sum(1 for x in range(x0, x1) if px[x, y] < lim) for y in range(y0, y1)]
    dentro = False
    for i, d in enumerate(dens):
        if d > 0 and not dentro: dentro, ini = True, i
        elif d == 0 and dentro:
            if i - ini >= 10: return dens[ini:i]
            dentro = False
    return None

def cap(seg):
    p = max(seg)
    topo = next(i for i, d in enumerate(seg) if d >= p * 0.10)
    base = max(i for i, d in enumerate(seg) if d >= p * 0.30)
    return (base - topo + 1) - (1 - seg[topo] / float(p)) * 0.5 - (1 - seg[base] / float(p)) * 0.5

vals = []
print('%-10s %-34s %8s %9s' % ('tela', 'título', 'cap px', 'corpo pt'))
for arq, titulo in TELAS:
    im = Image.open(os.path.join(CAP, arq)).convert('L')
    if im.size != (739, 1600): continue
    seg = primeira_banda(im.load(), 192, 300)
    if not seg: print('%-10s %-34s  banda não achada' % (arq, titulo[:34])); continue
    c = cap(seg); pt = c / ESCALA / CAP_EM
    vals.append(c)
    print('%-10s %-34s %8.2f %8.1f' % (arq, titulo[:34], c, pt))

if vals:
    m = sum(vals) / len(vals)
    dp = (sum((v - m) ** 2 for v in vals) / len(vals)) ** 0.5
    print('\nmédia %.2fpx ± %.2f  ->  %.1f pt ± %.1f  (%d telas)'
          % (m, dp, m / ESCALA / CAP_EM, dp / ESCALA / CAP_EM, len(vals)))
