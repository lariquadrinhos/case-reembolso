#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Geometria dos cards de contorno: borda, raio, margem e espaçamento.

A borda do card tem 1pt e o redimensionamento a espalhou por cerca de três
pixels misturados com branco, então o filtro não pode exigir #FF5000 puro:
exige apenas que o pixel puxe para o laranja (r bem acima de b). Sem isso
não se detecta card nenhum, que foi o resultado da primeira tentativa.

Entre a borda inferior de um card e a superior do próximo está o
espaçamento vertical da lista. O raio usa o mesmo ajuste por várias
amostras do 06, porque medir numa linha só subestima o valor.
"""
import glob, json, math, os
from collections import Counter
from PIL import Image

CAPTURAS = '../../../case-sulamerica/materiais/fluxo-atual'
ESCALA = 739.0 / 393
FORA = {'doc gov.png'}
alaranjado = lambda c: c[0] - c[2] > 35 and c[0] > 170

def linhas_cheias(px, w, h):
    out = []
    for y in range(190, h - 40):
        xs = [x for x in range(25, w - 25) if alaranjado(px[x, y])]
        if len(xs) > 380 and (max(xs) - min(xs)) > 480:
            out.append((y, min(xs), max(xs), len(xs)))
    grupos, atual = [], []
    for it in out:
        if atual and it[0] - atual[-1][0] <= 2: atual.append(it)
        else:
            if atual: grupos.append(atual)
            atual = [it]
    if atual: grupos.append(atual)
    return grupos

def raio(px, y_topo, x0, x1, limite):
    L = x1 - x0 + 1
    am = []
    for d in range(2, limite):
        xs = [x for x in range(x0 - 10, x1 + 11) if alaranjado(px[x, y_topo + d])]
        if len(xs) < 2: continue
        am.append((d + 0.5, (max(xs) - min(xs) + 1) / 2.0))
    if len(am) < 6: return None
    melhor, emin, r = None, None, 2.0
    while r <= 50:
        e = sum((hw - (L / 2.0 - r + (math.sqrt(max(0.0, 2 * r * d - d * d)) if d < r else r))) ** 2
                for d, hw in am)
        if emin is None or e < emin: emin, melhor = e, r
        r += 0.25
    return melhor

esp, raios, margens, esp_borda, alturas = [], [], [], [], []
telas = set()
for a in [x for x in sorted(glob.glob(os.path.join(CAPTURAS, '*.png')))
          if os.path.basename(x) not in FORA and Image.open(x).size == (739, 1600)]:
    im = Image.open(a).convert('RGB'); px = im.load(); w, h = im.size
    g = [x for x in linhas_cheias(px, w, h) if len(x) <= 5]   # só bordas finas
    if len(g) < 2: continue
    telas.add(os.path.basename(a))
    for grupo in g:
        esp_borda.append(len(grupo)); margens.append(grupo[0][1])
    for i in range(0, len(g) - 1, 2):
        topo, base = g[i], g[i + 1]
        alt = base[-1][0] - topo[0][0]
        if not (60 < alt < 700): continue
        alturas.append(alt)
        r = raio(px, topo[0][0], topo[0][1], topo[0][2], min(36, alt // 3))
        if r: raios.append(r)
        if i + 2 < len(g): esp.append(g[i + 2][0][0] - base[-1][0])

def stat(v):
    m = sum(v) / len(v); return m, (sum((x - m) ** 2 for x in v) / len(v)) ** 0.5

print('cards de contorno em %d telas: %s\n' % (len(telas), ', '.join(sorted(telas))))
saida = {}
for nome, v in [('raio', raios), ('espaçamento entre cards', esp),
                ('margem esquerda', margens), ('espessura da borda', esp_borda),
                ('altura do card', alturas)]:
    if not v: continue
    m, dp = stat(v)
    print('%-24s n=%-4d %7.1f px ± %-5.2f  ->  %6.1f pt ± %.1f' % (nome, len(v), m, dp, m / ESCALA, dp / ESCALA))
    saida[nome] = {'n': len(v), 'pt': round(m / ESCALA, 1), 'incerteza_pt': round(dp / ESCALA, 1)}
if esp:
    print('\nespaçamentos observados: %s' % ', '.join(
        '%dpt x%d' % kv for kv in sorted(Counter(round(x / ESCALA) for x in esp).items())))
json.dump(saida, open('cards.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
