# Playbook · Case UX/UI de redesign de fluxo

**Origem:** case SulAmérica · redesign do fluxo de reembolso (maio–setembro/2026)
**Para:** eu (na próxima vez) e para quem quiser replicar essa abordagem em outro produto.

Este playbook documenta **o processo que usei** para transformar 32 screenshots de um
fluxo real em um case completo: os documentos, o arquivo do Figma com 44 telas, um
design system medido do próprio app e um protótipo clicável. Não é sobre a SulAmérica
em si, é sobre o método, para que eu não precise reinventar a roda no próximo case.

## Quando usar este playbook

Use quando você tem:

- Um fluxo real de um produto (screenshots, protótipo navegável, ou app instalado);
- Pelo menos **uma pessoa que usa esse fluxo de verdade** e topa conversar;
- Prazo de alguns dias para entregar um case completo de portfólio;
- Zero acesso a métricas internas ou ao design system oficial do produto.

**Não use** para cases em que você tem acesso a dados quantitativos e pode fazer
pesquisa primária. Nesses, um playbook de UX Research se sobrepõe a este.

### Sobre o ponto de partida

A primeira versão deste playbook dizia para começar por um briefing. Mudei, porque
não foi o que aconteceu e porque o que aconteceu é melhor: **eu vi uma pessoa real
penando para pedir reembolso**. Ela me deu os prints, respondeu minhas perguntas
sobre o processo e depois olhou os wireframes e as soluções para dizer o que achava.

Briefing que você escreve para si mesma é um exercício de imaginação. Observação de
uma pessoa real é evidência, ainda que de n=1. Se você tem a segunda, não invente a
primeira: o case fica mais forte contando de onde o problema realmente veio.

---

## Visão geral · as 14 fases

```
PARTE 1 · do material ao plano (só texto)
 1. Coleta e organização do material          (30min)
 2. Avaliação heurística                      (2–4h)
 3. Mapeamento do fluxo atual                 (1–2h)
 4. Persona e princípios                      (30min)
 5. Redesign do fluxo                         (2–3h)
 6. Descrição das telas                       (2–4h)
 7. Microcopy                                 (1–2h)

PARTE 2 · do plano ao arquivo (Figma)
 8. Design system por medição                 (4–8h)
 9. As telas no Figma                         (8–16h)
10. Biblioteca publicável                     (3–6h)
11. Mockups sem perder os wireframes          (1–2h)
12. Protótipo clicável                        (3–6h)

PARTE 3 · fechamento
13. Consolidação do case                      (2–3h)
14. Auditoria: documento contra arquivo       (1–2h)
```

**Tempo total realista:** a Parte 1 cabe em 12 a 20 horas. A Parte 2 é maior que
todas as outras somadas, e foi o que a primeira versão deste playbook subestimou ao
escrever *"não fiz no Figma por falta de tempo"*.

**Ordem importa.** Cada fase alimenta a próxima. Pular fases, por exemplo ir direto
para as telas sem avaliação heurística, faz o case parecer opinativo em vez de
fundamentado.

**A Parte 2 não é opcional, e é onde o case ganha ou perde.** Documento descreve
intenção; arquivo tem comportamento. A lição mais repetida deste projeto, em três
defeitos seguidos, foi que **o documento pode estar certo e o arquivo estar fazendo
outra coisa**, e que ninguém descobre isso lendo: descobre clicando. Quem para na
Parte 1 entrega um case que não pode ser conferido.

---

## Entregáveis padrão

| Arquivo ou pasta | O que é | Fase |
|---|---|---|
| `heuristic-evaluation.md` | Avaliação Nielsen com notas, severidade, telas de referência | 2 |
| `fluxo-atual.md` | Mapa numerado do fluxo real com heurísticas violadas por etapa | 3 |
| `novo-fluxo.md` | Redesign etapa a etapa com justificativa por heurística | 5 |
| `microcopy.md` | Textos exatos de cada tela | 7 |
| `design-system/` | 7 documentos, os scripts de medição e o inventário de componentes | 8 |
| `wireframes/` | Um PNG por tela, mais as composições com as notas de design | 9 |
| `mockups/` | As mesmas telas com a biblioteca aplicada, com os mesmos nomes de arquivo | 11 |
| `anotacoes-ux.md` | Por que cada tela é assim, mais o mapa de destinos do protótipo | 9 e 12 |
| `case-completo.md` | Portfólio consolidado em 1ª pessoa | 13 |
| `playbook.md` | este arquivo | 13 |

**Dois arquivos da primeira versão não existem mais**, e o motivo é instrutivo.
O `wireframes-descritivos.md` foi absorvido: descrever tela em texto é um passo
intermediário útil, mas quando as telas existem no Figma o texto vira uma segunda
fonte de verdade que envelhece sozinha. O que sobreviveu dele virou `anotacoes-ux.md`,
que não descreve a tela (ela está lá para ser vista) e sim **por que ela é assim**.

Os `design-tokens.md` e `design-system.md` foram descartados e refeitos como pasta,
porque não concordavam entre si e nenhum dos dois dizia de onde tirou seus números.
Ver a Fase 8.

---

# Fase 1 · Coleta e organização do material

**Objetivo:** colocar tudo que você tem em um lugar previsível antes de começar a pensar.

## Passos

1. Crie a estrutura de pastas do case no seu computador, **e versione com git desde
   o primeiro dia**. Não é preciosismo: o case vai mudar de ideia várias vezes, e
   poder voltar é o que permite descartar um documento inteiro sem medo.
   ```
   case-{cliente} Portfolio/
   ├── case-{cliente}/
   │   └── materiais/
   │       ├── notas-da-observacao.md   ← o que a pessoa disse e fez
   │       └── fluxo-atual/             ← screenshots numerados
   └── entregaveis/                     ← saída de cada fase
   ```
