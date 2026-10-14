#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Inventário de cor das 32 capturas, por amostragem direta de pixel.

Conta cor exata, não estimativa visual. Superfícies chapadas grandes
sobrevivem ao redimensionamento das capturas, então os valores aqui são
confiáveis para preenchimentos; texto pequeno sofre antialiasing e por
isso é contado à parte, nunca como token.
"""
import glob, json, os
from collections import Counter, defaultdict
from PIL import Image

CAPTURAS = '../../../case-sulamerica/materiais/fluxo-atual'
MIN_PX_TELA = 900          # ruído de antialiasing abaixo disso

def hexa(c): return '#%02x%02x%02x' % c[:3]
def neutro(c): return max(c[:3]) - min(c[:3]) < 12

total_px = 0
global_cont = Counter()
por_tela = defaultdict(set)
arqs = sorted(glob.glob(os.path.join(CAPTURAS, '*.png')))

for a in arqs:
    nome = os.path.basename(a)
    im = Image.open(a).convert('RGB')
    total_px += im.size[0] * im.size[1]
    c = Counter(im.get_flattened_data() if hasattr(im, 'get_flattened_data') else im.getdata())
    for cor, n in c.items():
        global_cont[cor] += n
        if n >= MIN_PX_TELA:
            por_tela[cor].add(nome)

sig = [(c, n) for c, n in global_cont.items() if len(por_tela[c]) >= 1]
sig.sort(key=lambda t: -t[1])

def bloco(titulo, filtro, limite):
    print('\n=== %s ===' % titulo)
    print('%-9s %12s %7s  %s' % ('hex', 'pixels', 'telas', 'aparece em'))
    saida = []
    for c, n in sig:
        if not filtro(c): continue
        telas = sorted(por_tela[c])
        if not telas: continue
        print('%-9s %12d %7d  %s' % (hexa(c), n, len(telas), ', '.join(telas[:5]) + ('…' if len(telas) > 5 else '')))
        saida.append({'hex': hexa(c), 'px': n, 'telas': telas})
        if len(saida) >= limite: break
    return saida

crom = bloco('CROMÁTICAS (candidatas a token de marca e feedback)', lambda c: not neutro(c), 16)
neut = bloco('NEUTRAS (fundos, superfícies, bordas, texto)', neutro, 16)

json.dump({'escala_px_por_pt': 739.0 / 393, 'aparelho': 'iPhone 14 Pro / 15 / 16 (393 x 852 pt)',
           'total_px': total_px, 'min_px_por_tela': MIN_PX_TELA,
           'cromaticas': crom, 'neutras': neut},
          open('cores.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('\ncores.json gravado · %d capturas · %.1f M pixels lidos' % (len(arqs), total_px / 1e6))
