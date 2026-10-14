# Avaliação Heurística: Fluxo de Reembolso (App SulAmérica)

**Método:** 10 Heurísticas de Usabilidade de Jakob Nielsen
**Material analisado:** 32 screenshots do fluxo real de solicitação de reembolso (categoria *Sessão Psicologia ou Psiquiatria*), capturados em iPhone. As capturas **não estão neste repositório**: elas mostram nome, CPF, dados bancários e a foto de identidade de um usuário real, e por isso foram removidas. O que existe delas aqui são as leituras: este documento, o `fluxo-atual.md`, o inventário de componentes e as medições do design system.
**Escala de notas:** 1 (péssimo) a 10 (excelente)
**Escala de severidade:** baixa · média · alta · crítica

---

## Mapa do fluxo analisado

| Etapa | Telas |
|---|---|
| Entrada (home + menu Reembolso) | `home.png`, `5.png` |
| Estado de loading | `4.png` |
| Histórico | `6.png` |
| Prévia de reembolso (cálculo de estimativa) | `7.png`, `8.png`, `9.png` |
| Onboarding legal e bancário | `10.png`, `11.png`, `12.png` |
| Reembolso digital · categoria | `13.png` |
| Documentos necessários | `14.png` |
| Dados do procedimento | `15.png` |
| Datas do tratamento | `16.png`, `17.png`, `18.png`, `32.png` |
| Tipo de documento + dados do prestador | `19.png`, `20.png`, `21.png`, `33.png` |
| Anexos | `22.png`, `23.png`, `24.png` |
| Resumo | `25.png` |
| Verificação biométrica | `26.png`, `27.png`, `28.png` |
| Confirmação + NPS | `29.png`, `30.png`, `31.png` |
| Documento externo (gov.br) | `doc gov.png` |

---

## 1. Visibilidade do status do sistema

**Nota: 4 / 10**

### Problemas encontrados

- **Tela `4.png`**: Estado de carregamento exibe um indicador minúsculo (parece um simples parêntese laranja), sem mensagem (“Carregando…”, “Buscando seu plano…”) e ocupa uma tela cinza inteira. O usuário não sabe se o app travou.
- **Telas `14.png` → `25.png`**: Em todo o fluxo de solicitação (≈12 etapas), não há indicador de progresso (passo X de Y, breadcrumb, barra). O usuário não tem ideia de quanto falta.
- **Tela `30.png`**: Modal de NPS (avaliação 1–5) surge **sobre** a tela de confirmação ainda em renderização (`29.png`), gerando dúvida sobre se a solicitação foi enviada.
- **Tela `31.png`**: Texto da confirmação usa hedge: *“se estiver tudo certo, o reembolso será pago em até 30 dias”*. O “se” deixa o status real ambíguo.
- **Tela `6.png`** (histórico): Status mostrado apenas como `Reembolso pago`. Não há estados intermediários visíveis (“Em análise”, “Aguardando documento”, “Aprovado, em processamento bancário”).

### Severidade: **alta**

### Sugestão de melhoria

Inserir um *stepper* persistente no topo (ex.: `Passo 4 de 7 · Datas do tratamento`). Substituir o spinner genérico por skeleton screens com microcopy contextual. Adiar o NPS para 1–2 dias após o pagamento (ou expor após o usuário fechar a tela de confirmação). Reescrever a confirmação removendo o “se” e detalhando o status (“Sua solicitação está em análise. Acompanhe pelo número da SR.”). Expor estados intermediários no histórico.

---

## 2. Correspondência entre o sistema e o mundo real

**Nota: 5 / 10**

### Problemas encontrados

- **Tela `6.png`**: Termo `SR 1234567890` aparece como código sem explicação. “SR” é jargão interno (Solicitação de Reembolso).
- **Telas `7.png` e `13.png`**: “Prévia de reembolso” é termo técnico. Usuário leigo lê e pensa: *é o adiantamento? é o orçamento? é simulação?*
- **Telas `20.png` / `21.png`**: Pede `CRP do prestador` e `CNPJ ou CPF do prestador`. Usuário comum não sabe o que é CRP, e raramente conhece o CNPJ do consultório de cabeça.
- **Telas `10.png` / `11.png`**: Termo de Ciência redigido em juridiquês (`tipificadas no Código Penal`, `desobrigam a SulAmérica de realizar o reembolso`, `desidiosa`).
- **Tela `12.png`**: Banco apresentado como `341` (código bancário), não como “Itaú”. Mistura linguagem do mundo do sistema (código) com a do usuário (nome).
- **Tela `9.png`**: Texto longo explica o que é “Prévia”, mas só **depois** que o usuário já entrou na tela.
- **Tela `23.png`**: `VISUALIZE A IMAGEM NESTA ÁREA` em caixa alta soa imperativo e robótico.

