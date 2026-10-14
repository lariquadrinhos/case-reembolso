# Extração · base de evidência do design system

Esta pasta é a base de evidência do design system. Todo valor que o sistema afirma
sobre o app sai de um destes scripts, e cada um aponta para a captura onde o valor
aparece, com a incerteza da medida junto. Quem discordar de um número pode rodar o
script e conferir.

**Fonte:** 32 capturas do fluxo real, **que não estão mais neste repositório**: elas
mostram nome, CPF, dados bancários e a foto de identidade de um usuário real. Os
números medidos a partir delas continuam aqui, nos `.json`, e os scripts continuam
legíveis; o que não dá mais é reexecutá-los sem as capturas originais.
**Método:** amostragem direta de pixel, nunca estimativa visual.

Rode na ordem. Só precisa de Pillow.

| Script | O que responde |
|---|---|
| `01-escala.py` | dimensões das capturas e margens de conteúdo |
| `02-ancora.py` | qual aparelho, e quantos px valem 1pt |
| `03-cores.py` | inventário de cor bruto, com contagem de pixel |
| `04-superficies.py` | quais cores são superfície de verdade, e quais são composição |

## 1. Escala

As capturas estão em 739 × 1600, que não é resolução de aparelho nenhum: foram
redimensionadas. A proporção sozinha não resolve, porque toda a linha de iPhones
recentes tem praticamente o mesmo formato. Três medidas de elementos que o iOS
fixa e o app não controla resolvem:

| Medida | Esperado | Medido |
|---|---|---|
| Altura total | 852pt | 851pt |
| Divisor sob a barra de navegação | 54pt de status bar + 44pt de nav bar = 184,3px | 184px, em 20 telas |
| Caixa dos dígitos do relógio | 12,1pt de cap height = 22,8px | 23–24px |

Só uma hipótese passa nas três: **iPhone 14 Pro / 15 / 16, 393 × 852pt**, a
**1,8804 px/pt**. As outras erram o divisor em 12px ou mais.

Isso importa porque toda medida daqui para frente depende dessa régua. Com a
hipótese errada, o botão de 48pt viraria 44pt.

## 2. Cor

`doc gov.png` fica fora da paleta: é captura do gov.br, outro app. Ela sozinha
respondia por 9 dos 16 tons cromáticos mais frequentes e envenenava o resultado.

Contagem crua de pixel não serve para definir token, porque mistura preenchimento
com o halo de antialiasing em volta de texto e ícone. O `04` só conta cor que
sustenta um bloco chapado de 24 × 24pt.

### Superfícies confirmadas

| Cor | Blocos | Telas | Leitura |
|---|---|---|---|
| `#FFFFFF` | 5490 | 28 | fundo padrão |
| `#F8F8F8` | 580 | 2 | superfície secundária |
| `#F4F4F4` | 82 | 1 | superfície secundária |
| `#F2F2F2` | 118 | 1 | superfície secundária |
| `#F9F9F9` | 91 | 1 | superfície secundária |
| `#D2D2D2` | 41 | 5 | botão desabilitado |
| `#FF5000` | 33 | 4 | botão primário |
| `#2B2B2B` `#6A6A6A` `#14171C` | 205 | 4 | telas de câmera e teclado |

### Marca

| Token provável | Valor | Evidência |
|---|---|---|
| laranja primário | `#FF5000` | 508.636px em **12 telas** |
| navy | `#001E64` | 39.838px em 3 telas |

`#F05223` aparece só na home, 29.105px: é o logotipo, não a cor de interface.
São dois laranjas diferentes convivendo, e a decisão de qual é canônico é do time.

### Duas cores que não são token

| Cor | O que é de fato |
|---|---|
| `#999999` | branco sob véu preto a **40%** (10, 29, 30, 8) |
| `#B2B2B2` | branco sob véu preto a **30%** (16, 4) |

Não entram na paleta como cinza: entram como opacidade de overlay. E revelam a
primeira inconsistência achada por medição: **o mesmo app usa dois véus
diferentes** para a mesma função de escurecer o fundo atrás de um modal.

## 3. Tipografia

`05-tipografia.py`. A primeira tentativa mediu toda linha de texto e o histograma
saiu contínuo, sem degraus. O motivo é aritmético e vale registrar: a 1,8804 px/pt,
**1pt de corpo vale 0,98px de altura de x**, abaixo do ruído que o redimensionamento
deixou. Duas fontes de 15 e 16pt não se separam nesta resolução, e qualquer rampa
tirada daquele histograma seria invenção com cara de medida.

O que funciona é medir o mesmo elemento repetido em muitas telas: o erro de
subpixel é aleatório e cai com a raiz do número de amostras.

