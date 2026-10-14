# Estados

As 32 capturas mostram o caminho feliz e pouco mais. Este documento cobre o que
elas não mostram: interação, ausência de dado, falha e modo escuro.

Quase tudo aqui é **[decidido]**, e isso é honesto: não há o que medir num estado
que nunca foi fotografado. O que dá para fazer é decidir **dentro do sistema
publicado**, usando as rampas declaradas em vez de inventar cor nova. Onde um valor
sai de uma rampa da SulAmérica, ele vem marcado **[declarado]**.

As rampas completas estão em `extracao/tokens-site.json`. Cada família vai de 50 a
950, e cinza e azul cobrem quase tudo que estes estados precisam.

---

# 1. Estados de interação

Valem para qualquer elemento tocável.

| Estado | Tratamento | Origem |
|---|---|---|
| Repouso | como especificado no componente | **[medido]** |
| Foco | contorno `2pt` `brand/primary`, deslocado `2pt` para fora | **[decidido]** |
| Pressionado | preenchimento desce um degrau na rampa | **[declarado]** ver abaixo |
| Carregando | conteúdo some, spinner no lugar, largura preservada | **[decidido]** |
| Desabilitado | `surface/disabled` com `text/disabled` | **[decidido]** |

**[declarado] O pressionado desce um degrau.** Botão primário vai de `orange-500`
para `orange-600`. Botão de contorno escurece a linha e o rótulo do mesmo jeito.
A regra evita cor nova para cada componente: a rampa já resolve.

**[decidido] O foco é contorno, não preenchimento.** Preenchimento diferente no foco
confunde com selecionado. Contorno deslocado funciona sobre qualquer superfície e
atende teclado e navegação por controle externo, que o app precisa suportar mesmo
sem aparecer nas capturas.

**[decidido] Carregar não muda a largura.** O botão mantém a caixa e troca o rótulo
pelo spinner. Botão que encolhe ao carregar move o que está embaixo e faz o usuário
errar o toque seguinte.

---

# 2. Estados de conteúdo

Toda tela que carrega dado tem quatro, e não três. O app hoje só desenha um.

| Estado | Quando | O que mostra |
|---|---|---|
| Carregando | o dado está vindo | esqueleto com a forma do conteúdo |
| Vazio | não há dado, e isso é normal | explicação e a ação que cria o primeiro |
| Erro | o dado deveria estar aqui e falhou | o que houve, o que fazer, botão de repetir |
| Preenchido | o caso que o app já desenha | o conteúdo |

**[decidido] Vazio e erro são coisas diferentes e não podem parecer iguais.** Lista
vazia é estado normal de quem nunca pediu reembolso; falha de rede é problema. Se
os dois mostrarem "nada por aqui", o usuário com problema fica esperando.

## 2.1 Vazio

| Propriedade | Valor |
|---|---|
| Ilustração ou ícone | opcional, `gray-300` **[declarado]** |
| Título | `type/title-section` 20pt Bold, `text/primary` |
| Explicação | `type/body`, `text/secondary`, no máximo duas linhas |
| Ação | botão primário com a ação que preenche a lista |

O texto diz **o que aconteceria se houvesse dado**, não "nenhum resultado". No
histórico de reembolso: *"Você ainda não pediu reembolso. Quando pedir, o
acompanhamento aparece aqui."*

## 2.2 Erro de rede

| Propriedade | Valor |
|---|---|
| Superfície | `surface/error` `#FDE8E8` **[declarado]** |
| Ícone e título | `feedback/error` `#C80505` **[declarado]** |
| Texto | `text/primary` |
| Ação | botão secundário `Tentar de novo` |

**[decidido] A primeira frase diz que o preenchimento está salvo.** Num fluxo de sete
etapas com upload de documento, o medo é perder o que já foi feito. Responder isso
antes da instrução técnica é o que separa erro tolerável de abandono.

Modelo: *"Seus dados estão salvos. A conexão caiu antes de enviar."*