### Severidade: **alta**

### Sugestão de melhoria

Substituir “SR” por “Solicitação” (e mostrar o número como secundário). Trocar “Prévia de reembolso” por “Calcular quanto vou receber de volta”. Em vez de pedir CRP/CNPJ logo de saída, oferecer **OCR da nota fiscal** que extrai esses dados, ou um buscador com nome do profissional. Reescrever o termo legal em linguagem cidadã, com versão completa expansível. Mostrar “Itaú (341)” no lugar de “341”. Trocar a microcopy de visualização para “Pré-visualização do documento anexado”, em caixa mista.

---

## 3. Controle e liberdade do usuário

**Nota: 4 / 10**

### Problemas encontrados

- **Tela `8.png`**: Modal pop-up oferece *Saúde na Tela* (telemedicina) interrompendo o fluxo de prévia. Botões `FECHAR` e `ME LEVE ATÉ LÁ`, sem opção “Não mostrar novamente”. Cross-sell intrusivo no meio da tarefa.
- **Todo o fluxo `14.png` → `25.png`**: Não há botão de **salvar como rascunho**. Se o usuário descobre que falta um documento na metade, perde tudo.
- **Tela `31.png`**: Após enviar, o único botão é `Voltar ao início`. Não há *“Ver detalhes da solicitação”*, *“Acompanhar”* ou *“Compartilhar protocolo”*.
- **Telas `15.png`–`18.png`**: Para corrigir o número de sessões já preenchido, é preciso reabrir o seletor, sem aviso de que mudar isso apaga as datas já lançadas.
- **Tela `30.png`**: Modal de NPS aparece sem o usuário ter solicitado. Não há *“Avaliar depois”* claro, só o `X` no canto.

### Severidade: **alta**

### Sugestão de melhoria

Tornar o pop-up de telemedicina não-bloqueante (banner inferior dispensável) e respeitar a escolha do usuário com *“Não mostrar mais”*. Adicionar **rascunho automático** em cada etapa (com indicador visível: “Salvo automaticamente”). Na tela de confirmação, oferecer múltiplos próximos passos: *Ver solicitação*, *Adicionar outra*, *Compartilhar protocolo*, *Voltar ao início*. Adicionar confirmação ao alterar número de sessões (“Isso vai apagar as datas já preenchidas”).

---

## 4. Consistência e padrões

**Nota: 6 / 10**

### Problemas encontrados

- **Telas `7.png` (4 categorias) vs `13.png` (7 categorias)**: A lista de categorias da **Prévia** difere da lista do **Reembolso Digital**. *Por que Fisioterapia não está na prévia?* Inconsistência conceitual.
- **Tela `12.png`**: Botão `ATUALIZAR DADOS` em caixa alta como link laranja, enquanto `Confirmar` é botão sólido em caixa mista. Padrões diferentes para ações no mesmo card.
- **Tela `23.png`**: `VISUALIZE A IMAGEM NESTA ÁREA` em caixa alta vs todos os outros placeholders em caixa mista (telas `15.png`, `20.png`).
- **Telas `10.png` e `11.png`**: Botões `FECHAR` / `VER` / `Confirmar` mesclam caixa alta e mista em telas próximas.
- **Telas `19.png`, `20.png`, `21.png`**: Botão `Próximo` ora desabilitado (cinza), ora ativo (laranja sólido). É o padrão correto, **mas** não há nenhuma sinalização do que falta para habilitá-lo.
- **Tela `33.png` vs `21.png`**: Ao tocar no campo CRP, o teclado vira numérico, mas no campo CPF (também numérico) não há padrão evidente sobre quando o teclado decimal aparece.

### Severidade: **média**

### Sugestão de melhoria

Padronizar **uma única taxonomia de categorias** entre Prévia e Reembolso Digital. Padronizar tipografia dos botões (caixa mista, peso 600). Quando o `Próximo` estiver desabilitado, exibir microcopy `Falta: anexar pedido médico` (ou o motivo específico). Garantir que todo input numérico abra o teclado numérico desde o primeiro toque.

---

## 5. Prevenção de erros