2. **Numere os screenshots em ordem cronológica** (`1.png`, `2.png`, …). Se vieram do usuário sem numeração, renomeie você.
3. Abra todos os screenshots em ordem e faça uma leitura rápida, sem tomar notas ainda. É só para calibrar o que você vai analisar.
4. Se algum arquivo estiver em pasta cloud (OneDrive, iCloud), garanta que **sincronizou tudo antes de começar**. Case travado por arquivo cloud-only é o gargalo mais bobo possível.
5. **Escreva a observação enquanto ela está fresca.** O que a pessoa tentou fazer, onde
   parou, o que ela disse em voz alta, o que ela achou que o app ia fazer e não fez.
   Frases literais valem ouro: elas viram citação no case e argumento na Fase 5.

## Checklist final da Fase 1

- [ ] Notas da observação escritas, com pelo menos duas frases literais da pessoa.
- [ ] Screenshots numerados em ordem.
- [ ] Estrutura `case-*/materiais/` e `entregaveis/` criada, e `git init` feito.
- [ ] Sabe qual é o objetivo do case em 1 frase (ex.: *"reduzir fricção do fluxo de reembolso"*).

---

# Fase 2 · Avaliação heurística

**Objetivo:** transformar o "acho que tá ruim" em diagnóstico defensável.

## Como fazer

1. Abra as 10 heurísticas de Nielsen em uma aba. As 10:
   1. Visibilidade do status do sistema
   2. Correspondência entre o sistema e o mundo real
   3. Controle e liberdade do usuário
   4. Consistência e padrões
   5. Prevenção de erros
   6. Reconhecimento em vez de memorização
   7. Flexibilidade e eficiência de uso
   8. Estética e design minimalista
   9. Ajude usuários a reconhecer, diagnosticar e recuperar erros
   10. Ajuda e documentação
2. Para **cada heurística**, passe pelos screenshots identificando violações. Anote:
   - Referência à tela (ex.: `T.32`)
   - Frase objetiva do que está errado
3. Depois de listar problemas, atribua:
   - **Nota de 1 a 10** (calibre: 10 = excelente, 5 = mediano, 3 = crítico)
   - **Severidade dominante**: baixa · média · alta · crítica
4. Para cada heurística, escreva **uma sugestão de melhoria** concreta e implementável (não vaga).
5. No fim, gere:
   - **Tabela resumo** com todas as notas
   - **Diagnóstico geral** em 1 parágrafo: que trio de heurísticas é o mais frágil? Qual a raiz do problema?

## Template para cada heurística

```markdown
## N. Nome da heurística
**Nota:** X / 10

### Problemas encontrados
- **T.XX**: descrição objetiva.
- **T.YY**: descrição objetiva.

### Severidade: **{baixa|média|alta|crítica}**

### Sugestão de melhoria
Frase curta com verbo no imperativo + como implementar.
```

## Armadilhas comuns

- ❌ Escrever "linguagem confusa" sem citar a frase confusa e a tela onde aparece.
- ❌ Notar todos com 5–6 (medo de dar nota extrema). Se está ruim, é 3. Se está ótimo, é 8+.
- ❌ Sugerir "melhorar UX". Troque por *"validar CPF em tempo real com máscara XXX.XXX.XXX-XX e mensagem específica"*.

## Checklist Fase 2

- [ ] 10 heurísticas cobertas.
- [ ] Cada problema tem tela de referência.
- [ ] Notas variam (não são todas 5).
- [ ] Sugestões são específicas, não genéricas.
- [ ] Tabela resumo + diagnóstico geral prontos.

---

# Fase 3 · Mapeamento do fluxo atual

**Objetivo:** contar a história do que o usuário faz hoje, tela por tela, referenciando as heurísticas violadas.

## Como fazer

1. Abra os screenshots em ordem novamente.
2. Agrupe telas por **etapa lógica** (não 1 etapa = 1 tela; às vezes 3 telas compõem 1 etapa: input + modal + confirmação).
3. Numere as etapas (1, 2, 3…).
4. Para cada etapa, escreva:
   - **Nome curto** (ex.: "Termo de Ciência e Responsabilidade")
   - **Telas envolvidas** (`T.10`, `T.11`)
   - **O que o usuário faz** (verbo no presente: "Lê", "Escolhe", "Digita")
   - **Problemas heurísticos** com número e severidade da avaliação da Fase 2

## Template

```markdown
## N. Nome da etapa
**Telas:** `T.XX`, `T.YY`

**O que o usuário faz:** frase em 1–2 linhas.

**Problemas heurísticos:**
- Descrição · **HN (severidade)**.
- Descrição · **HN (severidade)**.
```

## No fim do documento

- **Tabela resumo** com número de etapas, tempo estimado, heurísticas mais violadas.
- **Pontos de abandono prováveis**: 3 a 5 etapas onde o usuário provavelmente desiste.

## Armadilhas

- ❌ Descrever telas em vez de **etapas**. A tela é um artefato; a etapa é uma unidade de comportamento.
- ❌ Repetir a avaliação heurística. Aqui você **referencia**, não reescreve.
- ❌ Esquecer as saídas do app (ex.: usuário precisa ir ao gov.br). Isso é uma etapa também.

---

# Fase 4 · Persona e princípios

**Objetivo:** criar um filtro para as decisões da fase 5.

## Passos

1. Escolha **uma persona primária**: quem sofre mais com o problema, quem é o usuário
   recorrente. Foque nele. **Se você observou alguém na Fase 1, a persona é essa
   pessoa**, não uma composição inventada. Diga isso no case: persona apoiada em
   alguém real é mais forte que persona montada a partir de suposição, e é honesta
   sobre o tamanho da amostra.
2. Escreva 3–5 **princípios de redesign** que respondam aos problemas críticos da avaliação. Cada princípio deve conectar a uma heurística.

## Exemplo (deste case)

- **Persona:** pessoa em psicoterapia semanal (uso recorrente do fluxo).
- **Princípios:**
  1. OCR + reuso substituem digitação manual (corrige H6, H7).
  2. Stepper persistente em todas as telas (corrige H1).
  3. Validação inline com mensagens prescritivas (corrige H5 e H9).
  4. Microcopy em linguagem cidadã com ícones de ajuda (corrige H2 e H10).
  5. Modo recorrente / atalhos para usuário frequente (corrige H7).