## 2.3 Carregando

**[decidido] Esqueleto onde a estrutura é previsível, spinner onde não é.**
Lista, formulário e card têm forma conhecida antes do dado chegar, e o esqueleto já
mostra essa forma. Validação de identidade e envio não têm layout de destino, e aí
o spinner é honesto.

Esqueleto: blocos `gray-100` **[declarado]**, raio `4pt`, pulsando entre
`gray-100` e `gray-200` em 1,2s.

Spinner: anel de `64pt` com trilho `border/subtle` e arco `brand/primary` de `5pt`,
girando em 1s linear. O texto vem abaixo, centralizado, em duas linhas: o que está
acontecendo e o que o usuário deve fazer enquanto isso (*"Não feche o app."*).

As duas telas que aplicam a regra do spinner estão montadas em `mockups`:
`Estado · Validando identidade` e `Estado · Lendo sua nota fiscal`. A primeira só
existiu depois que o protótipo clicável mostrou que o toque no Face ID caía no
sucesso sem passar por espera nenhuma; a regra já estava escrita aqui, a tela é que
faltava. Detalhe em `anotacoes-ux.md`, seção da Tela O.4.

---

# 3. Estados por componente que faltavam

## 3.1 Radio e checkbox

| Estado | Tratamento |
|---|---|
| Desabilitado, não marcado | anel `gray-300`, rótulo `text/disabled` |
| Desabilitado, marcado | anel e disco `gray-400`, rótulo `text/disabled` |
| Erro no grupo | mensagem em `feedback/error` abaixo do último item |

**[decidido]** O erro é do grupo, não de cada opção: marcar cada radio em vermelho
sugere que cada um está errado, quando o que falta é escolher.

## 3.2 Chip de filtro

| Estado | Contorno | Preenchimento | Rótulo |
|---|---|---|---|
| Disponível | `1,5pt` `gray-200` | nenhum | `text/primary` |
| Aplicado | nenhum | `brand/primary` | branco |
| Removível | como aplicado, mais `✕` | | |
| Desabilitado | `1,5pt` `gray-200` | nenhum | `text/disabled` |

**[decidido]** O chip aplicado usa preenchimento, não só contorno colorido. Quem não
distingue laranja de cinza precisa ver a diferença por peso, não por matiz.

## 3.3 Captura de identidade

Três falhas que um fluxo de identidade sempre tem e nenhuma captura mostra:

| Situação | Tratamento |
|---|---|
| Permissão de câmera negada | tela de instrução com botão que abre os Ajustes do sistema |
| Rosto não reconhecido | mantém a câmera, mensagem sobre a guia, tentativa nova sem sair |
| Sem câmera disponível | caminho alternativo, e não beco |

**[decidido] Falha de reconhecimento não devolve o usuário ao início.** Ele já
preencheu tudo. A tentativa acontece na mesma tela, e depois de três falhas o app
oferece outro caminho em vez de repetir.

## 3.4 Campo de texto

| Estado | Tratamento |
|---|---|
| Foco | linha `2pt` `brand/primary` |
| Somente leitura | sem linha, valor em `text/primary`, sem afordância de toque |
| Desabilitado | linha `gray-200`, valor `text/disabled` |

**[decidido]** Somente leitura e desabilitado não são a mesma coisa. O primeiro é
dado que não se edita aqui, e continua legível. O segundo é campo que poderia ser
editado e não pode agora, e precisa parecer inativo.

---

# 4. Modo escuro

Nenhuma captura mostra, e o site não publica paleta escura. Tudo nesta seção é
**[decidido]**, derivado das rampas declaradas.

**[decidido] O escuro inverte a escala de cinza, não as cores de marca.** Laranja,
verde, vermelho e azul mantêm a matiz e sobem um ou dois degraus para recuperar
contraste sobre fundo escuro.

## 4.1 Superfícies

