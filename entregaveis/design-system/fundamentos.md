# Fundamentos

Toda linha carrega **[declarado]**, **[medido]** ou **[decidido]**. A convenção
está no `README.md` desta pasta.

---

# 1. Cor

## 1.1 Marca

| Token | Valor | Origem |
|---|---|---|
| `brand/primary` | `#F05223` | **[declarado]** `--color-brand-primary` |
| `brand/secondary` | `#001C5C` | **[declarado]** `--color-brand-secondary`, é o `blue-600` |
| `brand/tertiary-1` | `#1769E0` | **[declarado]** `--color-brand-tertiary-1` |
| `brand/tertiary-2` | `#FC9C26` | **[declarado]** `--color-brand-tertiary-2` |

### O conflito do laranja, e por que escolhemos assim

**[medido]** O app usa `#FF5000` no botão primário (12 telas), no radio marcado
(44.036px) e na borda de card selecionado (38.576px). A distância para o
`#F05223` publicado é de **38**, visível a olho nu.

**[decidido] O sistema adota `#F05223`, o valor publicado.** Três razões:

1. É o que a própria SulAmérica declara como `brand-primary`, e um design system que
   contradiz a declaração da empresa não serve como fonte de verdade.
2. `#FF5000` aparece em três componentes com a mesma distância, o que indica um
   valor antigo carregado no app, não uma decisão de plataforma.
3. A web já está em `#F05223`. Alinhar o app fecha a diferença; alinhar a web ao app
   quebraria o site inteiro.

**O custo é real e precisa de aprovação de marca.** `#FF5000` é o laranja que os
usuários do app veem hoje, e trocá-lo muda a percepção da cor da marca no canal
mais usado. Esta decisão não é técnica: é de marca, e está aqui como recomendação
fundamentada, não como fato consumado.

Enquanto não houver decisão, **a regra é usar `#F05223` em tela nova** e tratar
`#FF5000` como dívida a migrar, nunca como alternativa válida.

## 1.2 Texto

| Token | Valor | Origem |
|---|---|---|
| `text/primary` | `#313333` | **[declarado]** `--color-text-primary` |
| `text/secondary` | `#6C6E6E` | **[declarado]** `--color-text-secondary` |
| `text/disabled` | `#949595` | **[declarado]** `--color-text-disabled` |
| `text/link` | `#1355B4` | **[declarado]** `--color-text-link` |
| `text/brand` | `#F05223` | **[declarado]** `--color-text-brand` |
| `text/on-brand` | `#FFFFFF` | **[decidido]** texto sobre preenchimento de marca |

`text/on-brand` não existe como token publicado, mas o app usa branco sobre laranja
em todos os botões primários. Contraste de branco sobre `#F05223`: **3,54:1**. Passa
em AA para texto grande (18pt, ou 14pt em negrito) e **reprova para texto normal**.
O rótulo do botão tem 15,4pt em peso forte, então fica na fronteira. Ver 1.6.

## 1.3 Feedback

| Token | Valor | Origem |
|---|---|---|
| `feedback/error` | `#C80505` | **[declarado]** `--color-feedback-error` |
| `feedback/alert` | `#EF9928` | **[declarado]** `--color-feedback-alert` |
| `feedback/success` | `#04843F` | **[declarado]** `--color-feedback-success` |
| `feedback/info` | `#1355B4` | **[declarado]** `--color-feedback-informational` |

Cada um tem superfície clara correspondente, também declarada:

| Token | Valor |
|---|---|
| `surface/error` | `#FDE8E8` |
| `surface/alert` | `#FDF4E7` |
| `surface/success` | `#E6F4ED` |
| `surface/info` | `#DFEAFC` |

## 1.4 Superfície

| Token | Valor | Origem |
|---|---|---|
| `surface/body` | `#FFFFFF` | **[declarado]** `--color-surface-body` |
| `surface/on-body` | `#F3F4F4` | **[declarado]** `--color-surface-on-body` |
| `surface/on-body-brand` | `#FFF6EB` | **[declarado]** `--color-surface-on-body-brand` |

### As cinco superfícies do app

**[medido]** O app usa cinco cinzas quase idênticos como superfície secundária, cada
um em telas diferentes e sem regra visível: `#F8F8F8`, `#F9F9F9`, `#F4F4F4`,
`#F3F5F4` e `#F2F2F2`.

**[decidido] Todos colapsam em `surface/on-body` `#F3F4F4`.** Nenhum dos cinco
carrega significado próprio: são o mesmo papel de fundo secundário, e a variação é
deriva. `#F3F5F4`, o da home, está a distância 2 do token publicado, o que reforça
que a intenção sempre foi uma só.

## 1.5 Estado desabilitado

