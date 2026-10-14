# Como este design system foi feito

Este documento existe para a pergunta "como você chegou nisso?". Ele conta a ordem
do trabalho, o que cada etapa produziu, as decisões que precisaram de julgamento e
os caminhos que não deram certo.

Os becos sem saída estão aqui de propósito. Num portfólio eles valem mais que os
acertos: mostram como a dúvida foi resolvida, não só qual foi a resposta.

---

## O ponto de partida

O material disponível eram **32 capturas** do fluxo de reembolso do app iOS, em
739 × 1600px. Não havia acesso ao app rodando, ao Figma de origem nem a ninguém do
time da SulAmérica.

A pergunta inicial era se dava para reconstruir o sistema visual só com isso. A
resposta foi sim, com três limites que ficaram declarados desde o começo:
resolução redimensionada, nenhum estado que não tivesse sido fotografado, e
nenhuma informação sobre movimento, som ou tipografia responsiva.

---

## O método, antes das etapas

Este sistema foi construído com IA como par de trabalho, e a decisão de método que
sustenta tudo é a mesma que torna isso seguro: **nada entra sem verificação.**

As três marcas, **[declarado]**, **[medido]** e **[decidido]**, respondem sempre à
mesma pergunta: como se sabe que isso é verdade? E os 14 scripts existem para que a
resposta não dependa de confiança. Um número que ninguém pode recalcular é um número
que ninguém deveria usar, venha ele de onde vier.

A seção "os caminhos que não deram certo", no fim deste documento, é o resultado
prático disso. Todo erro listado ali foi encontrado por uma verificação, não por
alguém reler o texto e achar estranho.

---

## Etapa 1 · Medir em vez de estimar

**O que fiz.** Em vez de olhar as capturas e anotar as cores, amostrei os pixels.

**Por que importa.** Um hex lido a olho erra por margem visível. Uma amostragem
diz `#FF5000` com 508.636 pixels de evidência, e qualquer pessoa pode rodar o
script e conferir.

Esse foi o princípio que organizou todo o resto: **se não dá para medir, o
documento diz que foi decidido.** Daí saíram as três marcas que cada afirmação do
sistema carrega, `[declarado]`, `[medido]` e `[decidido]`.

---

## Etapa 2 · Ancorar a régua

**O problema.** As capturas estão em 739 × 1600, que não é resolução de aparelho
nenhum: foram redimensionadas. Sem saber quantos pixels valem um ponto, nenhuma
medida de tamanho significa nada.

A proporção sozinha não resolve, porque toda a linha recente de iPhones tem
praticamente o mesmo formato.

**Como resolvi.** Três medidas de coisas que o iOS fixa e o app não controla:

| Medida | Esperado | Medido |
|---|---|---|
| Altura total | 852pt | 851pt |
| Divisor sob a barra de navegação | 54 + 44 = 184,3px | 184px, em 20 telas |
| Caixa dos dígitos do relógio | 22,8px | 23px |

Só uma hipótese passa nas três: iPhone 14 Pro / 15 / 16, **1,8804 px/pt**. As
concorrentes erram o divisor em 12px ou mais.

**Por que importa.** Com a hipótese errada, o botão de 48pt viraria 44.

---

## Etapa 3 · A descoberta que virou o diagnóstico

**O que aconteceu.** Fui buscar no site da SulAmérica alguma pista sobre a
tipografia. O CSS publica **o design system inteiro da empresa**: 149 variáveis de
cor, rampas de 50 a 950 e a família declarada, Figtree.

**O que isso mudou.** O projeto deixou de ser "reconstruir um sistema que não
temos" e virou "confrontar o sistema publicado com o que o app entrega".

E o confronto deu divergência em quatro famílias de cor:

| Onde | App | Publicado |
|---|---|---|
| Laranja de marca, em 3 componentes | `#FF5000` | `#F05223` |
| Verde de sucesso | `#1F662E` e `#00861F` | `#04843F` |
| Superfície secundária | cinco cinzas | um token |
| Título de tela | três tamanhos | um papel |

**A frase que o case usa:** o problema não é ausência de design system, é falta de
aderência ao que já existe. São problemas diferentes, e o segundo pede governança,
não construção.

---

## Etapa 4 · O que a medição achou e o olho não acha

O app escurece o fundo de modal de **duas maneiras**, preto a 40% em quatro telas e
a 30% em duas.

Ninguém percebe isso olhando. Só apareceu porque `#999999` e `#B2B2B2`, em áreas
chapadas grandes, são exatamente branco sob esses dois véus.

**Se eu tivesse anotado os dois como "cinza", o sistema nasceria com dois tokens
falsos.** É o melhor argumento que tenho para medir em vez de estimar.

---

## Etapa 5 · Identificar a tipografia sem chutar

O CSS do site declara Figtree, mas **o site não é o app**.

**Primeira tentativa:** comparar as letras a olho. Não serve como evidência, porque
quase toda sem-serifa geométrica se parece nesse tamanho.

**O que funcionou:** recortar uma palavra da captura, renderizar a mesma palavra em
**dez famílias candidatas** ajustadas à mesma altura de caixa alta, e medir a
interseção sobre união dos pixels com tinta.

