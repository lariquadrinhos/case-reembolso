# Componentes

Especificação dos componentes do fluxo de Reembolso. As marcas **[declarado]**,
**[medido]** e **[decidido]** seguem a convenção do `README.md`.

Cada componente traz os estados que as 32 capturas registram e os que elas não
registram. **Estado não fotografado é lacuna declarada**, nunca suposição escrita
como se fosse observação.

Os tokens vêm de `fundamentos.md`. O que existe hoje no app está em
`inventario-componentes.md`.

---

# 1. Botão

## 1.1 Primário

**[medido]** 12 telas: 6, 9, 11, 12, 14, 15, 18, 21, 23, 24, 25, 26, 31, 33.

| Propriedade | Valor | Origem |
|---|---|---|
| Altura | `48pt` | **[medido]** 48,3pt ± 0,8 |
| Raio | metade da altura, pílula | **[medido]** razão 1,002 ± 0,012 |
| Largura | preenche a coluna, margem de `20pt` | **[medido]** |
| Preenchimento | `brand/primary` | **[decidido]** ver o conflito do laranja |
| Rótulo | `type/button`, 16pt Semibold, branco | **[medido]** 15,4pt, arredondado |
| Alvo | a própria altura de 48pt cobre o mínimo de 44 | **[decidido]** |

### Estados

| Estado | Preenchimento | Rótulo | Origem |
|---|---|---|---|
| Ativo | `brand/primary` `#F05223` | branco | **[medido]** |
| Desabilitado | `surface/disabled` `#E5E6E6` | `text/disabled` `#949595` | **[decidido]** |
| Pressionado | `brand/primary-pressed` `#EA4210` | branco | **[declarado]** `--color-orange-600` |
| Carregando | `brand/primary` com spinner branco, rótulo oculto | **[decidido]** |

As capturas só registram **ativo** e **desabilitado**. Pressionado e carregando são
projeto, mas o pressionado não precisou ser inventado: a rampa publicada já traz o
degrau seguinte ao `orange-500`, que é o `brand/primary`. Usar `orange-600` mantém o
estado dentro do sistema da empresa em vez de criar uma cor nova.

Para referência, a rampa completa está em `extracao/tokens-site.json`: `orange-500`
`#F05223`, `600` `#EA4210`, `700` `#D23B0E`.

### Regras

**Nunca em caixa alta.** **[medido]** A tela 9 traz `CALCULAR` enquanto as outras
onze usam caixa mista. A caixa alta reduz a velocidade de leitura e aqui não tem
função: é resíduo.

**Navy não é cor de botão primário.** **[medido]** A tela 6 preenche o botão
`Filtrar` com navy sólido, mesma hierarquia do laranja em outras telas. Duas cores
para o mesmo papel ensinam o usuário a não confiar na cor como sinal.
**[decidido]** Onde hoje há botão navy, usar o secundário de contorno.

**Um botão primário por tela.** **[decidido]** Se duas ações competem, a segunda é
secundária.

## 1.2 Secundário (contorno)

**[decidido]** Não existe nas capturas. Entra para resolver os casos em que o app
hoje usa navy sólido ou empilha dois botões laranja.

| Propriedade | Valor |
|---|---|
| Altura, raio, rótulo | iguais ao primário |
| Preenchimento | transparente |
| Contorno | `1,5pt` em `brand/primary` |
| Rótulo | `brand/primary` |

## 1.3 Botão de texto

**[medido]** O app usa dois tratamentos sem regra:

| Tratamento | Onde |
|---|---|
| Caixa alta, laranja, sem sublinhado | `ATUALIZAR DADOS` (12), `FECHAR` e `ME LEVE ATÉ LÁ` (8), `VER` (10) |
| Caixa mista, laranja, sublinhado | `Ver detalhes` (5), `Ver` e `Anexar` (22, 24) |

**[decidido] Fica o segundo: caixa mista, sublinhado, `brand/primary`.** O sublinhado
é o que sinaliza "isto é acionável" sem depender só da cor, o que importa para quem
não distingue laranja de cinza. A caixa alta some.

| Propriedade | Valor |
|---|---|
| Corpo | `type/body` 16pt Medium |
| Cor | `brand/primary`, sublinhado |
| Área de toque | `44pt` de altura mínima, mesmo com texto menor |
| Desabilitado | `text/disabled`, sem sublinhado |

---

