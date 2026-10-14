# Fluxo atual · Solicitação de Reembolso (App SulAmérica)

**Categoria mapeada:** Sessão de Psicologia ou Psiquiatria (4 sessões)
**Base:** 32 screenshots de um fluxo real, capturados tela a tela
**Referência cruzada:** `heuristic-evaluation.md` (avaliação de Nielsen)

> Cada etapa lista (a) o que o usuário faz e (b) qual heurística é violada; entre parênteses estão o número da heurística e a severidade detectada na avaliação.

---

## 1. Entrada · Home do app
**Telas:** `home.png`

**O que o usuário faz:** Abre o app, vê “Olá, Rafael” e o carrossel “Mais acessados”. Identifica o ícone *Reembolso* e toca.

**Problemas heurísticos:**
- O carrossel mistura função (Reembolso), burocracia (Imposto de renda) e produto (Cobertura do plano), sem hierarquia clara: **H8 Estética e minimalismo (média)**.
- Ícones genéricos sem rótulo de status (ex.: “Você tem 1 reembolso em análise”): **H1 Visibilidade do status (alta)**.

---

## 2. Loading silencioso
**Telas:** `4.png`

**O que o usuário faz:** Aguarda o app carregar a área de Reembolso. Vê uma tela cinza inteira com um indicador minúsculo (parece um simples parêntese laranja), sem mensagem.

**Problemas heurísticos:**
- Spinner imperceptível, sem texto, sem fallback: **H1 Visibilidade do status (alta)**.
- Se travar, não há botão *Tentar novamente*: **H9 Recuperação de erros (crítica)**.

---

## 3. Menu Reembolso (3 caminhos paralelos)
**Telas:** `5.png`

**O que o usuário faz:** Vê três opções: *Histórico de solicitações*, *Prévia de reembolso*, *Reembolso digital*. Precisa interpretar a diferença entre “Prévia” (estimativa) e “Reembolso digital” (solicitação real).

**Problemas heurísticos:**
- Termo “Prévia de reembolso” é jargão (orçamento? simulação?): **H2 Sistema × mundo real (alta)**.
- Sem atalho para usuário recorrente (“Refazer última solicitação”): **H7 Flexibilidade (alta)**.

---

## 4. Histórico (visão paralela, opcional)
**Telas:** `6.png`

**O que o usuário faz:** Caso entre no histórico, vê SR (`SR 1234567890`), valor, categoria e status, quase sempre `Reembolso pago`.

**Problemas heurísticos:**
- Sigla `SR` sem explicação: **H2 (alta)**.
- Status binário: não há estados intermediários (`Em análise`, `Aguardando documento`): **H1 (alta)**.

---

## 5. Prévia · escolha de categoria
**Telas:** `7.png`

**O que o usuário faz:** Escolhe entre 4 categorias (*Consulta Médica, Exames e Terapias, Parto, Procedimento Cirúrgico*).

**Problemas heurísticos:**
- Lista difere da do Reembolso Digital (7 categorias, etapa 9): **H4 Consistência (média)**.
- Psicologia/Psiquiatria não estão aqui, mas estão em outro fluxo: usuário se confunde: **H4 (média)**.

---

## 6. Pop-up de cross-sell de telemedicina
**Telas:** `8.png`

**O que o usuário faz:** É interrompido por modal “Procurando Médico? Conheça o Saúde na Tela” com botões `FECHAR` / `ME LEVE ATÉ LÁ`.

**Problemas heurísticos:**
- Cross-sell intrusivo durante tarefa transacional, sem opção *“Não mostrar mais”*: **H3 Controle e liberdade (alta)**.
- Quebra de foco em fluxo crítico: **H8 Minimalismo (média)**.

---

## 7. Formulário de prévia
**Telas:** `9.png`

**O que o usuário faz:** Preenche Estado, Data, Valor da Consulta para receber estimativa. Lê parágrafo explicativo de 6 linhas.