| Elemento | Telas | Cap medida | Desvio | Corpo |
|---|---|---|---|---|
| Título da barra de navegação | 27 | 20,93px | 0,62px | **15,9pt ± 0,5**, ou seja 16pt |
| Rótulo do botão primário | 11 | 20,21px | 0,35px | **15,4pt ± 0,3** |
| Título de tela (H1) | 9 | ver `13-h1.py` | | **três tamanhos**, ver abaixo |

O H1 exigiu outro método. A janela por posição dava 4,09px de desvio, e a suspeita
era que ela não achava sempre o mesmo elemento. Com a lista de telas escolhida uma a
uma (`13-h1.py`), apareceu a causa real: **o app usa três tamanhos de título**, de
13,2 a 20,9pt, e um deles em laranja e peso Regular. O desvio não era ruído de
medição, era o app.

### Altura do botão primário

Medida na mesma passagem, e é a mais confiável de todas porque não depende de
tipografia: **48,2pt ± 0,8**, em 11 telas, desvio de 1,5px.

É o número que ancora a escala de espaçamento, porque é a única medida grande do
sistema que não depende de nenhuma suposição sobre tipografia.

### A razão cap/em, resolvida

A primeira versão convertia com 0,72, calibrado no relógio da status bar. Estava
errado: o relógio é desenhado pelo **iOS** em SF Pro, não pelo app, e a régua não
transferia. Com a fonte real identificada (ver seção 5), a razão passou a ser lida
do próprio arquivo do Figtree: **capHeight 700, unitsPerEm 1000, cap/em = 0,700**.

Os valores da tabela acima já usam 0,70. O título da nav bar cai em 15,9pt, ou seja
**16pt**, e o rótulo do botão em 15,4pt. Foi a correção da razão que fez o número
pousar em valor redondo, o que é um bom sinal de que a régua agora está certa.

## 4. Forma e espaço

`06-forma-espaco.py` e `07-cards.py`. Nada aqui depende de identificar a fonte
nem da razão cap/em, então são as medidas mais firmes do conjunto.

### Botão primário, 12 telas

| Medida | Valor |
|---|---|
| Altura | **48,3pt ± 0,8** |
| Raio | **24,2pt ± 0,4**, e raio ÷ (altura ÷ 2) = **1,002 ± 0,012** |
| Largura | 351,6pt ± 5,9 |
| Margem lateral | 20,7pt ± 3,0 |

A razão de 1,002 diz que é **pílula**: o raio acompanha a metade da altura, não é
um valor fixo. Isso muda o componente no Figma, que passa a ter raio relativo.

O primeiro estimador de raio devolveu 18,1pt, e estava errado. Ele lia a largura a
uma linha do topo, onde a curva já avançou, e por isso subestimava. Numa forma de
canto arredondado a meia largura a uma distância `d` do topo vale
`L/2 - r + raiz(2rd - d²)`; medir só perto do topo não resolve `r`. A versão final
amostra dezenas de distâncias e busca o raio que explica todas.

A razão importa mais que o número: um raio fixo de 24pt num botão que mude de
altura deixaria de ser pílula, e no Figma isso vira raio relativo em vez de valor
cravado.

### Cards de contorno

Medidos só em `14.png`, a única tela que os usa, então valem como indício e não
como token:

| Medida | Valor | Confiança |
|---|---|---|
| Espaçamento vertical entre cards | 12,0pt ± 0,3 | fraca, n=2 |
| Espessura da borda | 1,5pt ± 0,2 | fraca, espalhada pelo redimensionamento |
| Raio | **10,6pt** | por perfil de canto, `14-raio-card.py` |

O ajuste por mínimos quadrados não resolve o raio: a borda tem 1pt e o
redimensionamento a espalhou por três pixels misturados com branco, sem contraste
para a curva. Mas o perfil do canto resolve sem ajustar nada, e é o que o
`14-raio-card.py` faz. Vertical 19px, horizontal 21px, catetos concordando: quarto
de círculo de **10,6pt**.

## 5. Os tokens que a SulAmérica publica

`08-tokens-do-site.py`. Reconstruir cor a partir de captura é o melhor que dá para
fazer quando não existe outra fonte. Só que existe: **o site declara o sistema
inteiro em variáveis CSS**, e ali a informação é da própria empresa, não estimativa
minha.

**Fonte: `Figtree`**, declarada no CSS. É uma sem-serifa geométrica, e bate com as
letras das capturas: "a" de dois andares, "g" de cauda aberta, barrigas circulares,
terminais cortados retos.

### Tokens de marca e semânticos