## Armadilhas

- ❌ Persona vaga tipo "usuário do app". Persona precisa de **contexto de uso** (frequência, cenário, dor específica).
- ❌ Princípio de redesign genérico ("melhorar UX"). Cada princípio deve prescrever uma **ação de design**.
- ❌ Inventar dados demográficos que você não tem. Idade, renda e profissão só entram
  se você souber. Persona com ficha completa e nenhuma fonte é ficção com aparência
  de pesquisa.

---

# Fase 5 · Redesign do fluxo

**Objetivo:** propor um novo fluxo, etapa por etapa, com justificativa por heurística corrigida, respeitando as restrições de compliance.

## Passos

1. **Liste as restrições que não pode romper** (compliance, segurança, upload obrigatório, mobile-first). Coloque em destaque no início do documento.
2. Considere se algumas etapas atuais podem virar **onboarding único** (executadas uma vez, no primeiro uso). Isso retira peso do fluxo recorrente sem violar compliance.
3. Redesenhe cada etapa do novo fluxo. Para cada uma:
   - Nome + o que substitui do fluxo atual
   - O que o usuário faz agora
   - Heurísticas corrigidas
4. Faça uma **tabela comparativa** atual × novo no fim (etapas, telas, digitação manual, stepper, validação, atalhos, modais, saída do app).

## Regras que salvam a proposta

- Uma restrição = você **repensa a forma**, não elimina a etapa. Termo legal continua existindo, e o que muda é o formato (juridiquês → bullets curtos).
- Compliance de identidade obrigatório? Move para o onboarding e reaproveita biometria do dispositivo.
- Upload obrigatório? Consolida em 1 tela com multi-seleção, mantém o requisito.

## Armadilha central

O sistema tenta te fazer "remover etapas". Não é isso. É **reordenar** e **reformular**. A quantidade de compliance é dada; a experiência não.

---

# Fase 6 · Descrição das telas

**Objetivo:** ter, em texto, a lista completa de telas e o conteúdo de cada uma,
antes de abrir o Figma.

> **Isto é um andaime, não um entregável.** Na primeira versão deste playbook a fase
> se chamava *wireframes descritivos* e produzia um arquivo que ia junto no portfólio.
> Hoje ela produz um rascunho de trabalho que **é apagado** quando as telas existem
> no Figma. Manter os dois é manter duas fontes de verdade sobre a mesma tela, e a de
> texto sempre envelhece primeiro. O que sobrevive vira `anotacoes-ux.md`, que não
> descreve a tela e sim explica a decisão dela.

## Estrutura por tela

```markdown
## Tela X · Nome
**Status:** quando aparece.
**Stepper:** `Passo X de Y · Nome` (Z%).

### Layout (ASCII)
[bloco de código com wireframe em texto]

### Componentes e anotações UX
- Descrição de cada bloco.
- Referências às heurísticas corrigidas.
```

## Cobertura mínima

- Onboarding (uma vez): boas-vindas, dados sensíveis, termos, identidade, sucesso.
- Fluxo principal: entrada, cada etapa de input, revisão, confirmação.
- Pós-envio: acompanhar status, histórico.
- Bottom sheets auxiliares (tutorial, ajuda contextual, edição).
- Estados especiais: loading (skeleton), empty, erro de rede.

## Wireframe ASCII · convenções úteis

```
▢ card             ⬤ botão primário       ◯ botão secundário
▭ campo            ✓ checkbox              ✎ editar inline
🗎 preview          ⓘ ajuda contextual      › chevron
```

## Armadilhas

- ❌ Wireframe bonito no ASCII mas sem microcopy embutida, e aí o designer inventa texto.
- ❌ Tela sem os estados (default, erro, loading), e aí sai só o caminho feliz.
- ❌ Fazer wireframe de alta fidelidade em texto. Alta fidelidade é no Figma. Texto é para estrutura.
- ❌ Tratar esta fase como entregável. Ela é o índice do que construir, e sai do
  repositório quando as telas existirem.

## O teste que fecha esta fase

Antes de abrir o Figma, passe pela lista de telas perguntando, para cada elemento
tocável: **para onde isso leva?** Se a resposta for "uma tela que não está na lista",
a lista está incompleta. Foi assim que apareceram, neste case, seis destinos que a
interface prometia e que não existiam em lugar nenhum, além de dois bottom sheets
desenhados sem nenhuma origem que os abrisse.

É o mesmo exercício da Fase 12, feito barato. Fazer agora custa uma tarde; fazer
depois custa refazer telas.

---

# Fase 7 · Microcopy

**Objetivo:** deixar cada texto pronto. Nenhum campo `[TEXTO AQUI]` no Figma.

## Estrutura por tela

- **Título da tela**
- **Instrução principal** (frase de apoio abaixo do título)
- **Labels** (tabela: elemento × texto)
- **Mensagens de erro** (tabela: situação × texto, sempre específico e nunca genérico)
- **Mensagem de confirmação final** (quando aplicável)

## Princípios de voz (que uso desde este case)

1. **Clareza acima de simpatia.** Linguagem cidadã, frases curtas, verbo no imperativo direto.
2. **Sem juridiquês.** "SR", "prestador", "prévia" sem explicação são proibidos.
3. **Erros dizem: o quê + por quê + o que fazer.** Nunca "campo inválido".
4. **Sem hedge.** *"Em até 5 dias úteis"* > *"se estiver tudo certo, em até 30 dias"*.
5. **Sem caixa alta em CTA.** Sem emoticons em produto financeiro.

## Template de mensagem de erro

> **{o que aconteceu}.** {por que a regra existe, em linguagem simples}. **{o que fazer agora, com sugestão específica}.** *[Botão de recuperação]*

## Glossário de termos técnicos

Sempre monte uma tabela de tooltips no fim do arquivo:

```markdown
| Termo | Tooltip |
|---|---|
| CRP | Registro do profissional. A gente lê pelo recibo automaticamente, você não precisa decorar. |
```

---

# Fase 8 · Design system por medição

**Objetivo:** reconstruir o sistema visual do produto a partir das capturas, com cada
número rastreável até de onde veio.

> **Esta fase foi refeita do zero.** A primeira versão mandava "extrair hex aproximados
> e anotar uma nota de limitação". Funciona para descrever, não aguenta uma pergunta.
> Quando alguém perguntar *"por que o laranja é esse?"*, "olhei e parecia" não é
> resposta. O método abaixo responde.

## A regra que organiza tudo: três marcas

Toda afirmação do sistema carrega uma delas, e elas nunca se misturam:

| Marca | Significa | Como se obtém |
|---|---|---|
| **[declarado]** | a marca publica esse valor | CSS do site, guia de marca, documentação pública |
| **[medido]** | o app renderiza esse valor | contagem de pixels nas capturas |
| **[decidido]** | é escolha deste projeto | você, e o documento diz por quê |

A marca vale mais que o número. Um sistema em que todo valor diz de onde veio pode
ser contestado item a item; um sistema sem marcas só pode ser aceito ou rejeitado
inteiro.

**E o mais interessante do case mora justamente onde as marcas discordam.** Neste
projeto o app renderiza um laranja diferente do que a empresa publica, usa três verdes
onde o sistema declara um, e tem três tamanhos de título onde a documentação prevê um.
Isso não é erro de medição, é achado: o produto divergiu do próprio sistema. Um case
que mostra essa distância prova leitura de sistema, não só bom gosto.

## Passo 1 · Ancorar a escala

Sem isso nenhuma medida em pontos existe, só pixels soltos.

1. Descubra qual aparelho gerou as capturas pela largura em pixels.
2. Meça um elemento de altura **fixa e conhecida pela plataforma** na captura, como a
   barra de status ou a barra de guias do iOS.
3. A razão entre o medido e o valor de plataforma é a sua escala, em px por pt.
   Guarde esse número: ele multiplica tudo daqui em diante.

## Passo 2 · Medir, não estimar

Um script que conta pixels responde em segundos o que o olho erra por 10%. O que vale
medir, em ordem de retorno:

1. **Cores por frequência.** Quantos pixels de cada cor, em quais telas. As dez mais
   frequentes são o sistema; o resto é antialiasing.
2. **Superfícies contra borda.** Separar o que é preenchimento do que é contorno evita
   inventar um cinza que só existe na transição entre dois outros.
3. **Corpo de texto pela altura de caixa alta.** Meça a altura da caixa alta em pixels,
   divida pela razão `cap/em` da fonte e pela escala. Dá o corpo em pontos.
4. **Raio de canto pelo perfil da curva.** Não chute pela aparência: amostre várias
   distâncias do canto e resolva a geometria. A primeira tentativa neste case errou
   por 6pt porque amostrou uma linha só.
5. **Contraste de cada par texto sobre fundo**, para achar o que reprova em AA.

## Passo 3 · Identificar a fonte sem adivinhar

Renderize a mesma palavra da captura em cada família candidata, no mesmo corpo, e
compare a **sobreposição de forma** entre a imagem renderizada e o recorte real. A
candidata com maior sobreposição vence, e você tem um número para mostrar em vez de
uma opinião.

## Passo 4 · Escrever os documentos

A pasta que funcionou tem sete arquivos, e a divisão importa:

| Arquivo | Responde |
|---|---|
| `README.md` | por onde começar, e o que significam as três marcas |
| `fundamentos.md` | cor, tipografia, forma, espaço |
| `componentes.md` | cada componente, com anatomia, estados e em quantas telas aparece |
| `estados.md` | vazio, carregando, erro, desabilitado, foco |
| `guia-figma.md` | como construir a biblioteca, na ordem |
| `inventario-componentes.md` | o que existe no app hoje, tela por tela |
| `processo.md` | como o sistema foi construído, **incluindo o que não deu certo** |

O `processo.md` é o que separa um sistema de uma lista de valores. Registre os
caminhos que falharam e por quê: o estimador de raio que errou, a fonte que parecia
certa e não era, a busca de cor que emparelhou um cinza com um verde. Erro documentado
é método; erro escondido é sorte.

## Passo 5 · Contar a cobertura

Para cada componente, conte **em quantas telas ele aparece**. Isso ordena a construção
da biblioteca (Fase 10) e revela buracos: neste case a contagem mostrou um componente
de progresso ausente de 31 das 44 telas, o que era defeito de consistência, não de
documentação.

## Armadilhas

- ❌ Confundir o que existe com o que deveria ser, **sem dizer qual é qual**. A divisão
  em dois arquivos da primeira versão tentava resolver isso e falhou: os dois
  discordavam entre si e nenhum dizia de onde tirou seus números. As três marcas
  resolvem no nível da frase, que é onde o problema vive.
- ❌ Copiar Material Design ou HIG sem adaptar. Use padrão externo para **estados** e
  **acessibilidade**, nunca para cor ou tipografia do produto.
- ❌ Deixar cor literal em componente. Sempre a variável.
- ❌ Publicar um número que você não consegue reproduzir. Se não dá para refazer a
  medida, ela não entra.

## Checklist Fase 8

- [ ] Escala ancorada em um elemento de plataforma, e o número está escrito.
- [ ] Toda afirmação tem uma das três marcas.
- [ ] Os scripts de medição estão no repositório e rodam.
- [ ] As divergências entre declarado e medido estão listadas, não escondidas.
- [ ] Contraste conferido, com os reprovados nomeados.
- [ ] `processo.md` inclui os caminhos que não deram certo.

---

# Fase 9 · As telas no Figma

**Objetivo:** sair do texto e ter as telas, com a estrutura que aguenta virar
protótipo depois.

## O frame é a viewport, e isso é uma decisão