**Problemas heurísticos:**
- Texto explicativo extenso compete com os campos: **H8 (média)**.
- Sem geolocalização para preencher Estado, sem máscara de moeda: **H7 (alta)**, **H5 Prevenção de erros (crítica)**.

---

## 8. Termo de Ciência e Responsabilidade
**Telas:** `10.png`, `11.png`

**O que o usuário faz:** Lê (ou mais provavelmente apenas role-passa por) duas telas inteiras de juridiquês, marca declaração e toca *Confirmar*. No meio do termo, surge ainda um modal “Documentação necessária”.

**Problemas heurísticos:**
- Linguagem jurídica densa, sem hierarquia: **H2 (alta)**, **H8 (média)**.
- Modal sobre tela com texto cria duas camadas de leitura simultâneas: **H8 (média)**.
- Sem ajuda contextual: **H10 Ajuda (alta)**.

> **Restrição de compliance:** o termo é etapa obrigatória. O problema é a **forma**, não a presença.

---

## 9. Informações bancárias
**Telas:** `12.png`

**O que o usuário faz:** Confere `Banco 341 · Agência 00123-4 · Conta 000000004567`. Toca *Confirmar* (ou *Atualizar dados*).

**Problemas heurísticos:**
- Banco mostrado por código (`341`), não por nome (Itaú): **H2 (alta)**.
- Ausência de validação visível de banco × agência × conta: **H5 (crítica)**.
- Sem reforço da regra “a conta deve estar em nome do titular” como check visual: **H10 (alta)**.

---

## 10. Reembolso Digital · escolha da categoria (segunda lista)
**Telas:** `13.png`

**O que o usuário faz:** Vê 7 opções (*Consulta médica, Fisioterapia, Exames e outras terapias, Procedimentos hospitalares, Procedimentos no exterior, Sessão Psicologia ou Psiquiatria, Nutrição*) e escolhe a sua.

**Problemas heurísticos:**
- Inconsistência com a tela 5: **H4 (média)**.
- Categorias com peso visual idêntico, sem destacar “Mais usadas”: **H8 (média)**, **H7 (alta)**.

---

## 11. Documentação necessária (a tela que lista os anexos)
**Telas:** `14.png`

**O que o usuário faz:** Lê três cards: *Nota fiscal/recibo*, *Pedido médico*, *Comprovante de pagamento*.

**Problemas heurísticos:**
- Sem exemplos visuais (foto-modelo de cada documento): **H6 Reconhecimento (alta)**, **H10 (alta)**.
- A lista aparece **uma vez** e não persiste como checklist no fluxo: **H6 (alta)**.

---

## 12. Dados do procedimento (segurado, valor, tipo)
**Telas:** `15.png`

**O que o usuário faz:** Confirma o segurado, digita o valor da sessão (`R$ 600,00`), seleciona *Psicologia* / *Psiquiatria* / *Terapias multidisciplinares*.

**Problemas heurísticos:**
- Campo *Valor* sem máscara monetária: **H5 (crítica)**.
- Sem reuso do valor da última solicitação: **H7 (alta)**.

---

## 13. Datas do tratamento
**Telas:** `16.png`, `17.png`, `18.png`, `32.png`

**O que o usuário faz:** Seleciona quantas sessões realizou (1–N), depois digita cada data manualmente. Se errar (ex.: data futura `19/06/2026`), recebe erro **só depois** que termina o preenchimento.

**Problemas heurísticos:**
- Validação reativa, não preventiva: **H5 (crítica)**.
- Mensagem de erro confusa: *“O pedido só pode ser feito para procedimentos realizados antes do dia 04/05/2026”* (a data digitada é futura, a regra real é ‘últimos 12 meses’): **H9 (crítica)**.
- Sem atalho “sessões semanais a partir de…”: **H7 (alta)**.

---

## 14. Tipo de documento (Nota fiscal × Recibo)
**Telas:** `19.png`, `20.png`, `21.png`, `33.png`

**O que o usuário faz:** Escolhe entre `Nota fiscal` (CNPJ obrigatório) ou `Recibo` (CPF). Digita CNPJ/CPF e CRP do prestador.