**Nota: 3 / 10**

### Problemas encontrados

- **Tela `32.png`**: Mensagem de erro só aparece **depois** que o usuário preenche todas as datas. Em vez de bloquear preventivamente, o app deixa o usuário cometer o erro.
- **Tela `32.png`**: Texto: *“O pedido só pode ser feito para procedimentos realizados antes do dia 04/05/2026”*. Como a data digitada é 19/06/2026 (futura), a mensagem é confusa (não indica claramente o motivo: limite de 12 meses retroativos? procedimentos futuros não reembolsáveis?).
- **Tela `12.png`**: Não há validação aparente de conta bancária (DV, banco × agência × conta). Sem aviso sobre titularidade.
- **Telas `20.png` / `21.png`**: Não há máscara nem validação visível de CPF (formato XXX.XXX.XXX-XX) ou CRP. Erro de dígito vai passar.
- **Tela `22.png`**: Não diz formatos aceitos (PDF? PNG? tamanho máximo? quantidade máxima?). Usuário descobre por tentativa e erro.
- **Tela `15.png`**: Campo `Valor do documento (R$)` sem máscara monetária visível, sem indicação de centavos.
- **Tela `26.png`**: Verificação biométrica facial só ocorre ao final. Se o usuário falha, perde tempo já investido (12+ etapas).

### Severidade: **crítica**

### Sugestão de melhoria

Validar a data **inline** no momento da digitação, com microcopy explicativa do motivo (“Reembolsos retroativos só nos últimos 12 meses. Limite: dd/mm/aaaa”). Adicionar máscara em CPF, CRP, valor monetário e contas bancárias. Validar dígito verificador em tempo real. Mostrar formatos e tamanhos aceitos no card de upload (`PDF ou JPG, até 10 MB, máx. 5 arquivos`). Mover a verificação biométrica para o início do fluxo (ou aceitar biometria do dispositivo / Face ID já autenticado).

---

## 6. Reconhecimento em vez de memorização

**Nota: 4 / 10**

### Problemas encontrados

- **Telas `20.png` / `21.png`**: Usuário precisa saber de cabeça o **CRP do prestador**. Não há autocomplete, busca por nome, ou OCR da nota fiscal.
- **Telas `17.png` / `18.png`**: Datas das sessões devem ser inseridas manualmente, uma a uma. Não há atalho “sessões semanais a partir de…” ou “mesmo dia da semana por X semanas”.
- **Tela `12.png`**: Dados bancários cadastrados: usuário precisa lembrar se a conta está atualizada. Não há confirmação visual (“Itaú · ag. 00123 · conta final 4567 · em nome de Rafael A.”) com a alternativa fácil de mudar.
- **Tela `14.png`**: Lista de documentos só aparece **uma vez** no início. Nas telas seguintes (`22.png`), não há lembrete de qual documento serve para quê.
- **`doc gov.png`**: Para anexar o recibo do IRPF, o usuário precisa **sair do app**, ir ao gov.br, baixar o PDF, voltar ao SulAmérica e anexar. Quebra completa de contexto.
- **Tela `25.png`** (resumo): Mostra apenas que “Arquivos: 1” foi anexado em cada categoria. Não exibe miniaturas para o usuário **reconhecer** que anexou o documento certo.

### Severidade: **alta**

### Sugestão de melhoria

Implementar **OCR de nota fiscal** que pré-preenche prestador, CPF/CRP, valor e data. Permitir busca de prestador por nome (autocompletar a partir da rede credenciada / histórico). No seletor de datas, incluir “repetir semanalmente”. No resumo, mostrar miniaturas dos documentos anexados. Persistir um “Checklist” fixo no topo com os documentos pendentes (✓ Nota fiscal · ✓ Pedido médico · ✗ Comprovante de pagamento).

---

## 7. Flexibilidade e eficiência de uso

**Nota: 4 / 10**

### Problemas encontrados

- **Todo o fluxo**: Não há **reuso** de dados entre solicitações. Quem faz reembolso semanal de psicologia precisa repreencher CPF, CRP, valor, prestador e dados bancários toda vez.
- **Tela `13.png`**: Não há atalho “Refazer última solicitação”. Não há favoritos.
- **Telas `22.png` / `23.png`**: Anexar exige 3 ações separadas (3 documentos × tocar “Anexar” × selecionar fonte × confirmar). Usuário poderia anexar tudo em uma seleção múltipla.
- **Tela `15.png`**: Sem opção de fotografar a nota e o sistema preencher os campos.
- **Tela `9.png`**: Para calcular prévia, é preciso digitar Estado + Data + Valor manualmente. Sem geolocalização, sem histórico.
- **Tela `5.png`**: Menu Reembolso tem 3 opções no topo. Para usuário recorrente, “Reembolso digital” poderia ser o atalho direto da home (já é via `Mais acessados` em `home.png`, mas leva por todo o caminho).

