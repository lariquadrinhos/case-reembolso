# Anotações de UX · telas do fluxo de reembolso

**Wireframes:** [Reembolso SulAmérica · página `wireframes`](https://www.figma.com/design/LUp4aT7fVYH4cD8ZwrHIfd/Reembolso-SulAmerica?node-id=33-5) · 44 frames
**Densidade:** baixa fidelidade, mobile (iPhone, frame 390 × 844pt)
**PNGs locais:** [`wireframes/`](wireframes/) traz os 44 frames em @2x, com `wireframes/exportar.sh` para atualizar. As mesmas telas com o design system aplicado estão em [`mockups/`](mockups/), com os mesmos nomes de arquivo. Servem para consulta rápida; o Figma continua sendo a fonte da verdade.
**Base de design system:** ver `design-system/`, construído a partir dos tokens publicados pela SulAmérica e da medição das 32 capturas. Os wireframes estão em escala de cinza; a cor entra na alta fidelidade, com os tokens de lá.

**Como o quadro está organizado.** Sete fileiras, uma por parte deste documento, com passo fixo de **1600pt** na vertical e **470pt** na horizontal. O passo vertical era 1280 e cresceu para abrir os 420pt que as notas de design ocupam sob cada tela. Cada fileira tem um cabeçalho com título, subtítulo e contagem de telas, posicionado a 110pt da própria fileira e a 190pt da de cima. A assimetria é proposital, para o cabeçalho pertencer visualmente à fileira que anuncia. No topo, uma capa com a legenda das convenções de anotação (checkbox × ícone, erro × alerta, tela que rola, rodapé fixo), as mesmas descritas nas notas gerais no fim deste arquivo.

Os oito frames de anotação (capa + sete cabeçalhos) são nomeados só com números, **`1` a `8`**, para não competirem com os nomes das telas no painel de camadas. Eles não fazem parte do produto: são apoio de leitura do quadro.

## Notas de design no quadro

Sob 37 das 44 telas há um post-it laranja intitulado **Notas de Design**, com a decisão de design daquela tela em um parágrafo. As camadas se chamam `Nota · <nome da tela>`.

**São a única cor do quadro.** Os wireframes têm exatamente cinco cinzas; o papel `#ffd3a8` existe justamente para não ser confundido com interface. Se algo colorido aparece no quadro, é anotação. A regra é essa e não tem exceção. A cor veio do FigJam do mapeamento, onde os stickies já usavam esse tom, e a proporção foi mantida: lá o texto era 24pt sobre capturas de 604pt de largura; aqui é 15pt sobre telas de 390pt, a mesma relação.

**Dez telas não têm nota**, e isso é proposital: `O.4b` (fallback da identidade), `Empty state`, `Primeiro acesso (Tela 1)`, `2 de 3 documentos`, `Preenchimento manual` (nos dois estados), `Validando identidade`, `Home após o onboarding` e as duas Sheet B de nota fiscal e comprovante. Todas são variações de estado cuja decisão já está explicada na nota da tela de origem. Repetir o texto ao lado de cada variante transformaria a anotação em ruído. O post-it marca onde houve uma escolha, não onde há uma tela.

As notas resumem; este documento detalha. Quando divergirem, vale o documento.

> **O layout de cada tela mora no Figma, não aqui.** Este documento guarda o que o arquivo de design não consegue guardar: por que cada tela é assim, qual heurística ela corrige e o que precisa ser previsto na implementação. Quando os dois divergirem, o Figma é a fonte da verdade sobre *forma*; este documento é a fonte da verdade sobre *intenção*.

## Índice · seção deste documento → frame no Figma

| **Parte 1 · Onboarding** | |
| Tela O.0 · Home (ponto de entrada) | `Tela O.0 · Home (ponto de entrada)` |
| Tela O.1 · Boas-vindas ao Reembolso Digital | `Tela O.1 · Boas-vindas ao Reembolso` |
| Tela O.2 · Dados bancários (dois caminhos) | `Tela O.2a · Confirmação dos dados bancários`<br>`Tela O.2b · Cadastro dos dados bancários` |
| Tela O.3 · Termo de Ciência e Responsabilidade | `Tela O.3 · Termo de Ciência` |
| Tela O.4 · Validação de identidade | `Tela O.4a · Identidade (Face ID)`<br>`Tela O.4b · Identidade (selfie · fallback)` |
| Tela O.5 · Onboarding concluído | `Tela O.5 · Onboarding concluído` |
| **Parte 2 · Fluxo principal** | |
| Tela 1 · Início da solicitação | `Tela 1 · Início da solicitação` |
| Tela 2 · Captura da nota fiscal/recibo | `Tela 2 · Captura da nota fiscal` |
| Tela 2A · Conferência dos campos extraídos (OCR) | `Tela 2A · Conferência dos campos (OCR)` |
| Tela 3 · Detalhes do tratamento | `Tela 3 · Detalhes do tratamento` |
| Tela 4 · Upload de documentos complementares | `Tela 4 · Upload de documentos` |
| Tela 5 · Revisão dos dados | `Tela 5 · Revisão dos dados` |
| Tela 6 · Confirmação de envio | `Tela 6 · Confirmação de envio` |
| **Parte 3 · Pós-envio** | |
| Tela 7 · Acompanhar status da solicitação | `Tela 7 · Acompanhar status` |
| Tela 8 · Histórico de solicitações | `Tela 8 · Histórico de solicitações` |
| **Parte 4 · Bottom sheets** | |
| Sheet A · Tutorial gov.br | `Sheet A · Tutorial gov.br` |
| Sheet B · Exemplos de documento | `Sheet B · Exemplo · pedido médico`<br>`Sheet B · Exemplo · nota fiscal`<br>`Sheet B · Exemplo · comprovante` |
| Overlay · Visualizador de documento | `Overlay · Visualizador de documento` |
| Sheet C · Editar conta bancária | `Sheet C · Editar conta bancária` |
| **Parte 5 · Estados especiais** | |
| Estado · Home no primeiro acesso | `Estado · Home no primeiro acesso` |
| Estado · Primeiro acesso (Tela 1 sem histórico) | `Estado · Primeiro acesso (Tela 1 sem histórico)` |
| Estado · Loading com skeleton | `Estado · Loading com skeleton` |
| Estado · Empty state (sem histórico) | `Estado · Empty state (sem histórico)` |
| Estado · Erro de rede | `Estado · Erro de rede` |
| Estado · 2 de 3 documentos (Tela 4) | `Estado · 2 de 3 documentos (Tela 4)` |
| Estado · Documentos completos (Tela 4) | `Estado · Documentos completos (Tela 4)` |
| Estado · Retomada de rascunho (Tela 5) | `Estado · Retomada de rascunho (Tela 5)` |
| Estado · Preenchimento manual (Tela 2A vazia) | `Estado · Preenchimento manual (Tela 2A vazia)` |
| **Parte 6 · Erros e validação** | |
| Erro · Data fora do prazo (Tela 3) | `Erro · Data fora do prazo (Tela 3)` |
| Erro · Campos com alerta e erro (Tela 2A) | `Erro · Campos com alerta e erro (Tela 2A)` |
| Erro · Solicitação com pendência (Tela 7) | `Erro · Solicitação com pendência (Tela 7)` |
| **Parte 7 · Captura, espera e retomada** | |
| Tela 2 · Câmera (guia de enquadramento) | `Tela 2 · Câmera (guia de enquadramento)` |
| Estado · Lendo sua nota fiscal | `Estado · Lendo sua nota fiscal` |
| Modal · Retomar de onde parou? | `Modal · Retomar de onde parou?` |
| **Parte 8 · Detalhe, filtros e ajuda** | |
| Tela 9 · Detalhe da solicitação paga | `Tela 9 · Detalhe da solicitação paga` |
| Sheet D · Filtrar histórico | `Sheet D · Filtrar histórico` |
| Sheet E · Quem fez o procedimento? | `Sheet E · Quem fez o procedimento?` |
| Sheet F · Buscar banco | `Sheet F · Buscar banco` |
| Sheet G · Ajuda desta etapa | `Sheet G · Ajuda desta etapa` |
| Estado · Protocolo copiado (Tela 6) | `Estado · Protocolo copiado (Tela 6)` |

## Mapa do fluxo de telas

```
                ┌───────────────────────┐
                │   Home (entry point)  │
                └──────────┬────────────┘
                           │
       ─────── [primeiro acesso? sim] ────────
                           │
              ┌── ONBOARDING (uma vez) ──┐
              │                          │
   O.1 Boas-vindas → O.2 Dados bancários
        → O.3 Termo de Ciência → O.4 Identidade
                  → O.5 Pronto
              │
              └──────────┬───────────────┘
                         │
           ───── FLUXO PRINCIPAL (a cada solicitação) ─────
                         │
   1 Início → 2 Captura nota → [câmera → lendo…] → 2A Conferência OCR
        → 3 Detalhes tratamento → 4 Upload anexos
        → 5 Revisão → 6 Confirmação enviada
                         │
                    PÓS-ENVIO
                         │
              7 Acompanhar status (timeline)
              8 Histórico de solicitações

                         │
              9 Detalhe da solicitação paga

  Bottom sheets auxiliares:  A) Tutorial gov.br  ·  B) Exemplos de documento  ·  C) Editar conta bancária
                             D) Filtrar histórico · E) Quem fez o procedimento · F) Buscar banco
                             G) Ajuda desta etapa
  Estados especiais:         Primeiro acesso (home e Tela 1) · Loading · Empty state · Erro de rede
  Erros e validação:         Data fora do prazo (3) · Campos com alerta e erro (2A) · Pendência (7)
  Captura, espera, retomada: Câmera com guia · Lendo a nota fiscal · Modal "Retomar de onde parou?"
```

## Protótipo · o que ele cobre

A página `mockups` tem **um fluxo clicável**, começando em `Estado · Home no
primeiro acesso`, que alcança **43 das 50 telas com 145 ligações e nenhum beco sem
saída**.

Ele chegou a ter dois. O histórico era um ponto de partida separado porque
**nenhuma tela do app abria a Tela 8**: a home levava a *uma* solicitação
(*"1 solicitação em análise ›"* → Tela 7), nunca à lista. Isso não era esquecimento
de prototipagem, era buraco de design, e mantê-lo como fluxo à parte servia para
deixar o buraco visível em vez de escondê-lo com uma ligação inventada.

**O buraco foi fechado, e o segundo ponto de partida deixou de fazer sentido.** A
seção seguinte conta como.

### Onde mora a entrada do histórico

O `anotacoes-ux.md` já dizia, na ficha da Tela 8, que ela é *"acessível pelo menu
Reembolso ou pela home"*. A intenção existia desde o começo; o elemento nunca tinha
sido desenhado. Três lugares foram considerados:

| Onde | Por que não |
|---|---|
| Mais uma linha no card, junto do rascunho e da solicitação em análise | Aquelas duas linhas são **pendências**, coisas que pedem ação. Histórico é arquivo. Dar a ele o mesmo peso visual diria que ele também cobra algo |
| Um quinto item em *Atalhos* | Os atalhos são recursos do app fora do reembolso (rede credenciada, telemedicina). O histórico é da área de reembolso, não vizinho dela |
| Uma aba na tab bar | A tab bar é do app inteiro, não do reembolso. E ela está declarada fora do escopo deste case |

Ficou um link discreto **abaixo do CTA, dentro do card de Reembolso**:
*Ver todas as solicitações*, sublinhado, centralizado, com 44pt de alvo. A posição
carrega o significado: está dentro do card certo, mas depois da ação principal, que
é o que separa arquivo de pendência.

**Ele só existe na home com histórico.** As duas homes sem histórico não o mostram,
pela mesma regra que já valia para o card de *Mais usadas*: não se oferece a lista
de solicitações para quem ainda não tem nenhuma. Para essa pessoa existe o
`Estado · Empty state`, que é a Tela 8 vazia, e que segue sem entrada no protótipo
porque quem a veria é justamente quem não vê o link.

**O custo foi a home passar a rolar.** O `Spacer` elástico dela tinha 34pt de folga
e um alvo tocável precisa de 44. Não dava para espremer: alvo de 34pt é o defeito
que este projeto já corrigiu uma vez, em *Um alvo por ação*. A home ganhou a mesma
construção das outras telas que rolam, com status bar e cabeçalho fixos no topo, a
tab bar fixa embaixo e 24pt de rolagem no miolo. Home de app rola; a nossa é que não
rolava.

Seis telas nasceram por causa do protótipo, e a razão da maioria vale registrar:
**protótipo não digita**. O toque num campo precisa levar a uma versão já
preenchida, então cada formulário do caminho precisa existir nos dois estados.

| Tela | Existia | Faltava |
|---|---|---|
| `O.2b · Cadastro bancário` | vazia | a **preenchida** |
| `Tela 3 · Detalhes` | preenchida | a **vazia** |
| `O.3 · Termo de Ciência` | com o aceite em branco | a **aceita** |
| `Preenchimento manual` | vazia | a **preenchida** |
| `Validação de identidade` | nada | a **espera**, ver abaixo |
| `Home sem histórico` | só a de antes do onboarding | a de **depois**, ver abaixo |

A regra que sai daí vale para qualquer protótipo: **todo controle que destrava um
botão precisa dos dois estados.** Não basta o botão parecer travado, ele tem que
estar sem ligação, e quem destrava é que leva ao estado seguinte.

O termo foi o caso que escapou na primeira montagem: o botão estava cinza e mesmo
assim clicável, o que deixa o protótipo mentir sobre a própria regra que a tela
enuncia. Hoje os cinco porteiros do caminho estão coerentes, conferidos por
varredura: botão travado tem zero ligações, botão ativo tem uma.

A Tela 3 era o caso que quebrava: num primeiro acesso ninguém chega com o formulário
respondido. Ela começa vazia, com o CTA travado em *"Preencha as sessões para
avançar"*, e o toque em qualquer campo leva à preenchida.

**Decisões de prototipagem**, todas visíveis nas ligações:

- A leitura do OCR avança **sozinha**, em 1,6s. Carregamento que exige toque não
  existe na vida real.
- O Face ID **mantém o toque**, porque ali o prompt do sistema de fato pede ação,
  mas não salta para o sucesso: passa por `Estado · Validando identidade`, que
  avança sozinho em 1,8s. O caminho da selfie passa pela mesma tela.
- Os sheets entram por baixo (`Move in`), não como troca de página. Eles são frames
  de tela cheia com o fundo embutido, então a sobreposição é simulada pela transição.
- Todo `‹` usa a ação `Back`, que devolve para onde a pessoa veio em vez de para um
  destino fixo.
- Os becos fora de escopo ficam inertes: carteirinha, atalhos e tab bar não
  respondem, e isso é mais honesto que fingir profundidade que o case não tem.

### As sete telas que ficam fora, e por quê

Nenhuma das sete está fora por descuido. A varredura que produziu esta lista contava
controle mudo por tela, e o que sobrou se separa em três causas distintas.

**Cinco são estados que nenhum toque produz.** `Loading com skeleton`, `Empty state`,
`Erro de rede`, `Erro · Data fora do prazo` e `Erro · Campos com alerta e erro`
acontecem por rede lenta, por conta nova ou por validação, não por alguém apertar um
botão. Um protótipo clicável não tem como chegar nelas sem inventar um gatilho que o
app não tem. Elas existem para o handoff, que é onde importam.

**Duas são o ramo de quem já tem conta bancária cadastrada.** A `O.2a` é a bifurcação
da O.1 para quem já tem conta, e a `Sheet C` é desenhada sobre ela. O protótipo
percorre o outro lado da bifurcação, o de quem cadastra pela primeira vez, que é o
caminho mais longo e o que o case se propõe a provar. Isso tem uma consequência que
vale registrar: **a Revisão não consegue abrir a Sheet C**, porque a única Sheet C
desenhada tem a O.2a de fundo, e abri-la a partir da Tela 5 mostraria a tela errada
atrás do escurecimento. Sheet reaproveitada em N telas precisa de N frames; é o preço
da decisão de desenhar cada sheet sobre a tela que a abre.

**A oitava era inconsistência entre documento e tela, e foi resolvida.** A
`Sheet B · Exemplo · comprovante` existia sem nada que a abrisse: o `microcopy.md`
dizia que ela abre pelo link *Ver exemplo*, mas o slot de comprovante oferecia só
*Como obter o recibo do IRPF*. O link entrou, e com ele uma decisão de ordem. As
duas ações secundárias não cabem na mesma linha do card, então a linha quebra, e
quem desce para a segunda linha some abaixo da dobra. Ficou em cima o *Como obter o
recibo do IRPF*: quem chega nesse slot geralmente ainda **não tem** o documento, e
saber como consegui-lo importa mais do que saber como ele deve ser. O *Ver exemplo*
é o que desce.

### O que o `?` faz, e onde ele não faz nada

O ícone de ajuda aparece no cabeçalho de quase toda tela e **só abre em três**: a
Tela 4 e seus dois estados. A razão é a mesma da Sheet C. A `Sheet G · Ajuda desta
etapa` é desenhada sobre a Tela 4 e as quatro perguntas dela são sobre documentos
(*"Posso enviar foto do documento?"*, *"E se eu perdi a nota fiscal?"*). Ligar o `?`
da Tela 3 nela mostraria a tela de documentos atrás do escurecimento e responderia
perguntas de outra etapa.

O nome da sheet é literal: **ajuda *desta* etapa**. Cumpri-la significa uma sheet por
etapa, com perguntas próprias, e essas perguntas ainda não estão escritas. Fica
registrado como pendência de conteúdo, não de arquivo: são cinco listas de perguntas
frequentes que precisam vir de quem atende o reembolso hoje, pelo mesmo motivo que as
checklists de documento precisam de homologação.

## Mapa de destinos · o que acontece ao tocar

Esta tabela existe por causa do protótipo. Enquanto os wireframes são só para revisão, basta que cada tela esteja certa; para prototipar, **todo elemento clicável precisa apontar para um frame que existe**. Foi ao montar esta lista que apareceram os seis destinos prometidos na interface e nunca desenhados, e as duas Sheet B que existiam sem nenhuma origem.

Três destinos legítimos **não são tela**, e é importante não confundi-los com buraco:

| Tipo | O que é | No protótipo |
|---|---|---|
| **Sistema** | seletor de arquivos, prompt do Face ID, share sheet do iOS, teclado, date picker, PDF do termo | não se desenha; o protótipo salta direto para o resultado |
| **Fora do escopo** | carteirinha, rede credenciada, telemedicina, autorizações, cobertura do plano, chat de atendimento, aba Serviços | beco proposital: são recursos do app que não fazem parte do fluxo de reembolso |
| **Fica na tela** | checkbox, radio, campo de texto, acordeão, sublinhado que abre sheet sobre a mesma tela | nenhum salto; muda o estado, não a tela |

### Parte 1 · Onboarding

| Origem | Ação | Destino |
|---|---|---|
| O.0 Home | `Pedir reembolso` | Tela 1, ou `Modal · Retomar de onde parou?`, se houver rascunho |
| O.0 Home | `Rascunho salvo · Sessão Psicologia ›` | `Estado · Retomada de rascunho (Tela 5)` |
| O.0 Home | `1 solicitação em análise ›` | Tela 7 |
| O.0 Home | card Carteirinha, 4 atalhos, abas Serviços/Ajuda | fora do escopo |
| O.0 Home | `Alvo · Avisos` (sino) | fora do escopo |
| O.1 Boas-vindas | `Começar` | O.2a se já há conta cadastrada; **O.2b** se não há |
| O.1 Boas-vindas | `Agora não` · `✕` | O.0 Home |
| O.2a Confirmação | `Está tudo certo` | O.3 |
| O.2a Confirmação | `Atualizar dados` · `✎` | `Sheet C · Editar conta bancária` |
| O.2b Cadastro | campo `Banco ▾` | **`Sheet F · Buscar banco`** |
| O.2b Cadastro | agência, conta, tipo de conta, titularidade | fica na tela |
| O.2b Cadastro | `Salvar e continuar` | O.3 |
| O.3 Termo | `Ler termo completo (PDF)` | sistema (visualizador de PDF do iOS) |
| O.3 Termo | aceite | fica na tela |
| O.3 Termo | `Aceito e continuar` | O.4a, ou O.4b direto, pela regra de roteamento de identidade |
| O.4a Face ID | `Usar Face ID` | sistema (prompt de biometria) → `Estado · Validando identidade` → O.5 |
| O.4a Face ID | `Tirar selfie em vez disso` | O.4b |
| O.4b Selfie | `Capturar` | `Estado · Validando identidade` → O.5 |
| O.5 Concluído | `Pedir reembolso agora` | Tela 1 |
| O.5 Concluído | `Voltar para a home` · `✕` | `Estado · Home após o onboarding` |
| Home após o onboarding | `Pedir reembolso` | Tela 1, **sem passar pelo onboarding de novo** |

### Parte 2 · Fluxo principal

| Origem | Ação | Destino |
|---|---|---|
| Tela 1 | card `Sessão Psicologia` | Tela 2 |
| Tela 1 | 6 linhas de categoria `›` | Tela 2, **destino único e compartilhado**, ver nota abaixo |
| Tela 1 | `Refazer última solicitação` | `Estado · Retomada de rascunho (Tela 5)` |
| Tela 2 | `Tirar foto agora` | `Tela 2 · Câmera (guia de enquadramento)` |
| Tela 2 | `Anexar arquivo` | sistema (seletor) → `Estado · Lendo sua nota fiscal` |
| Tela 2 | `Inserir manualmente` | `Estado · Preenchimento manual (Tela 2A vazia)` |
| Tela 2 | `Ver exemplo de nota fiscal` | `Sheet B · Exemplo · nota fiscal` |
| Câmera | disparador | `Estado · Lendo sua nota fiscal` |
| Câmera | `Alvo · Galeria` | sistema (seletor) |
| Câmera | `Alvo · ⚡` (flash) · `✕` | fica na tela · volta para Tela 2 |
| Lendo a nota | *(automático)* | Tela 2A |
| Tela 2A | `Ver original` | `Overlay · Visualizador de documento` |
| Tela 2A | `Trocar` | Tela 2 |
| Tela 2A | 6 `✎` de campo | fica na tela (teclado) |
| Tela 2A | `Tudo certo, avançar` | Tela 3 |
| Preenchimento manual | qualquer campo | `Estado · Preenchimento manual (preenchido)` |
| Preenchimento manual (preenchido) | `Tudo certo, avançar` | Tela 3 |
| Tela 3 | tipo de terapia, frequência | fica na tela |
| Tela 3 | `Quantas sessões ▾` · `Com que frequência ▾` · `Primeira sessão ▦` | sistema (picker nativo) |
| Tela 3 | `Avançar` | Tela 4 |
| Tela 4 | `Ver` (nota fiscal) | `Overlay · Visualizador de documento` |
| Tela 4 | `Trocar` | Tela 2 |
| Tela 4 | `Anexar` (pedido médico) | sistema (seletor) → `Estado · 2 de 3 documentos` |
| Tela 4 | `Ver exemplo` | `Sheet B · Exemplo · pedido médico` |
| Tela 4 | `Anexar` (comprovante) | sistema (seletor) → `Estado · Documentos completos` |
| Tela 4 | `Como obter o recibo do IRPF` | `Sheet A · Tutorial gov.br` |
| Tela 4 | `Avançar` | bloqueado até os 3 slots; ver `Estado · Documentos completos` |
| Tela 5 | `✎ Beneficiário` | **`Sheet E · Quem fez o procedimento?`** |
| Tela 5 | `✎ Prestador` | Tela 2A, onde esses campos moram |
| Tela 5 | `✎ Procedimento` | Tela 3 |
| Tela 5 | `✎ Documentos anexados` | Tela 4 |
| Tela 5 | `✎ Conta para depósito` | `Sheet C · Editar conta bancária` |
| Tela 5 | 3 miniaturas de documento | `Overlay · Visualizador de documento` |
| Tela 5 | `Enviar solicitação` | Tela 6 |
| Tela 5 | `Salvar como rascunho` | O.0 Home |
| Tela 6 | `Copiar` | **`Estado · Protocolo copiado (Tela 6)`** |
| Tela 6 | `Acompanhar status` | Tela 7 |
| Tela 6 | `Adicionar mais uma sessão` | Tela 2 |
| Tela 6 | `Compartilhar protocolo` | sistema (share sheet) |
| Tela 6 | `Voltar ao início` · `✕` | O.0 Home |

### Parte 3 · Pós-envio

| Origem | Ação | Destino |
|---|---|---|
| Tela 7 | `Compartilhar protocolo` | sistema |
| Tela 7 | `Pedir ajuda` | fora do escopo (chat) |
| Tela 8 | `Filtrar ▾` | **`Sheet D · Filtrar histórico`** |
| Tela 8 | `Input · Busca` | fica na tela (teclado) |
| Tela 8 | card `Em análise` | Tela 7 |
| Tela 8 | `Ver detalhes →` (2 cards pagos) | **`Tela 9 · Detalhe da solicitação paga`** |
| Tela 8 | `Resolver agora →` | `Erro · Solicitação com pendência (Tela 7)` |
| **Tela 9** | 3 miniaturas | `Overlay · Visualizador de documento` |
| **Tela 9** | `Copiar` | fica na tela (mesmo padrão de toast da Tela 6) |
| **Tela 9** | `Compartilhar comprovante` | sistema |

### Sheets, overlays e estados

| Origem | Ação | Destino |
|---|---|---|
| Sheet A | `Abrir gov.br` | sistema (app externo) |
| Sheet A | `Já tenho o arquivo` | sistema (seletor) → Tela 4 |
| Sheet A | `Paguei por PIX ou cartão` | `Sheet B · Exemplo · comprovante` |
| Sheet B (3 variantes) | `Entendi, anexar agora` | sistema (seletor) → Tela 4 |
| Sheet C | `Salvar nova conta` | O.2a ou Tela 5, conforme a origem |
| Sheet C | campo `Banco ▾` | `Sheet F · Buscar banco` |
| Sheet C | `Cancelar` | fecha, volta para a origem |
| **Sheet D** | `Aplicar filtros` | Tela 8 filtrada |
| **Sheet D** | `Limpar tudo` | fica na tela |
| **Sheet E** | `Confirmar beneficiário` · `Cancelar` | Tela 5 |
| **Sheet F** | linha de banco | fecha e preenche o campo na origem |
| **Sheet G** | linhas de pergunta `▾` | fica na tela (acordeão) |
| **Sheet G** | `Falar com atendimento` | fora do escopo (chat) |
| **Sheet G** | `Fechar` | volta para a tela de origem |
| Visualizador | `Compartilhar` · `Baixar` | sistema |
| Visualizador | `✕` | volta para a tela de origem |
| Modal Retomar | `Retomar` | `Estado · Retomada de rascunho (Tela 5)` |
| Modal Retomar | `Começar do zero` | Tela 2 |
| Erro de rede | `Tentar novamente` | a tela que falhou |
| Empty state | `Pedir reembolso agora` | Tela 1 |
| Pendência (Tela 7) | `Corrigir agora` | Tela 4 |
| Todo header | `Alvo · Ajuda` (`?`) | `Sheet G · Ajuda desta etapa` |
| Todo header | `Alvo · Voltar` (`‹`) | tela anterior |

**Por que as seis categorias da Tela 1 compartilham um destino.** Consulta médica, Fisioterapia, Exames, Procedimentos hospitalares, Procedimentos no exterior e Nutrição levam ao mesmo lugar que Psicologia: a captura da nota. O fluxo é idêntico; o que muda é o rótulo do stepper e, mais adiante, os campos específicos da Tela 3. Desenhar seis frames iguais infla o protótipo sem provar nada que o caminho de Psicologia já não prove. **Na implementação eles são telas distintas**; no protótipo, um destino só.

**O `?` do header é a exceção que confirma a regra.** Ele aparece em quase todo o fluxo e, até esta revisão, não levava a lugar nenhum. É o defeito mais espalhado do arquivo, e o mais fácil de não ver, justamente porque estava em todas as telas. O `Sheet G` é genérico de propósito: no produto real o conteúdo muda por etapa, e o wireframe mostra a versão da etapa de documentos.


# Parte 1 · Onboarding (uma vez, no primeiro acesso ao Reembolso)

> Acontece **uma única vez** por usuário e fica salvo no perfil. Reagendar ou refazer somente se algum dado pré-aprovado mudar (ex.: troca de conta bancária).

---

## Tela O.0 · Home (ponto de entrada)

**Status:** tela inicial do app, à qual o usuário sempre volta. É aqui que ele dispara o pedido de reembolso.

### Componentes e anotações UX

- **Card "Reembolso"** com destaque visual e **status do conjunto** ("1 solicitação em análise"): corrige H1 (visibilidade) já na home.
- **Três ações, três alvos.** A primeira versão deste card era um bloco único tocável, com o título *"Pedir reembolso"* e a microcopy *"Você tem 1 solicitação em análise. Toque para acompanhar."*: ou seja, o título prometia uma coisa e o texto logo abaixo prometia outra, para o mesmo toque. Separei: o card virou "Reembolso" (rótulo, não ação) e contém três alvos independentes, nesta ordem:
  1. **Rascunho salvo**: `✎ Rascunho salvo · Sessão Psicologia / 3 de 5 etapas · salvo em 05/05, 14:09 ›`, retoma direto de onde parou.
  2. **Solicitação aberta**: `◷ 1 solicitação em análise / Resposta até 08/05/2026 ›`, leva à Tela 7.
  3. **Botão "Pedir reembolso"**: inicia uma solicitação nova.
- A ordem não é acidental: **trabalho inacabado vem antes de acompanhamento**, que vem antes de começar algo novo. O rascunho é a única das três que exige ação do usuário para destravar.
- **Relação com o modal "Retomar de onde parou?".** Com o rascunho explícito na home, o caminho rápido deixa de depender do modal: quem quer continuar toca na linha e vai direto. O modal não some: ele passa a ser a **proteção do caminho oposto**, quando o usuário toca em *Pedir reembolso* existindo rascunho pendente. Sem ele, começar de novo apagaria trabalho salvo em silêncio.
- Regra geral que sai daí: **card com mais de uma ação não pode ser um alvo só**. Card com ação única (Carteirinha, atalhos, cards do Histórico) pode continuar sendo tocável por inteiro, desde que traga a sinalização explícita (`→` ou `›`).
- O botão *Pedir reembolso* leva a uma das três rotas:
  1. Primeiro acesso → onboarding (Tela O.1).
  2. Onboarding já concluído → fluxo principal (Tela 1).
  3. Já existe rascunho salvo → modal *"Retomar de onde parou?"* com opções *Retomar* / *Começar do zero*.
- O carrossel "Mais acessados" da versão atual foi substituído por uma seção plana **"Atalhos"**: corrige H8 (hierarquia confusa).
- A tab bar mantém *Ajuda* visível em toda navegação: corrige H10.

---

## Tela O.1 · Boas-vindas ao Reembolso Digital

**Status:** primeira tela do onboarding, exibida apenas no primeiro acesso à área de Reembolso. Aparece como **bottom sheet** ocupando 90% da tela (não tela cheia) para sinalizar que é um setup rápido.

### Componentes e anotações UX

- **Stepper de onboarding** diferenciado do stepper de solicitação (cor azul, não laranja), sinaliza que é um sub-fluxo.
- Lista numerada cria expectativa clara: corrige H1 (visibilidade do que virá).
- Promessa quantificada (*"menos de 3 minutos"*) reduz ansiedade: corrige H1.
- *Agora não* é importante: usuário pode adiar o onboarding e voltar quando quiser. No retorno, retoma do passo onde parou (rascunho do onboarding).

---

## Tela O.2 · Dados bancários (dois caminhos)

**Status:** passo 2 do onboarding. Foco crítico: corrige H5 (validação) e H2 (linguagem).

**De onde vêm esses dados.** A conta não é pedida no onboarding porque, na maioria dos casos, **a operadora já a tem**: vem do cadastro do plano ou de um reembolso anterior. Isso não é suposição: na tela `12.png` do fluxo atual o app já exibe `Banco 341 · Agência 00123-4 · Conta 000000004567` e oferece apenas *Confirmar* ou *Atualizar dados*. A avaliação heurística registra o problema disso (H6): *"dados bancários cadastrados: usuário precisa lembrar se a conta está atualizada"*. Confirmar em vez de digitar é justamente a correção.

Mas isso vale para o caso comum, não para todos. Quem entrou no plano agora e nunca recebeu nada não tem conta no cadastro, e não há o que confirmar. Daí os dois caminhos, na mesma convenção da O.4:

### Caminho A · Confirmação (existe conta no cadastro)

- **Banco apresentado pelo nome** (`Itaú`) com o código entre parênteses (`341`): corrige H2.
- **Conta mascarada** por padrão (final 4 dígitos), com ✎ para revelar (privacidade visual).
- **Regras explícitas como checks visuais** ("conta em seu nome", "tipos aceitos"): corrige H5 e H10.
- *Atualizar dados* abre **Sheet C** (Editar conta bancária), em vez de levar para outra tela do app.
- Se o backend detectar inconsistência (titularidade, conta inativa), exibir **banner vermelho** abaixo do card com microcopy específica da `microcopy.md`.

### Caminho B · Cadastro (não existe conta no cadastro)

- O título diz o que aconteceu antes de pedir qualquer coisa: *"Não encontramos uma conta no seu cadastro."* Sem isso, o usuário que esperava só confirmar não entende por que está diante de um formulário.
- **É o mesmo formulário do Sheet C**, promovido a tela cheia. A regra do próprio documento manda: bottom sheet para informação contextual, tela cheia para passo sequencial, e aqui é passo obrigatório do onboarding, não ajuda.
- **Estado inicial honesto**: campos vazios, titularidade **desmarcada** e CTA bloqueado com o motivo escrito (*"Preencha os dados e confirme a titularidade para continuar"*). A titularidade é afirmação do usuário; vir pré-marcada seria coletar consentimento por inércia.
- O aviso de validação muda de texto entre os dois caminhos: no A existe conta anterior valendo enquanto a nova é checada; no B não existe, então a promessa é outra: *"Vamos validar a conta antes do primeiro depósito."*
- Depois de salvo, o retorno do usuário a esta etapa cai sempre no caminho A.

---

## Tela O.3 · Termo de Ciência e Responsabilidade

**Status:** passo 3 do onboarding. Corrige H2 (linguagem), H8 (estética) e H10 (ajuda).

### Componentes e anotações UX

- **4 bullets curtos** substituem as 2 telas inteiras de juridiquês: corrige H2 e H8.
- O **link "Ler termo completo"** preserva o conteúdo legal integral para quem quiser (cumprindo compliance): corrige H10.
- O **checkbox de aceitação** é a única ação destrutiva: nenhum dado é registrado até o tap em "Aceito e continuar".
- O CTA fica **cinza desabilitado** com tooltip *"Marque a caixa para continuar"*: corrige H9.

> **Co-design obrigatório com jurídico:** os 4 bullets precisam ser homologados pela equipe de compliance da SulAmérica antes de ir para produção. A versão completa em PDF mantém a redação original.

---

## Tela O.4 · Validação de identidade (Face ID + fallback)

**Status:** passo 4 do onboarding. Move biometria do FIM (atual) para o início: corrige H5.

### Qual caminho o usuário vê

A escolha **não é do usuário, é do aparelho**, e acontece antes de qualquer tela renderizar:

| Situação do aparelho | Tela que abre | Saída alternativa |
|---|---|---|
| Biometria disponível e cadastrada | **O.4a** | *Tirar selfie em vez disso* → O.4b |
| Sem biometria, não cadastrada, ou permissão negada | **O.4b, direto** | nenhuma, é o único caminho |

Isso importa porque a O.4a diz, em texto fixo, *"Vamos usar o Face ID do seu iPhone"*. Rotear para ela um aparelho sem Face ID faz o app afirmar algo falso na primeira frase. **A checagem de capacidade vem antes da renderização**, não depois.

> **Dependência de plataforma.** "Face ID" é marca da Apple. Em Android o mesmo caminho A existe, mas a string precisa virar *"a biometria do seu aparelho"* e o ícone acompanha. Não é tradução, é variante de plataforma; registrar como tal no handoff.

### Componentes e anotações UX

- **Caminho A (Face ID)** é o default em iPhones, usuário não tira foto, só confirma. Reduz fricção dramaticamente.
- **Caminho B (selfie)** funciona sozinho, sem depender de ter passado pela O.4a, e precisa funcionar, já que é o primeiro contato de quem não tem biometria.
- **O "porquê" mora nos dois caminhos.** Na primeira versão a explicação (*"confirma que é você quem está pedindo o reembolso"*) existia só na O.4a, dentro do card *Por que isso?*. Quem não tinha Face ID caía direto numa câmera frontal aberta, sem nunca ler por que precisava fotografar o próprio rosto, o passo mais invasivo de todo o onboarding. A O.4b ganhou explicação própria **acima da câmera**, com um acréscimo que a O.4a não precisa fazer: *"A foto não vai para o seu perfil."*
- **Regras visuais como checklist persistente** durante a captura (não some quando o usuário aproxima o rosto): corrige H1.
- Em caso de falha, microcopy específica (ver `microcopy.md`): *"Não conseguimos validar. Vamos tentar de novo com mais luz?"*: corrige H9.
- Após sucesso, mostra **Tela O.5** automaticamente.

### O que o protótipo cobrou: a espera entre o toque e o sucesso

O primeiro teste clicável bateu num problema que nenhuma revisão estática tinha
pegado: tocar em *Usar Face ID* levava direto à tela de onboarding concluído. Sem
nada entre um e outro, o toque não parecia validar coisa alguma, parecia só trocar
de página.

O erro não estava na ligação, estava na ausência de uma tela. O `estados.md` já
tinha decidido a regra meses antes de ela ser cobrada: *esqueleto onde a estrutura é
previsível, spinner onde não é. Validação de identidade e envio não têm layout de
destino, e aí o spinner é honesto.* A especificação existia; a tela nunca tinha sido
desenhada, porque no fluxo estático nada exigia desenhá-la.

Daí o `Estado · Validando identidade`: spinner sobre trilho neutro, *"Validando sua
identidade"* e *"Leva alguns segundos. Não feche o app."* Avança sozinho em **1,8s**,
pela mesma regra do OCR: carregamento que exige toque não existe na vida real. Volta
e ajuda saem do cabeçalho, porque durante uma validação não há para onde voltar.

Os dois caminhos passam por ela, e essa é a parte que importa: o Face ID chega
rápido, a selfie chega depois de uma captura, mas os dois desembocam na mesma espera
antes do sucesso. Se a espera existisse só no caminho B, quem cai no fallback veria
uma tela a mais que quem não cai, e a diferença leria como se a selfie fosse a via
lenta. É a mesma simetria que fez a explicação do *porquê* aparecer nos dois lados.

> **Onde isso aparece no app atual:** a captura 28 do fluxo mapeado tem exatamente
> essa tela, um *"Validando..."* com spinner laranja. O que a versão atual acerta é
> mostrar a espera; o que ela erra é o lugar, no fim do pedido, quando desistir
> custa caro. Aqui a mesma espera acontece no onboarding, uma vez.

---

## Tela O.5 · Onboarding concluído

**Status:** confirmação de que o setup acabou. Usuário pronto para pedir reembolso.

### Anotações UX

- **Confirmação clara do que foi feito**: corrige H1 e dá senso de progresso.
- Dois caminhos diretos: começar logo ou voltar.
- Salva no perfil que o onboarding foi concluído em `dd/mm/aaaa` para auditoria de compliance.

---

# Parte 2 · Fluxo principal (a cada solicitação)

> Cinco etapas com input ativo + uma de captura inicial (que dispensa digitação). Stepper persistente no topo em todas as telas.

---

## Tela 1 · Início da solicitação

**Status:** primeira tela após o usuário tocar em *Pedir reembolso* na home.
**Stepper:** `Passo 1 de 5 · Categoria` no topo, com progresso 20%.

### Componentes

- **Header bar** (44pt, a altura de navegação do iOS) com ícone de voltar (esquerda), título centralizado, ícone de ajuda `(?)` (direita) que abre uma sheet com FAQ rápido.
- **Stepper persistente** (barra horizontal, 4pt) com porcentagem e nome da etapa. Cor `brand/primary`, ver `design-system/fundamentos.md`.
- **Card primário** com ícone, título da categoria mais usada, e microcopy contextual *"última: dd/mm/aaaa"*, diferenciado por leve sombra e fundo `#FFF7F2`.
- **Lista vertical** das demais categorias, cada item: ícone (24pt) + label + chevron à direita.
- **Botão secundário** *Refazer última solicitação* com ícone `↻`, posicionado abaixo da lista, separado por linha tênue.

### Hierarquia visual

1. Stepper + título da etapa (orientação)
2. Pergunta direta ("Qual procedimento você fez?")
3. **Mais usadas** em destaque (CTA quente para usuário recorrente)
4. Outras categorias (lista densa, equivalentes)
5. Atalho *Refazer última* (ação avançada, não compete com novo fluxo)

### Anotações de UX

- O card de "Mais usadas" só aparece se houver histórico; para o primeiro acesso, mostrar apenas "Outras categorias".
- *Refazer última* deve abrir a Etapa 5 (Revisão) já preenchida com os dados anteriores e um banner amarelo: *"Confira se algum dado mudou antes de enviar"*.
- Tap target mínimo 44×44pt em todos os itens da lista.
- Acessibilidade: contraste mínimo AA; ícones com `aria-label`.
- Não exibir pop-ups de cross-sell nesta tela.

---

## Tela 2 · Captura da nota fiscal/recibo

**Status:** etapa 2 do fluxo. Substitui a digitação manual por OCR: corrige H5, H6, H7.
**Stepper:** `Passo 2 de 5 · Nota fiscal` (40%).

### Componentes e anotações UX

- **Três cards de mesmo tamanho**, um por ação: *Tirar foto agora*, *Anexar arquivo*, *Inserir manualmente*. Mesma altura, mesma borda, mesmo peso tipográfico.
- **Por que peso igual, e não hierarquia.** A primeira versão desta tela dava um card grande à câmera, um card menor à galeria e um link solto ao preenchimento manual: hierarquia que empurrava o usuário para o caminho que o *produto* prefere, porque OCR reduz erro e retrabalho. O problema é que a escolha aqui não depende da preferência do produto, e sim de uma circunstância que o app não conhece: se a pessoa tem a nota em papel na mão, se recebeu por e-mail, se a câmera do aparelho é ruim, se está num lugar sem luz. Rebaixar visualmente duas das três opções faz o usuário em circunstância diferente sentir que está saindo do fluxo certo, quando na verdade só tem um documento em outro formato.
- Com peso igual, o subtítulo passa a carregar a orientação (*"Escolha como enviar"*) e cada card explica **quando serve**, não o quanto vale.
- Cada card é uma ação única, então o card inteiro é o alvo tocável, sem chevron, que sugeriria navegação em vez de ação.
- **Rodapé com o rascunho automático**: *"Não tem a nota agora? Seu progresso fica salvo. É só voltar quando tiver."* Esta é a tela onde o usuário mais provavelmente descobre que está sem o documento, e é onde a promessa de salvamento automático (que o resto do fluxo repete) precisa aparecer para valer alguma coisa.
- Ao tocar em "Tirar foto agora", abre câmera fullscreen com **guia de enquadramento** (ver Parte 7) e microcopy: *"Enquadre a nota fiscal toda dentro do retângulo".*
- Após captura, exibe **loading com skeleton** + microcopy contextual *"Lendo sua nota fiscal..."* (15–30s típicos).

---

## Tela 2A · Conferência dos campos extraídos (OCR)

**Status:** intermediária após OCR. Usuário valida o que foi extraído antes de prosseguir: corrige H5, H6, H9.
**Stepper:** ainda `Passo 2 de 5 · Nota fiscal` (40%).

### Componentes e anotações UX

- **O documento lido continua trocável.** O card de preview no topo traz *Ver original* **e** *Trocar*, os mesmos dois botões que a Tela 4 oferece num slot preenchido. Sem o *Trocar*, quem fotografou a nota errada ou tirou uma foto ruim só teria a saída de corrigir seis campos na mão, quando refazer a foto resolve tudo de uma vez. Vale ainda mais na variante de erro, onde os campos marcados costumam ser sintoma de uma captura ruim, não de seis enganos independentes.
- **Cada campo é um card editável** com ✎: toque expande para edição inline (não muda de tela).
- Campos com **baixa confiança do OCR** (ex.: nome difícil de ler) aparecem com **borda amarela** e microcopy *"Confira se está certo".*
- Campos com **erro de validação** (ex.: CPF inválido) aparecem com **borda vermelha** + microcopy específica.
- **Mini-preview do documento** original sempre acessível por *"Ver original"*, usuário pode comparar.
- Se OCR falhar em algum campo crítico, exibir microcopy: *"Não conseguimos ler {campo}. Por favor, digite."*

---

## Tela 3 · Detalhes do tratamento

**Status:** etapa 3. Corrige H5 (validação inline), H7 (smart defaults), H9 (mensagens).
**Stepper:** `Passo 3 de 5 · Tratamento` (60%).

### Componentes e anotações UX

- **Tipo de terapia pré-selecionado** com base em OCR + histórico (corrige H6/H7).
- **Frequência é escolha, não constante.** A primeira versão trazia o atalho como *"Semanais a partir de"*, com semanal embutido no rótulo do radio. Isso contradizia a própria tela, que oferece Psicologia, Psiquiatria e Terapias multidisciplinares logo acima: **psiquiatria costuma ser mensal**, fisioterapia pode ser duas ou três vezes por semana. Quem não fosse semanal era empurrado para *Inserir uma a uma*, perdendo o atalho justamente por não caber no caso que o produto assumiu.
- O atalho virou **"Gerar as datas para mim"**, com dois campos: *Com que frequência?* (semanais · quinzenais · mensais) e *Primeira sessão*. O preview das datas geradas continua, e é o que fecha o ciclo: o usuário vê o resultado antes de avançar (corrige H7).
- O **default da frequência acompanha o tipo de terapia**: psicologia abre em semanais, psiquiatria em mensais. Mesmo princípio do tipo pré-selecionado: o smart default vale para os dois campos ou para nenhum.
- **Regra de prazo visível ANTES** de o usuário digitar: corrige H5 (prevenção). Não esperar erro acontecer. Por isso o banner abre a pergunta *"Quando aconteceram?"* em vez de encerrar o formulário: no rodapé, ele caía abaixo da dobra e só seria lido depois do erro, que é exatamente o que ele existe para evitar.
- Em caso de modo manual, abrir tela com N campos de data; cada campo valida **inline** ao perder foco.
- Mensagem de erro de data: ver `microcopy.md`.

---

## Tela 4 · Upload de documentos complementares

**Status:** Etapa 4 do fluxo (após captura/OCR e detalhes do tratamento).
**Stepper:** `Passo 4 de 5 · Documentos` (80%).

### Componentes

- **3 cards de slot**, cada um com:
  - Indicador de estado (✓ verde quando preenchido / ☐ cinza quando pendente).
  - Título do documento.
  - Microcopy explicativa (1–2 linhas, em linguagem cidadã).
  - Ação principal em pílula: `Anexar`, ou `Ver` + `Trocar` quando já preenchido.
  - Ajuda, quando existe, no formato que corresponde ao esforço que ela pede (abaixo).
- **Pílula é ação; sublinhado é ajuda.** Os dois convivem no mesmo par de botões de cada slot, e a diferença de forma carrega a diferença de comportamento:

| Forma | Significa | Exemplos |
|---|---|---|
| **Pílula** com borda | *executa algo*: abre o seletor de arquivos, o visualizador, a câmera | `Anexar` · `Ver` · `Trocar` |
| **Texto sublinhado** | *abre conteúdo aqui mesmo*, sem sair da tela nem perder o preenchimento | `Ver exemplo` · `Como obter o recibo do IRPF` |

  O sublinhado é o que dá a sensação de clicável sem prometer navegação, que é exatamente o que um bottom sheet faz: cobre a tela e devolve o usuário ao mesmo lugar. Enquanto as duas ajudas eram pílulas iguais a *Anexar*, a interface dizia que abrir uma explicação e anexar um arquivo eram a mesma classe de coisa.
- **Status agregado** em barra inferior com contagem de pendências.
- **Botão sticky** *Avançar*, sólido laranja quando todos preenchidos, cinza desabilitado caso contrário, com microcopy *"Falta: pedido médico"*.
- **Tutorial gov.br** abre como **bottom sheet** (ver Sheet A) com 3 cards visuais (1. abrir gov.br · 2. login · 3. baixar PDF). O tutorial em si acontece dentro do app; o download, não; por isso o rótulo promete um guia, não uma solução em um toque.

### Hierarquia visual

1. Pergunta direta + regras de aceite.
2. Slots em ordem de prioridade: Nota fiscal primeiro (já preenchido pelo OCR).
3. Status agregado.
4. Avançar (sticky no fim).

### Anotações de UX

- Permitir multi-seleção de arquivos quando o usuário toca em *Anexar*.
- Pré-visualização inline (mini-thumbnail no card) ao invés de ir para outra tela.
- O slot já preenchido mostra o **nome do arquivo** e oferece *Trocar*, não pede `Confirmar` extra.
- Microcopy de erro inline quando arquivo for inválido (tamanho/formato): exibida no próprio card em vermelho-tijolo `#B71C1C`.
- Tap target mínimo 44×44pt nos botões.
- Banner *"Restam 2 documentos"* com ícone informativo (azul), não vermelho, pois não é erro, é status.

---

## Tela 5 · Revisão dos dados

**Status:** Etapa 5 do fluxo, antes do envio.
**Stepper:** `Passo 5 de 5 · Revisão` (100%).

### Componentes

- **Cards-resumo** verticais com label + valor + ícone de edição (lápis ✎). O ícone leva o usuário **direto** à etapa correspondente, com retorno automático para esta tela, sem perder o restante das informações.
- **Miniaturas** dos documentos (60×60pt) tocáveis para visualização ampliada.
- **Banner informativo** com estimativa de reembolso (só após backend retornar), claramente etiquetado como "estimativa, não garantia".
- **Botões sticky** no rodapé: *Enviar solicitação* (primário, laranja sólido) e *Salvar como rascunho* (secundário, outline).
- **Indicador de salvamento automático** "Salvo automaticamente às 14:09" no canto superior direito, em cinza claro.

### Hierarquia visual

1. Título + instrução de uso (*toque no ✎ para editar*).
2. Bloco beneficiário/prestador/procedimento (dados estruturados).
3. Bloco documentos com miniaturas (reconhecimento visual).
4. Bloco conta bancária.
5. Banner de estimativa.
6. CTAs de envio.

### Anotações de UX

- Cada lápis ✎ deve ser **visualmente discreto** (cinza médio) para não competir com o CTA.
- Ao tocar em uma miniatura, abrir lightbox/preview com gestos pinch-to-zoom.
- A microcopy *"Confira tudo antes de enviar"* substitui a abordagem do termo legal sobreposto da versão atual.
- O banner de estimativa traz transparência (não promete, sinaliza ordem de grandeza).
- *Salvar como rascunho* só aparece se o usuário tiver modificado algo desde a tela anterior; caso contrário, o app já salva sozinho em background.
- Em caso de algum dado inválido (ex.: documento corrompido, conta sem titularidade), bloco fica com borda vermelha + mensagem específica + bloqueia *Enviar*.

---

## Tela 6 · Confirmação de envio

**Status:** após envio bem-sucedido.

### Componentes

- **Ilustração de sucesso** (verde / laranja claro), sem sobrecarga visual, sem sobreposição.
- **Card-protocolo** com número formatado em grupos legíveis (`1234.5678.9012.3456.7890`) e botão *Copiar* embutido.
- **Lista numerada** "O que acontece agora": 3 marcos com cronograma esperado.
- **3 ações principais empilhadas** + 1 link de saída.

### Hierarquia visual

1. Ilustração de sucesso + frase de status (clara, sem hedge "se estiver tudo certo").
2. Protocolo com botão de copiar.
3. Próximos passos (transparência sobre o pós-envio).
4. CTAs de continuidade (acompanhar / repetir / compartilhar).
5. Saída secundária.

### Anotações de UX

- **NÃO** exibir o NPS aqui. Disparar push 24–48h depois (`Como foi pedir reembolso?`).
- *Adicionar mais uma sessão* leva ao fluxo de Etapa 2 com prestador, conta bancária e tipo de terapia **pré-preenchidos**.
- *Acompanhar status* leva à Tela 7.
- *Compartilhar protocolo* abre o share-sheet nativo (WhatsApp, e-mail, copiar) com texto pronto (ver `microcopy.md`).
- Usar fundo branco limpo, sem modais sobrepostos. Para acessibilidade: ilustração com `aria-hidden`, foco inicial no título.
- Botão *Voltar ao início* discreto, para não competir com as ações de continuidade.

---

# Parte 3 · Pós-envio

---

## Tela 7 · Acompanhar status da solicitação

**Status:** depois do envio, sempre que o usuário toca em "Acompanhar status" ou em um item do histórico em andamento.

### Componentes e anotações UX

- **Timeline com 4 marcos**: Enviado → Em análise → Aprovado → Pago. Cada marco fica preto/cinza dependendo do andamento.
- **Previsão de próximo marco** SEMPRE visível ("Previsão de resposta: até dd/mm"): corrige H1.
- Se a solicitação for **rejeitada** ou **pendente de mais documentos**, exibir card vermelho-alaranjado com motivo e CTA *"Corrigir"* que leva direto ao ponto.
- "Pedir ajuda" abre chat, não sai do app: corrige H10.

---

## Tela 8 · Histórico de solicitações

**Status:** lista de todas as SRs do usuário. A entrada é o link *Ver todas as solicitações*, no pé do card de Reembolso da home, e ela só aparece para quem tem histórico. Ver *Onde mora a entrada do histórico*, no começo deste documento.

### Componentes e anotações UX

- **Agrupamento por mês** dá contexto temporal: corrige H1.
- **Status visual com cor + ícone** (verde/cinza/laranja/vermelho): corrige H1, H4.
- **Cards com pendência** ficam no topo do grupo e têm CTA destacado *"Resolver agora"*: corrige H9.
- Search e filtros para usuário com muitas solicitações.

---

# Parte 4 · Bottom sheets e auxiliares

---

## Sheet A · Tutorial gov.br

**Status:** acionado pelo link "Como obter" no slot "Comprovante de pagamento" da Tela 4.

### Anotações UX

- Cada card tem **mini-ilustração** com a tela real do gov.br (não screenshot real, wireframe estilizado): corrige H10 e H6.
- *Abrir gov.br* abre via `universal link` se o app gov.br estiver instalado; caso contrário, abre no Safari mantendo a sessão do SulAmérica ativa (deep-link de retorno).
- Após retorno, banner: *"Você baixou o recibo? Toque em 'Anexar' para enviar."*

---

## Sheet B · Exemplos de documento

**Status:** acionado pelo link "Ver exemplo" em qualquer slot da Tela 4.

### Anotações UX

- Imagem com **anotações visuais** (setas + labels): corrige H6 (reconhecimento) e H10.
- **Três frames, um por slot.** O layout é o mesmo (título, imagem-modelo, checklist e CTA) e só o conteúdo muda. Cheguei a tratar isso como template de um frame só, o que bastaria para revisar o design; **não basta para prototipar**, porque um link de protótipo aponta para um frame concreto, não para uma instrução. As três checklists estão em `microcopy.md` (*Exemplos de documento*).
- O frame está montado sobre a **Tela 4**, que é de onde o link parte, e o slot que abriu a sheet é o do pedido médico; daí o exemplo escolhido.
- As checklists são a parte que precisa de **homologação com a área de regulação de reembolso**. Uma checklist otimista gera exatamente o retrabalho que o redesign tenta eliminar: o usuário anexa achando que cumpriu, e a solicitação volta.

---

## Sheet C · Editar conta bancária

**Status:** acionado em qualquer tela onde apareça a conta bancária (Onboarding O.2, Revisão Tela 5, Acompanhar Tela 7).

### Anotações UX

- **Autocomplete de banco por nome**: usuário digita "Itaú" e o app mostra; nunca pede o código primeiro. Corrige H2, H6.
- **Máscaras em todos os campos numéricos**: corrige H5.
- **Checkbox de titularidade explícito** com CPF visível: corrige H5 e H10.
- A validação real da conta (banco × agência × conta × DV) é **assíncrona**: o usuário salva e recebe push em até 1 dia útil. Enquanto isso, a conta antiga continua válida: corrige H1 e H3.

---

# Parte 5 · Estados especiais

> Os dois primeiros são **estados de primeiro acesso**: o que o usuário vê antes de existir qualquer histórico. Sem eles, o fluxo só está desenhado para quem já usou o app, que é justamente quem tem menos dificuldade.

---

## Estado · Home no primeiro acesso

**Quando aparece:** usuário nunca pediu reembolso. Substitui a Tela O.0 até a primeira solicitação existir.

### Anotações UX

- O card *Reembolso* **perde a linha de status**: não há solicitação para acompanhar, então o alvo simplesmente não existe. Sobra um único alvo, o botão *Pedir reembolso*. No lugar do status, uma linha que **antecipa o esforço**: *"Primeira vez? A gente prepara tudo com você em 3 passos rápidos."*, mesma promessa da O.1, para que o onboarding não chegue de surpresa.
- O botão leva ao onboarding (O.1), não à Tela 1: corrige H1 (o usuário sabe o que vem).
- Nada mais muda na home. Resistir à tentação de encher a tela de estado vazio: o resto (carteirinha, atalhos) já é útil no primeiro dia.

### A home tem três estados, não dois

Outro achado do protótipo clicável, e do mesmo tipo do Face ID: o defeito só existe
quando alguém percorre o fluxo de verdade. Ao terminar o onboarding e tocar em
*Voltar para a home*, a pessoa caía nesta tela; tocava em *Pedir reembolso* e **o
onboarding recomeçava**. Fazer duas vezes o que a O.5 acabou de dizer que estava
feito.

A causa é que eu tinha modelado a home por **histórico**, e o eixo certo são dois:

| Estado | Onboarding | Histórico | O que muda |
|---|---|---|---|
| `Home no primeiro acesso` | não feito | nenhum | *Pedir reembolso* → O.1, e a linha *"Primeira vez?"* |
| `Home após o onboarding` | feito | nenhum | *Pedir reembolso* → Tela 1, e a linha vira *"Tudo pronto."* |
| `Tela O.0 · Home` | feito | existe | ganha rascunho e solicitação em análise |

As duas primeiras são pixel por pixel a mesma tela, menos uma frase e um destino, e
foi exatamente por isso que o buraco passou: **olhando, elas são iguais; clicando,
não**. Wireframe não distingue estado por destino, só por aparência. É o argumento
mais forte que encontrei, neste projeto, para prototipar antes de entregar.

O texto acompanha o estado, porque senão a tela mente: *"Primeira vez? A gente
prepara tudo com você em 3 passos rápidos."* é falso no segundo em que os 3 passos
terminam. Depois do onboarding ele vira *"Tudo pronto. Seus dados já estão salvos,
agora é só enviar a nota."*, que troca a promessa de preparo pela remoção de
fricção: o motivo de a próxima tela não pedir nada além da nota.

> **Na implementação isso não são três telas**, é uma com duas flags (`onboarding
> concluído`, `tem histórico`). Aqui são três frames porque protótipo aponta para
> frames, não para condições, a mesma razão que já valia para as Sheet B.

---

## Estado · Primeiro acesso (Tela 1 sem histórico)

**Quando aparece:** primeira solicitação do usuário, logo após concluir o onboarding (O.5).

### Anotações UX

- **Sem a seção "Suas mais usadas"**: ela depende de histórico. Sem histórico, ela não aparece vazia nem com placeholder: some.
- Com uma lista só na tela, o rótulo **"Outras categorias" deixa de fazer sentido** (outras em relação a quê?) e vira **"Categorias"**. É a única diferença de microcopy entre este estado e a Tela 1 normal, e é fácil de esquecer na implementação.
- **Sem o atalho "Refazer última solicitação"** no rodapé, pela mesma razão.
- A lista mostra as 7 categorias ordenadas pela frequência geral do plano, já que não há sinal individual para priorizar.
- Sobra espaço em branco no rodapé, e tudo bem: não preencher com cross-sell nem com dica genérica. A tela pede uma escolha, e a escolha está toda visível sem rolar.

---

## Estado · Loading com skeleton

**Quando aparece:** ao abrir Reembolso pela primeira vez na sessão; ao processar OCR; ao buscar histórico.

### Anotações UX

- **Skeleton** em vez de spinner cinza: corrige H1.
- **Microcopy contextual** ("Carregando seu plano…", "Lendo sua nota fiscal…") diz **o que** está acontecendo.
- Após 8s sem resposta, exibir banner *"Está demorando mais que o normal."*
- Após 15s, exibir botão *"Tentar novamente"*.

---

## Estado · Empty state (sem histórico)

**Quando aparece:** primeira vez do usuário na Tela 8 (Histórico).

### Anotações UX

- **Ilustração leve**, sem peso emocional negativo.
- Texto explicativo do que vai aparecer ali: corrige H1 e H10.
- Um único CTA, claro.

---

## Estado · Erro de rede

**Quando aparece:** falha em qualquer chamada de backend.

### Anotações UX

- **Não bloqueia a tela**: usuário continua vendo o conteúdo já carregado.
- **Reassurance explícita** ("Seus dados estão salvos"): corrige H1, H3, H5.
- **Retry inline**: corrige H9.
- Se a desconexão for prolongada, exibir banner no topo de todas as telas, similar a Apple Pay/iMessage.


## Estado · Documentos completos (Tela 4)

**Quando aparece:** os três documentos anexados. É o estado que destrava a etapa.

### Anotações UX

- **Cada slot preenchido troca de conteúdo, não só de ícone.** A microcopy explicativa ("Documento com nome do paciente, assinatura do profissional e diagnóstico") **some** e dá lugar ao nome do arquivo. Ela existia para ajudar a escolher o documento certo; com o arquivo anexado, ela vira ruído entre o usuário e as ações.
- **A ajuda também some.** Sem documento, o slot oferece *Ver exemplo* ou *Como obter o recibo do IRPF*; com documento, oferece *Ver* e *Trocar*. Manter o link de ajuda ali sugeriria que ainda falta entender alguma coisa.
- **O status do conjunto vira confirmação**, não contagem: *"Tudo pronto para a próxima etapa."* (ver `microcopy.md`). O botão *Avançar* passa de cinza para sólido, e é a única mudança de estado do rodapé fixo.
- **O título da tela não muda.** Continua *"Anexe os 3 documentos"* mesmo com os três anexados: ele nomeia para que serve a tela, não o estado dela. Quem carrega o estado são os três ✓, o nome dos arquivos e o banner. Título que muda a cada estado faz a tela parecer outra.

---

# Parte 6 · Erros e validação

> As 24 telas anteriores mostram o caminho feliz. Estas três mostram o que acontece quando ele não acontece, que é onde o fluxo observado travou, e onde a qualidade da mensagem decide se a pessoa corrige ou desiste. Os textos exatos estão em `microcopy.md`.

**Como erro e alerta aparecem num wireframe em escala de cinza.** Sem cor, a diferença é feita por peso de borda e glifo, e cada um mapeia para uma cor na alta fidelidade:

| Estado | No wireframe | Na alta fidelidade |
|---|---|---|
| **Erro** (bloqueia o avanço) | borda contínua 2pt `#1a1a1a` + glifo `⚠` | borda `feedback/error` `#D32F2F` |
| **Alerta** (não bloqueia, pede conferência) | borda tracejada 1.5pt `#8c8c8c` + glifo `ⓘ` | borda `feedback/warning` `#F9A825` |

---

## Erro · Data fora do prazo (Tela 3)

**Quando aparece:** usuário informa uma data de atendimento anterior à janela de 12 meses.

### Anotações UX

- É a mensagem-bandeira do redesign. O app atual só reage **depois** do envio, com *"O pedido só pode ser feito para procedimentos realizados antes do dia 04/05/2026"*, que informa uma data sem dizer o que fazer. A versão nova diz o limite e **entrega a data válida**: *"Data fora do prazo de 12 meses. Última data válida: 04/05/2025."*
- O banner de regra continua visível no rodapé mesmo com o erro na tela. Redundância proposital: a regra preventiva e a mensagem corretiva dizem a mesma coisa em momentos diferentes, e quem já errou uma vez precisa das duas.
- **O preview das datas geradas some.** Com data inválida não há o que gerar, e manter "05/02, 12/02, 19/02 e 26/02" na tela sugeriria que algo foi aceito.
- O CTA fica desabilitado: corrige H5 (nenhuma tela deixa avançar com dado inválido).
- O erro nasce ao **perder o foco** do campo, não a cada tecla digitada: validar durante a digitação acusa erro em número ainda incompleto.

---

## Erro · Campos com alerta e erro (Tela 2A)

**Quando aparece:** o OCR leu a nota, mas um campo saiu inválido e outro saiu com baixa confiança.

### Anotações UX

- **Dois níveis, não um.** O CPF inválido bloqueia (`⚠`, borda contínua); o nome com leitura incerta apenas pede conferência (`ⓘ`, borda tracejada). Tratar os dois como erro treinaria o usuário a ignorar os dois.
- O CTA passa a dizer **o que falta**, não um genérico *Avançar*: *"Corrija o CPF para avançar"*. Botão cinza silencioso é o antipadrão que o app atual tem hoje.
- O banner agregado muda de *"Encontramos 6 campos"* para *"Encontramos 6 campos. 2 precisam da sua atenção."*. A contagem de pendências evita que o usuário role a lista procurando o problema.
- Só os campos marcados ganham borda. Marcar todos, mesmo os corretos, transformaria a tela num formulário de erros.
- Se o OCR falhar em campo crítico, a microcopy é outra: *"Não conseguimos ler {campo}. Por favor, digite."*

---

## Erro · Solicitação com pendência (Tela 7)

**Quando aparece:** a análise parou porque falta documento, ou a solicitação foi recusada.

### Anotações UX

- Fechava um fio solto: o Histórico (Tela 8) já tinha um card *"Aguardando documento · Resolver agora →"* que **apontava para uma tela que não existia**.
- **A ação de recuperação fica dentro do card de status**, não no rodapé. O motivo e a saída precisam estar no mesmo bloco visual, senão o usuário lê o problema e rola procurando o que fazer.
- A timeline **não regride**: o marco continua sendo o segundo, mas passa a se chamar *Pendência* e a legenda vira *"Parado aqui até você enviar o documento"*. Mostrar a solicitação voltando ao início daria a impressão de que o trabalho foi perdido.
- A previsão de resposta **some** enquanto está pendente. Manter "até 08/05" seria uma promessa que o app não pode cumprir enquanto depende do usuário.
- O documento que falta aparece como **slot tracejado com `＋`** entre os já enviados, e a contagem vira "2 de 3". O buraco fica visível em vez de implícito.
- *Compartilhar protocolo* sai do rodapé: com pendência aberta, só há uma ação que importa.

---

# Parte 7 · Captura, espera e retomada

---

## Tela 2 · Câmera (guia de enquadramento)

**Quando aparece:** ao tocar em *Tirar foto agora* na Tela 2.

### Anotações UX

- É onde a qualidade do OCR é ganha ou perdida. O **retângulo-guia** não é decoração: ele define o recorte que vai para o motor de leitura.
- Microcopy em duas camadas: a instrução (*"Enquadre a nota fiscal toda dentro do retângulo"*) e a causa mais comum de falha (*"Evite sombra e reflexo"*). A segunda linha existe porque reflexo em papel térmico é o motivo nº 1 de leitura ruim.
- **Fundo escuro, controles claros**: única tela do fluxo que inverte a paleta, e de propósito: sinaliza modo de captura, não de formulário.
- *Galeria* fica acessível aqui também: quem abriu a câmera por engano não precisa voltar.
- *Exemplo* abre o **Sheet B** sem perder o enquadramento.

---

## Estado · Lendo sua nota fiscal

**Quando aparece:** entre a captura e a Tela 2A, tipicamente 15–30s.

### Anotações UX

- **Skeleton na forma dos campos que virão**, não spinner. O usuário já vê a estrutura da tela seguinte se montando: reduz a sensação de espera e antecipa o que ele vai ter que conferir.
- O documento capturado aparece no topo, confirmando **o que** está sendo lido.
- Microcopy dá a duração esperada e libera o usuário: *"Isso leva de 15 a 30 segundos. Pode deixar o app aberto."*
- O CTA existe mas está desabilitado com *"Aguarde a leitura"*; some seria pior, porque a tela perderia o rodapé e "pularia" quando ele voltasse.
- Após 8s a mais que o previsto, banner *"Está demorando mais que o normal."*; após 15s, *"Tentar novamente"*.

---

## Modal · Retomar de onde parou?

**Quando aparece:** terceira das três rotas de entrada descritas na Tela O.0: usuário toca em *Pedir reembolso* e existe rascunho salvo.

### Anotações UX

- É o **pagamento da promessa de salvamento automático** que o case repete em várias telas. Sem esta tela, "salvo automaticamente às 14:09" é uma afirmação que o usuário nunca vê ser cumprida.
- O modal **diz o que está salvo**, não só que existe algo: categoria, data e hora, "3 de 5 etapas preenchidas" com a barra de progresso e quais etapas já foram. Sem isso, *Retomar* é uma aposta.
- *Começar do zero* é secundário e **não é destrutivo por engano**: descarta apenas o rascunho, e o rascunho anterior permanece recuperável no Histórico por 30 dias.
- Modal, não bottom sheet: é uma bifurcação de rota que precisa de resposta antes de seguir. Bottom sheet fica reservado para informação contextual (Sheets A–C).
- A tela por trás continua visível sob o escurecimento: mostra ao usuário onde ele vai cair se escolher *Começar do zero*.

---

# Parte 8 · Detalhe, filtros e ajuda

Esta parte não veio do fluxo: veio da auditoria de protótipo descrita no *Mapa de destinos*. São as seis telas que a interface **já prometia** e que não existiam, mais a que faltava para fechar a promessa do salvamento de protocolo.

---

## Tela 9 · Detalhe da solicitação paga

**Quando aparece:** `Ver detalhes →` nos cards de solicitação paga do Histórico.

### Anotações UX

- Era o buraco mais grave do arquivo. A seta `→` é uma **promessa explícita de navegação**, escrita na própria tela, e não tinha para onde ir. Uma seta que não leva a lugar nenhum é pior do que nenhuma seta: ela ensina o usuário a duvidar das outras.
- A tela responde à pergunta que o card não cabe: **por que R$ 450,00 e não R$ 600,00?** O bloco *Valores* mostra solicitado, reembolsado e, num banner, a razão da diferença: a coparticipação de 25% prevista no plano. Sem essa linha, o usuário atribui a diferença a erro da operadora, e é exatamente aí que nasce a ligação para a central.
- A explicação é **texto fixo, não link**. Um *"por que o valor foi menor?"* sublinhado criaria mais um destino a desenhar para entregar a mesma frase, e a frase cabe.
- O andamento aparece como três linhas datadas em vez de timeline gráfica: a solicitação já terminou, então o estado é histórico, não progresso.
- O protocolo repete o padrão de cópia da Tela 6, incluindo o alvo de 44pt.

---

## Sheet D · Filtrar histórico

**Quando aparece:** chip `Filtrar ▾` no Histórico.

### Anotações UX

- O `▾` no chip é a mesma convenção dos campos com picker: **abre algo aqui, não navega**. Por isso é bottom sheet e não tela cheia.
- **Situação usa checkbox, período usa radio.** A diferença não é estética: dá para querer ver *em análise* e *aguardando documento* ao mesmo tempo, mas não dois períodos. A forma do controle já responde "posso marcar mais de um?" antes do usuário tentar.
- O sheet abre com **Em análise** e **Aguardando documento** marcados, as duas situações que pedem ação do usuário. O filtro mais útil é o padrão, não a lista vazia.
- `Limpar tudo` é sublinhado, não botão: desfaz sem sair.

---

## Sheet E · Quem fez o procedimento?

**Quando aparece:** `✎ Beneficiário` na Revisão.

### Anotações UX

- Foi o gap que a auditoria revelou por eliminação: dos cinco `✎` da Tela 5, quatro voltavam para uma etapa do fluxo (2A, 3, 4, Sheet C) e o do beneficiário **não tinha para onde voltar**: não existe etapa onde se escolha o paciente.
- Isso expôs uma decisão implícita no fluxo: até aqui, o beneficiário era sempre o titular. Em plano familiar isso é falso na maior parte das vezes: filho e cônjuge geram mais reembolso que o titular.
- O aviso é a parte importante: **trocar o beneficiário pode mudar os documentos exigidos**. Reembolso de dependente menor costuma pedir documento adicional. Sem esse aviso, a troca acontece na revisão e a recusa chega três dias depois.
- Radio, não lista com `›`: escolher uma pessoa é selecionar, não navegar.

---

## Sheet F · Buscar banco

**Quando aparece:** campo `Banco` na O.2b e no Sheet C.

### Anotações UX

- O campo já dizia *"Buscar banco pelo nome ▾"* e não abria nada. Era um dos destinos prometidos e não desenhados.
- **Busca e lista juntas.** São mais de 200 instituições; nenhum picker rolável resolve, e nenhuma busca pura ajuda quem não lembra o nome exato ("Nubank" ou "Nu Pagamentos"?).
- O bloco *Mais usados* vem antes de *Todos*, com o número do banco à esquerda em cinza. O número serve a quem tem o dado bancário na mão e não quer errar de banco pelo nome parecido.
- Linhas de 58pt, sem CTA: tocar já escolhe e fecha. Um botão *Confirmar* aqui só adicionaria um toque.

---

## Sheet G · Ajuda desta etapa

**Quando aparece:** ícone `?` no header, presente em quase todas as telas do fluxo.

### Anotações UX

- **O defeito mais espalhado e o mais fácil de não ver.** O `?` estava em mais de trinta telas sem destino. Como aparecia em todas, virou paisagem.
- Acordeão, não lista com `›`. Se cada pergunta abrisse uma tela, o `?` teria gerado uma árvore de destinos. `▾` mantém tudo aqui, e é a mesma convenção do resto do arquivo.
- A primeira pergunta já vem aberta: mostra que as linhas expandem, sem precisar de instrução.
- O conteúdo é **específico da etapa**. O wireframe mostra a versão da etapa de documentos; na implementação o sheet recebe o conjunto de perguntas do passo atual. Um FAQ genérico obrigaria o usuário a procurar exatamente no momento em que ele já está travado.
- `Falar com atendimento` é a saída honesta quando a ajuda não resolve, e é o único ponto do fluxo onde o chat é oferecido de forma deliberada.

---

## Estado · Protocolo copiado (Tela 6)

**Quando aparece:** toque em `Copiar` na confirmação de envio.

### Anotações UX

- Cópia sem confirmação é a ação mais fácil de duvidar: nada muda na tela, e o usuário toca de novo. O toast existe para encerrar essa dúvida.
- **Dois sinais, não um.** O botão vira `✓ Copiado` com contorno escuro (permanente na sessão) e o toast aparece por ~2s (transitório). O botão responde "funcionou?" mesmo depois que o toast some.
- O toast é escuro sobre a tela clara: é a única inversão de paleta fora da câmera e do visualizador, e marca que ele é camada de sistema, não conteúdo.
- Nesta tela o alvo de `Copiar` também foi corrigido: **estava com 27pt**, no meio de uma tela cuja função inteira é entregar esse número.

---

# Notas gerais para o designer

## Convenção de altura dos frames

A altura do frame carrega significado, não é só o tamanho do artboard:

**Todos os 44 frames têm 390 × 844pt**, iPhone 13/14. Nenhuma exceção: o frame é a viewport, e mostra exatamente o que o usuário vê sem rolar. Telas cujo conteúdo passa de 844 não crescem; elas **cortam**, como o aparelho corta.

### Telas que rolam

Doze telas têm mais conteúdo do que cabe (quatorze na página `mockups`, que soma as duas telas de apoio do protótipo). Elas são marcadas por três elementos. Os dois primeiros são anotação e não fazem parte da interface; o terceiro é layout de verdade:

| Marcação | Especificação |
|---|---|
| `Scroll indicator` | 3pt de largura, `#8c8c8c` a 50%, raio 1,5, encostado na borda direita (4pt de recuo), começando 8pt abaixo do topo do `Conteúdo rolável`. Comprimento proporcional: `(janela ÷ conteúdo) × (janela − 16)`. **Só na página `wireframes`**: é anotação, e mockup não carrega anotação |
| `Rodapé fixo` | Frame branco ancorado na base da viewport, com sombra `elev/sticky` (`0 −2 8`, preto 6%) marcando que o conteúdo passa por baixo |
| `Conteúdo rolável` | Frame sem preenchimento entre o cabeçalho e o rodapé, com altura fixa igual à janela útil e `overflow: vertical`. **É ele que rola**, não o aparelho. Ver *O rodapé fixo rolava junto*, abaixo |

Os números abaixo são da página `wireframes` e seguem a construção atual: o cromo
de topo (status bar e cabeçalho, 88pt em toda tela) e o rodapé ficam **fora** da
área que rola, e a janela é o que sobra entre os dois.

| Tela | Rodapé | Janela | Conteúdo | Rola |
|---|---|---|---|---|
| Estado · 2 de 3 documentos | 168pt | 588pt | 599pt | 11pt |
| Estado · Lendo sua nota fiscal | 156pt | 600pt | 622pt | 22pt |
| Tela O.0 · Home | 84pt *(tab bar)* | 672pt | 696pt | 24pt |
| Tela 4 · Upload de documentos | 183pt | 573pt | 625pt | 52pt |
| Tela 3 · Detalhes do tratamento | 75pt | 681pt | 741pt | 60pt |
| Erro · Data fora do prazo | 75pt | 681pt | 757pt | 76pt |
| Estado · Preenchimento manual | 156pt | 600pt | 713pt | 113pt |
| Tela 9 · Detalhe da solicitação paga | 102pt | 654pt | 857pt | 203pt |
| Tela 2A · Conferência (OCR) | 156pt | 600pt | 821pt | 221pt |
| Tela 5 · Revisão | 164pt | 592pt | 855pt | 263pt |
| Erro · Campos com alerta e erro | 171pt | 585pt | 865pt | 280pt |
| Estado · Retomada de rascunho | 164pt | 592pt | 931pt | 339pt |

A página `mockups` tem as mesmas doze mais duas telas de apoio do protótipo:
`Tela 3 · Detalhes (vazio)`, que rola 30pt, e `Preenchimento manual (preenchido)`,
que rola 96pt. Nela a 2A e o erro de campos rolam 2pt a menos, porque o rodapé é
1pt mais baixo depois que a biblioteca foi aplicada.

> **A Sheet E saiu desta tabela.** O conteúdo dela também passa da janela, mas o que
> passa é a Tela 5 servindo de fundo atrás do scrim. Fundo de sheet não rola: quem
> rola é o painel, e o painel cabe inteiro. A home é o caso oposto e por isso entrou:
> ali o que rola é a tela de verdade, e quem fica parado é a tab bar.

**A Tela 4 saiu e voltou para esta lista, e o motivo vale registrar.** O rodapé fixo dela leva o banner de pendências junto com o *Avançar* bloqueado (a contagem e a ação que ela trava são um par). Por um tempo o conteúdo coube exatamente na janela, por 2pt, e ela saiu da lista junto com as cinco telas que a clonam (Sheets A, B ×3 e G). Ao ganhar o *Ver exemplo* no slot de comprovante, o card cresceu 54pt e ela voltou a rolar, agora 52pt. Dois pontos de folga não são folga: qualquer acréscimo de conteúdo derruba. Hoje são 11 telas que rolam em `wireframes` e 13 em `mockups`.

As telas de revisão cresceram nesta rodada porque cada `✎` passou a ocupar 44pt em vez de 17; ver *Um alvo por ação*, adiante. Isso empurrou a Revisão de 129 para 263pt de rolagem. É o custo correto: um alvo tocável de 17pt não é tocável.

### O rodapé fixo rolava junto

Terceiro defeito que só o protótipo cobrou, e o que levou duas tentativas para
acertar. Na Tela 2A a tela rolava, mas os últimos campos lidos pelo OCR nunca
apareciam.

O primeiro diagnóstico estava certo pela metade. O conteúdo da 2A tem 909pt num
frame de 844, então sobravam 65pt de rolagem, e o rodapé ocupa os 156pt de baixo:
o fim do conteúdo parava atrás dele. A correção foi somar um espaçador transparente
com a altura do rodapé, o mesmo *content inset* que iOS e Android aplicam sob uma
barra fixa. A conta fechou, a rolagem cresceu para os 221pt que a tabela acima
sempre previu, **e o problema continuou**, porque o rodapé rolava junto com o
conteúdo. Ele estava absoluto dentro do aparelho, e absoluto em auto layout não é o
mesmo que fixo na rolagem: são duas propriedades distintas, e a segunda não estava
ligada.

A construção certa não depende dessa propriedade. **Quem rola não é o aparelho, é um
frame interno.** Cada tela passou a ter três blocos: o cromo de topo (status bar e
cabeçalho), um `Conteúdo rolável` de altura fixa igual à janela útil, e o rodapé.
Os três somam exatamente 844, o rodapé é irmão da área que rola em vez de estar por
cima dela, e o espaçador deixou de fazer sentido e saiu. É como qualquer app é
montado de verdade: a barra não fica parada por truque de ancoragem, ela fica parada
porque está fora do container que rola.

| | Antes | Agora |
|---|---|---|
| Quem rola | o aparelho inteiro | o `Conteúdo rolável` |
| Rodapé | absoluto, por cima, rolando junto | irmão da área que rola, parado |
| Janela útil da 2A | 844, com 156 cobertos | 600, e nada coberto |

A varredura que corrigiu isso achou o irmão maior do defeito: **das dez telas que
rolam, sete estavam com a rolagem simplesmente desligada** (`overflow: none`),
inclusive duas telas de erro. Nessas, o conteúdo abaixo do corte era inalcançável,
e não só o pedaço atrás do rodapé. Numa tela de correção de erro é o pior caso
possível: o que está escondido é justamente a explicação do que corrigir. Hoje são
nove telas rolando na página `wireframes` e onze em `mockups`, cada uma com o valor
exato da coluna *Rola* da tabela acima.

**A Sheet E fica de fora de propósito.** O conteúdo dela também passa de 844, mas é
a Tela 5 servindo de fundo atrás do scrim. Fundo de sheet não rola: quem rola é o
painel, e o painel cabe inteiro. Rolar o que está atrás do escurecimento seria
simular uma interação que nenhum app permite.

A lição é a mesma das outras duas: **marcação de rolagem não é rolagem**. O
`Scroll indicator` estava desenhado nas dez telas desde o começo, anunciando um
comportamento que sete delas não tinham. Uma anotação correta ao lado de um arquivo
que não a cumpre passa em qualquer revisão visual, e passou.

**Por que o rodapé é fixo, e não o fim da rolagem.** Antes de fixar, os três CTAs principais caíam fora da primeira tela: o de *Corrija o CPF para avançar* ficava inteiro abaixo do corte. Isso deixava o usuário da tela de erro vendo campos marcados e **nenhuma indicação do que fazer**, porque tanto o resumo de pendências quanto o botão bloqueado estavam fora da vista. Numa tela de correção de erro, esconder a saída é o pior lugar possível para economizar espaço.

Nas duas telas de OCR o rodapé fixo carrega **o banner de status junto com o botão**, mesma decisão da Tela 4: a contagem de pendências e a ação que elas bloqueiam são um par e não podem se separar.

**O custo dessa escolha:** o frame mostra só a primeira tela, então parte do conteúdo fica escondida atrás do rodapé no arquivo estático. É proposital: o corte no meio de um campo é o próprio sinal de que há mais abaixo. Para revisar o conteúdo inteiro de uma tela que rola, use o protótipo, não o frame.

**Sobreposições sempre em frame de 844.** Bottom sheets e modais nunca são desenhados soltos. Cada um é um aparelho inteiro contendo: a tela que o abriu, uma camada de escurecimento a 45% e o painel por cima, ancorado na base, no caso do sheet; centralizado, no caso do modal.

Duas razões. A primeira é honestidade: sheet não flutua no vazio, ele cobre uma tela específica, e mostrar qual deixa explícito de onde o usuário veio e para onde volta ao fechar (Sheets A, B e G saem da Tela 4; o C e o F, da O.2; o D, da Tela 8; o E, da Tela 5). A segunda é de leitura do quadro: um frame mais baixo e de base reta, ao lado de aparelhos inteiros, parece tela cortada. Foi exatamente assim que os sheets estavam antes.

A altura do painel continua seguindo o conteúdo, de 483pt (Sheet G) a 765pt (Sheet A); o que muda é que ela é medida dentro do aparelho, não como o frame todo.

**Ancorado na base era regra, não era arquivo.** Quatro dos nove sheets estavam
presos pelo **topo**: cresciam para baixo conforme o conteúdo, e passavam da borda
do aparelho. No *Exemplo: nota fiscal* e no *Exemplo: comprovante* isso cortava o
botão *Entendi, anexar agora*, que ficava 5pt para fora. A conta é direta: os dois
têm cinco itens de checklist contra os quatro do *pedido médico*, e cada item pesa
29pt. O painel cresceu 29pt para baixo em vez de subir 29pt.

| Sheet | Topo antes | Base antes | Topo agora |
|---|---|---|---|
| A · Tutorial gov.br | 133 | 898 | 79 |
| B · Exemplo · nota fiscal | 230 | **873** | 201 |
| B · Exemplo · comprovante | 230 | **873** | 201 |
| C · Editar conta bancária | 134 | 852 | 126 |

Os nove agora fecham em 844 e todos deixam **24pt abaixo do último elemento
tocável**, a mesma folga do `Rodapé fixo`. Os painéis passaram a ter constraint
vertical `MAX`, para que crescer conteúdo empurre o topo para cima em vez de
empurrar o botão para fora.

É o terceiro defeito da mesma família numa semana: o documento descrevia o
comportamento certo (*"o painel por cima, ancorado na base"*, dois parágrafos
acima) e o arquivo fazia outra coisa. A diferença entre os dois só aparece quando
o conteúdo muda de tamanho, e num arquivo estático o conteúdo nunca muda.

> **Nomes de camada, de quebra.** As checklists de nota fiscal e comprovante ainda
> se chamavam `Checklist · Nome do paciente`, herdado do *pedido médico*, que é de
> onde essas duas sheets foram clonadas. O texto sempre esteve certo; o nome é que
> mentia, e nome de camada errado foi a causa-raiz do defeito de alvos pequenos
> descrito em *Um alvo por ação*. Doze camadas renomeadas a partir do próprio texto.

**Rodapé grudado na base.** Toda tela com bloco de rodapé (CTA, ações, link de escape) tem um `Spacer` elástico logo antes dele, empurrando-o para a borda inferior. Sem isso o botão flutua no meio da tela quando sobra espaço, e sobra em quase toda tela do onboarding. Na Tela 4 o `Spacer` vem **antes do banner de status**, porque o banner ("Restam 2 documentos") e o botão *Avançar* são um par: a pendência precisa estar colada na ação bloqueada.

**Telas sem rodapé** (Tela 2 · Captura, Estado · Primeiro acesso) terminam onde o conteúdo termina, alinhadas ao topo, e sobra branco embaixo. É intencional: são telas de escolha, e centralizar a lista só afastaria o primeiro item do título.

## Outras notas

- **Padronização**: caixa mista em todos os botões (não usar caixa alta).
- **Microcopy**: ver `microcopy.md` para textos exatos de todas as telas.
- **Estados**: prever empty/loading/erro de cada tela, usando os padrões da Parte 5.
- **Acessibilidade**: contraste mínimo AA, tap targets ≥ 44pt, suporte a Dynamic Type (escalonamento), VoiceOver com rótulos descritivos.
- **Um alvo por ação.** Se um bloco oferece mais de uma coisa para fazer, cada uma precisa da própria área tocável: botão ou linha com `›`. Bloco com ação única pode ser tocável por inteiro. O sintoma de que a regra foi quebrada é a microcopy: quando o texto de apoio precisa dizer *"toque para X"* e o título diz *"Y"*, existem duas ações disputando o mesmo toque.
- **Todo alvo tocável se chama `Button · …` ou `Alvo · …`** no Figma. Não é preciosismo de nomenclatura: é o que permite auditar os 44pt mínimos de uma vez em todas as telas. Os botões-pílula de ação secundária (*Ver*, *Trocar*, *Anexar*, *Ver exemplo*, *Como obter*, *Ver original*) ficaram **32pt por muito tempo** justamente porque estavam nomeados como grupos genéricos e escapavam da varredura, apesar de a anotação da Tela 4 exigir 44pt desde o começo. Hoje o arquivo tem quatro formatos de alvo, todos ≥ 44pt:

| Formato | Altura / raio | Uso |
|---|---|---|
| Botão de largura total | 51pt / 26 | CTA principal e secundário |
| Pílula | 44pt / 22 | ações dentro de card (*Ver*, *Trocar*, *Anexar*…) |
| Linha de card | 58pt / 10 | alvos do card "Reembolso" na home |
| Link sublinhado | 44pt de área, texto 13 Medium | ajuda que abre bottom sheet ou PDF |

**A varredura estava do lado errado.** O padrão acima já tinha sido alargado três vezes: cada vez que uma camada mal nomeada revelava um alvo pequeno, o regex ganhava mais um prefixo. A auditoria de protótipo mostrou que isso nunca ia terminar: `Chip · Filtrar` com 32pt, `Copiar` com 27pt e os cinco `✎` da Revisão com **17pt** escaparam todos pelo mesmo buraco. A regra foi invertida: **audita-se tudo, e a lista de exceções estáticas é que fica explícita**. Assim uma camada nova nasce dentro da auditoria em vez de fora dela, o oposto do que acontecia antes, quando esquecer o prefixo certo era o bastante para o defeito sumir.

Nessa mesma passagem, todo header ganhou alvos reais: `‹` e `?` eram glifos de 24pt dentro de uma barra de 45. Viraram frames de 44 × 44 (`Alvo · Voltar`, `Alvo · Ajuda`), e a barra passou a ter 44pt de altura, sem padding vertical, a altura de navegação do iOS. Onde o ícone à direita era só espaçador de simetria, ele se chama `Espaçador` e **não** é alvo: alvo invisível que não faz nada é pior do que espaço vazio.

### Escala de glifos

Os wireframes usam glifos de texto onde a alta fidelidade terá ícones. Eles seguem uma escala própria, separada da escala tipográfica, para não serem confundidos com texto na auditoria de tipos:

| Tamanho | Uso |
|---|---|
| 18pt | chevron `›`, setas, tab bar (`⌂ ☰ ?`), compartilhar `⧉` |
| 22pt | documento `🗎` em miniatura e em slot |
| 24pt | `‹` e `✕` de header, `✎`, `⚡`, `↻` |
| 32pt | `✓` dentro do disco de sucesso (Tela 6 e O.5) |

**Pílula, link ou linha inteira?** A forma responde "o que acontece quando eu tocar":

| Forma | O que acontece | Onde |
|---|---|---|
| Botão de largura total | avança ou conclui a etapa | CTAs de rodapé |
| Pílula | executa uma ação e volta | `Anexar`, `Ver`, `Trocar`, `Copiar` |
| **Texto sublinhado** | abre conteúdo sobre a tela, sem sair dela | `Ver exemplo`, `Como obter o recibo do IRPF`, `Ler termo completo (PDF)` |
| Texto com `→` ou `›` | leva para outra tela | `Ver detalhes →` (Tela 9), `Resolver agora →`, linhas do card "Reembolso" |

Nos wireframes essa distinção vive no nome da camada: `Button · …` para pílulas e CTAs, `Link · …` para sublinhados, `Alvo · …` para linhas de card.

## Quadrado vazio × quadrado preenchido

Duas coisas diferentes usam a mesma forma no wireframe, e a diferença **não é decorativa**:

| Forma | Significa | Onde |
|---|---|---|
| Quadrado **vazio**, contorno 1,5pt `#8c8c8c`, raio 4 | **Checkbox desmarcado** | Slots da Tela 4, aceite do termo (O.3), titularidade (Sheet C), categorias da Tela 1 |
| Quadrado **preenchido `#1a1a1a` com ✓ branco**, raio 4 | **Checkbox marcado**, mesma forma, só muda o preenchimento | Slots preenchidos da Tela 4, titularidade do Sheet C |
| Quadrado **preenchido** `#d1d1d1`, sem contorno, raio 6 | **Ícone**: reserva o espaço de um ícone que entra na alta fidelidade | Cards da Tela 2, atalhos e sino da home, galeria da câmera |

Confundir os dois foi um erro real durante a construção: os atalhos da home estavam desenhados como checkbox, sugerindo que o usuário marcaria "Telemedicina" em vez de navegar até lá. Outro: o slot preenchido da Tela 4 usava um **círculo** preenchido para o estado marcado, enquanto os pendentes eram quadrados: o controle mudava de forma ao ser marcado, o que sugere dois controles diferentes em vez de dois estados do mesmo.

**Todo placeholder declara o que vai substituí-lo.** Os de ilustração já faziam isso no próprio desenho: *"(Ilustração: pessoa com celular + recibo)"*. Os 14 de ícone eram quadrados anônimos, o que num wireframe de baixa fidelidade não informa nada e, em cards lado a lado, chega a atrapalhar: três quadrados idênticos sugerem que as três opções são a mesma coisa.

### Como esses placeholders viram ícone na alta fidelidade

> ⚠️ **O quadrado cinza é medida, não forma.** Ele reserva a área que o ícone vai ocupar. Na alta fidelidade ele **desaparece** e dá lugar ao ícone outline direto, **sem fundo, sem caixa, sem círculo**. Reproduzir o quadrado preenchido repete o antipadrão que o app tem hoje: o clipe de anexo dentro de um círculo navy preenchido, o único lugar da interface que usa "círculo colorido + ícone branco" e que por isso destoa do resto.

Especificação por slot. O tamanho já está correto no wireframe, então a troca é 1:1, sem reflow:

| Tela | Camada no Figma | Ícone da `Icons / 24` | Tamanho | Token |
|---|---|---|---|---|
| Tela 2 · card | `Ícone · câmera` | `camera` | 32pt | `size/icon-xl` |
| Tela 2 · card | `Ícone · clipe de anexo` | `paperclip` | 32pt | `size/icon-xl` |
| Tela 2 · card | `Ícone · teclado` | `keyboard` * | 32pt | `size/icon-xl` |
| Home · header | `Ícone · sino de avisos` | `bell` | 24pt | `size/icon-lg` |
| Home · atalhos | `Ícone · mapa` | `map-pin` * | 24pt | `size/icon-lg` |
| Home · atalhos | `Ícone · vídeo` | `video` * | 24pt | `size/icon-lg` |
| Home · atalhos | `Ícone · documento com check` | `doc-check` * | 24pt | `size/icon-lg` |
| Home · atalhos | `Ícone · escudo` | `shield` * | 24pt | `size/icon-lg` |
| Câmera | `Ícone · galeria` | `gallery` | 24pt | `size/icon-lg` |

\* Cinco ícones (`keyboard`, `map-pin`, `video`, `doc-check`, `shield`) não aparecem em nenhuma das 32 capturas do app atual, então não há referência de forma para eles. Precisam ser desenhados junto com a biblioteca nova, na mesma família outline 1,5pt.

**Todos em navy de marca `#001E64`, outline 1,5pt**, alinhados ao centro vertical da linha ou do card. O `44pt` que aparece em alguns lugares é `size/tap-target`: área de toque, nunca tamanho de ícone; a área de toque de todos esses é o card ou a linha inteira, não o ícone.

**A tab bar da home é outro caso**: usa glifos de texto (`⌂ ☰ ?`) por limitação da fonte no wireframe, não placeholders. Na alta fidelidade viram `home`, `grid` e `help` da mesma biblioteca, a 24pt.

> **Em aberto:** as categorias da Tela 1 usam quadrado vazio (checkbox) **e** chevron `›` na mesma linha, ou seja, marcar e navegar ao mesmo tempo. Como a seleção de categoria avança o fluxo em vez de acumular escolhas, vale decidir se a linha deve perder o checkbox e virar só ícone + chevron.
- **Validação prévia**: nenhuma tela deve permitir avançar com dado inválido, sempre bloquear e explicar inline.
- **Persistência**: rascunho salvo automaticamente a cada 30s; indicador discreto no canto.
- **Onboarding único**: as telas O.1–O.5 só aparecem uma vez. No retorno do usuário (rastreado por flag no perfil), o fluxo entra direto pela Tela 1.
- **Stepper de onboarding** (azul) vs **stepper de solicitação** (laranja), cores diferentes para o usuário entender que são contextos distintos.
- **Sem pop-ups de cross-sell** em nenhuma tela do fluxo transacional.
- **Modais**: nunca sobrepor um modal a um conteúdo crítico. Usar bottom sheets para informação contextual; usar tela cheia para passos sequenciais.
