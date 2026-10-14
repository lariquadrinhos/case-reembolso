#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Lê os tokens que a SulAmérica publica no CSS do site.

Reconstruir cor a partir de screenshot é o melhor que dá para fazer quando
não há outra fonte. Mas o site declara o sistema inteiro em variáveis CSS,
inclusive a família tipográfica, então aqui a informação é declarada pela
própria empresa e não estimada por mim.

Ressalva que precisa acompanhar todo uso deste arquivo: **isto é o sistema
da web**. As 32 capturas são do app iOS, e os dois divergem. A divergência
é achado, não erro de medição.
"""
import json, re, urllib.request

URL = 'https://www.sulamerica.com.br/'
UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/124 Safari/537.36'

req = urllib.request.Request(URL, headers={'User-Agent': UA})
html = urllib.request.urlopen(req, timeout=40).read().decode('utf-8', 'replace')

var = {}
for k, v in re.findall(r'--([a-z0-9-]+)\s*:\s*([^;}"\']{1,80}?)\s*[;}]', html):
    var.setdefault(k, v.strip())

cor = {k: v for k, v in var.items() if k.startswith('color-') and v.startswith('#')}
fontes = sorted(set(re.findall(r'font-family\s*:\s*([^;}"\']{1,60})', html)))

def bloco(titulo, cond):
    itens = {k: v for k, v in sorted(cor.items()) if cond(k)}
    if not itens: return {}
    print('\n### %s' % titulo)
    for k, v in itens.items():
        print('   --%-44s %s' % (k, v))
    return itens

print('font-family declaradas: %s' % ', '.join(fontes))
print('variáveis de cor: %d' % len(cor))
saida = {'fonte_url': URL, 'font_family': fontes, 'total_cores': len(cor)}
saida['marca']    = bloco('marca',     lambda k: 'brand' in k)
saida['texto']    = bloco('texto',     lambda k: k.startswith('color-text'))
saida['feedback'] = bloco('feedback',  lambda k: 'feedback' in k or 'informational' in k)
saida['superficie'] = bloco('superfície', lambda k: k.startswith('color-surface'))
saida['borda']    = bloco('borda',     lambda k: k.startswith('color-border'))
saida['rampas']   = {k: v for k, v in sorted(cor.items())
                     if re.match(r'color-(orange|red|green|yellow|blue|neutral|gray|grey)-\d+$', k)}
print('\n### rampas numéricas: %d valores' % len(saida['rampas']))

json.dump(saida, open('tokens-site.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('\ntokens-site.json gravado')