| Token | Valor |
|---|---|
| `--color-brand-primary` | `#F05223` |
| `--color-brand-secondary` | `#001C5C` |
| `--color-text-primary` | `#313333` |
| `--color-text-secondary` | `#6C6E6E` |
| `--color-text-disabled` | `#949595` |
| `--color-text-link` | `#1355B4` |
| `--color-feedback-error` | `#C80505` |
| `--color-feedback-alert` | `#EF9928` |
| `--color-feedback-success` | `#04843F` |
| `--color-surface-body` | `#FFFFFF` |
| `--color-surface-on-body` | `#F3F4F4` |

São 149 variáveis de cor, com rampas de 50 a 950 para laranja, vermelho, verde e
amarelo. `tokens-site.json` guarda tudo.

### A divergência que isso revela

Eu tinha visto `#F05223` só na home do app, em 29.105 pixels, e classifiquei como
logotipo. Estava errado: é o **`brand-primary` declarado**. E o laranja que o app
usa em 12 telas de botão, `#FF5000`, **não aparece no sistema da web**.

| | Web, declarado | App iOS, medido |
|---|---|---|
| Laranja de marca | `#F05223` | `#FF5000` |
| Navy | `#001C5C` | `#001E64` |

Não é erro de medição: é o app divergindo do sistema publicado, nas duas cores
principais da marca. Para o case, isso deixa de ser detalhe técnico e vira achado.

> **Ressalva que precisa acompanhar todo uso desta seção.** Isto é o sistema da
> **web**. As 32 capturas são do **app iOS**. Onde os dois divergem, o documento
> tem que dizer qual está descrevendo, em vez de escolher um e chamar de verdade.

## Fontes descartadas

### App Store

Verificada e rejeitada, para ninguém repetir a tentativa. `SulAmérica Saúde`,
`trackId 492556516`, v10.34.0 de 02/09/2026, sete capturas.

Não servem como material de medição por três motivos somados: são **composições de
marketing**, com mockup de celular em perspectiva sobre fundo colorido e título por
cima; vêm **ampliadas** de um asset menor, no máximo 1242 × 2208; e mostram
**interface de 2021**, anterior às 32 capturas que já temos (uma delas traz um
seletor de período em "09/2021", e outra o menu antigo em pílulas navy com rótulos
em caixa alta).

Vale registrar um quase-erro: a primeira leitura de cor dessas imagens devolveu
`#FF4F00` com 1,15 milhão de pixels, e por um momento pareceu confirmar o laranja
do app contra o da web. Não confirma nada: aquele laranja é o **fundo da peça
publicitária**, não interface. Amostragem de pixel só vale quando se sabe o que o
pixel está mostrando.

O único dado aproveitável é de contexto: o app está em manutenção ativa, e são as
capturas da loja que estão paradas.

## Medidas que não fecharam

Registradas para não voltarem como suposição:

As três que estavam em aberto foram resolvidas:

| O que | Como saiu |
|---|---|
| Corpo do H1 | `13-h1.py`, telas escolhidas uma a uma: não há um H1, há três |
| Raio do card | `14-raio-card.py`, perfil de canto em vez de ajuste de curva |
| Família tipográfica | `12-identifica-fonte.py`, sobreposição de forma contra dez candidatas |

Continuam em aberto, e nenhuma se resolve com este material:

| O que | Por quê |
|---|---|
| Cor do texto de erro, do clipe e do título da nav bar | elementos finos, o antialiasing consome a cor |
| Tipografia responsiva e Dynamic Type | não há captura em outro aparelho nem com corpo aumentado |
| Animação, som e retorno tátil | screenshot não registra |

## Achados que o sistema novo precisa resolver

1. **Cinco superfícies quase idênticas** (`#F8F8F8`, `#F9F9F9`, `#F4F4F4`,
   `#F3F5F4`, `#F2F2F2`) fazendo o mesmo trabalho, cada uma em uma tela
   diferente, sem regra visível.
2. **Dois véus de modal**, 30% e 40%.
3. **Dois laranjas**, `#FF5000` na interface e `#F05223` no logotipo.

## Limites conhecidos

- **Texto pequeno não tem cor confiável.** O antialiasing do redimensionamento
  contamina a borda dos glifos. Cor de texto sai por medição no miolo de títulos
  grandes, não por contagem.
- **Só existe o que foi fotografado.** Modo escuro, componentes fora do fluxo de
  reembolso e estados não capturados ficam fora, e o documento final precisa
  dizer isso em vez de inventar.
- **A tipografia não se identifica por raster.** Dá para medir tamanho e peso,
  não para afirmar a família.
