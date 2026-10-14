#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Identifica a família tipográfica do app por sobreposição de forma.

O CSS do site declara Figtree, mas o site não é o app. Olhar as letras e
achar parecido não é evidência: quase toda sem-serifa geométrica parece
com as outras nesse tamanho.

O teste aqui é objetivo. Recorta uma palavra da captura, renderiza a
mesma palavra em cada família candidata no mesmo tamanho de caixa alta,
alinha as duas pela caixa de tinta e mede a sobreposição (interseção
sobre união dos pixels com tinta). A família certa deve ganhar por
margem, não por empate.

Uso: python3 12-identifica-fonte.py <pasta com os .ttf>
"""
import glob, os, sys
from PIL import Image, ImageDraw, ImageFont

CAP = '../../../case-sulamerica/materiais/fluxo-atual/14.png'
ESC = 6                          # amplia antes de comparar, para subpixel contar

# duas amostras independentes: uma em peso forte, outra em regular.
# Uma família só ganha de verdade se ganhar nas duas.
AMOSTRAS = [
    ('título, peso forte', 'Atenção!', (20, 205, 400, 275), ('600', '700')),
    ('corpo, peso regular', 'Para que você possa prosseguir com seu pedido',
     (20, 305, 720, 338), ('400',)),
]

def caixa_tinta(img, lim=140):
    px = img.load(); w, h = img.size
    xs = [x for y in range(h) for x in range(w) if px[x, y] < lim]
    ys = [y for y in range(h) for x in range(w) if px[x, y] < lim]
    return (min(xs), min(ys), max(xs) + 1, max(ys) + 1)

def mascara(img, lim=140):
    return img.point(lambda v: 255 if v < lim else 0).convert('1')

def pontua(caminho, PALAVRA, A, LA, HA):
    melhor = 0.0
    for tam in range(60, 320, 2):
        try: f = ImageFont.truetype(caminho, tam)
        except Exception: return None
        l, t, r, b = f.getbbox(PALAVRA)
        if r - l < 10 or b - t < 10: continue
        img = Image.new('L', (r - l + 40, b - t + 40), 255)
        ImageDraw.Draw(img).text((20 - l, 20 - t), PALAVRA, font=f, fill=0)
        c = caixa_tinta(img)
        img = img.crop(c).resize((LA, HA), Image.LANCZOS)
        B = mascara(img)
        pa, pb = A.load(), B.load()
        inter = uni = 0
        for y in range(0, HA, 2):
            for x in range(0, LA, 2):
                a, b2 = pa[x, y], pb[x, y]
                if a or b2: uni += 1
                if a and b2: inter += 1
        if uni:
            iou = inter / float(uni)
            if iou > melhor: melhor = iou
    return melhor

pasta = sys.argv[1]
for rotulo, palavra, faixa, pesos in AMOSTRAS:
    alvo = Image.open(CAP).convert('L').crop(faixa)
    alvo = alvo.crop(caixa_tinta(alvo))
    alvo = alvo.resize((alvo.width * ESC, alvo.height * ESC), Image.LANCZOS)
    A = mascara(alvo); LA, HA = A.size
    res = []
    for f in sorted(glob.glob(os.path.join(pasta, '*.ttf'))):
        if not any(f.endswith('-%s.ttf' % w) for w in pesos): continue
        v = pontua(f, palavra, A, LA, HA)
        if v: res.append((v, os.path.basename(f)[:-4]))
    res.sort(reverse=True)
    print('\n=== %s · "%s" ===' % (rotulo, palavra[:38]))
    for v, n in res[:6]:
        print('   %-20s %6.1f%%  %s' % (n, v * 100, '#' * int(v * 50)))
    if len(res) > 1:
        print('   vantagem do 1º sobre o 2º: %.1f ponto percentual' % ((res[0][0] - res[1][0]) * 100))
