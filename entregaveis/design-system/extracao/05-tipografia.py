#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Corpo tipográfico por elemento identificado, com média entre telas.

Medir toda linha de texto não funciona: a 1,8804 px/pt, 1pt de corpo vale
0,98px de altura de x, abaixo do ruído do redimensionamento. Os
agrupamentos saem contínuos e qualquer rampa tirada dali seria invenção
com cara de medida.

O que funciona é medir o MESMO elemento em muitas telas e tirar média,
porque o erro de subpixel é aleatório e cai com a raiz do número de
amostras. Cada janela é primeiro segmentada em bandas de tinta contínua,
e só a banda mais alta e plausível é medida: sem isso a janela engole
ícone e divisor junto com o texto, e o desvio explode.

Razão cap/em = 0,70, lida do arquivo do Figtree (capHeight 700, upem 1000),
que é a fonte declarada no CSS do site da SulAmérica. A primeira versão usava
0,72 do SF Pro, calibrado no relógio da status bar; mas o relógio é desenhado
pelo iOS, não pelo app, e a régua não transferia.
"""
import glob, json, os
from PIL import Image

CAPTURAS = '../../../case-sulamerica/materiais/fluxo-atual'
ESCALA, CAP_EM = 739.0 / 393, 0.70   # Figtree: capHeight 700 / upem 1000
FORA = {'doc gov.png'}
escuro = lambda c: sum(c[:3]) < 430
claro  = lambda c: sum(c[:3]) > 620
lar    = lambda c: c[0] > 200 and c[1] < 130 and c[2] < 70

def melhor_banda(px, x0, x1, y0, y1, tinta, alt_min=9, alt_max=44):
    dens = [sum(1 for x in range(x0, x1) if tinta(px[x, y])) for y in range(y0, y1)]
    bandas, dentro, ini = [], False, 0
    for i, d in enumerate(dens):
        if d > 0 and not dentro: dentro, ini = True, i
        elif d == 0 and dentro:
            dentro = False; bandas.append((ini, i))
    if dentro: bandas.append((ini, len(dens)))
    cands = []
    for a, b in bandas:
        alt = b - a
        if not (alt_min <= alt <= alt_max): continue
        seg = dens[a:b]
        pico = max(seg)
        if pico < 6: continue
        largura = sum(1 for d in seg if d >= pico * 0.15)
        if largura < 4: continue
        cands.append((pico * alt, seg))
    if not cands: return None
    seg = max(cands)[1]
    pico = max(seg)
    topo = next(i for i, d in enumerate(seg) if d >= pico * 0.10)
    base = max(i for i, d in enumerate(seg) if d >= pico * 0.30)
    if base - topo < 5: return None
    return (base - topo + 1) - (1 - seg[topo] / float(pico)) * 0.5 - (1 - seg[base] / float(pico)) * 0.5

def faixa_laranja(px):
    for y in range(1596, 1150, -2):
        if sum(1 for x in range(80, 660, 4) if lar(px[x, y])) > 100:
            fim = y
            while y > 1150 and sum(1 for x in range(80, 660, 4) if lar(px[x, y])) > 100:
                y -= 2
            return y, fim
    return None

arqs = [a for a in sorted(glob.glob(os.path.join(CAPTURAS, '*.png')))
        if os.path.basename(a) not in FORA and Image.open(a).size == (739, 1600)]
alvos = {}
for a in arqs:
    nome = os.path.basename(a)
    px = Image.open(a).convert('RGB').load()
    for rot, args in [
        ('título da nav bar',        (150, 600, 100, 180, escuro)),
        ('título de tela (H1)',      (30, 709, 195, 285, escuro)),
    ]:
        c = melhor_banda(px, *args)
        if c: alvos.setdefault(rot, []).append(c)
    fl = faixa_laranja(px)
    if fl:
        y0, y1 = fl
        if y1 - y0 > 40:
            c = melhor_banda(px, 100, 640, y0 + 10, y1 - 10, claro)
            if c: alvos.setdefault('rótulo do botão primário', []).append(c)
            alvos.setdefault('_altura do botão (px)', []).append(y1 - y0)

print('%-28s %6s %10s %8s %14s' % ('elemento', 'telas', 'cap média', 'desvio', 'corpo'))
saida = {}
for k in ['título da nav bar', 'título de tela (H1)', 'rótulo do botão primário']:
    v = alvos.get(k)
    if not v: print('%-28s   sem detecção' % k); continue
    m = sum(v) / len(v)
    dp = (sum((c - m) ** 2 for c in v) / len(v)) ** 0.5
    print('%-28s %6d %8.2fpx %7.2fpx %7.1f pt ± %.1f'
          % (k, len(v), m, dp, m / ESCALA / CAP_EM, dp / ESCALA / CAP_EM))
    saida[k] = {'telas': len(v), 'cap_px': round(m, 2), 'desvio_px': round(dp, 2),
                'corpo_pt': round(m / ESCALA / CAP_EM, 1),
                'incerteza_pt': round(dp / ESCALA / CAP_EM, 1)}

alt = alvos.get('_altura do botão (px)')
if alt:
    m = sum(alt) / len(alt)
    dp = (sum((c - m) ** 2 for c in alt) / len(alt)) ** 0.5
    print('\naltura do botão primário: %.1fpx ± %.1f  ->  %.1f pt ± %.1f  (%d telas)'
          % (m, dp, m / ESCALA, dp / ESCALA, len(alt)))
    saida['altura do botão primário'] = {'telas': len(alt), 'pt': round(m / ESCALA, 1),
                                          'incerteza_pt': round(dp / ESCALA, 1)}

json.dump({'escala_px_pt': ESCALA, 'cap_em': CAP_EM, 'elementos': saida},
          open('tipografia.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
