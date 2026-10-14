# Design System · Reembolso SulAmérica

Sistema visual do fluxo de Reembolso, escrito a partir de duas fontes
verificáveis: os tokens que a SulAmérica publica e a medição das 32 capturas do
app iOS. Todo valor aqui aponta para uma das duas, ou declara que é escolha nossa.

## As três fontes, e o que cada uma pode dizer

Este sistema não tem uma fonte só, e é por isso que toda afirmação carrega uma
marca dizendo de onde ela veio:

| Marca | Significa | Verificável em |
|---|---|---|
| **[declarado]** | a SulAmérica publica este valor | `extracao/tokens-site.json`, lido do CSS de `sulamerica.com.br` |
| **[medido]** | o app iOS entrega este valor | `extracao/`, amostragem de pixel nas 32 capturas |
| **[decidido]** | não há token nem evidência, então é escolha nossa | a justificativa vem junto, no próprio texto |

A regra é simples e não tem exceção: **onde houver marca, há como conferir.**
Se uma linha deste documento não puder receber uma das três, ela não entra.

Um alerta que vale para o documento inteiro: **[declarado] é o sistema da web** e
**[medido] é o app iOS**. Os dois divergem em pontos importantes, e a divergência
está mapeada em `inventario-componentes.md`. Onde eles conflitam, este documento
escolhe, marca como **[decidido]** e diz o custo da escolha.

## Por onde começar

Se você quer **entender o sistema**, leia este arquivo e depois `fundamentos.md`.

Se você quer **entender como ele foi feito**, comece por `processo.md`: ele conta a
ordem do trabalho, as decisões que precisaram de julgamento e os caminhos que não
deram certo.

Se você quer **construir a biblioteca**, vá direto para `guia-figma.md`.

## No Figma

O sistema está apresentado visualmente na página **`design system`** do arquivo
[Reembolso SulAmérica](https://www.figma.com/design/LUp4aT7fVYH4cD8ZwrHIfd/Reembolso-SulAmerica?node-id=33-4):
rampas, tokens semânticos nos dois modos, espécime tipográfico, forma, espaço,
elevação, os componentes com seus estados e o painel de divergências.

A mesma página traz a **biblioteca publicável**, que não é ilustração e sim o
material que os arquivos de produto consomem:

| O que | Quanto |
|---|---|
| Variáveis de cor | 94, sendo 70 primitivas ocultas da publicação e 24 semânticas, em dois modos |
| Variáveis numéricas | 20, de espaçamento, raio, tamanho e traço |
| Text styles | 8, todos em Figtree |
| Effect styles | 2 |
| Ícones | 36, outline de 1,5pt em caixa de 24, desenhados do zero |
| Componentes | 18, cobrindo todos os padrões que aparecem nas 44 telas |

Os componentes saíram de uma auditoria, não de intuição: contei quantas telas usam
cada padrão recorrente e comparei com a biblioteca. A primeira versão cobria oito
padrões e deixava de fora o **Stepper, que está em 31 das 44 telas** e é a assinatura
do redesenho, além de Banner (22), Rodapé fixo (21) e Checkbox (16). Hoje a cobertura
é total:

| Padrão | Telas | Componente |
|---|---|---|
| Nav bar | 44 | `Nav bar` |
| Button e Link | 39 | `Button` |
| Stepper | 31 | `Stepper` |
| Card | 31 | `Card/Row`, `Card/Content` |
| Banner | 22 | `Banner` |
| Rodapé fixo | 21 | `Rodapé fixo` |
| Checkbox | 16 | `Checkbox` |
| Bottom sheet | 9 | `Bottom sheet` |
| Radio e Input | 7 | `Radio`, `Input` |
| Timeline e Linha de revisão | 3 | `Timeline`, `Linha de revisão` |
| Tab bar e Chip | 2 | `Tab bar`, `Chip` |
| Skeleton e Toast | 1 | `Skeleton`, `Toast` |

`Alvo · …` aparece nas 44 telas e continua sendo **convenção de nomenclatura**, não
componente: é o que permite auditar os 44pt mínimos de uma vez.

Os preenchimentos e contornos estão ligados às variáveis semânticas, não a valores
soltos, e as primitivas estão marcadas como ocultas: quem consome a biblioteca vê a
semântica e não consegue pegar um degrau da rampa por engano. Trocar o modo da
coleção `Color` para `Escuro` troca a paleta de todos os componentes sem duplicar
nenhum.

## Os mockups

A página **`mockups`** traz as 44 telas com a biblioteca aplicada: **2.564
preenchimentos e contornos ligados às variáveis semânticas, e zero soltos**. A
paleta final tem 14 cores, todas do sistema.

Os ícones também são reais: **148 instâncias** do conjunto `Icon`, no lugar dos
quadrados cinza e dos glifos de texto que os wireframes usavam como reserva de
espaço. Nas telas de paleta invertida, câmera e visualizador, o traço do vetor
aponta para `text/on-brand` em vez de `brand/secondary`, senão o ícone somiria no
fundo escuro.

Cinco telas não têm ícone nenhum, e está certo: são as de sucesso, a de boas-vindas
e a de carregamento.

Os PNGs em @2x estão em [`../mockups/`](../mockups/), com os mesmos nomes de arquivo
da pasta `wireframes/`, para dar a comparação lado a lado da mesma tela.

Os **wireframes continuam intactos** em sua própria página, em escala de cinza e sem
nenhuma ligação a variável. São artefatos de fases diferentes e nenhum substitui o
outro: o wireframe julga ordem, hierarquia e microcopy sem a cor interferir; o mockup
mostra o sistema aplicado.

Duas coisas ficaram só no wireframe, de propósito: as **notas de design**, que são
anotação e não interface, e os **indicadores de rolagem**, que são marcação de
revisão. Um mockup com anotação por cima não serve para julgar a tela.

O quadro é a apresentação; estes documentos são a fonte. Quando divergirem, valem os
documentos, porque é neles que cada valor carrega a marca de origem.

## Arquivos

| Arquivo | O que é |
|---|---|
| `processo.md` | como este sistema foi feito, com os becos sem saída |
| `fundamentos.md` | cor, tipografia, forma, espaço e elevação |
| `componentes.md` | especificação de cada componente, com estados e lacunas |
| `estados.md` | interação, vazio, erro, carregamento e modo escuro |
| `guia-figma.md` | como montar a biblioteca a partir de tudo isso |
| `inventario-componentes.md` | o que existe hoje no app, e como ele diverge do publicado |
| `extracao/` | os scripts que produzem a evidência, e os dados que eles geram |

## O que este sistema ainda não cobre

Os estados que as capturas não registram estão especificados em `estados.md`, todos
marcados **[decidido]** e derivados das rampas publicadas, porque ali o sistema está
projetando e não descrevendo.

Fica de fora, e sem previsão: tipografia responsiva, Dynamic Type, animação, som e
retorno tátil. Nenhum se resolve com screenshot, e entram quando houver acesso ao
app rodando.

**As ilustrações também ficam de fora, por decisão.** As telas têm oito marcações de
ilustração, mas só duas são ilustração de fato: a de boas-vindas e a do estado
vazio. Das outras seis, uma é ícone, três são capturas do gov.br e duas são conteúdo
que só existe com o app rodando, câmera e documento.

Ilustração é um ofício com sistema próprio, e o estilo de marca vem do time de
marca. Inventar um aqui seria o mesmo improviso que este documento critica no app.
As marcações ficam declaradas, com tamanho e o que precisam comunicar, para quem for
desenhar receber especificação em vez de espaço em branco.
