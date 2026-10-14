#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gera as composições "tela + Notas de Design" em composicoes/.

    export FIGMA_TOKEN=figd_xxx
    python3 compor.py

Renderiza cada tela e cada nota como nós separados e monta as duas sobre uma
tela de tamanho fixo, respeitando o espaçamento que elas têm no quadro. Telas
sem nota são puladas: o PNG solto delas já está na pasta de cima.

Requisitos: Pillow (pip install pillow).
"""
import io, json, os, sys, urllib.request
from PIL import Image

FILE_KEY = 'LUp4aT7fVYH4cD8ZwrHIfd'
PAGE_ID  = '33:5'
DEST     = 'composicoes'
ESCALA   = 2                       # px por pt
FUNDO    = (30, 30, 30)            # #1e1e1e, o mesmo do canvas do Figma
LARG, ALT, TOPO = 1000, 2520, 80   # tela fixa das composições, em px
LOTE     = 40                      # ids por chamada de render

token = os.environ.get('FIGMA_TOKEN')
if not token:
    sys.exit('Defina FIGMA_TOKEN primeiro.')

def api(url):
    req = urllib.request.Request(url, headers={'X-Figma-Token': token})
    with urllib.request.urlopen(req) as r:
        return json.load(r)

# 1. frames da página, com id e posição
doc = api('https://api.figma.com/v1/files/%s/nodes?ids=%s&depth=2'
          % (FILE_KEY, PAGE_ID))['nodes'][PAGE_ID]['document']
filhos = [c for c in doc['children'] if c.get('absoluteBoundingBox')]
telas = {c['name']: c for c in filhos if round(c['absoluteBoundingBox']['width']) == 390}
notas = {c['name'][len('Nota · '):]: c for c in filhos if c['name'].startswith('Nota · ')}

arquivo = {}
for linha in open('frames.tsv', encoding='utf-8'):
    _node, arq, nome = linha.rstrip('\n').split('\t')
    arquivo[nome] = arq

pares, pulados = [], []
for nome, tela in sorted(telas.items()):
    nota, arq = notas.get(nome), arquivo.get(nome)
    if not nota:   pulados.append(nome); continue
    if not arq:    pulados.append(nome + ' (fora do frames.tsv)'); continue
    pares.append((arq, tela, nota))

if not pares:
    sys.exit('Nenhum par tela/nota encontrado.')

# 2. render de cada nó, em lotes
ids = [n['id'] for _a, t, n in pares for n in (t, n)]
urls = {}
for i in range(0, len(ids), LOTE):
    fatia = ids[i:i + LOTE]
    resp = api('https://api.figma.com/v1/images/%s?ids=%s&format=png&scale=%s'
               % (FILE_KEY, ','.join(fatia), ESCALA))
    if resp.get('err'):
        sys.exit('Figma respondeu: %s' % resp['err'])
    urls.update({k: v for k, v in resp['images'].items() if v})

def baixa(node_id):
    url = urls.get(node_id)
    if not url:
        return None
    with urllib.request.urlopen(url) as r:
        return Image.open(io.BytesIO(r.read())).convert('RGB')

# 3. montagem
os.makedirs(DEST, exist_ok=True)
feito, faltou, estourou = [], [], []
for arq, tela, nota in pares:
    imgT, imgN = baixa(tela['id']), baixa(nota['id'])
    if imgT is None or imgN is None:
        faltou.append(arq); continue

    bt, bn = tela['absoluteBoundingBox'], nota['absoluteBoundingBox']
    vao = int(round((bn['y'] - (bt['y'] + bt['height'])) * ESCALA))   # respiro do quadro
    alturaTotal = TOPO + imgT.height + vao + imgN.height
    if imgN.width > LARG or alturaTotal > ALT:
        estourou.append('%s (precisa de %dx%d)' % (arq, imgN.width, alturaTotal))

    canvas = Image.new('RGB', (LARG, ALT), FUNDO)
    canvas.paste(imgT, ((LARG - imgT.width) // 2, TOPO))
    canvas.paste(imgN, ((LARG - imgN.width) // 2, TOPO + imgT.height + vao))
    canvas.save(os.path.join(DEST, arq + '.png'), optimize=True)
    feito.append(arq)

print('composições geradas: %d' % len(feito))
print('telas sem nota (puladas): %d' % len(pulados))
if faltou:   print('sem render: %s' % ', '.join(faltou))
if estourou: print('NÃO COUBE na tela fixa, aumente LARG/ALT: %s' % ', '.join(estourou))