### Severidade: **alta**

### Sugestão de melhoria

Criar **modo recorrente / Reembolso recorrente**: usuário cadastra prestador + valor padrão + dados bancários uma vez, e cada nova sessão é “Adicionar sessão” → anexar nota → confirmar (3 toques). Permitir seleção múltipla de arquivos no upload. Disponibilizar “Refazer última” no histórico. Capturar nota fiscal por câmera + OCR para pré-preencher.

---

## 8. Estética e design minimalista

**Nota: 5 / 10**

### Problemas encontrados

- **Telas `10.png` / `11.png`**: Termo de Ciência ocupa **duas telas inteiras** de texto corrido sem hierarquia (tudo cinza, mesmo peso, sem subtítulos). Difícil ler, difícil compreender.
- **Tela `9.png`**: Parágrafo explicativo da prévia tem ~6 linhas em cinza claro logo abaixo do formulário, competindo por atenção com os campos a preencher.
- **Tela `10.png`**: Modal “Documentação necessária” aparece **sobre** o termo, criando duas camadas de leitura simultâneas.
- **Tela `8.png`**: Pop-up de cross-sell sobreposto a um fluxo transacional. Quebra o foco.
- **Tela `30.png`**: Modal de NPS sobreposto à tela de confirmação. Mesma sobrecarga visual.
- **Tela `13.png`**: 7 categorias verticais, todas com peso visual idêntico, usuário precisa ler todas para escolher.
- **`home.png`**: Carrossel “Mais acessados” mistura função (Reembolso) com burocracia (Imposto de renda) e produto (Cobertura do plano). Sem hierarquia clara.

### Severidade: **média**

### Sugestão de melhoria

Reescrever o termo de Ciência em **bullets curtos com cabeçalhos**, e oferecer “Ler termo completo” em link. Eliminar modais sobre modais. Converter para fluxos de tela única. Remover o pop-up de cross-sell durante a tarefa de reembolso (ou movê-lo para a home). Diferenciar visualmente categorias mais usadas no menu (`13.png`). Reduzir parágrafos explicativos a 1–2 linhas com link “Saiba mais”.

---

## 9. Ajude usuários a reconhecer, diagnosticar e recuperar erros

**Nota: 3 / 10**

### Problemas encontrados

- **Tela `32.png`**: Mensagem em vermelho discreto, **sem ícone** de alerta, **sem destaque** de qual campo (na verdade, está abaixo da data 3, mas o erro é genérico do formulário).
- **Tela `32.png`**: Texto da mensagem é confuso: *“O pedido só pode ser feito para procedimentos realizados antes do dia 04/05/2026”*. Não explica **por quê** (regra de 12 meses?), nem indica **a data correta** que o usuário deveria informar (a data está no futuro, então a regra real é “datas passadas até 12 meses atrás”).
- **Telas `19.png` / `22.png`**: Quando o botão `Próximo` está desabilitado, **não há mensagem** dizendo o que falta.
- **Tela `26.png`** → **`28.png`**: Se a verificação biométrica falhar, o usuário não tem visibilidade do erro nem caminho de recuperação claro nas screenshots.
- **Telas `20.png` / `21.png`**: CPF inválido não é sinalizado em tempo real; provável que só o backend reclame depois.
- **Tela `4.png`**: Se o carregamento travar, não há botão de “Tentar novamente”.

### Severidade: **crítica**

### Sugestão de melhoria

Mensagens de erro devem (a) **identificar o campo** com borda vermelha e ícone, (b) **explicar a causa** em linguagem natural, (c) **sugerir a correção**. Exemplo: *“A data 19/06/2026 é futura. O reembolso só pode ser solicitado para sessões já realizadas, dentro dos últimos 12 meses (a partir de 04/05/2025).”*. Quando o `Próximo` estiver desabilitado, exibir tooltip ou microcopy: *“Faltam: tipo de terapia”*. Em todo loading, oferecer fallback de erro com `Tentar novamente` após 10s sem resposta.

---

## 10. Ajuda e documentação

**Nota: 3 / 10**