# 2. Campo de texto

**[medido]** Telas 9, 15, 20, 21, 32, 33.

Rótulo acima em corpo menor, valor abaixo, linha inferior de 1pt. Sem caixa em
volta.

| Propriedade | Valor | Origem |
|---|---|---|
| Rótulo | `type/label` 12pt Medium, `text/secondary` | **[decidido]** |
| Valor | `type/body` 16pt Regular, `text/primary` | **[decidido]** |
| Linha inferior | `stroke/hairline` 1pt | **[medido]** |
| Altura do alvo | `48pt` | **[decidido]** |

### Estados

| Estado | Linha | Origem |
|---|---|---|
| Vazio | `#D2D2D2`, valor em `text/disabled` | **[medido]** tela 20 |
| Preenchido | `#D2D2D2`, valor em `text/primary` | **[medido]** |
| Erro | `feedback/error`, 2pt, mensagem abaixo | **[medido]** tela 32 |
| Foco | `brand/primary`, 2pt | **[decidido]**, não capturado |
| Desabilitado | linha `#E5E6E6`, valor `text/disabled` | **[decidido]**, não capturado |

### Regras

**Placeholder não é máscara.** **[medido]** A tela 20 usa `XX.XXX.XXX/0001-XX` como
texto de exemplo. **[decidido]** A máscara aplica-se durante a digitação; o
placeholder, quando existir, descreve o que preencher.

**A mensagem de erro diz o que fazer.** **[medido]** A tela 32 mostra a data em
vermelho e um texto explicando a regra de prazo. Isso está certo e vira padrão:
mensagem abaixo do campo, em `feedback/error`, com o limite e a saída.

---

# 3. Card

## 3.1 Linha de lista com chevron

**[medido]** Telas 4, 7, 13. Ícone opcional à esquerda, título, subtítulo opcional,
`›` à direita.

| Propriedade | Valor |
|---|---|
| Altura mínima | `58pt` **[decidido]**, acima do alvo de 44 |
| Título | `type/body` 16pt Semibold, `text/primary` |
| Subtítulo | `type/caption` 14pt Regular, `text/secondary` |
| Chevron | `text/secondary` |
| Separador | `stroke/hairline` entre linhas |

**Regra: ícone sem fundo.** **[medido]** As telas 7 e 13 são a mesma lista de
categorias renderizada de dois jeitos: na 7 os ícones vêm dentro de círculo azul
preenchido, na 13 são outline soltos. **[decidido]** Fica o outline. O círculo
colorido só aparece nesses dois lugares do app e não é padrão do sistema.

## 3.2 Card de conteúdo

**[medido]** Telas 5, 14, 25.

| Propriedade | Valor | Origem |
|---|---|---|
| Raio | `12pt` | **[medido]** 10,6pt, arredondado para a escala |
| Contorno | `1pt` `#E5E6E6` | **[medido]** espessura, **[decidido]** cor |
| Espaçamento entre cards | `12pt` | **[medido]**, amostra pequena |
| Preenchimento interno | `16pt` | **[decidido]** |

**[decidido] Contorno laranja não é decoração.** A tela 14 usa borda laranja em
cards puramente informativos. O contorno de marca fica reservado para seleção (ver
componente 6). Card informativo usa contorno neutro.

---

# 4. Radio

**[medido]** Tela 15. Três opções, seleção única, marcado em laranja. O checkbox,
que compartilha a mecânica mas permite seleção múltipla, está no componente 19.

| Propriedade | Valor |
|---|---|
| Marcado | anel `brand/primary` com disco central `brand/primary` |
| Não marcado | anel `1,5pt` `#D2D2D2` |
| Rótulo | `type/body` 16pt Regular, `text/primary` |
| Linha inteira | tocável, altura mínima `44pt` |

**Lacunas nas capturas:** desabilitado e erro não aparecem em nenhuma. Os dois estão especificados em `estados.md`, 3.1, e construídos na biblioteca.

---

# 5. Barra de navegação

**[medido]** Presente em quase todas as telas.

| Propriedade | Valor | Origem |
|---|---|---|
| Altura | `44pt` | **[medido]** divisor em 184px = 54pt de status + 44 |
| Título | `type/title-nav` 16pt Semibold, centralizado | **[medido]** 15,9pt ± 0,5 |
| Cor do título | `brand/secondary` | **[medido]**, amostra fraca |
| Voltar | chevron à esquerda, alvo de `44 x 44pt` | **[decidido]** |
| Divisor | `stroke/hairline` na base | **[medido]** |

