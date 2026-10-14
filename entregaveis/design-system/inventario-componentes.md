# Inventário de componentes · app iOS de Reembolso

Levantado a partir das 32 capturas do fluxo real (removidas do repositório por conterem dados pessoais),
com as cores medidas por `extracao/09-estados.py` e comparadas com os tokens que a
SulAmérica publica no CSS do site (`extracao/tokens-site.json`).

**As duas fontes não são a mesma coisa.** Os tokens são do sistema **web**; as
capturas são do **app iOS**. Onde divergem, as duas colunas ficam lado a lado e a
diferença é o achado, não um erro a corrigir na medição.

Só entra aqui o que aparece nas capturas. Componente não fotografado não existe
neste documento, e estado não fotografado é listado como lacuna em vez de suposto.

---

## Confronto de cor

| Onde | App, medido | Web, declarado | Distância |
|---|---|---|---|
| Botão primário, preenchimento | `#FF5000` (12 telas) | `--color-brand-primary` `#F05223` | 38 |
| Radio marcado | `#FF5000` (44.036px) | `--color-brand-primary` `#F05223` | 38 |
| Borda de card selecionado | `#FF5000` (38.576px) | `--color-brand-primary` `#F05223` | 38 |
| Botão navy ("Filtrar") | `#001E64` (36.108px) | `--color-blue-500` `#001E64` | **0** |
| Ícone de categoria | `#1A365D` (2.517px) | `--color-blue-500` `#001E64` | 37 |
| Botão desabilitado | `#D2D2D2` (52.808px) | **não existe token equivalente** | 58 do mais próximo |

O laranja é o caso mais grave: **a cor de marca do app não é a cor de marca
publicada**, e a diferença de 38 é visível a olho nu, não arredondamento. Ele
também não é degrau nenhum da rampa laranja publicada: fica a 29,9 do `orange-600`,
o mais próximo.

**O navy não é divergência.** `#001E64` é exatamente `--color-blue-500`, distância
zero. O que a marca chama de `brand-secondary` é o `blue-600`, o degrau vizinho.
São duas escolhas dentro da mesma rampa declarada, não uma cor inventada.

O cinza de desabilitado é o segundo: o sistema da web tem `--color-text-disabled`
para texto, mas **nenhum token de superfície desabilitada**. O app inventou um.

Três medições ficaram sem amostra suficiente e por isso não entram: cor do texto de
erro, do círculo do ícone de clipe e do título da nav bar. São elementos pequenos, e
o antialiasing do redimensionamento consome a cor real. Ficam como lacuna.

## Quarta divergência: o título de tela

**[medido]** Nove telas com título, três tamanhos: 13,2pt nas telas 22 e 24, algo
entre 17,0 e 17,8pt em sete telas, e 20,9pt na tela 9. A tela 9 ainda escreve o
título em laranja e peso Regular, enquanto as outras usam escuro e Bold.

É o mesmo padrão dos cinco cinzas, dos dois véus e dos três verdes: um papel só,
resolvido de várias maneiras.

---

## Componentes

### 1. Botão primário (largura total)

**Telas:** 6, 9, 11, 12, 14, 15, 18, 21, 23, 24, 25, 26, 31, 33.

| Propriedade | Valor |
|---|---|
| Altura | 48,3pt ± 0,8 |
| Forma | pílula, raio = metade da altura (razão medida 1,002 ± 0,012) |
| Preenchimento ativo | `#FF5000` |
| Preenchimento desabilitado | `#D2D2D2` |
| Corpo do rótulo | 15,4pt ± 0,3 |

**Estados capturados:** ativo, desabilitado.
**Lacunas:** pressionado, carregando, foco.

**Inconsistências.** Em `6.png` o botão primário é **navy sólido** (`Filtrar`), não
laranja: a mesma hierarquia com duas cores diferentes. Em `9.png` o rótulo está em
**caixa alta** (`CALCULAR`) enquanto todos os outros usam caixa mista.

### 2. Botão de texto

**Telas:** 5, 8, 10, 12, 22, 24.

Convivem dois tratamentos sem regra aparente:

| Tratamento | Onde |
|---|---|
| Caixa alta, laranja, sem sublinhado | `ATUALIZAR DADOS` (12), `FECHAR` e `ME LEVE ATÉ LÁ` (8), `FECHAR` e `VER` (10) |
| Caixa mista, laranja, sublinhado | `Ver detalhes` (5), `Ver` e `Anexar` (22, 24) |

**Estados capturados:** normal, desabilitado (o `Ver` cinza em 22, antes de haver
arquivo).

### 3. Card de lista com chevron

**Telas:** 4, 7, 13.

Título, subtítulo opcional e `›` à direita. Em `4.png` sem ícone; em `7.png` e
`13.png` com ícone à esquerda.

**Inconsistência.** As telas 7 e 13 são a mesma lista de categorias renderizada de
dois jeitos: em `7.png` os ícones vêm dentro de um círculo azul preenchido, em
`13.png` são outline sem fundo. Duas versões do mesmo componente no mesmo fluxo.

### 4. Card de conteúdo com borda

**Telas:** 14 (borda laranja), 5 e 25 (borda cinza).

| Propriedade | Valor | Confiança |
|---|---|---|
| Espaçamento vertical entre cards | 12,0pt ± 0,3 | fraca, n=2 |
| Espessura da borda | 1,5pt ± 0,2 | fraca |
| Raio | não resolvido | ver `extracao/README.md` |

### 5. Campo de texto

**Telas:** 9, 15, 20, 21, 32, 33.

Rótulo acima em corpo menor, valor abaixo, linha inferior de 1pt. Sem caixa.

**Estados capturados:** vazio com placeholder (`XX.XXX.XXX/0001-XX` em 20),
preenchido, erro (32), select com `⌄` (9, 15).
**Lacunas:** foco, desabilitado, somente leitura.

**Observação.** O placeholder de 20 usa a máscara como texto de exemplo. Isso é
padrão discutível, mas é o que está lá.

### 6. Radio

**Tela:** 15. Marcado em `#FF5000`. Três opções, seleção única.
**Lacunas:** desabilitado, erro.

### 7. Seletor de tipo de documento

**Telas:** 19, 20, 21, 33. Dois cards lado a lado com ilustração, borda laranja
quando selecionado.
**Estados capturados:** nenhum selecionado (19), selecionado à esquerda (20),
selecionado à direita (21, 33).

### 8. Barra de navegação

**Telas:** quase todas. Chevron de voltar à esquerda, título centralizado, ícone de
grade à direita.

| Propriedade | Valor |
|---|---|
| Altura | 44pt (padrão iOS, confirmado pelo divisor em 184px) |
| Corpo do título | 15,9pt ± 0,5, ou seja 16pt |

### 9. Modal

**Telas:** 10 (documentação necessária), 16 (picker de sessões), 29 e 30 (NPS).

**Véu de escurecimento, e aqui está a segunda inconsistência achada por medição:**

| Véu | Telas |
|---|---|
| Preto a 40% | 8, 10, 29, 30 |
| Preto a 30% | 4, 16 |

O mesmo app escurece o fundo de duas maneiras diferentes.

### 10. Anexo de documento

**Telas:** 22, 24. Ícone de clipe dentro de círculo navy preenchido, título,
subtítulo de estado, ações `Ver` e `Anexar`.

**Observação de sistema.** O círculo navy preenchido é o único lugar da interface
que usa "círculo colorido com ícone dentro". Todo o resto usa ícone solto. É o
antipadrão que já estava anotado nos wireframes.

### 11. Estado de carregamento

**Telas:** 4 (parcial), 28 (`Validando...` com spinner laranja).
**Lacuna:** não há skeleton em nenhuma tela; o carregamento é sempre spinner.

### 12. Captura de identidade

**Tela:** 27. Overlay escuro com guia de rosto e instrução.
**Observação.** Única tela do fluxo que inverte a paleta.

---

## Estados que o fluxo inteiro não mostra

Nenhuma das 32 capturas registra:

- botão pressionado ou em carregamento;
- campo em foco;
- qualquer componente desabilitado que não seja botão;
- estado vazio de lista (o histórico aparece sempre preenchido);
- erro de rede ou falha de carregamento;
- modo escuro.

Isso limita o que o design system pode afirmar. Onde o sistema novo precisar
definir esses estados, a definição é **decisão de projeto**, não descrição do que
existe, e o documento tem que marcar a diferença.