**Problemas heurísticos:**
- Pede `CRP do prestador`, e o usuário leigo não tem isso de cabeça: **H6 (alta)**.
- Sem máscara em CPF/CNPJ: **H5 (crítica)**.
- Botão `Próximo` desabilitado **sem dizer o que falta**: **H9 (crítica)**, **H4 (média)**.

---

## 15. Anexar documentos (3 cards)
**Telas:** `22.png`, `23.png`, `24.png`

**O que o usuário faz:** Toca em cada card (*Nota fiscal/recibo*, *Pedido médico*, *Comprovante de pagamento*), seleciona arquivo da galeria ou tira foto, vê pré-visualização (`VISUALIZE A IMAGEM NESTA ÁREA`), confirma. Repete três vezes.

**Problemas heurísticos:**
- Anexar exige 3 fluxos separados: **H7 (alta)**.
- Sem indicação de formato/tamanho/quantidade aceitos: **H5 (crítica)**.
- *Caps lock* no placeholder e tom robótico: **H4 (média)**, **H2 (alta)**.

---

## 15-A. Saída do app para gov.br
**Telas:** `doc gov.png`

**O que o usuário faz:** Para anexar o recibo do IRPF, **sai do app**, abre o gov.br/ Receita Federal/Meu IRPF, baixa o PDF, volta ao SulAmérica, anexa.

**Problemas heurísticos:**
- Quebra completa de contexto: **H6 (alta)**.
- Sem tutorial guiado: **H10 (alta)**.

---

## 16. Resumo da solicitação
**Telas:** `25.png`

**O que o usuário faz:** Confere beneficiário, valor e contagem de arquivos por categoria (`Arquivos: 1`).

**Problemas heurísticos:**
- Não exibe miniaturas dos documentos, e o usuário não consegue **reconhecer** se anexou o arquivo certo: **H6 (alta)**.
- Sem caminho para editar etapa específica sem refazer tudo: **H3 (alta)**.

---

## 17. Verificação biométrica
**Telas:** `26.png`, `27.png`, `28.png`

**O que o usuário faz:** Lê instruções, tira selfie, aguarda “Validando…”.

**Problemas heurísticos:**
- Biometria só ao **final**, se falha, perde o esforço já feito: **H5 (crítica)**.
- Sem fallback claro de erro: **H9 (crítica)**.

> **Restrição de compliance:** validação de identidade é obrigatória. O problema é o **timing** (deveria ser upfront via Face ID já validado pela autenticação do app).

---

## 18. Confirmação + NPS sobreposto
**Telas:** `29.png`, `30.png`, `31.png`

**O que o usuário faz:** Vê “Agora é só esperar :)” mas, antes da tela carregar, surge modal de NPS (1–5). Após, a tela final mostra protocolo, número da SR e *Voltar ao início*.

**Problemas heurísticos:**
- NPS sobreposto à confirmação: **H1 (alta)**, **H8 (média)**.
- Texto da confirmação usa *“se estiver tudo certo…”*, o que abre dúvida: **H1 (alta)**.
- Único CTA é `Voltar ao início`; sem *Ver detalhes*, *Compartilhar protocolo*, *Adicionar outra sessão*: **H3 (alta)**, **H7 (alta)**.

---

## Resumo do fluxo atual

| Etapas | Tempo estimado | Telas | Heurísticas violadas (severidade dominante) |
|---|---|---|---|
| 18 etapas (~12 com input ativo) | 8–14 minutos | 30+ telas distintas | H5 e H9 (crítica) · H1, H2, H3, H6, H7, H10 (alta) |

**Pontos de abandono mais prováveis** (baseado nas heurísticas com severidade crítica/alta):
1. Etapa 13 (datas): erro só pós-fato + texto confuso → reiniciar fluxo.
2. Etapa 14 (CRP do prestador): usuário não tem o dado.
3. Etapa 15-A (gov.br): quebra de contexto.
4. Etapa 17 (biometria no final): se falha, perde esforço.