---

# 6. Seletor de tipo de documento

**[medido]** Telas 19, 20, 21, 33. Dois cards lado a lado, ilustração e rótulo.

| Estado | Contorno | Origem |
|---|---|---|
| Não selecionado | `1pt` `#E5E6E6` | **[medido]** |
| Selecionado | `2pt` `brand/primary` | **[medido]** `#FF5000`, migra para `#F05223` |

**[decidido] A seleção não pode depender só da cor do contorno.** Quem não distingue
laranja de cinza claro não vê a diferença. Acrescentar marca de seleção, um `✓` no
canto, além do contorno.

---

# 7. Linha de anexo

**[medido]** Telas 22, 24. Ícone de clipe em círculo navy, título, estado, ações
`Ver` e `Anexar`.

| Propriedade | Valor |
|---|---|
| Ícone | clipe outline `brand/secondary`, **sem círculo** **[decidido]** |
| Título | `type/body` 16pt Semibold |
| Estado | `type/caption` 14pt, `text/secondary` |
| Ações | botão de texto, um alvo de 44pt para cada |

**[decidido] Sem o círculo navy preenchido.** É o único lugar da interface que usa
"círculo colorido com ícone branco dentro", e por isso destoa do resto. O ícone
entra solto, como em todo o sistema.

**[medido]** O `Ver` aparece em cinza quando ainda não há arquivo. Isso está certo:
a ação existe mas não se aplica ainda. Vira padrão para ações condicionais.

---

# 8. Modal

**[medido]** Telas 10, 16, 29, 30.

| Propriedade | Valor | Origem |
|---|---|---|
| Véu | preto a `40%` | **[decidido]**, o app usa 40% e 30% |
| Painel | `surface/body`, raio `16pt` no topo | **[decidido]** |
| Título | `type/title-section` 20pt Bold | **[decidido]** |
| Fechar | `✕` com alvo de `44 x 44pt` | **[medido]** telas 29 e 30 |

**[decidido] Bottom sheet para informação, modal central para decisão.** O app hoje
usa card central para as duas coisas. Sheet preserva o contexto de trás; modal
central interrompe, e interromper deve ser reservado para quando a resposta é
obrigatória para seguir.

---

# 9. Carregamento

**[medido]** Telas 4 e 28. Spinner laranja com texto abaixo.

**[decidido] Skeleton no lugar de spinner onde a estrutura da tela é previsível.**
O spinner não informa nada sobre o que vem; o skeleton já mostra a forma do
conteúdo e reduz a sensação de espera. O spinner fica para operações sem layout
conhecido, como a validação de identidade da tela 28.

**Lacuna:** nenhuma captura mostra falha de carregamento. O estado de erro de rede
é projeto, e entra marcado como **[decidido]** quando for especificado.

---

# 10. Chip de filtro

**[medido]** Tela 6, `Últimos 2 meses`.

| Propriedade | Valor | Origem |
|---|---|---|
| Forma | pílula de contorno | **[medido]** |
| Contorno | `1,5pt` `brand/secondary` `#001E64` | **[medido]** 36.108px de navy na tela |
| Rótulo | `type/caption` 14pt Medium, `brand/secondary` | **[decidido]** |
| Altura | `44pt` | **[decidido]**, o app usa menos e fica abaixo do alvo mínimo |

**[decidido] O chip não usa navy.** Ele herdou a cor do botão `Filtrar` da mesma
tela, que por sua vez é o botão primário fora do padrão. Com o botão migrando para
`brand/primary`, o chip fica em contorno neutro `#E5E6E6` com rótulo
`text/primary`, e o estado ativo é que ganha `brand/primary`.

**Lacuna:** só existe uma captura, com um chip, no estado aplicado. Chip vazio,
múltiplos chips e chip removível não aparecem.

---

# 11. Card de solicitação

**[medido]** Tela 6. Fundo claro, número da SR, lista de atributos, caixa de status,
texto explicativo e `Ver detalhes`.

| Parte | Valor | Origem |
|---|---|---|
| Fundo | `surface/on-body` | **[decidido]**, o app usa um dos cinco cinzas |
| Número da SR | `type/body` 16pt Semibold | **[decidido]** |
| Atributos | lista com marcador, rótulo Regular e valor Semibold | **[medido]** |
| Caixa de status | contorno `1pt`, raio `8pt`, rótulo `Status: ...` | **[medido]** |
| Ação | botão de texto sublinhado | **[medido]** |

