# Redesign do Fluxo de Reembolso

**Aplicativo SulAmérica · Estudo de caso UX/UI**

## Resumo executivo

Redesenhei o fluxo de solicitação de reembolso do app da SulAmérica, partindo da observação de um usuário real percorrendo o fluxo mais de uma vez e da análise heurística das 32 telas que ele registrou. O fluxo atual tem ~12 etapas com input ativo, validação reativa e linguagem técnica, gerando alta fricção. Minha proposta reduz para 5 etapas (mais um onboarding único), substitui digitação manual por OCR da nota fiscal, traz validação inline com mensagens prescritivas e mantém todas as etapas obrigatórias por compliance, só que reorganizadas para criar menos atrito. Espero, com isso, reduzir abandono no meio do fluxo, encurtar o tempo até envio e diminuir o retrabalho gerado por erros de preenchimento.

Além da análise de fluxo, medi o sistema visual pixel a pixel e comparei com os tokens que a própria SulAmérica publica no site. O achado mudou meu diagnóstico: **o problema não é ausência de design system, é falta de aderência ao que já existe.**

## Sumário

1. [Contexto](#1-contexto)
2. [Problemas identificados](#2-problemas-identificados)
3. [Processo](#3-processo)
4. [Solução: novo fluxo](#4-solução-novo-fluxo)
5. [Wireframes-chave](#5-wireframes-chave)
6. [Microcopy](#6-microcopy)
7. [Resultados esperados](#7-resultados-esperados)
   - [Anexo · Mapeamento heurística → solução](#anexo--mapeamento-heurística--solução)

---

## 1. Contexto

Esse case nasceu de observação, não de enunciado. Acompanhei uma pessoa pedindo reembolso de sessões de psicologia pelo app da SulAmérica e registrei o caminho inteiro, tela por tela. O que era para ser um pedido simples virou doze etapas de digitação, uma saída do app para o gov.br e um erro de data que só apareceu no fim.

Fui atrás desse fluxo porque ele toca quem mais precisa de simplicidade: pessoas em tratamento de saúde mental fazendo reembolso semanal, gente que se machucou e precisa de fisioterapia, mães e pais de primeira viagem lidando com partos. Para todo esse público, cada minuto de fricção pesa.

O que a observação mostrou, e que a análise depois confirmou tela a tela: a pessoa não sabe quais documentos enviar até já estar no meio do fluxo, a linguagem é jurídica onde precisa ser clara, são muitos passos para uma tarefa repetida todo mês, a confirmação no fim não diz o que acontece agora, e o erro de preenchimento só aparece depois de tudo pronto.

Duas restrições vieram do próprio produto e não podiam ser removidas: **as etapas obrigatórias por compliance** (termo de ciência, validação de identidade, comprovante de pagamento) e o **upload de documentos**. O redesenho reorganiza essas etapas, não as elimina.

### Persona principal

A persona não foi inventada: ela é o usuário que acompanhou o projeto. Pessoa em terapia semanal, que pede reembolso de psicologia todo mês e por isso percorre o mesmo fluxo repetidas vezes. Esse perfil expõe os pontos mais críticos justamente pela repetição: paciência curta para preencher os mesmos dados de novo, memória de onde errou da última vez e necessidade de previsibilidade financeira. Se o fluxo funciona bem para quem usa muito, funciona ainda melhor para quem usa pouco.

### Material analisado

- 32 screenshots do fluxo real, cedidos pelo usuário que acompanhou o projeto, tirados durante os próprios pedidos (categoria Sessão de Psicologia/Psiquiatria, 4 sessões, em iPhone).
- Mapeamento de etapas, telas de erro (32.png) e ponto de saída do app (uso do gov.br/Meu IRPF).
- O CSS público de `sulamerica.com.br`, que expõe o design system da empresa em 149 variáveis de cor e declara a família tipográfica.

---

## 2. Problemas identificados

Antes de propor qualquer mudança, fiz uma avaliação heurística completa usando as 10 heurísticas de Nielsen. A média das notas ficou em 4,1/10, com duas heurísticas em severidade crítica e seis em alta. Esse painel é o ponto de partida da decisão de redesign.

### Painel de notas (resumo)

| # | Heurística | Nota | Severidade |
|---|---|---|---|
| 1 | Visibilidade do status do sistema | 4/10 | Alta |
| 2 | Sistema × mundo real | 5/10 | Alta |
| 3 | Controle e liberdade do usuário | 4/10 | Alta |
| 4 | Consistência e padrões | 6/10 | Média |
| 5 | Prevenção de erros | 3/10 | Crítica |
| 6 | Reconhecimento vs. memorização | 4/10 | Alta |
| 7 | Flexibilidade e eficiência | 4/10 | Alta |
| 8 | Estética e minimalismo | 5/10 | Média |
| 9 | Recuperação de erros | 3/10 | Crítica |
| 10 | Ajuda e documentação | 3/10 | Alta |

### Os pontos que mais me chamaram a atenção

**Erro só pós-fato**
Na tela de datas das sessões (32.png), o usuário pode digitar uma data inválida e só descobre depois de preencher tudo. Pior, a mensagem de erro é confusa: diz "o pedido só pode ser feito para procedimentos realizados antes do dia 04/05/2026", quando a data digitada era 19/06/2026 (futura). Para quem está no fluxo, é difícil entender qual é a regra real.

**Pedindo dados que o usuário não tem**
Em uma das telas, o app pede o CRP do prestador. Eu tive que parar e pensar: eu mesma, marcando psicóloga uma vez por semana há um ano, não saberia o número do CRP de cabeça. Pedir isso é jogar na cara do usuário uma informação que está, no máximo, em algum recibo guardado.

**Saída forçada do app**
Para anexar o recibo do IRPF como comprovante de pagamento, o usuário precisa sair do SulAmérica, abrir o gov.br, fazer login, baixar o PDF e voltar. Não é um problema de interface bonita ou feia: é uma quebra de contexto que custa abandono real.

**NPS sobreposto à confirmação**
Logo depois de o usuário tocar em enviar, antes mesmo da tela de sucesso terminar de carregar, surge um modal pedindo nota de 1 a 5. É uma demanda do produto sobre o usuário em um momento em que ele só quer saber se deu certo.

**Termo legal denso, em juridiquês**
Duas telas inteiras (10.png e 11.png) com texto corrido sem hierarquia, com palavras como "desidiosa" e "tipificadas no Código Penal". Eu sei que o termo é exigência de compliance (não dá para tirar), mas a forma como está apresentado faz com que ninguém leia, o que ironicamente esvazia o propósito legal.

### O sistema visual: o que a medição mostrou

Eu ia estimar as cores olhando as capturas, como se faz normalmente. Em vez disso amostrei os pixels e fui buscar o CSS do site da SulAmérica, que publica o design system da empresa: **149 variáveis de cor**, rampas de 50 a 950 e a família tipográfica declarada. Isso deu duas fontes verificáveis para comparar, em vez de uma estimativa minha.

**O app não segue o sistema da própria empresa.** A divergência aparece em quatro famílias de cor:

| Onde | O app usa | A SulAmérica publica |
|---|---|---|
| Laranja de marca, em 3 componentes | `#FF5000` | `#F05223` |
| Verde de sucesso | `#1F662E` e `#00861F` | `#04843F` |
| Superfície secundária | cinco cinzas diferentes | um token |
| Título de tela | três tamanhos, de 13 a 21pt | um papel |

Isso muda o diagnóstico. Eu esperava encontrar um app sem sistema; encontrei um sistema que o app não segue. São problemas diferentes, com soluções diferentes: o primeiro pede construção, o segundo pede governança e migração.

**Uma falha de acessibilidade com número.** O botão desabilitado preenche com `#D2D2D2` e escreve em branco: contraste de **1,51:1**. O rótulo é ilegível, então quem chega num botão bloqueado não consegue ler o que ele faria. E a causa não é descuido: o sistema publicado tem token de *texto* desabilitado e **nenhum de superfície** desabilitada. O app precisou de um e inventou.

**A medição achou o que o olho não acha.** O app escurece o fundo atrás de modal de duas maneiras, preto a 40% em quatro telas e a 30% em duas. Ninguém percebe isso olhando, e eu só achei porque `#999999` e `#B2B2B2` em áreas grandes são exatamente branco sob esses dois véus. Se eu tivesse anotado os dois como "cinza", o sistema nasceria com dois tokens falsos.

O padrão se repete: **um papel, várias respostas**. Cinco cinzas de superfície, três verdes de sucesso, três tamanhos de título, dois véus. Nenhuma dessas variações carrega significado, e cada uma custa uma decisão que o time refaz toda vez.

> O sistema completo, com os scripts que produzem cada número, está em `design-system/`. Toda afirmação lá carrega uma marca: **[declarado]** para o que a SulAmérica publica, **[medido]** para o que o app entrega, **[decidido]** para o que foi escolha minha.

---

## 3. Processo

O trabalho começou antes destas quatro etapas: acompanhando um usuário real percorrer o fluxo mais de uma vez e conversando com ele sobre o que trava. Foi dali que saíram as capturas, a persona e a lista de problemas que a análise depois confirmou tela a tela.

As quatro etapas abaixo são o que fiz com esse material. O que não tive foi métrica interna, então onde este documento afirma tamanho, e não direção, a afirmação está marcada como hipótese.

### 3.1 Mapeamento do fluxo atual

Comecei abrindo todas as 32 capturas em sequência e numerando as etapas como o usuário enxerga. Saíram 18 etapas, das quais ~12 com input ativo. Para cada uma anotei o que o usuário faz e qual heurística é violada (referência cruzada com a avaliação). Esse arquivo (`fluxo-atual.md`) virou minha base para tudo que veio depois.

### 3.2 Avaliação heurística

Usei as 10 heurísticas de Nielsen. Para cada uma dei nota de 1 a 10, listei os problemas com referência à tela e classifiquei a severidade em baixa, média, alta ou crítica. Cheguei à média de 4,1 com dois itens em severidade crítica (Prevenção e Recuperação de erros) e seis em alta. Esse painel ficou disponível como `heuristic-evaluation.md` para consulta independente.

### 3.3 Definição da persona e princípios

A persona veio pronta da observação, pessoa em psicoterapia semanal, e dela tirei cinco princípios de redesign: OCR e reuso substituem digitação manual sempre que possível; stepper persistente em todas as telas; validação inline com mensagens prescritivas; microcopy em linguagem cidadã com ícones de ajuda; e modo recorrente para a persona principal. Esses princípios viraram o filtro de cada decisão depois.

### 3.4 Redesign do fluxo + wireframes + microcopy

Com os princípios definidos, redesenhei o fluxo etapa por etapa, justificando cada mudança pela heurística que estava sendo corrigida (`novo-fluxo.md`). Em paralelo, descrevi quatro telas-chave em baixa fidelidade para um designer executar no Figma (Início da solicitação, Upload de documentos, Revisão e Confirmação) e escrevi a microcopy de cada uma, incluindo títulos, instruções, labels, mensagens de erro específicas e a confirmação final.

### O usuário que acompanhou o projeto

Trabalhei com um usuário real do começo ao fim, e é dele que vem quase tudo que este
case afirma sobre a experiência.

Observei ele pedir reembolso **mais de uma vez**, o que importa: o fluxo é mensal, e
os problemas de repetição só aparecem na segunda ou terceira vez. Conversei com ele
sobre como o processo funciona, o que trava e o que dá medo de errar. As **32
capturas são dele**, tiradas durante os pedidos.

Ele também acompanhou o redesenho. Mostrei os wireframes e as soluções conforme
ficaram prontas, para ouvir o que fazia sentido e o que não fazia.

**O que isso é e o que não é.** É pesquisa qualitativa com um participante:
observação repetida, entrevista e devolutiva sobre a proposta. Não é amostra, não é
teste de usabilidade com tarefa cronometrada, e não substitui dado quantitativo,
que eu não tenho.

Um participante mostra bem **onde** o fluxo dói e mal **quanto** ele dói. Por isso
os números da próxima seção estão como hipótese, e por isso a primeira coisa na
lista de próximos passos é levar o protótipo para mais gente.

### Como trabalhei com IA

Conduzi este projeto usando Claude como par de trabalho, do mapeamento à
construção da biblioteca. Registro isso porque o método importa mais que a
ferramenta, e o método aqui foi um só: **nada entra sem verificação.**

Foi disso que nasceu a convenção que organiza o design system inteiro. Toda
afirmação carrega **[declarado]**, **[medido]** ou **[decidido]**, e as três
respondem à mesma pergunta: como eu sei que isso é verdade? Um valor que não pode
receber nenhuma das marcas não entra no documento.

Os 14 scripts em `design-system/extracao/` existem pela mesma razão. Cada número do
sistema pode ser recalculado por quem quiser conferir, e foi rodando essas
verificações que apareceram os erros: cores que pareciam certas e não eram,
contagens que envelheceram, uma medição de raio enviesada pelo próprio método, um
comparador que emparelhava cinza com verde. **Trabalhar bem com IA é construir onde
checar**, e depois checar.

A direção continuou minha. Descartei a documentação de design system que não estava
boa e pedi para refazer do zero. Fui eu que percebi que a biblioteca estava
incompleta, e a auditoria que pedi encontrou onze componentes faltando, entre eles o
stepper, que aparece em 31 das 44 telas. Cortei escopo onde a ferramenta não
agregava: as ilustrações ficaram como especificação, não como desenho fraco.

O que a IA acelerou foi a parte mecânica: medir 32 capturas pixel a pixel, cruzar
149 tokens, aplicar variáveis em 2.564 pontos. O julgamento de quando o resultado
estava errado continuou sendo trabalho humano, e é ele que aparece em cada
**[decidido]** deste repositório.

---

### Sobre o que ficou de fora

Não tive acesso ao app rodando, o que deixa de fora animação, retorno tátil, Dynamic
Type e qualquer estado que as 32 capturas não registram. Também não tive dado
quantitativo: taxa de abandono por etapa, tempo até envio e volume de retrabalho são
exatamente os números que confirmariam ou derrubariam o diagnóstico, e eles existem
dentro da SulAmérica.

---

## 4. Solução: novo fluxo

A proposta reduz o fluxo principal para 5 etapas de preenchimento ativo, com 1 onboarding único feito apenas no primeiro acesso e uma tela de confirmação ao final (que não conta como etapa de preenchimento, o usuário não insere nada nela). Mantive 100% das etapas exigidas por compliance: termo de ciência, validação biométrica e confirmação de dados bancários, mas as movi para o onboarding (uma vez), em vez de repeti-las a cada solicitação. A premissa é simples: pedir reembolso pela quarta vez no mesmo trimestre não pode ser tão pesado quanto pedir pela primeira.

### Onboarding (uma vez)

- Confirmação dos dados bancários, com banco apresentado pelo nome ("Itaú · ag. 00123 · final ●●●●4567") em vez do código. A conta já vem do cadastro do plano: é o que o app faz hoje, e confirmar em vez de digitar é a correção. Para quem entrou no plano agora e não tem conta cadastrada, a mesma etapa vira cadastro em vez de conferência, com o formulário vazio e o motivo dito no título ("Não encontramos uma conta no seu cadastro").
- Termo de Ciência apresentado em 4 bullets curtos, em linguagem cidadã, com link para versão completa abaixo.
- Identidade verificada via Face ID/biometria do dispositivo, aproveitando a autenticação que o usuário já fez ao abrir o app. Quem não tem biometria disponível cai direto na captura de selfie. O aparelho decide o caminho antes da tela abrir, e as duas versões carregam a explicação de por que a identidade está sendo pedida.

### Fluxo principal

**Etapa 1 · Início inteligente**
Usuário entra pelo botão "Pedir reembolso", dentro do card "Reembolso" da home, o mesmo card onde ele retoma um rascunho salvo ou acompanha uma solicitação em análise, cada um com sua própria área tocável. Já na Tela 1 vê duas opções claras: escolher a categoria ou "Refazer última solicitação" (atalho que só aparece para quem já fez antes). Se escolher pedir, vê uma única lista de categorias com ícones: as 3 mais usadas no topo, marcadas como "Suas mais usadas". Corrige consistência (não mais duas listas paralelas), flexibilidade (atalho para recorrente) e visibilidade.

**Etapa 2 · Capturar nota fiscal/recibo**
Tela única com dois caminhos: tirar foto ou anexar arquivo. Após captura, OCR lê a nota e pré-preenche o tipo de documento, CNPJ/CPF e CRP do prestador, valor e data, tudo já com máscara aplicada. O usuário confere os campos extraídos e pode editar com 1 toque. Substitui digitação manual de CRP, CPF e valor (três pontos clássicos de erro) e elimina a memorização forçada de dados que o usuário não tem na cabeça.

**Etapa 3 · Detalhes do tratamento (smart defaults)**
Para Psicologia/Psiquiatria, oferece: tipo de terapia pré-selecionado conforme histórico, número de sessões e duas opções para datas: "Gerar as datas para mim", com frequência (semanais, quinzenais ou mensais) e data da primeira sessão, mostrando o preview das datas geradas; ou "Inserir uma a uma" (manual). A frequência tem smart default pelo tipo de terapia: psicologia abre em semanais, psiquiatria em mensais, porque assumir semanal para todo mundo empurraria justamente o paciente de psiquiatria para o preenchimento manual. Validação inline: se a data estiver fora da janela permitida, o campo fica vermelho com microcopy clara: "Data fora do prazo de 12 meses. Última data válida: 04/05/2025."

**Etapa 4 · Anexos complementares**
Tela única com 3 slots de upload em checklist visível: nota fiscal/recibo (já vinda da Etapa 2), pedido médico, comprovante de pagamento. Cada slot mostra os formatos aceitos, um botão "Ver exemplo" com miniatura do que é aceito e, para o comprovante de pagamento, um tutorial passo-a-passo embutido para baixar o recibo do gov.br/Meu IRPF, sem sair do app. Permite seleção múltipla.

**Etapa 5 · Revisão**
Card único com beneficiário, prestador, procedimento, datas, valor, miniaturas dos 3 documentos anexados, conta bancária e estimativa de reembolso. Cada bloco tem um lápis ✎ que leva ao ponto exato para editar, sem perder o restante do que já foi preenchido. Inclui também "Salvar como rascunho" para quem precisa pausar.

**Confirmação · tela de retorno (pós-envio, não conta como etapa de preenchimento)**
Tela limpa, sem modais sobrepostos. Texto direto: "Solicitação enviada. Em até 5 dias úteis você verá o status atualizado aqui." Card de protocolo com botão de copiar, lista "O que acontece agora" (3 marcos com cronograma esperado) e quatro caminhos: Acompanhar status, Adicionar mais uma sessão (atalho que pré-preenche tudo), Compartilhar protocolo, Voltar ao início. NPS é movido para um push 24–48h depois, fora do contexto da transação.

### Comparativo

| Indicador | Fluxo atual | Novo fluxo |
|---|---|---|
| Etapas com input ativo | ~12 | 5 (+1 onboarding único) |
| Telas até envio | 30+ | ~10 |
| Digitação manual de CRP/CPF/valor | Sim | Não (OCR) |
| Stepper persistente | Não | Sim |
| Validação de datas | Pós-preenchimento | Inline |
| Mensagens de erro prescritivas | Não | Sim |
| Atalho para usuário recorrente | Não | Refazer última + Adicionar mais uma |
| Modais sobrepostos no fluxo | 3 (cross-sell, doc, NPS) | 0 |
| Saída do app durante o fluxo | Sim (gov.br) | Não (tutorial guiado embutido) |
| Biometria | Final do fluxo | Aproveitada do login (Face ID) |

---

## 5. Wireframes-chave

Levei o fluxo inteiro para o Figma: **44 telas em baixa fidelidade**, em escala de cinza, organizadas em sete blocos: onboarding (8 telas), fluxo principal (7), pós-envio, sheets e visualizador (8), estados especiais (9), erros e validação (3), captura/espera/retomada (3) e detalhe/filtros/ajuda (6). [Ver no Figma →](https://www.figma.com/design/LUp4aT7fVYH4cD8ZwrHIfd/Reembolso-SulAmerica?node-id=33-5)

Optei por baixa fidelidade sem cor de propósito: nesta fase o que precisa ser julgado é a ordem das perguntas, a hierarquia e a microcopy, não a paleta.

A cor entrou depois. As mesmas 44 telas existem em alta fidelidade na página `mockups`, com o design system aplicado: 2.564 preenchimentos ligados a variável, zero valores soltos, e 148 ícones desenhados para a biblioteca. **Os wireframes continuam intactos na página deles**, porque respondem a perguntas diferentes e nenhum substitui o outro. As anotações de cada tela, com o motivo de ela ser assim e a heurística que corrige, estão em `anotacoes-ux.md`.

Abaixo, as quatro telas que carregam o argumento do redesign.

**Tela 1 · Início da solicitação**
Stepper no topo ("Passo 1 de 5 · Categoria"), pergunta direta ("Qual procedimento você fez?"), seção "Suas mais usadas" em destaque (card com fundo levemente colorido), seção "Outras categorias" como lista densa. Atalho "Refazer última solicitação" abaixo, separado por linha tênue para não competir com o fluxo novo. Sem pop-ups de cross-sell.

**Tela 4 · Upload de documentos**
3 slots de upload em uma tela só, com indicador de estado (✓/☐), microcopy explicativa do que é cada documento, botões duplos (Anexar/Trocar + Ver exemplo/Como obter). Status agregado abaixo ("Restam 2 documentos: pedido médico e comprovante") e botão "Avançar" sticky no rodapé, desabilitado com a pendência dita por extenso, não um botão cinza silencioso. O slot "Comprovante de pagamento" abre o tutorial gov.br como bottom sheet, sem sair do app.

**Tela 5 · Revisão dos dados**
Cards-resumo verticais (Beneficiário, Prestador, Procedimento, Documentos com miniaturas, Conta bancária), cada um com lápis ✎ que leva ao ponto exato para editar. Banner informativo com estimativa de reembolso, rotulado como estimativa e não promessa. Indicador discreto "Salvo automaticamente às hh:mm" acima do título. Dois CTAs: "Enviar solicitação" (primário) e "Salvar como rascunho" (secundário).

**Tela 6 · Confirmação de envio**
Tela limpa, sem modais. Ilustração de sucesso, frase direta sem hedge, card de protocolo com botão Copiar, lista "O que acontece agora" com 3 marcos cronológicos. Três ações empilhadas (Acompanhar status, Adicionar mais uma sessão, Compartilhar protocolo) e um link discreto "Voltar ao início". NPS removido daqui.

Além dessas, os wireframes cobrem o que normalmente fica de fora de um case e é onde o fluxo real quebra: a conferência dos campos lidos pelo OCR (2A), a timeline de acompanhamento pós-envio (7), o histórico com card de pendência acionável (8), os três bottom sheets de ajuda e cinco estados: loading, vazio, erro de rede e os dois de **primeiro acesso**.

Os de primeiro acesso merecem nota. É fácil desenhar um fluxo inteiro para o usuário que já tem histórico, e foi o que eu fiz na primeira passada: a home anunciava "você tem 1 solicitação em análise" e a tela de categorias abria com "Suas mais usadas". Nada disso existe para quem nunca pediu reembolso, justamente quem tem mais dificuldade. Nesse estado a seção de mais usadas some (não aparece vazia), o rótulo "Outras categorias" vira "Categorias" (não há outras em relação a quê) e o atalho "Refazer última solicitação" não é renderizado. São três detalhes pequenos, do tipo que passa direto na implementação se não estiver desenhado.

O mesmo raciocínio me fez voltar e desenhar os **estados de erro**. Eu tinha 24 telas e todas mostravam o caminho feliz, o que é confortável e desonesto, porque erro de preenchimento foi justamente o que travou o fluxo na observação. Sem frame de erro, a promessa de "validação inline com mensagens prescritivas" fica só como tabela em documento. Desenhei três: a data fora do prazo de 12 meses (Tela 3), os campos do OCR com erro e com baixa confiança (Tela 2A) e a solicitação parada por falta de documento (Tela 7). Nos wireframes em cinza, erro é borda contínua de 2pt com `⚠` e alerta é borda tracejada com `ⓘ`; na alta fidelidade viram `#D32F2F` e `#F9A825`.

Essa última fechou um fio solto que eu não tinha visto: o Histórico já tinha um card *"Aguardando documento · Resolver agora →"* que apontava para uma tela inexistente.

---

## 6. Microcopy

Adotei três princípios de voz: clareza acima de simpatia (linguagem cidadã, frases curtas, verbos no imperativo direto); sem juridiquês ou jargão (palavras como "SR", "prévia" e "prestador" sem explicação foram banidas dos rótulos visíveis ao usuário); e mensagens de erro que dizem o que aconteceu, por quê e o que fazer agora, não generalidades.

### Exemplos de mensagens de erro reescritas

| Situação | Antes (atual) | Depois (proposto) |
|---|---|---|
| Data inválida | "O pedido só pode ser feito para procedimentos realizados antes do dia 04/05/2026." | "Data fora do prazo de 12 meses. Última data válida: 04/05/2025." |
| Avançar desabilitado | (silencioso, botão fica cinza) | "Falta anexar: pedido médico." |
| Arquivo grande demais | (o app simplesmente não aceita) | "Arquivo muito grande. Reduza para até 10 MB ou tire uma foto com qualidade média." |
| Sem internet | (spinner indefinido) | "Sem internet. Conecte-se para ver as categorias. [Tentar novamente]" |

### Exemplo da confirmação final

**Antes (atual):**
> Agora é só esperar :) Sua solicitação foi recebida e, se estiver tudo certo, o reembolso será pago em até 30 dias.

**Depois (proposto):**
> Solicitação enviada. Em até 5 dias úteis você verá o status atualizado aqui.

A diferença pode parecer cosmética, mas tirar o "se estiver tudo certo" e prometer um marco verificável em 5 dias úteis (em vez de "até 30 dias", que mistura prazo de análise com prazo de pagamento) muda a percepção de controle do usuário.

As mensagens da tabela acima não ficaram só no papel: as três primeiras aparecem desenhadas nos wireframes de erro (Parte 6, no Figma). Isso importa porque a qualidade de uma mensagem de erro depende de onde ela cai. *"Data fora do prazo de 12 meses. Última data válida: 04/05/2025"* funciona colada ao campo e com o CTA bloqueado logo abaixo; a mesma frase num toast que some em 3 segundos não funciona. O texto completo de todas as telas está em `microcopy.md`.

---

## 7. Resultados esperados

As metas abaixo são hipóteses. Elas nascem do que observei com um usuário e da análise heurística, não de medição: sem dado interno da SulAmérica e com um participante só, dá para apontar a direção, não o tamanho. Ficam como ponto de partida para uma rodada de validação.

### Hipóteses quantitativas

- **Redução do tempo até envio**: de 8–14 minutos (estimado pela contagem de etapas e digitação manual) para 3–5 minutos no caminho recorrente, principalmente pela substituição da digitação por OCR e pelo atalho "Adicionar mais uma sessão".
- **Queda do abandono entre as etapas de datas e anexos**: os dois pontos com severidade crítica na avaliação (H5 e H9) estão concentrados aí. A validação inline e o tutorial gov.br embutido atacam diretamente esses gargalos.
- **Redução de retrabalho de back-office**: erros de CPF, CRP e valor (causados pela ausência de máscara e validação) são significativamente reduzidos pelo OCR + máscara aplicada.
- **Aumento de NPS do fluxo**: medindo via push 24–48h depois (e não no calor da transação), espero que a nota suba especificamente em "clareza do que fazer" e "clareza do status do pedido", as duas coisas que a pessoa observada não conseguiu responder sozinha.

### Hipóteses qualitativas

- O usuário em terapia recorrente passa a sentir o app como uma ferramenta de apoio, não um obstáculo entre ele e seu reembolso.
- Equipes de atendimento recebem menos chamados sobre "o que é CRP", "o app não aceita meu arquivo", "como pego o recibo do imposto de renda".
- O time de produto SulAmérica ganha um modelo replicável para os outros tipos de reembolso (consulta, exames, fisioterapia), com microcopy e padrões consistentes.

### Próximos passos

- Levar o protótipo para 5 a 8 pessoas em tratamento recorrente, com tarefa de fim a fim: é o que transforma o que observei com um usuário em padrão, ou mostra que não era.
- Validar a viabilidade técnica do OCR de nota fiscal e do tutorial gov.br embutido com o time de engenharia.
- Co-design com compliance e jurídico para versão cidadã do termo de ciência (mantendo conformidade legal).
- Definir métricas de sucesso e baseline antes de qualquer rollout (tempo até envio, taxa de abandono por etapa, taxa de retrabalho por solicitação, NPS).
- Validar com o time de marca o alinhamento do laranja do app ao token publicado. É a única decisão do sistema visual que muda a percepção da cor da marca, e adiá-la só aumenta o número de telas a refazer.
- Definir a governança que evita a divergência voltar: sem alguém responsável pelo sistema, cinco cinzas viram seis.

### Reflexão de fim

Esse projeto me ensinou principalmente uma coisa: as restrições de compliance (que parecem ser as principais responsáveis pela complexidade) quase nunca são o problema real. O termo de ciência precisa ser assinado, sim. A identidade precisa ser validada, sim. Os documentos precisam ser anexados, sim. O que faz o fluxo ser ruim é como esses elementos foram organizados ao redor da pessoa, não a presença deles. Reorganizar com um pouco mais de carinho, mantendo o mesmo conteúdo, faz uma diferença enorme, e essa é, no fundo, a mensagem que eu quis deixar nesse case.

---

## Anexo · Mapeamento heurística → solução

Para garantir rastreabilidade, listo abaixo cada heurística e qual decisão do redesign endereça os problemas detectados.

| Heurística | Severidade | Solução proposta |
|---|---|---|
| 1. Visibilidade do status | Alta | Stepper persistente; estados intermediários no histórico; confirmação sem hedge; skeleton screens com microcopy. |
| 2. Sistema × mundo real | Alta | Linguagem cidadã; banco pelo nome; troca de "SR" por "Solicitação"; termo de ciência em bullets. |
| 3. Controle e liberdade | Alta | Rascunho automático; múltiplas saídas na confirmação; cross-sell removido do fluxo; edição direcionada na revisão. |
| 4. Consistência e padrões | Média | Lista única de categorias; padronização tipográfica e de botões. |
| 5. Prevenção de erros | Crítica | Validação inline; máscaras de CPF/CRP/valor; formatos de upload visíveis; biometria movida para onboarding. |
| 6. Reconhecimento vs. memorização | Alta | OCR da nota fiscal; checklist persistente; miniaturas no resumo; reuso de dados. |
| 7. Flexibilidade e eficiência | Alta | "Refazer última"; "Adicionar mais uma sessão"; multi-seleção no upload; smart defaults para recorrentes. |
| 8. Estética e minimalismo | Média | Sem modais sobrepostos; termo legal com hierarquia; categorias com peso visual diferenciado. |
| 9. Recuperação de erros | Crítica | Mensagens prescritivas (causa + correção); fallback de "Tentar novamente" em loadings; tooltip no botão desabilitado. |
| 10. Ajuda e documentação | Alta | Ícones (?) inline com explicações; "Ver exemplo" nos uploads; tutorial gov.br embutido; chat persistente no rodapé do fluxo. |

---

## Anexo · O que está neste repositório

| Pasta ou arquivo | O que é |
|---|---|
| `case-study-reembolso-sulamerica.md` | o case narrativo, em 5 etapas, para portfólio |
| `case-completo.md` | este documento, a versão longa e técnica |
| `fluxo-atual.md` | mapeamento das etapas do fluxo de hoje |
| `heuristic-evaluation.md` | avaliação pelas 10 heurísticas de Nielsen |
| `novo-fluxo.md` | o fluxo proposto, em texto |
| `microcopy.md` | textos exatos das telas-chave |
| `anotacoes-ux.md` | por que cada uma das 44 telas é assim, e o mapa de destinos do protótipo |
| `wireframes/` | 44 PNGs em baixa fidelidade, mais 37 composições com as notas de design |
| `mockups/` | as mesmas 44 telas com o design system aplicado, mesmos nomes de arquivo |
| `design-system/` | 7 documentos, 14 scripts de medição e a biblioteca do Figma |
| `playbook.md` | o método, em 14 fases, para reaplicar em outro produto |

No Figma, cinco páginas: `apresentação do case`, `mapeamento do fluxo atual`,
`wireframes`, `design system` e `mockups`.

**O protótipo clicável** mora na página `mockups`, começa na home de primeiro
acesso e alcança 43 das 50 telas com 145 ligações e nenhum beco sem saída, passando
pelo onboarding, pelo primeiro pedido e pelo histórico. As sete de fora são deliberadas e estão listadas
em `anotacoes-ux.md`: cinco são estados que só a rede ou a validação produzem e duas
são o ramo de quem já tem conta bancária cadastrada.

**Para entender como o design system foi construído**, incluindo os caminhos que não
deram certo, o documento é `design-system/processo.md`.

Fim.
