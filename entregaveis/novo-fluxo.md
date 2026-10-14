# Novo fluxo · Solicitação de Reembolso (proposta de redesign)

**Foco:** mobile · sessões recorrentes (psicoterapia) como persona primária
**Objetivo:** reduzir erros, diminuir abandono, aumentar clareza do que fazer e do status do pedido.

## Restrições respeitadas

- **Mobile-first**: todo o fluxo otimizado para uma mão e teclado mobile.
- **Upload de documentos é obrigatório**: mantido em todos os caminhos.
- **Compliance preservado**: termo de ciência, validação biométrica e confirmação dos dados bancários **continuam**, mas reorganizados em momentos onde geram menos atrito.

## Princípios de redesign

1. **OCR + reuso** substituem digitação manual sempre que possível (corrige H6, H7).
2. **Stepper persistente** dá contexto de progresso em cada tela (corrige H1).
3. **Validação inline** com mensagens prescritivas (corrige H5 e H9).
4. **Microcopy em linguagem cidadã** + ícone `(?)` em todos os campos técnicos (corrige H2 e H10).
5. **Modo recorrente** ("Adicionar sessão") para a persona principal (corrige H7).

---

## Etapa 0 · Onboarding (primeira solicitação · uma vez por usuário)

> Acontece **antes** de qualquer fluxo, no primeiro acesso à área de Reembolso. Em seguida, fica salvo no perfil.

- **0.1 Confirmação dos dados bancários**: mostra `Itaú · ag. 00123 · conta final ●●●●4567 · em nome de Rafael A. C. Moreira` e oferece *Confirmar* ou *Atualizar*.
- **0.2 Termo de Ciência (resumo + completo)**: bullets com 4 pontos-chave em linguagem cidadã + link "Ler termo completo".
- **0.3 Identidade verificada via Face ID/biometria do dispositivo**: se já autenticado no app, dispensa selfie no fluxo de reembolso.

**Por quê:** isolar etapas de compliance que são **pré-requisitos** elimina retrabalho cada vez que o usuário pede reembolso. Corrige H1, H2, H5 e H8.

---

## Fluxo principal

> **Stepper persistente no topo** (`Passo X de 5`) e **rascunho automático** com indicador "Salvo".

### Etapa 1 · Início inteligente
**Substitui:** etapas 1–3, 5, 10 do fluxo atual.

O usuário entra direto pela home no card *Pedir reembolso*. Vê duas opções **claras**:

- **Pedir reembolso** (CTA primário)
- **Refazer última solicitação** (atalho que só aparece para quem já fez antes)

Se escolher *Pedir reembolso*, vê uma única lista enxuta de categorias com ícones e descrição em uma linha. As 3 mais usadas pelo usuário ficam no topo, etiquetadas como “Suas mais usadas”.

**Heurísticas corrigidas:** H4 Consistência (uma única taxonomia), H7 Flexibilidade (atalho), H8 Minimalismo, H1 Visibilidade.

---

### Etapa 2 · Capturar nota fiscal/recibo (substitui digitação manual)
**Substitui:** etapas 12 e 14 do fluxo atual.

Tela única com dois caminhos:

- **Tirar foto agora** (câmera abre dentro do app, CTA primário)
- **Anexar arquivo da galeria** (PDF, JPG, PNG)

Após captura, **OCR** lê a nota e pré-preenche:
- Tipo de documento (Nota fiscal × Recibo)
- CNPJ/CPF e CRP do prestador (com máscara já aplicada)
- Valor (com máscara monetária)
- Data do atendimento (validada inline)

O usuário **confere** os campos extraídos em uma única tela; pode editar com 1 toque.

**Heurísticas corrigidas:** H5 Prevenção de erros (máscara, validação inline), H6 Reconhecimento (não memorizar CRP), H7 Flexibilidade (1 ação no lugar de 4 telas), H9 Recuperação (erros já em tempo real).

---

### Etapa 3 · Detalhes do tratamento (smart defaults)
**Substitui:** etapas 13 e 12 (parte) do fluxo atual.

Para Psicologia/Psiquiatria especificamente:

- *Tipo de terapia* (Psicologia / Psiquiatria / Multidisciplinar), pré-selecionado se houver histórico recente.
- *Quantas sessões?*: input numérico.
- *Quando aconteceram?*: duas opções:
  - **Semanais a partir de** [data picker], gera as datas automaticamente
  - **Inserir uma a uma** (modo manual)