### O verde do status, e uma terceira divergência

**[medido]** A caixa de status usa contorno verde `#1F662E`. O ícone de sucesso da
tela 31 usa outro verde, `#00861F`. O sistema publicado declara
`--color-feedback-success` `#04843F`. **São três verdes para o mesmo significado**,
e nenhum dos dois do app bate com o token.

**[decidido]** O status usa `feedback/success` `#04843F` sobre `surface/success`
`#E6F4ED`, ambos declarados. Contorno some: superfície tonal já carrega o
significado e não depende de linha fina para ser percebida.

**[decidido] O status não pode ser só cor.** `Reembolso pago` em verde e
`Em análise` em outra cor ficam idênticos para quem não distingue as duas. A caixa
leva ícone além da cor.

---

# 12. Captura de identidade

**[medido]** Tela 27. Câmera em tela cheia, guia oval sobre o rosto, instrução curta
na base.

| Propriedade | Valor | Origem |
|---|---|---|
| Fundo | imagem da câmera, sem superfície | **[medido]** |
| Guia | oval de contorno claro | **[medido]** |
| Instrução | `type/body` sobre véu escuro | **[medido]** |

**[decidido]** É a única tela do fluxo que inverte a paleta, e deve continuar assim:
a inversão sinaliza que o app assumiu a tela inteira e que a câmera está ativa.

**Lacuna:** as capturas não mostram falha de reconhecimento, permissão negada nem
ausência de câmera. Os três são estados obrigatórios num fluxo de identidade e
precisam ser projetados.

---

# 13. Home

**[medido]** `home.png`. Saudação, card de carteirinha, grade de atalhos, blocos de
programas e banner promocional.

| Parte | Valor | Origem |
|---|---|---|
| Saudação | `type/title-screen` 24pt Bold | **[decidido]** |
| Atalhos | grade de ícone com rótulo abaixo | **[medido]** |
| Ícones | outline, sem fundo | **[decidido]**, ver a regra do componente 3.1 |

**[decidido] Fora do escopo deste sistema.** A home pertence ao app inteiro, não ao
fluxo de Reembolso, e especificá-la a partir de uma única captura produziria regra
sem base. Fica registrada como fronteira: o Reembolso começa no card de entrada da
home e termina na confirmação.

---

# 14. Elevação

**[medido]** Os cards da tela 5 têm sombra, não contorno. Medida no perfil vertical
abaixo da borda: cerca de `5px`, ou seja `2,7pt`, com variação máxima de **3 em 255**
por canal.

É uma sombra praticamente imperceptível. Ela não separa o card do fundo branco, e o
resultado é uma lista que parece plana.

**[decidido]** Duas superfícies, e nenhuma depende de sombra sutil:

| Nível | Tratamento |
|---|---|
| `elevation/flat` | card sobre `surface/on-body`, sem sombra |
| `elevation/raised` | sombra `0 2 8` a 12% de preto, para modal e sheet |

Card em lista usa `flat` com fundo tonal, que separa por contraste de superfície em
vez de por sombra. Sombra fica para o que de fato flutua.

---

# 16. Stepper

**[medido]** Presente em **31 das 44 telas**. É a peça mais usada do sistema depois
da barra de navegação, e o app atual não tem nenhuma.

| Propriedade | Valor |
|---|---|
| Rótulo | `type/label` 12pt Medium, `text/secondary`, no formato `PASSO 4 DE 5 · DOCUMENTOS` |
| Trilho | 4pt de altura, `border/subtle`, raio 2 |
| Preenchido | `brand/primary`, largura proporcional ao passo |
| Variantes | `Passo = 1 a 5` |

**[decidido] O rótulo diz o número e o nome da etapa.** Só a barra informa progresso
sem dizer do quê, e só o número não diz o que vem agora. Os dois juntos respondem
"onde estou" e "quanto falta" numa linha de 12pt.

---

# 17. Banner

**[medido]** Em **22 das 44 telas**.

| Tipo | Superfície | Tinta e glifo |
|---|---|---|
| Info | `surface/on-body` | `text/secondary`, `ⓘ` |
| Alerta | `surface/alert` | `feedback/alert`, `⚠` |
| Erro | `surface/error` | `feedback/error`, `⚠` |
| Sucesso | `surface/success` | `feedback/success`, `✓` |