**[medido]** O botão desabilitado do app preenche com `#D2D2D2` e escreve em branco.
Contraste de branco sobre `#D2D2D2`: **1,51:1**. O rótulo é praticamente ilegível, e
o usuário não consegue ler o que o botão faria se estivesse ativo.

**[declarado]** O sistema da web tem `--color-text-disabled` para texto, mas
**nenhum token de superfície desabilitada**. É uma lacuna do sistema publicado, não
uma escolha do app.

**[decidido]** O sistema define o par:

| Token | Valor | Contraste |
|---|---|---|
| `surface/disabled` | `#E5E6E6` | do sistema publicado, é o `neutral-200` da rampa |
| `text/disabled` sobre ele | `#949595` | **2,40:1** |

Continua abaixo de 4,5:1, e isso é intencional: controle desabilitado precisa
**parecer** desabilitado, e a WCAG isenta componentes inativos do critério de
contraste. Mas 2,40:1 é legível e 1,51:1 não é. A troca corrige a falha real sem
perder o sinal de indisponibilidade.

## 1.6 Contraste, o que passa e o que não passa

**[medido]** Verificação dos pares que o app usa hoje:

Calculados por `extracao/10-contraste.py`, não escritos de memória.

| Par | Contraste | AA texto normal | AA texto grande |
|---|---|---|---|
| `#313333` sobre branco | 12,71:1 | passa | passa |
| `#001C5C` sobre branco | 15,90:1 | passa | passa |
| `#1355B4` sobre branco | 7,03:1 | passa | passa |
| `#C80505` sobre branco | 6,03:1 | passa | passa |
| `#6C6E6E` sobre branco | 5,13:1 | passa | passa |
| `#04843F` sobre branco | 4,80:1 | passa | passa |
| Branco sobre `#F05223` | 3,54:1 | **reprova** | passa |
| Branco sobre `#FF5000` | 3,28:1 | **reprova** | passa |
| `#949595` sobre branco | 3,00:1 | **reprova** | passa |
| `#949595` sobre `#E5E6E6` | 2,40:1 | **reprova** | **reprova** |
| Branco sobre `#D2D2D2` | 1,51:1 | **reprova** | **reprova** |

**[decidido]** Duas regras saem daí:

1. **Texto branco sobre laranja só em 16pt semibold ou maior.** É a condição de
   "texto grande" da WCAG, e é o que o botão primário já cumpre por folga se o
   rótulo subir de 15,4 para 16pt. Abaixo disso, usar `text/primary` sobre superfície
   clara.
2. **`text/disabled` nunca em texto corrido.** Sobre branco ele dá 3,00:1, que
   reprova para texto normal. Ele existe para rótulo de controle inativo, sobre
   `surface/disabled`, e nunca para conteúdo que o usuário precise ler.

---

# 2. Tipografia

## 2.1 Família

**[declarado]** `Figtree`, declarada no CSS do site. Métricas lidas do próprio
arquivo da fonte: `unitsPerEm` 1000, `capHeight` 700, `xHeight` 500.

**[medido] E o app usa a mesma família.** Confirmado por sobreposição de forma, não
por semelhança visual: `extracao/12-identifica-fonte.py` recorta uma palavra da
captura, renderiza a mesma palavra em dez famílias candidatas ajustadas à mesma
altura de caixa alta e mede a interseção sobre união dos pixels com tinta.

| Amostra | 1º lugar | 2º lugar | Vantagem |
|---|---|---|---|
| `Atenção!`, peso forte | Figtree 700, **87,8%** | Montserrat 700, 83,0% | 4,8 pontos |
| Linha de corpo, Regular | Figtree 400, **79,3%** | DM Sans 400, 57,9% | **21,4 pontos** |

A primeira amostra é curta e a margem fica apertada, porque nesse tamanho quase toda
sem-serifa geométrica se parece. A segunda, com uma frase inteira, decide: 21 pontos
de vantagem não é coincidência. Nos dois testes o Figtree ficou em primeiro, e no
primeiro teste ele ocupou também o segundo lugar com o outro peso.

## 2.2 Corpos

Dois valores são medidos. O resto é rampa.

| Papel | Corpo | Peso | Origem |
|---|---|---|---|
| `type/title-screen` | 20pt | Bold | **[decidido]**, ver abaixo |
| `type/title-section` | 20pt | Bold | **[decidido]** |
| `type/title-nav` | 16pt | Semibold | **[medido]** 15,9pt ± 0,5 em 27 telas |
| `type/body` | 16pt | Regular | **[decidido]** |
| `type/button` | 16pt | Semibold | **[medido]** 15,4pt ± 0,3, arredondado para cima, ver 1.6 |
| `type/caption` | 14pt | Regular | **[decidido]** |
| `type/label` | 12pt | Medium | **[decidido]** |