| Token | Claro | Escuro | Origem do escuro |
|---|---|---|---|
| `surface/body` | `#FFFFFF` | `#191D1D` | `gray-950` **[declarado]** |
| `surface/on-body` | `#F3F4F4` | `#272929` | `gray-900` **[declarado]** |
| `surface/raised` | `#FFFFFF` | `#313333` | `gray-800` **[declarado]** |

**[decidido] Superfície mais alta é mais clara, não mais sombreada.** No escuro a
sombra some contra o fundo. A hierarquia passa a ser dada por luminosidade, que é
como o iOS resolve.

## 4.2 Texto

| Token | Claro | Escuro | Origem do escuro |
|---|---|---|---|
| `text/primary` | `#313333` | `#F3F4F4` | `gray-100` **[declarado]** |
| `text/secondary` | `#6C6E6E` | `#ACAEAE` | `gray-400` **[declarado]** |
| `text/disabled` | `#949595` | `#737575` | `gray-600` **[declarado]** |

## 4.3 Marca e feedback no escuro

| Token | Claro | Escuro | Origem |
|---|---|---|---|
| `brand/primary` | `#F05223` | `#F05223` | `orange-500`, não muda **[declarado]** |
| `brand/on-surface` | `#F05223` | `#F58E70` | `orange-400` **[declarado]** |
| `feedback/error` | `#C80505` | `#F17474` | `red-400` **[declarado]** |
| `feedback/success` | `#04843F` | `#68BB8E` | `green-400` **[declarado]** |
| `feedback/alert` | `#EF9928` | `#F3B159` | `yellow-400` **[declarado]** |

**[decidido] São dois tokens, não um.** `brand/primary` preenche superfície e não
muda no escuro: o botão continua em `orange-500` com rótulo branco, porque clarear o
preenchimento enfraqueceria a hierarquia. `brand/on-surface` é o laranja de **texto e
ícone**, e esse sobe para `orange-400`, porque laranja escuro sobre fundo escuro fica
pesado e vibra.

Um token só para os dois casos obrigaria a escolher entre botão fraco no escuro e
texto vibrando. A separação custa uma variável e resolve os dois.

## 4.4 Contraste da paleta escura

Calculado por `extracao/10-contraste.py`, com os mesmos limites do modo claro.

| Par | Razão | AA texto | AA grande |
|---|---|---|---|
| `text/primary` sobre `surface/body` | 15,43:1 | passa | passa |
| `text/primary` sobre `surface/on-body` | 13,28:1 | passa | passa |
| `alert` sobre `surface/body` | 9,11:1 | passa | passa |
| `text/secondary` sobre `surface/body` | 7,63:1 | passa | passa |
| `success` sobre `surface/body` | 7,36:1 | passa | passa |
| `brand/primary` sobre `surface/body` | 7,28:1 | passa | passa |
| `error` sobre `surface/body` | 6,07:1 | passa | passa |
| Branco sobre botão `orange-500` | 3,54:1 | reprova | passa |
| `text/disabled` sobre `surface/on-body` | 3,16:1 | reprova | passa |

As duas reprovações são as mesmas do modo claro e pelas mesmas razões: o rótulo do
botão depende da regra de 16pt Semibold, e o desabilitado deve parecer desabilitado.

Vale notar que o desabilitado no escuro fica em 3,16:1 contra 2,40:1 no claro. O
modo escuro sai mais legível nesse ponto, o que é um bom sinal de que a inversão da
rampa de cinza está bem escolhida.

---

# 5. O que continua sem cobertura

| O que | Por que fica de fora |
|---|---|
| Tipografia responsiva | não há captura em aparelho diferente do de 393pt |
| Dynamic Type | nenhuma captura com corpo aumentado |
| Animação e transição | screenshot não registra movimento |
| Som e retorno tátil | fora do alcance de qualquer medição visual |

Nenhum desses se resolve com o material que existe. Entram quando houver acesso ao
app rodando, e não antes.