Todas as telas com a mesma altura, a do aparelho. Tela cujo conteúdo passa disso
**não cresce, ela corta**, como o aparelho corta. Frame alto demais mente: mostra de
uma vez o que o usuário só vê rolando, e some com o problema de hierarquia que existe
na vida real.

## A construção que evita retrabalho

Toda tela que rola se divide em **três blocos que somam exatamente a altura da
viewport**:

```
┌─────────────────┐
│ cromo de topo   │  status bar + cabeçalho, fixos
├─────────────────┤
│ conteúdo        │  altura fixa = janela, overflow vertical
│ rolável         │  ← é ESTE que rola
├─────────────────┤
│ rodapé          │  fixo, irmão do conteúdo, não por cima dele
└─────────────────┘
```

**Não faça o rodapé como camada sobreposta.** Parece equivalente e não é: a última
linha de conteúdo nunca consegue subir acima dele, e some um pedaço de tela do tamanho
exato do rodapé. Descobri isso com o protótipo rodando, depois de já ter "corrigido"
o problema uma vez pela metade.

## Um alvo por ação, com no mínimo 44pt

Card que é rótulo não deve ser tocável; o botão dentro dele é que é. Onde houver duas
ações, dois alvos. E **audite tudo em vez de confiar no nome da camada**: neste case a
varredura de alvos pequenos foi alargada três vezes, sempre adicionando mais um
prefixo de nome, até ficar claro que o método estava invertido. Audita-se todos os
nós, e a lista de exceções é que fica explícita.

## Cada estado é um frame

Vazio, preenchido, erro, carregando, primeiro acesso. Especialmente **primeiro
acesso**: é fácil desenhar o fluxo inteiro para quem já tem histórico, e é o que eu
fiz na primeira passada. Quem nunca usou o produto é justamente quem tem mais
dificuldade, e a tela dele é diferente em detalhes que passam batido na implementação
se não estiverem desenhados.

## Notas de design no quadro

Ao lado de cada tela, um post-it com **a decisão**, não a descrição. Uma cor só no
quadro inteiro, reservada para anotação, para que nada seja confundido com interface.
Telas que são variação de estado não precisam de nota própria: a nota marca onde houve
escolha, não onde há tela.

## Armadilhas

- ❌ Frame que cresce com o conteúdo. Ele esconde o problema de hierarquia.
- ❌ Marcação de rolagem sem rolagem de verdade. Anotação que mente sobre
  comportamento passa em qualquer revisão visual, e foi o que aconteceu aqui em sete
  telas.
- ❌ Nome de camada herdado de um clone. O texto fica certo e o nome mente, e é o nome
  que as varreduras leem.
- ❌ Deixar 2pt de folga e considerar que coube. Não é folga: qualquer acréscimo de
  conteúdo derruba.

---

# Fase 10 · Biblioteca publicável

**Objetivo:** sair da descrição do sistema para componentes que alguém consegue usar.

## Ordem de construção

Variáveis → estilos → ícones → átomos → compostos → padrões. Nunca o contrário: um
componente construído antes das variáveis nasce com cor literal dentro, e trocar
depois é refazer.

1. **Variáveis** de cor e numéricas, agrupadas com `/`, com modo claro definido.
2. **Estilos** de texto e de efeito, separados das variáveis.
3. **Ícones** como conjunto, para poderem ser trocados por instância.
4. **Componentes**, na ordem de cobertura que a Fase 8 mediu: o que aparece em mais
   telas primeiro.

## A armadilha que custou duas horas

Ao vincular uma variável a um preenchimento, a API devolve **um preenchimento novo** e
guarda como reserva o valor literal que você passou. Se você passou preto como
literal, o componente renderiza preto em qualquer contexto que não resolva a variável.
Passe sempre o valor real do modo padrão como literal, não um placeholder.

## Checklist antes de publicar

- [ ] Nenhum preenchimento literal sobrou: tudo vinculado a variável.
- [ ] Todo componente tem os estados que o `estados.md` prevê, incluindo foco.
- [ ] Os nomes seguem uma convenção só, e ela está escrita.
- [ ] A contagem de componentes no documento bate com a do arquivo. Confira: é fácil
      contar duas vezes um conjunto de ícones, ou somar variáveis de cor com numéricas.

---

# Fase 11 · Mockups sem perder os wireframes

**Objetivo:** aplicar a biblioteca sem destruir a versão de baixa fidelidade.

Duplique a página antes de aplicar. Os wireframes provam estrutura e os mockups provam
sistema, e um case que só tem o segundo perde a chance de mostrar que a estrutura veio
antes da cor.

**Mantenha os mesmos nomes de arquivo nas duas pastas de exportação.** Se
`01-home.png` existe nas duas, dá para abrir a mesma tela lado a lado e ver o que a
cor mudou e o que ela não mudou. É a comparação que o recrutador faz sozinho, sem
você explicar.

**Exporte, mas trate a exportação como retrato datado.** Toda vez que o arquivo mudar,
os PNGs ficam velhos. Tenha um script de reexportação no repositório e rode antes de
fechar. E **confira cada download pelo tamanho em bytes**: metade de uma leva falhou
em silêncio neste projeto, e eu quase commitei arquivo velho achando que estava novo.

---

# Fase 12 · Protótipo clicável

**Objetivo:** sair do arquivo estático e ter comportamento. É a fase que mais achou
defeito por hora gasta.

> **Esta fase não existia na primeira versão do playbook, e ela é a que mais mudou o
> resultado.** Tudo que vem abaixo é defeito que passou por várias revisões visuais e
> só apareceu quando um dedo tocou a tela.

## A regra de ouro: protótipo não digita

O toque num campo precisa levar a uma **versão já preenchida** da tela. Então todo
formulário do caminho precisa existir nos dois estados, vazio e preenchido. Neste case
isso criou seis telas que não estavam previstas em lugar nenhum.

## Todo controle que destrava um botão precisa dos dois estados

Não basta o botão **parecer** travado: ele tem que estar **sem ligação**, e quem
destrava é que leva ao estado seguinte. O termo de ciência escapou na primeira
montagem, com o botão cinza e clicável, e o protótipo mentia sobre a regra que a
própria tela enunciava.