**[decidido]** A rampa é 12 / 14 / 16 / 20 / 24. Ela sai dos dois valores medidos:
ambos pousaram em 16pt, então 16 é a base, e a rampa cresce e decresce a partir
dela em passos que a Figtree distingue bem em tela pequena.

O rótulo do botão mediu 15,4 e a rampa manda 16. A diferença de meio ponto está
dentro da incerteza da medição, **e subir resolve o contraste**: em 16pt semibold o
texto branco sobre laranja entra na regra de texto grande da WCAG. Arredondar para
baixo manteria a reprovação.

## 2.3 O título de tela, e por que ele não tinha um tamanho

**[medido]** Medido em nove telas escolhidas uma a uma, por
`extracao/13-h1.py`. O resultado não é um número, são três:

| Corpo | Telas |
|---|---|
| ~13,2pt | 22, 24 |
| ~17,0 a 17,8pt | 5, 7, 14, 15, 19, 20, 25 |
| ~20,9pt | 9 |

E não é só o tamanho: a tela 9 escreve o título em **laranja e peso Regular**,
enquanto as outras usam escuro e Bold.

Isso explica por que a primeira tentativa de medição deu desvio de 4,09px. Não era
só a janela errando de elemento: **os títulos variam de verdade**.

**[decidido] O sistema fixa 20pt Bold.** O grupo dominante mede 17,0 a 17,8, e 18pt
seria o arredondamento fiel. Mas 18 fica a dois pontos do título da nav bar e do
corpo, ambos em 16, e dois pontos não estabelecem hierarquia em tela pequena. Os
20pt abrem um degrau que se lê, e a rampa já tem esse valor.

---

# 3. Forma

| Token | Valor | Origem |
|---|---|---|
| `radius/button` | metade da altura, pílula | **[medido]** razão 1,002 ± 0,012 em 12 telas |
| `radius/card` | 12pt | **[medido]** 10,6pt, arredondado para a escala |
| `stroke/hairline` | 1pt | **[medido]** 1,5pt ± 0,2, arredondado |

**[medido]** O botão é pílula de verdade: o raio acompanha a metade da altura, não é
um número fixo. No Figma isso vira raio relativo, não um valor cravado.

**[medido] O raio do card saiu por perfil de canto**, em `extracao/14-raio-card.py`.
O ajuste por mínimos quadrados não convergia porque a borda de 1pt se espalhou por
três pixels no redimensionamento. O perfil dispensa ajuste: para cada linha a partir
do topo, onde a tinta começa. A coordenada cai enquanto a curva avança e trava na
lateral reta.

Vertical 19px, horizontal 21px. Os dois catetos concordam dentro do erro, o que
confirma quarto de círculo, e a média dá **10,6pt**. O token fica em `12pt`, o degrau
vizinho da escala de espaçamento, porque 10,6 não pertence a nenhuma escala e a
diferença de 1,4pt não se vê.

---

# 4. Espaço

| Token | Valor | Origem |
|---|---|---|
| `size/button-height` | 48pt | **[medido]** 48,3pt ± 0,8 em 12 telas |
| `space/list-gap` | 12pt | **[medido]** 12,0pt ± 0,3, amostra pequena (n=2) |
| `space/screen-margin` | 20pt | **[medido]** 20,7pt ± 3,0, desvio alto |
| `size/tap-target` | 44pt | **[decidido]** mínimo da Human Interface Guidelines |

**[decidido]** A escala de espaçamento é **4 / 8 / 12 / 16 / 20 / 24 / 32**. Os dois
valores medidos (12 e 20) caem nela sem forçar, e a base de 4 acomoda os dois.

---

# 5. Elevação e véu

**[medido]** O app escurece o fundo de modal de duas maneiras: preto a **40%** nas
telas 8, 10, 29 e 30, e preto a **30%** nas telas 4 e 16.

**[decidido] O véu é preto a 40%.** É o valor majoritário, é o que cobre os modais de
decisão (termo, NPS), e 30% deixa o conteúdo de trás competir com o do modal. Um só
valor, sem variação por contexto.

> Estes dois valores não estavam visíveis para ninguém. Saíram da medição: `#999999`
> e `#B2B2B2` em áreas chapadas grandes são exatamente branco sob véu de 40% e de
> 30%. Se tivessem entrado na paleta como cinzas, o sistema nasceria com dois tokens
> falsos.

---

# 6. O que este documento não cobre

Nenhuma das 32 capturas registra botão pressionado ou carregando, campo em foco,
componente desabilitado que não seja botão, lista vazia, erro de rede ou modo
escuro. Definir esses estados é projeto, não descrição, e cada um vai entrar
marcado como **[decidido]** quando entrar.
