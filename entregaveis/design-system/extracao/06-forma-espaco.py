#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Geometria: raio de canto, altura e margens do botão primário.

Nada aqui depende de identificar a fonte nem da razão cap/em: são medidas
de forma, e por isso saem firmes.

O raio não pode ser lido de uma linha só. Numa forma de canto arredondado,
a meia largura a uma distância d do topo vale (L/2 - r + raiz(2rd - d^2)),
então amostrar perto do topo subestima r: a curva já avançou. Aqui a meia
largura é medida em várias distâncias e o r que melhor explica todas elas
é achado por busca, o que também revela se a forma é pílula ou raio fixo.
"""
import glob, json, math, os
from PIL import Image

CAPTURAS = '../../../case-sulamerica/materiais/fluxo-atual'
ESCALA = 739.0 / 393
FORA = {'doc gov.png'}
lar = lambda c: c[0] > 210 and c[1] < 120 and c[2] < 60

def blob(px, w, h):
    faixa = []
    for y in range(h - 4, int(h * 0.55), -1):
        xs = [x for x in range(w) if lar(px[x, y])]
        if len(xs) > 200: faixa.append((y, min(xs), max(xs)))
    if len(faixa) < 40: return None
    ys = [y for y, _, _ in faixa]
    y0, y1 = min(ys), max(ys)
    if y1 - y0 < 40: return None
    meio = (y0 + y1) // 2
    xs = [x for x in range(w) if lar(px[x, meio])]
    return y0, y1, min(xs), max(xs)

def ajusta_raio(px, y0, x0, x1, h_meia):
    L = x1 - x0 + 1
    amostras = []
    for d in range(1, int(h_meia * 0.9)):
        xs = [x for x in range(x0 - 6, x1 + 7) if lar(px[x, y0 + d])]
        if not xs: continue
        amostras.append((d + 0.5, (max(xs) - min(xs) + 1) / 2.0))
        if len(amostras) >= 30: break
    if len(amostras) < 8: return None
    melhor, err_min = None, None
    r = 3.0
    while r <= h_meia + 2:
        err = 0.0
        for d, hw in amostras:
            prev = L / 2.0 - r + (math.sqrt(max(0.0, 2 * r * d - d * d)) if d < r else r)
            err += (hw - prev) ** 2
        if err_min is None or err < err_min:
            err_min, melhor = err, r
        r += 0.25
    return melhor

med = {k: [] for k in ['altura', 'largura', 'margem_esq', 'raio', 'razao']}
arqs = [a for a in sorted(glob.glob(os.path.join(CAPTURAS, '*.png')))
        if os.path.basename(a) not in FORA and Image.open(a).size == (739, 1600)]
for a in arqs:
    im = Image.open(a).convert('RGB'); px = im.load(); w, h = im.size
    b = blob(px, w, h)
    if not b: continue
    y0, y1, x0, x1 = b
    alt = y1 - y0 + 1
    r = ajusta_raio(px, y0, x0, x1, alt / 2.0)
    med['altura'].append(alt); med['largura'].append(x1 - x0 + 1); med['margem_esq'].append(x0)
    if r:
        med['raio'].append(r); med['razao'].append(r / (alt / 2.0))

def stat(v):
    m = sum(v) / len(v)
    return m, (sum((x - m) ** 2 for x in v) / len(v)) ** 0.5

print('=== botão primário · %d telas ===' % len(med['altura']))
saida = {}
for k in ['altura', 'largura', 'margem_esq', 'raio']:
    if not med[k]: continue
    m, dp = stat(med[k])
    print('%-12s %8.1f px ± %-5.2f  ->  %6.1f pt ± %.1f' % (k, m, dp, m / ESCALA, dp / ESCALA))
    saida[k] = {'px': round(m, 1), 'pt': round(m / ESCALA, 1), 'incerteza_pt': round(dp / ESCALA, 1)}
if med['razao']:
    m, dp = stat(med['razao'])
    forma = 'pílula (raio = metade da altura)' if m > 0.92 else 'raio fixo'
    print('\nraio / (altura/2) = %.3f ± %.3f  ->  %s' % (m, dp, forma))
    saida['forma'] = forma
json.dump(saida, open('geometria.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
