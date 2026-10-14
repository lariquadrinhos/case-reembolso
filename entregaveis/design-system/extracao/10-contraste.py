#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Contraste WCAG dos pares que o app usa e dos que o sistema propõe.

Números de contraste são fáceis de escrever de memória e difíceis de
acertar de memória, então saem daqui calculados. Fórmula da WCAG 2.1:
luminância relativa com o degrau sRGB, e razão (L1 + 0,05) / (L2 + 0,05).
"""
def lum(h):
    h = h.lstrip('#')
    c = [int(h[i:i+2], 16) / 255.0 for i in (0, 2, 4)]
    c = [(v / 12.92 if v <= 0.04045 else ((v + 0.055) / 1.055) ** 2.4) for v in c]
    return 0.2126 * c[0] + 0.7152 * c[1] + 0.0722 * c[2]

def razao(a, b):
    la, lb = lum(a), lum(b)
    if lb > la: la, lb = lb, la
    return (la + 0.05) / (lb + 0.05)

PARES = [
    ('text/primary #313333 sobre branco',        '#313333', '#ffffff'),
    ('text/secondary #6C6E6E sobre branco',      '#6c6e6e', '#ffffff'),
    ('text/disabled #949595 sobre branco',       '#949595', '#ffffff'),
    ('branco sobre brand/primary #F05223',       '#ffffff', '#f05223'),
    ('branco sobre laranja do app #FF5000',      '#ffffff', '#ff5000'),
    ('branco sobre desabilitado do app #D2D2D2', '#ffffff', '#d2d2d2'),
    ('text/disabled sobre surface/disabled',     '#949595', '#e5e6e6'),
    ('branco sobre brand/secondary #001C5C',     '#ffffff', '#001c5c'),
    ('feedback/error #C80505 sobre branco',      '#c80505', '#ffffff'),
    ('feedback/success #04843F sobre branco',    '#04843f', '#ffffff'),
    ('text/link #1355B4 sobre branco',           '#1355b4', '#ffffff'),
    ('ESCURO text/primary #F3F4F4 sobre #191D1D',   '#f3f4f4', '#191d1d'),
    ('ESCURO text/secondary #ACAEAE sobre #191D1D', '#acaeae', '#191d1d'),
    ('ESCURO text/disabled #737575 sobre #272929',  '#737575', '#272929'),
    ('ESCURO brand #F58E70 sobre #191D1D',          '#f58e70', '#191d1d'),
    ('ESCURO error #F17474 sobre #191D1D',          '#f17474', '#191d1d'),
    ('ESCURO success #68BB8E sobre #191D1D',        '#68bb8e', '#191d1d'),
    ('ESCURO alert #F3B159 sobre #191D1D',          '#f3b159', '#191d1d'),
    ('ESCURO branco sobre botão #F05223',           '#ffffff', '#f05223'),
    ('ESCURO text/primary sobre surface/on-body',   '#f3f4f4', '#272929'),
]
print('%-44s %8s  %-8s %s' % ('par', 'razão', 'AA texto', 'AA grande'))
for nome, a, b in PARES:
    r = razao(a, b)
    print('%-44s %7.2f:1  %-8s %s' % (nome, r,
          'passa' if r >= 4.5 else 'REPROVA', 'passa' if r >= 3.0 else 'REPROVA'))