### Problemas encontrados

- **Todo o fluxo**: Não há ícone de ajuda contextual (`?`) nos campos críticos: CRP, CNPJ, Tipo de terapia, Data limite, Conta bancária.
- **Telas `10.png` / `11.png`**: Termo legal serve como “documentação” mas é juridiquês, não substitui ajuda prática.
- **Tela `14.png`**: Lista de documentos é razoável (Nota fiscal/recibo, Pedido médico, Comprovante de pagamento), mas **não explica** *o que é* um pedido médico aceito, *o que é* um comprovante de pagamento aceito (extrato bancário? PIX? recibo do prestador?).
- **`home.png`**: Há um item “Ajuda” no rodapé, mas dentro do fluxo de reembolso ele não é visível.
- **`doc gov.png`**: Não há nenhum tutorial explicando *como* obter o recibo no gov.br para anexar. O usuário se vira sozinho.
- **Tela `9.png`**: Texto explicativo da prévia traz utilidade mas é estático e longo.

### Severidade: **alta**

### Sugestão de melhoria

Adicionar ícone `(?)` ao lado de **todo** campo técnico, abrindo um *sheet* com explicação curta + exemplo + foto/diagrama. Para “Pedido médico” e “Comprovante de pagamento”, mostrar miniatura de exemplo (foto de um recibo válido). Criar **micro-guia em vídeo** de 30s “Como solicitar reembolso” disponível em `home.png` e dentro do fluxo. Embutir o caminho gov.br como passo guiado: *“Não tem o recibo? Veja como baixar no Meu IRPF →”*. Disponibilizar canal WhatsApp/chat persistente no rodapé do fluxo.

---

## Tabela resumo

| # | Heurística de Nielsen | Nota | Severidade dominante |
|---|---|:---:|:---:|
| 1 | Visibilidade do status do sistema | 4 | Alta |
| 2 | Correspondência entre o sistema e o mundo real | 5 | Alta |
| 3 | Controle e liberdade do usuário | 4 | Alta |
| 4 | Consistência e padrões | 6 | Média |
| 5 | Prevenção de erros | 3 | **Crítica** |
| 6 | Reconhecimento em vez de memorização | 4 | Alta |
| 7 | Flexibilidade e eficiência de uso | 4 | Alta |
| 8 | Estética e design minimalista | 5 | Média |
| 9 | Ajude o usuário a reconhecer, diagnosticar e recuperar erros | 3 | **Crítica** |
| 10 | Ajuda e documentação | 3 | Alta |
| | **Média geral** | **4,1** | **Alta → Crítica** |

---

## Diagnóstico geral

O fluxo de reembolso do app SulAmérica cumpre o *job to be done* (o usuário consegue, ao final, enviar a solicitação), mas o faz à custa de fricção alta, retrabalho previsível e abandono provável. Os pontos mais frágeis são **Prevenção de erros (nota 3)** e **Recuperação de erros (nota 3)**: o sistema deixa o usuário cometer enganos óbvios (datas fora do prazo, CPF/CRP sem máscara, anexos sem critérios visíveis) e, quando o erro acontece, comunica em linguagem técnica e sem apontar a correção. **Ajuda e documentação (nota 3)** completa o trio crítico: não há suporte contextual em pontos de bloqueio (CRP, conta bancária, recibo IRPF do gov.br), e a única documentação “rica” é o termo jurídico, ilegível para o usuário leigo. As heurísticas 1, 3, 6 e 7 (notas 4) revelam um fluxo desenhado como *form long*: 12+ etapas lineares, sem stepper, sem rascunho, sem reuso de dados, sem OCR, sem atalhos para usuários recorrentes, particularmente penalizante para quem faz reembolso semanal de psicoterapia (uso típico desta categoria). As heurísticas 2, 8 e 4 (notas 5–6) mostram que a base visual é razoável, mas o produto é *tecnocrático*: jargão (SR, CRP, código bancário 341), termos legais densos, modais empilhados e cross-sell intrusivo no meio da tarefa transacional. **O ganho mais alto com menor esforço** está em (a) substituir digitação manual por OCR da nota fiscal, (b) validar campos críticos em tempo real com mensagens prescritivas, (c) introduzir um stepper persistente e rascunho automático, e (d) reescrever microcopy técnica em linguagem cidadã. Essas quatro intervenções, isoladamente, devem reduzir significativamente abandono e retrabalho, sem alterar a estrutura de compliance do produto.