## Carregamento avança sozinho

Use tempo, não toque. Carregamento que exige clique não existe na vida real. E
**não pule direto para o sucesso**: se há validação, ela precisa de uma tela, ainda
que por 1,8 segundo. Sem ela o toque não parece validar nada, parece trocar de página.

## Nenhum beco sem saída

Varra o protótipo a partir do ponto de partida e liste **toda tela alcançável sem
nenhuma ligação de saída**. Cada uma é uma armadilha. Varra também o contrário: toda
tela que existe e nunca é alcançada.

> Tela órfã às vezes não é buraco de protótipo, é **buraco de design**. Neste case a
> lista de histórico não tinha porta de entrada em nenhuma tela do app, e isso só
> apareceu quando tentei ligá-la. Quando acontecer, resista a inventar uma ligação
> para fechar a conta: decida onde a entrada mora, e registre a decisão.

## Sheet é desenhada sobre a tela que a abre

Cada bottom sheet é um aparelho inteiro contendo a tela de origem, o escurecimento e o
painel. Isso é honesto e tem um custo que você precisa aceitar de olhos abertos:
**sheet reaproveitada em N telas precisa de N frames**. Uma sheet de ajuda desenhada
sobre a tela de documentos não pode abrir a partir da tela de pagamento, porque
mostraria a tela errada atrás do escurecimento.

## O que só o protótipo cobra

| Defeito | Por que a revisão visual não pega |
|---|---|
| Rodapé que rola junto com o conteúdo | parado, o arquivo está idêntico ao certo |
| Onboarding que recomeça depois de concluído | as duas telas são iguais menos uma frase e um destino |
| Botão desabilitado que responde ao toque | a aparência de travado está correta |
| Sheet cujo botão caiu fora da tela | só acontece quando o conteúdo cresce |
| Tela que promete "toque para corrigir" e não faz nada | o texto está lá, bonito |

## Checklist Fase 12

- [ ] Um ponto de partida, nomeado. Cuidado: **clone de tela herda o ponto de partida**.
- [ ] Zero becos sem saída, conferido por varredura e não por memória.
- [ ] Toda tela órfã é órfã de propósito, e a razão está escrita.
- [ ] Todo botão travado tem zero ligações; todo botão ativo tem uma.
- [ ] Todo `‹` volta para onde a pessoa veio, não para um destino fixo.
- [ ] Os becos fora de escopo ficam inertes, o que é mais honesto que fingir
      profundidade que o case não tem.

---

# Fase 13 · Consolidação do case

**Objetivo:** empacotar tudo em um formato compartilhável para portfólio.

## Estrutura do case

1. **Capa** com título, subtítulo e assinatura.
2. **Resumo executivo** (callout de 5–7 linhas).
3. **Sumário**.
4. **1. Contexto**: 1ª pessoa, curto. Por que este case importa? Qual persona?
5. **2. Problemas identificados**: painel heurístico + os 3–5 pontos que mais te chamaram a atenção, com voz pessoal.
6. **3. Processo**: como você trabalhou. Sobre limitações, ver abaixo: a versão
   anterior deste playbook dava um conselho que eu mudei.
7. **4. Solução**: novo fluxo etapa a etapa.
8. **5. Telas-chave**: as telas principais, com link do Figma.
9. **6. Microcopy**: 2 ou 3 exemplos de "antes × depois" que carreguem a proposta.
10. **7. Resultados esperados**: hipóteses, nunca afirmações, com próximos passos.
11. **Anexo · Mapeamento heurística → solução**, a tabela de rastreabilidade.

## Voz do case

- **1ª pessoa.** "Redesenhei", "escolhi", "aprendi".
- **Confiança sem arrogância.** Reconheça limites, sem se diminuir.
- **Reflexão no fim.** O parágrafo final do case pesa muito para o recrutador.

## Diga o que você fez, não o que deixou de fazer

A primeira versão deste playbook mandava escrever uma seção *"o que não fiz"*, com
*"não testei com usuários"* na lista. Mudei, e a diferença é grande.

Eu **não fiz pesquisa formal**, é verdade. Mas observei uma pessoa real passar pelo
fluxo mais de uma vez, conversei com ela sobre o processo, perguntei quais eram os
problemas, recebi dela as capturas que fundamentam o case inteiro, e depois mostrei os
wireframes e as soluções para ouvir a opinião dela. Chamar isso de "não fiz pesquisa"
é apagar o trabalho que sustenta a proposta.

A regra que uso hoje:

> **Descreva o que foi feito, com o tamanho da amostra explícito.** Não esconda o
> limite e não o transforme em desculpa. *"Acompanhei uma pessoa"* é honesto e forte.
> *"Não testei com usuários"* é honesto e fraco, e descreve pior a mesma realidade.

O que continua valendo é separar **direção** de **tamanho**. Onde o documento afirma
que algo melhora, tudo bem. Onde afirma **quanto** melhora sem métrica interna, marque
como hipótese. Essa é a limitação real, e ela é sobre número, não sobre esforço.

## Consolide também o processo

Depois do case, crie **este playbook** (você está lendo). Ele mostra que você tem
método, não só um caso pontual. E ele só vale se for **atualizado logo depois**:
fases que você descobriu, armadilhas em que caiu, conselhos antigos que se mostraram
errados. Este arquivo ganhou cinco fases e oito armadilhas na segunda rodada, e três
conselhos da primeira versão foram revogados.

---

# Fase 14 · Auditoria: documento contra arquivo

**Objetivo:** garantir que o que os documentos afirmam é o que o arquivo faz.

> **Esta fase existe por causa de três defeitos seguidos**, todos do mesmo formato: o
> documento descrevia o comportamento certo e o arquivo fazia outra coisa. O documento
> dizia que o painel era ancorado na base, e ele estava preso pelo topo. A tabela de
> rolagem calculava a rolagem certa, e o arquivo rolava menos. A marcação de rolagem
> estava desenhada em dez telas, e sete não rolavam.
>
> Os três passaram por várias revisões visuais, porque **só aparecem quando alguma
> coisa se mexe**: o conteúdo muda de tamanho, ou o dedo rola. Num arquivo estático,
> nada disso acontece.

