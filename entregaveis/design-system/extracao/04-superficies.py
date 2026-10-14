#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Separa superfície de artefato.

Contagem crua de pixel mistura preenchimento real com o halo de
antialiasing que o redimensionamento deixou em volta de texto e ícone.
Aqui só conta cor que preenche um bloco chapado de 24x24pt ou mais: se
uma cor sustenta uma área dessas, ela é superfície, não borda.

`doc gov.png` fica de fora da paleta: é screenshot do gov.br, outro app.
"""
import glob, json, os
from collections import Counter, defaultdict
from PIL import Image

CAPTURAS = '../../../case-sulamerica/materiais/fluxo-atual'
ESCALA = 739.0 / 393
BLOCO = int(round(24 * ESCALA))     # 24pt em px
FORA = {'doc gov.png'}

def hexa(c): return '#%02x%02x%02x' % c[:3]

areas = Counter()
telas = defaultdict(set)
arqs = [a for a in sorted(glob.glob(os.path.join(CAPTURAS, '*.png')))
        if os.path.basename(a) not in FORA]

for a in arqs:
    nome = os.path.basename(a)
    im = Image.open(a).convert('RGB')
    w, h = im.size
    px = im.load()
    for by in range(0, h - BLOCO, BLOCO):
        for bx in range(0, w - BLOCO, BLOCO):
            base = px[bx, by]
            uniforme = True
            for dy in range(0, BLOCO, 3):
                for dx in range(0, BLOCO, 3):
                    if px[bx + dx, by + dy] != base:
                        uniforme = False; break
                if not uniforme: break
            if uniforme:
                areas[base] += 1
                telas[base].add(nome)

print('superfícies chapadas de %dx%d px (%dpt), em %d capturas\n' % (BLOCO, BLOCO, 24, len(arqs)))
print('%-9s %8s %6s  %s' % ('hex', 'blocos', 'telas', 'aparece em'))
saida = []
for c, n in areas.most_common(22):
    t = sorted(telas[c])
    print('%-9s %8d %6d  %s' % (hexa(c), n, len(t), ', '.join(t[:6]) + ('…' if len(t) > 6 else '')))
    saida.append({'hex': hexa(c), 'blocos': n, 'telas': t})

# derivadas: cor que é outra cor sob véu preto
print('\n=== derivadas por véu preto (não são token, são composição) ===')
BASES = {'branco': (255, 255, 255), 'laranja': (255, 80, 0), 'navy': (0, 30, 100)}
for c, n in areas.most_common(22):
    for nome_b, b in BASES.items():
        for op in (0.20, 0.25, 0.30, 0.35, 0.40, 0.45, 0.50, 0.60):
            alvo = tuple(int(round(v * (1 - op))) for v in b)
            if max(abs(alvo[i] - c[i]) for i in range(3)) <= 2:
                print('   %s  =  %s sob preto %d%%   (%d blocos, %d telas)'
                      % (hexa(c), nome_b, op * 100, n, len(telas[c])))
                break

json.dump(saida, open('superficies.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