**[decidido] Sempre glifo mais superfície tonal, nunca cor sozinha.** Um banner que
se distingue só pela matiz é invisível para quem não separa laranja de verde, e o
glifo resolve isso sem depender de leitura.

---

# 18. Rodapé fixo

**[medido]** Em **21 das 44 telas**.

Contêiner ancorado na base, com o banner de estado imediatamente acima do CTA.
Sombra superior de `0 -2 8` a 6%, marcando que o conteúdo é cortado por ele.

**[decidido] Ele fica fora da área que rola, não por cima dela.** A tela se divide em
três blocos que somam a altura da viewport: cromo de topo, área rolável e rodapé.
Implementar o rodapé como camada sobreposta parece equivalente e não é: a última
linha de conteúdo nunca consegue subir acima dele, e some um pedaço de tela do
tamanho exato do rodapé. O relato completo está em `anotacoes-ux.md`, em
*O rodapé fixo rolava junto*.

**[decidido] O banner de pendência viaja junto com o botão que ela trava.** A
contagem e a ação bloqueada são um par: separá-los na rolagem deixa o usuário vendo
um botão cinza sem saber o que falta.

---

# 19. Checkbox

**[medido]** Em **16 das 44 telas**: slots de documento, aceite do termo,
titularidade da conta.

| Estado | Caixa | Rótulo |
|---|---|---|
| Marcado | `brand/primary` preenchido, `✓` em `text/on-brand` | `text/primary` |
| Vazio | contorno `1,5pt` `border/strong` | `text/primary` |
| Desabilitado | contorno `border/subtle` | `text/disabled` |

**[decidido] Quadrado nos dois estados.** Durante a construção dos wireframes o slot
marcado usava círculo e o vazio usava quadrado: o controle mudava de forma ao ser
marcado, o que sugere dois controles diferentes em vez de dois estados do mesmo.

---

# 20. Bottom sheet

**[medido]** Em 9 telas.

Pega de 36 × 5pt, raio `radius/sheet` só no topo, superfície `surface/raised`.

**[decidido] Sheet para informação, modal central para decisão.** O sheet preserva o
contexto de trás; o modal interrompe, e interromper deve ser reservado a quando a
resposta é obrigatória para seguir.

---

# 21. Toast

**[medido]** Uma tela, mas especificado porque é o padrão de confirmação transitória
do sistema inteiro.

Superfície `gray/900`, texto `text/on-brand`, raio `radius/lg`, cerca de 2s.

**[decidido] Nunca sozinho.** Vem em par com uma mudança permanente no controle: o
toast some e o botão continua dizendo que funcionou.

---

# 22. Skeleton

Blocos em `surface/on-body`, raio `radius/sm`, com a forma do conteúdo que vai chegar.

**[decidido]** Esqueleto onde a estrutura é previsível, spinner onde não é. Ver
`estados.md`, 2.3.

---

# 23. Tab bar

**[medido]** Duas telas de home. Três itens, cada um em alvo de 44pt.

**[decidido] O item ativo usa cor de marca mais peso, nunca só cor.**

---

# 24. Timeline

**[medido]** Três telas de acompanhamento.

| Etapa | Forma |
|---|---|
| Concluída | disco sólido `brand/primary` |
| Atual | anel `brand/primary` de 3pt |
| Futura | contorno fino `border/strong` |

**[decidido] Três formas, não três cores.** A diferença entre passado, presente e
futuro não pode depender de matiz.

---

# 25. Linha de revisão

**[medido]** Três telas.

Rótulo em `Label`, valor em `Body`, e o `✎` num alvo próprio de 44 × 44pt.

**[decidido]** Cada seção volta para a etapa certa e retorna. No fluxo atual,
corrigir um dado no resumo obriga a refazer o caminho inteiro.

---

# 15. O que ainda não tem especificação

Os estados que nenhuma captura registra (botão pressionado ou carregando, campo em
foco, lista vazia, erro de rede, modo escuro) estão em `estados.md`.

Três medições ficaram sem amostra confiável e estão marcadas **[decidido]** onde
foram necessárias: a cor do chevron dos cards de menu (traço fino demais, nenhum
valor com mais de 15 pixels), a cor do texto de erro e a do título da barra de
navegação.