## Como fazer

1. **Liste toda afirmação numérica dos documentos**: contagens de tela, alturas,
   quanto cada tela rola, quantas ligações tem o protótipo.
2. **Meça cada uma no arquivo** e compare. Não leia o documento e confie: meça.
3. Onde divergir, decida qual está certo. Às vezes é o arquivo que está errado (e você
   corrige o arquivo), às vezes é o documento (e você corrige o texto). Neste case
   aconteceram os dois.
4. **Confira as convenções declaradas**, não só os números. Se o documento diz que
   todo alvo tem 44pt, varra o arquivo atrás de alvos menores. Se diz que uma marcação
   aparece em toda tela que rola, confira as duas listas.
5. Refaça as exportações que ficaram velhas, e **confira cada arquivo pelo tamanho**.

## Armadilha

- ❌ Confiar no relatório do próprio script de correção. Ele diz o que tentou fazer,
  não o que ficou. Meça depois, com outro script, a partir do arquivo.

## Checklist Fase 14

- [ ] Toda contagem do documento bate com a varredura do arquivo.
- [ ] Toda convenção declarada foi conferida por varredura, não por amostragem.
- [ ] PNGs exportados são posteriores à última mudança do arquivo.
- [ ] Nenhum documento cita arquivo que não existe mais.

---

# Trabalhar com IA sem terceirizar o julgamento

Usei IA em todas as fases, e a diferença entre usar bem e usar mal não está no
prompt: está em **onde você aceita a resposta e onde você exige prova**.

## A regra

> **IA para executar e medir. Eu para decidir e conferir.**

O que ela fez melhor que eu: varrer 44 telas contando alvos menores que 44pt, medir
cor pixel a pixel em 32 capturas, montar 145 ligações de protótipo sem errar destino,
achar toda tela sem saída. Trabalho exaustivo, mecânico, do tipo que a atenção humana
falha por cansaço e não por falta de capacidade.

O que continuou meu: qual problema vale resolver, o que a pessoa que eu observei
realmente precisava, se mover a biometria para o onboarding é defensável, onde mora a
entrada do histórico, e qual conselho do playbook antigo estava errado.

## Peça o número, não a opinião

A pergunta que muda a qualidade da resposta é **"como você sabe?"**. Trocar *"que cor
é essa?"* por *"conte os pixels e me diga a frequência de cada cor"* transforma uma
impressão em dado que eu posso conferir. Foi assim que o design system inteiro saiu:
nenhum valor dele veio de "parece", todos vieram de contagem, e os scripts ficaram no
repositório para qualquer um refazer.

## Desconfie do relatório, confira o resultado

Um script relata o que **tentou** fazer, não o que ficou. Neste projeto um relatório
disse que 22 telas tinham sido corrigidas, e estavam mesmo, só que a correção resolvia
metade do problema. Depois de qualquer mudança em lote, meça de novo, com outra
varredura, lendo o arquivo.

E isso vale para o próprio trabalho da IA: ela errou contagens que eu repeti sem
conferir (somou dois tipos de variável e reportou um número inflado, contou duas vezes
um conjunto de ícones). O erro é barato quando você mede; é caro quando você publica.

## O que isso muda no case

Não escondo que usei, e não é sobre a ferramenta. O que o case mostra é **método de
verificação**: toda afirmação com origem declarada, todo número reproduzível por um
script que está no repositório, e os caminhos que não deram certo registrados junto
com os que deram. Isso é o que eu quero que alguém veja, e é o que continuaria valendo
se a ferramenta mudasse amanhã.

---

# Ferramentas que usei

| Ferramenta | Para quê |
|---|---|
| VS Code / editor markdown | Redação dos `.md` |
| git | Versionar tudo desde o primeiro dia. É o que permite descartar sem medo |
| Figma | As 44 telas, a biblioteca, os mockups e o protótipo |
| ASCII em blocos de código | Estrutura das telas antes do Figma |
| Python + Pillow | Medir cor, corpo, raio e contraste a partir das capturas |
| Nielsen Norman Group (site) | Consulta das heurísticas quando esqueço a redação exata |
| Contraste calculado no script | Validação AA sem depender de plugin |

## O que não usei mas usaria em um case real

- Maze / UsabilityHub, para teste moderado remoto de 5 a 8 pessoas.
- Notion, para timeline visual do processo.
- Loom, para gravar walkthroughs do protótipo.

---

# Formato dos entregáveis

**Padrão que adoto:**

- Textos longos: `.md`, versionável, legível, fácil de editar.
- Telas: link do Figma **mais** PNGs exportados no repositório. O link é a fonte da
  verdade; os PNGs são o retrato datado que sobrevive se o acesso cair.
- Protótipo: link do Figma, com o ponto de partida nomeado.
- Case final: o `.md` no repositório, mais o link do Figma.

**Nunca** entregar o case só como documento solto. Sempre tem uma versão navegável
(link) e uma versão que não depende de você estar online.

---

# Checklists finais

## Antes de mandar o case

- [ ] Todos os entregáveis da tabela estão em `entregaveis/`, e nenhum documento cita
      arquivo que foi apagado no meio do caminho.
- [ ] Case não menciona "Prezado(a) segurado(a)" nem juridiquês.
- [ ] Case diz **o que foi feito** de pesquisa, com o tamanho da amostra explícito.
- [ ] Onde afirma tamanho e não direção, está marcado como hipótese.
- [ ] Nenhuma tela referenciada sem número (`T.XX`).
- [ ] Cada mudança proposta tem uma heurística que ela corrige.
- [ ] A Fase 14 rodou: os números dos documentos batem com o arquivo.
- [ ] O protótipo abre, tem ponto de partida nomeado e não tem beco sem saída.
- [ ] Ortografia revisada por leitura invertida (do fim para o começo).
- [ ] Nomes de arquivos em kebab-case sem acento (`fluxo-atual.md`, não `Fluxo Atual.md`).

