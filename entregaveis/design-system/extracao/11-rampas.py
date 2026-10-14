#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Confere cada cor medida no app contra as rampas completas do site.

O `09-estados.py` comparava só com os tokens semânticos (brand, feedback,
text). Mas o site publica também as rampas numéricas de 50 a 950 para
cinza, azul, laranja, verde, vermelho e amarelo. Uma cor do app pode não
bater com o token semântico e mesmo assim ser um degrau declarado da
rampa, o que é coisa bem diferente de valor inventado.
"""
import json

d = json.load(open('tokens-site.json', encoding='utf-8'))
rampas = d['rampas']
sem = {}
for g in ('marca', 'texto', 'feedback', 'superficie'):
    sem.update(d.get(g, {}))

def rgb(h): return tuple(int(h.lstrip('#')[i:i+2], 16) for i in (0, 2, 4))
def neutro(h):
    r = rgb(h)
    return max(r) - min(r) < 8
def dist(a, b):
    ra, rb = rgb(a), rgb(b)
    return sum((ra[i] - rb[i]) ** 2 for i in range(3)) ** 0.5

MEDIDAS = [
    ('laranja do botão, radio e seleção', '#ff5000'),
    ('navy do botão Filtrar e do chip',   '#001e64'),
    ('cinza do botão desabilitado',       '#d2d2d2'),
    ('verde do contorno de status',       '#1f662e'),
    ('verde do ícone de sucesso',         '#00861f'),
    ('superfície secundária, home',       '#f3f5f4'),
    ('superfície secundária, telas 26/28','#f8f8f8'),
]

print('%-36s %-9s %-22s %8s' % ('medido no app', 'valor', 'degrau mais próximo', 'distância'))
for nome, h in MEDIDAS:
    todos = list(rampas.items()) + [(k, v) for k, v in sem.items()]
    # cinza só se compara com cinza: casar um neutro com um degrau de verde
    # produz par sem sentido, ainda que a distância euclidiana seja menor
    todos = [(k, v) for k, v in todos if neutro(v) == neutro(h)]
    k, v = min(todos, key=lambda kv: dist(h, kv[1]))
    dd = dist(h, v)
    if dd == 0:      ver = 'IDÊNTICO, é token declarado'
    elif dd <= 6:    ver = 'praticamente idêntico'
    elif dd <= 40:   ver = 'próximo, mas não é o degrau'
    else:            ver = 'fora da rampa'
    print('%-36s %-9s %-22s %8.1f  %s' % (nome, h.upper(), '--' + k, dd, ver))