Validação **inline** das datas: se houver data fora da janela (futura ou >12 meses), o campo fica em vermelho com microcopy: *"Data fora do prazo de 12 meses. Última data válida: 04/05/2025."*

**Heurísticas corrigidas:** H5 (validação inline), H9 (mensagem prescritiva), H7 (atalho “semanais a partir de”), H6 (reuso do tipo).

---

### Etapa 4 · Anexos complementares (consolidados)
**Substitui:** etapa 15 do fluxo atual (3 cards separados).

Uma tela única com **3 slots de upload em linha** (checklist visível):

1. ✓ Nota fiscal/recibo (já anexado na Etapa 2)
2. ☐ Pedido médico
3. ☐ Comprovante de pagamento

Cada slot indica:
- Formatos aceitos (`PDF, JPG, PNG · até 10 MB`)
- Botão *“Ver exemplo”* que abre miniatura do que é aceito.
- Para o comprovante de pagamento: tutorial passo-a-passo embutido para baixar o recibo do gov.br/Meu IRPF (corrige a quebra de contexto da etapa 15-A do atual).

Permite **selecionar múltiplos arquivos** de uma vez.

**Heurísticas corrigidas:** H6 (exemplos visuais), H7 (multi-seleção), H10 (ajuda contextual com tutorial gov.br), H5 (formatos visíveis).

---

### Etapa 5 · Revisão
**Substitui:** etapa 16 do fluxo atual.

Card único com:
- Beneficiário, prestador (nome + CRP), tipo de terapia, número e datas das sessões.
- **Miniaturas** dos 3 documentos anexados (toque para preview maior).
- Valor total a reembolsar (estimativa).
- Conta bancária resumida (`Itaú · final ●●●●4567`), com link *Trocar*.
- Cada bloco tem um lápis ✎ que leva ao ponto exato para editar, **sem perder os outros dados**.

**Heurísticas corrigidas:** H6 (reconhecimento via miniaturas), H3 (controle/edição direcionada), H1 (visibilidade do conjunto).

---

### Etapa 6 · Confirmação
**Substitui:** etapa 18 do fluxo atual (sem NPS sobreposto).

- Ícone de sucesso, microcopy clara: **"Solicitação enviada. Em até 5 dias úteis você verá o status atualizado aqui."** (sem o "se estiver tudo certo").
- **Número de protocolo** + botão *Copiar*.
- 4 ações:
  - *Acompanhar status* (CTA primário)
  - *Adicionar mais uma sessão* (smart cross-sell, usa os dados já cadastrados, 3 toques)
  - *Compartilhar protocolo*
  - *Voltar ao início* (secundária)
- NPS é **enviado por push 24–48h depois**, fora do fluxo de transação.

**Heurísticas corrigidas:** H1 (status claro), H3 (múltiplas saídas), H8 (sem modais sobrepostos), H7 (atalho “Adicionar mais uma”).

---

## Comparativo · atual × proposto

| Indicador | Fluxo atual | Novo fluxo |
|---|---|---|
| Etapas com input ativo | ~12 | 5 (+1 onboarding único) |
| Telas até envio | 30+ | ~10 |
| Digitação manual de CPF/CRP/valor | Sim | Não (OCR) |
| Stepper de progresso | Não | Sim, persistente |
| Validação de datas | Pós-preenchimento | Inline |
| Mensagens de erro prescritivas | Não | Sim |
| Atalho para usuário recorrente | Não | *Refazer última* + *Adicionar mais uma* |
| Modais sobrepostos | 3 (cross-sell, doc, NPS) | 0 durante a tarefa |
| Saída do app durante o fluxo | Sim (gov.br) | Não (tutorial guiado embutido) |
| Biometria | Final do fluxo | Aproveitada do login (Face ID) |

## O que foi mantido (compliance e regras de negócio)

- Termo de Ciência e Responsabilidade (reformulado, ainda **assinado**).
- Confirmação dos dados bancários (no onboarding).
- Validação de identidade (delegada à autenticação do app via biometria do dispositivo, com fallback selfie no primeiro acesso).
- Upload obrigatório dos 3 documentos.
- Lista completa de campos legais necessários (CRP, CPF/CNPJ do prestador, datas, valor), **mas extraídos por OCR** em vez de digitados.

---

**Resultado esperado:** o redesign mantém 100% dos requisitos de compliance (não remove etapas obrigatórias, mantém upload, foco mobile), mas reduz erros previsíveis, abandono e tempo até envio, atacando especificamente as heurísticas com severidade **crítica** (H5 e H9) e as **altas** (H1, H2, H3, H6, H7, H10).