## Antes de sentar para começar

- [ ] Sei em 1 frase o objetivo do case.
- [ ] Sei quem é a persona primária, e ela tem nome de gente real que eu observei.
- [ ] Tenho café/água ao lado.
- [ ] Bloco de 2–4h ininterruptas reservado no calendário.
- [ ] Referências abertas: Nielsen 10, HIG do iOS, Material Design (para contraste).

---

# Armadilhas em que já caí, e como evito hoje

## 1. Começar pelos wireframes

Comecei um case anteriormente pulando direto para Figma. Sem heurística, o wireframe vira "achismo bonito". Hoje **sempre** passo pelas fases 2–4 antes de qualquer traço.

## 2. Notas todas em 5–6

Medo de dar nota extrema faz o painel heurístico virar sopa morna. Se está ruim, é 3. Se está ótimo, é 8+. O diagnóstico geral **precisa** ter contraste.

## 3. Sugestões vagas

*"Melhorar UX"* não é sugestão. *"Adicionar máscara XXX.XXX.XXX-XX no campo CPF com validação de dígito verificador em tempo real"* é sugestão.

## 4. Ignorar compliance

Achar que compliance é o inimigo. Não é. Compliance é dado, e sua criatividade está em **reorganizar** o compliance, não em removê-lo. Termo continua obrigatório; muda para bullets em linguagem cidadã.

## 5. Copiar Material Design

O produto tem uma paleta observada. Extraia dela. Só use padrões externos como referência para **estados** e **acessibilidade**, não para cor ou tipografia.

## 6. Portfólio impessoal

Case sem "eu" não convence. O recrutador quer saber **como você pensa**, não só o que você entrega. Escreva em 1ª pessoa, reconheça limites, mostre reflexão no fim.

## 7. Design system antes de tokens

Se você faz o sistema ideal antes de extrair o observado, você está inventando, não fundamentando. Sempre tokens primeiro, sistema depois.

## 8. Publicar Figma sem checklist

Publicar biblioteca sem `Focus`, sem microcopy, sem antipadrões documentados é
publicar biblioteca que ninguém vai usar. Use o checklist do `guia-figma.md` antes de
qualquer publish.

## 9. Parar no documento

A primeira versão deste playbook terminava em texto, com uma linha dizendo que o
Figma ficou de fora "por falta de tempo". Não foi falta de tempo, foi subestimar a
fase. Tudo de mais interessante que este case tem hoje veio depois daquele ponto, e
**nada disso era descobrível lendo**. Documento descreve intenção; arquivo tem
comportamento.

## 10. Confiar no documento em vez de medir o arquivo

Três defeitos seguidos aqui tinham a mesma forma: o documento dizia o certo e o
arquivo fazia outra coisa. Eu li os dois e não vi, porque ler não mostra. Hoje eu
meço o arquivo e comparo com o texto, sempre com script, nunca por amostragem.

## 11. Achar que revisão visual pega defeito de comportamento

Rodapé que rola junto, botão travado que responde ao toque, onboarding que recomeça,
tela que promete "toque para corrigir" e não faz nada. Parados, todos esses arquivos
estão idênticos ao certo. Só um dedo encontra.

## 12. Anotar comportamento que o arquivo não tem

Eu tinha indicador de rolagem desenhado em dez telas e sete não rolavam. A anotação
estava linda e mentindo. Anotação é promessa: se ela descreve comportamento, o
comportamento precisa existir no arquivo.

## 13. Confiar em nome de camada

Camada clonada herda o nome da origem. Neste case as checklists de dois documentos
diferentes tinham o texto certo e o nome de camada da tela de onde foram copiadas, e
foi o nome que minhas varreduras leram. Audite o conteúdo, e trate o nome como pista,
não como verdade.

## 14. Chamar folga de 2pt de folga

A tela de documentos coube na janela por 2pt e eu tirei ela da lista de telas que
rolam. Um link novo num card, 54pt, e ela voltou. Folga que não aguenta um acréscimo
de conteúdo não é folga, é coincidência.

## 15. Escrever "não fiz pesquisa" quando você fez alguma coisa

Observar uma pessoa real, receber as capturas dela, perguntar onde dói e depois
mostrar a solução para ouvir a opinião é pouca pesquisa, não nenhuma. Descreva o que
fez, com a amostra explícita. A honestidade está em dizer n=1, não em apagar o n.

## 16. Corrigir pela metade e comemorar

Eu "consertei" a rolagem somando um espaçamento, a conta fechou, e o problema
continuou porque o rodapé rolava junto. Conta que fecha não é comportamento que
funciona. Depois de corrigir, **reproduza o defeito original**: se ele não volta, aí
sim acabou.

---

# Como este playbook evolui

A cada case novo, eu:
1. Sigo o playbook.
2. Anoto o que não deu certo ou o que faltou.
3. Volto aqui e edito a fase correspondente.

O playbook **é vivo**. Se ele congelar, é sinal de que parei de aprender.

## Segunda rodada, no mesmo case

A primeira versão saiu quando os documentos ficaram prontos. Depois eu construí as
telas, o design system medido, a biblioteca, os mockups e o protótipo, e voltei aqui.
O que mudou:

- **Cinco fases novas** (9 a 12 e 14), todas da metade que acontece dentro do Figma.
- **A Fase 8 foi reescrita do zero.** Estimar hex a olho virou medir com script, e
  toda afirmação passou a carregar a origem.
- **Oito armadilhas novas** (9 a 16), todas descobertas com o arquivo na mão.
- **Três conselhos revogados**: escrever "não fiz pesquisa", entregar
  `wireframes-descritivos.md` como produto, e separar tokens de sistema em dois
  arquivos que não conversam.

Guardo isso aqui em vez de apagar porque **conselho revogado ensina mais que conselho
certo**: mostra o que parecia razoável e não era.