| Amostra | 1º | 2º | Vantagem |
|---|---|---|---|
| `Atenção!`, peso forte | Figtree, 87,8% | Montserrat, 83,0% | 4,8 pontos |
| Linha de corpo, Regular | Figtree, 79,3% | DM Sans, 57,9% | **21,4 pontos** |

A primeira amostra é curta e a margem ficou apertada. Por isso não parei nela: a
segunda, com uma frase inteira, decide.

---

## Etapa 6 · Do sistema escrito à biblioteca

Os documentos vieram antes do Figma, e nessa ordem de propósito: **o guia de
construção não introduz valor nenhum**, e diz isso no topo. Se um número aparece
só lá, é erro do arquivo.

A biblioteca ficou com 94 variáveis de cor em dois modos, 20 numéricas, 8 estilos
de texto, 2 de efeito, 36 ícones e 18 componentes, e foi aplicada nas 44 telas da
página `mockups`, com os wireframes preservados em escala de cinza na sua própria
página.

Duas decisões de arquitetura que vale saber explicar:

**As 70 primitivas estão ocultas da publicação.** Quem consome vê as semânticas e
não consegue pegar um degrau da rampa por engano. A regra "primitiva nunca entra
direto" virou impedimento, não recomendação.

**`radius/full` vale 999, não 24.** O Figma corta o raio na metade da menor
dimensão, então a pílula sobrevive a qualquer altura. Com 24 cravado, mudar a
altura do botão o transformaria em retângulo arredondado sem ninguém perceber.

---

## Os caminhos que não deram certo

### A App Store

Verifiquei e rejeitei. As sete capturas da loja são composições de marketing, com
mockup em perspectiva, ampliadas de um asset menor, e mostram interface de 2021.

**O quase-erro que vale contar:** a primeira leitura de cor dessas imagens devolveu
`#FF4F00` com 1,15 milhão de pixels, e por um momento pareceu confirmar o laranja do
app. Não confirma nada: aquele laranja é o **fundo da peça publicitária**.
Amostragem de pixel só vale quando se sabe o que o pixel está mostrando.

### O estimador de raio

Minha primeira medição do raio do botão deu 18,1pt. Estava errada: eu lia a largura
a uma linha do topo, onde a curva já avançou, então subestimava sempre.

Numa forma arredondada, a meia largura a uma distância `d` do topo vale
`L/2 - r + √(2rd - d²)`. Uma linha só não resolve `r`. A versão final amostra
dezenas de distâncias e busca o raio que explica todas: **24,2pt**, e a razão de
1,002 com a metade da altura confirmou que é pílula.

### O título que não tinha tamanho

A medição do H1 deu desvio de 4,09px e eu descartei, achando que a janela não
achava o mesmo elemento.

Ao refazer com as telas escolhidas uma a uma, apareceu a causa real: **o app usa
três tamanhos de título**, de 13,2 a 20,9pt, e um deles em laranja e peso Regular.
O desvio não era ruído de medição, era o app.

### O comparador que casou cinza com verde

A busca por cor mais próxima emparelhou um cinza com um degrau de verde, porque a
distância euclidiana era menor. Par sem sentido. Neutro agora só compara com neutro.

### A cobertura pela metade

A primeira biblioteca tinha oito componentes e parecia completa. Uma auditoria
contando quantas telas usam cada padrão mostrou que faltavam onze, incluindo o
**Stepper, presente em 31 das 44 telas** e assinatura do redesenho.

Lição que virou item de checklist: cobertura se confere **contando**, não olhando.

---

## O que continua em aberto

| O que | Por quê | Quem resolve |
|---|---|---|
| Migrar o laranja do app para o token publicado | muda a cor da marca no canal mais usado | time de marca |
| Governança do sistema | sem responsável, cinco cinzas viram seis | o time |
| Dynamic Type e tipografia responsiva | não há captura em outro aparelho nem com corpo aumentado | acesso ao app |
| Animação, som e retorno tátil | screenshot não registra | acesso ao app |
| Ilustrações de boas-vindas e de estado vazio | é outro ofício, e o estilo de marca não é nosso para inventar | time de marca |
| Cor do texto de erro, do clipe e do título da nav bar | elementos finos, o antialiasing consome a cor | recorte manual |

Nenhum desses está escondido: todos aparecem marcados nos documentos onde deveriam
existir. Um sistema que declara o próprio limite é mais confiável que um que
preenche o vazio com suposição.

---

## Como conferir qualquer número daqui

Os scripts em `extracao/` rodam sozinhos e só precisam de Pillow.

| Pergunta | Script |
|---|---|
| Que aparelho, e quantos px valem 1pt | `02-ancora.py` |
| Quais cores o app usa, e quantos pixels cada uma | `03-cores.py` |
| O que é superfície e o que é antialiasing | `04-superficies.py` |
| Qual o corpo de cada elemento | `05-tipografia.py`, `13-h1.py` |
| Qual a geometria do botão e do card | `06-forma-espaco.py`, `14-raio-card.py` |
| Que tokens a SulAmérica publica | `08-tokens-do-site.py` |
| As cores do app batem com as rampas publicadas | `11-rampas.py` |
| Qual a fonte, de verdade | `12-identifica-fonte.py` |
| Que pares passam em AA | `10-contraste.py` |
