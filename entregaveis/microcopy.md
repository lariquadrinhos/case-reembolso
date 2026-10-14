# Microcopy · telas-chave do redesign

**Princípios de voz e tom**

- Clareza acima de simpatia: linguagem cidadã, frases curtas, verbos no imperativo direto.
- Sem juridiquês, sem jargão (`SR`, `prévia`, `prestador`, `desidiosa` proibidos).
- Mensagens de erro: dizem **o que aconteceu**, **por quê** e **o que fazer agora**.
- Sem hedge (`se`, `talvez`) na confirmação final.
- Não usar caixa alta nem reticências em CTAs.
- **Sem travessão (`—`)**, em nenhum texto do projeto: microcopy, documentos, textos dentro do Figma e do FigJam. No lugar dele entra a pontuação que a frase pede: dois-pontos quando o que vem depois explica o que veio antes, vírgula em aposto, ponto e vírgula entre orações independentes, ponto final quando são duas frases, parênteses em inciso. Apagar o travessão sem reescrever quebra a frase, então a troca é sempre uma reescrita. Meia-risca em intervalo numérico (`24–48h`) não é travessão e continua valendo, e o separador de rótulo nos nomes de tela e de camada é `·`.

---

## Tela 1 · Início da solicitação

### Título da tela
**Pedir reembolso**

### Stepper
**Passo 1 de 5 · Categoria**

### Instrução principal
**Qual procedimento você fez?**
*Selecione para começar.*

### Labels e elementos

| Elemento | Texto |
|---|---|
| Section "Mais usadas" | **Suas mais usadas** |
| Microcopy do card recorrente | última: 28/04/2026 |
| Section outras categorias | **Outras categorias** |
| Card 1 | Sessão Psicologia |
| Card 2 | Consulta médica |
| Card 3 | Fisioterapia |
| Card 4 | Exames e outras terapias |
| Card 5 | Procedimentos hospitalares |
| Card 6 | Procedimentos no exterior |
| Card 7 | Nutrição |
| Atalho secundário | ↻ Refazer última solicitação |
| Ícone de ajuda no header | Ajuda sobre reembolso |

### Mensagens de erro

| Situação | Texto |
|---|---|
| Sem conexão de rede | **Sem internet.** Conecte-se para ver as categorias. *[Tentar novamente]* |
| Categorias não carregadas | **Não conseguimos carregar agora.** Tente em alguns segundos. *[Tentar novamente]* |
| Usuário sem cobertura para reembolso | **Seu plano não inclui reembolso.** Veja sua cobertura ou fale com a gente. *[Ver cobertura]* |

### Mensagens auxiliares
- Banner topo (apenas em caso de manutenção): **Manutenção programada hoje, 22h às 23h. O envio pode demorar.**
- Tooltip ⓘ no header: **Reembolso é o valor que você recebe de volta após pagar uma consulta ou exame por conta própria.**

---

## Tela 4 · Upload de documentos

### Título da tela
**Documentos**

### Stepper
**Passo 4 de 5 · Documentos**

### Instrução principal
**Anexe os 3 documentos**
*Aceitamos PDF, JPG ou PNG, até 10 MB cada.*

### Labels dos slots

| Slot | Label primário | Microcopy explicativa |
|---|---|---|
| 1 | **Nota fiscal ou recibo** | Documento com os dados do prestador, sua data de emissão e o valor pago. |
| 2 | **Pedido médico** | Documento com nome do paciente, assinatura do profissional e diagnóstico (CID). |
| 3 | **Comprovante de pagamento** | Recibo do IRPF (gov.br/Meu IRPF) ou comprovante de PIX/cartão. |

### Card de Reembolso na home

| Elemento | Texto | Quando aparece |
|---|---|---|
| Link no pé do card | **Ver todas as solicitações** | Só com histórico. Leva à Tela 8 |

Ele fica **abaixo** do CTA *Pedir reembolso*, não junto das linhas de pendência:
rascunho e solicitação em análise pedem ação, histórico é consulta.

### Botões de cada slot

| Estado | Ação principal | Ação secundária |
|---|---|---|
| Vazio | **Anexar** | **Ver exemplo** |
| Preenchido | **Trocar** | **Ver** |
| Comprovante de pagamento, vazio | **Anexar** | **Como obter o recibo do IRPF** *(abre tutorial gov.br)* e **Ver exemplo**, nessa ordem |

O slot 3 é o único com **duas ações secundárias**, e a ordem é a prioridade: quem chega
aqui normalmente ainda não tem o documento, então *como obter* vem antes de *como ele
deve ser*. As duas não cabem na mesma linha do card, e é a segunda que desce.

### Status do conjunto

| Situação | Texto |
|---|---|
| Nenhum anexado | Faltam 3 documentos para enviar. |
| 1 anexado | Restam 2 documentos: pedido médico e comprovante. |
| 2 anexados | Falta o **{nome do documento pendente}**. |
| 3 anexados | Tudo pronto para a próxima etapa. |

### CTA principal

| Estado | Texto | Ação extra |
|---|---|---|
| Habilitado | **Avançar** | Nenhuma |
| Desabilitado | **Avançar** *(cinza)* | Tooltip: *Falta anexar: {nome do documento}* |

### Mensagens de erro

| Situação | Texto |
|---|---|
| Arquivo > 10 MB | **Arquivo muito grande.** Reduza para até 10 MB ou tire uma foto com qualidade média. *[Tentar outro]* |
| Formato inválido | **Formato não aceito.** Use PDF, JPG ou PNG. *[Tentar outro]* |
| Falha de upload | **Não conseguimos enviar.** Verifique a conexão e tente de novo. *[Tentar novamente]* |
| Imagem ilegível detectada (OCR) | **Não conseguimos ler esse documento.** Tire uma foto com mais luz ou anexe um PDF claro. *[Trocar arquivo]* |
| Arquivo duplicado | **Esse arquivo já está em outro slot.** Anexe o documento certo para esta etapa. *[Escolher outro]* |

### Exemplos de documento (texto da bottom sheet · Sheet B)

O layout é o mesmo para os três slots; o que muda é o título e a checklist. Abre pelo link *Ver exemplo*.

**Slot 1 · Nota fiscal ou recibo**
Título: **Exemplo: nota fiscal ou recibo** · Subtítulo: *Veja como o documento deve ser.*
O documento precisa ter:
- Nome e CNPJ ou CPF do prestador.
- Data do atendimento e data de emissão.
- Valor pago, por extenso ou em número.
- Descrição do procedimento realizado.
- Assinatura ou carimbo do prestador.

**Slot 2 · Pedido médico**
Título: **Exemplo: pedido médico** · Subtítulo: *Veja como o documento deve ser.*
O documento precisa ter:
- Nome do paciente.
- Assinatura do profissional.
- CID (código do diagnóstico).
- Carimbo ou CRP/CRM.

**Slot 3 · Comprovante de pagamento**
Título: **Exemplo: comprovante de pagamento** · Subtítulo: *Veja como o documento deve ser.*
O documento precisa ter:
- Nome de quem pagou (precisa ser o titular ou o beneficiário).
- Valor e data do pagamento.
- Identificação de quem recebeu.
- Forma de pagamento (PIX, cartão, transferência).

CTA da sheet: **Entendi, anexar agora**

> As três checklists precisam ser homologadas pela área de regulação de reembolso antes de ir para produção: são elas que definem o que o analista aceita, e uma checklist otimista gera exatamente o retrabalho que o redesign tenta eliminar.

### Tutorial gov.br (texto da bottom sheet)
**Como baixar o recibo do IRPF**
1. **Abra o Meu IRPF** no app gov.br.
2. **Faça login** com sua conta gov.br.
3. **Toque em ‘Recibo Médico’** no perfil do paciente.
4. **Baixe o PDF** e volte aqui para anexar.

CTA da sheet: **Abrir gov.br** *(link externo)* / **Já tenho o arquivo**

---

## Tela 5 · Revisão dos dados

### Título da tela
**Revisão final**

### Stepper
**Passo 5 de 5 · Revisão**

### Instrução principal
**Confira tudo antes de enviar**
*Toque em ✎ para editar uma seção sem perder o resto.*

### Labels das seções

| Seção | Label | Conteúdo de exemplo |
|---|---|---|
| Beneficiário | **Beneficiário** | Rafael A. C. Moreira |
| Prestador | **Prestador** | Dra. Maria Silva (CRP 06/54321) |
| Procedimento | **Procedimento** | Sessão Psicologia · 4 sessões |
| Datas | (sub-bloco do procedimento) | 05, 12, 19 e 26/02/2026 |
| Valor | (sub-bloco do procedimento) | R$ 600,00 por sessão · Total: R$ 2.400,00 |
| Documentos | **Documentos anexados (3)** | (miniaturas) |
| Conta bancária | **Conta para depósito** | Itaú · ag. 00123 · final ●●●●4567 |

### Banner de estimativa
**Estimativa de reembolso: até R$ 1.680,00.**
*Valor sujeito a análise. Você verá o valor final no acompanhamento.*

### CTAs

| Posição | Texto | Estado |
|---|---|---|
| Sticky primário | **Enviar solicitação** | habilitado |
| Sticky secundário | **Salvar como rascunho** | sempre disponível |

### Indicador de salvamento
**Salvo automaticamente às 14:09** (em cinza médio, canto superior direito)

### Mensagens de erro

| Situação | Texto |
|---|---|
| Documento corrompido detectado pelo backend | **Um dos documentos não pode ser processado.** Verifique o arquivo de **{nome do documento}** e anexe novamente. *[Editar documentos]* |
| Conta bancária inconsistente (titularidade) | **A conta cadastrada não está em seu nome.** Atualize antes de enviar. *[Atualizar conta]* |
| Valor maior que o limite mensal da cobertura | **Seu plano cobre até {valor} por mês.** O excedente não será reembolsado. *[Continuar mesmo assim] / [Editar valor]* |
| Falha ao enviar | **Não conseguimos enviar agora.** Seus dados estão salvos. Tente em alguns minutos. *[Tentar novamente]* |
| Usuário tenta enviar com seção pendente | **Antes de enviar, complete a seção {nome}.** *[Ir para {nome}]* |

---

## Tela 6 · Confirmação de envio

### Título da tela
**Reembolso**

### Mensagem de confirmação principal (substitui o atual *“Agora é só esperar :)”* + *“se estiver tudo certo…”*)
**Solicitação enviada.**
**Em até 5 dias úteis você verá o status atualizado aqui.**

### Card de protocolo

| Elemento | Texto |
|---|---|
| Label | **Protocolo** |
| Valor | 1234.5678.9012.3456.7890 |
| Botão | **Copiar** |
| Botão depois de copiar | **✓ Copiado**, permanece assim na sessão |
| Toast após copiar | **Protocolo copiado.** Some em ~2s |

### Seção "O que acontece agora"
**O que acontece agora**
1. **Análise dos documentos**: em até 3 dias úteis.
2. **Confirmação**: você recebe push e e-mail quando aprovado.
3. **Pagamento**: depositado na conta {Itaú · final ●●●●4567} em até 30 dias.

### Botões de ação

| Posição | Texto | Comportamento |
|---|---|---|
| Primário | **Acompanhar status** | Abre detalhe da SR com timeline |
| Secundário | **Adicionar mais uma sessão** | Reabre fluxo Etapa 2 com dados pré-preenchidos |
| Terciário | **Compartilhar protocolo** | Abre share sheet nativo |
| Link discreto | Voltar ao início | Volta para a home |

### Texto pré-preenchido para compartilhamento
**Protocolo SulAmérica:** 1234.5678.9012.3456.7890
**Enviado em:** 05/05/2026
**Tipo:** Sessão de Psicologia (4 sessões)

### Push de NPS (24–48h depois, fora do fluxo)
**Como foi pedir reembolso pelo app?**
*Sua nota nos ajuda a melhorar.*
CTAs: 1 · 2 · 3 · 4 · 5 · *“Avaliar depois”*

### Mensagens auxiliares

| Situação | Texto |
|---|---|
| Erro 500 no servidor (último passo) | **Não foi possível concluir o envio.** Sua solicitação está salva como rascunho. Tente novamente em alguns minutos. *[Tentar enviar]* |
| Solicitação duplicada detectada | **Já existe uma solicitação parecida (Protocolo {n}) enviada hoje.** *[Ver solicitação]* / *[Enviar mesmo assim]* |

---

## Ajuda desta etapa (bottom sheet do `?` no header · Sheet G)

O `?` do header abre as dúvidas **da etapa em que o usuário está**, não um FAQ geral. Abaixo, a versão da etapa de documentos, a que está desenhada no wireframe.

| Elemento | Texto |
|---|---|
| Título | **Ajuda · Documentos** |
| Subtítulo | As dúvidas mais comuns desta etapa. |
| Pergunta 1 (aberta) | **Posso enviar foto do documento?** |
| Resposta 1 | Pode. A foto precisa estar legível, sem corte e sem reflexo. PDF também vale. |
| Pergunta 2 | **E se eu perdi a nota fiscal?** |
| Pergunta 3 | **Preciso do pedido médico sempre?** |
| Pergunta 4 | **Quanto tempo leva a análise?** |
| CTA | **Falar com atendimento** |
| Saída | **Fechar** |

## Glossário rápido (para `(?)` inline, ao lado de termos específicos)

Diferente do `?` do header: este aparece colado a um termo e explica **aquela palavra**, não a etapa.

| Termo | Tooltip / definição |
|---|---|
| Reembolso | Valor que você recebe de volta após pagar uma consulta ou exame por conta própria. |
| Prestador | Profissional ou clínica que fez o atendimento (psicólogo, médico, fisioterapeuta…). |
| CRP/CRM | Registro do profissional. **A gente lê pelo recibo automaticamente**, você não precisa decorar. |
| CID | Código que identifica o motivo do atendimento. Costuma estar no pedido médico. |
| Recibo do IRPF | Comprovante oficial de pagamento de saúde, baixado no gov.br/Meu IRPF. |
| Protocolo | Número da sua solicitação. Use para acompanhar ou falar com a gente. |
| Cobertura | Quanto seu plano paga de reembolso por mês ou por procedimento. |
