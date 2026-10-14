# Wireframes exportados

PNGs em **@2x** dos 44 frames da página `wireframes`, para consultar a fidelidade visual sem chamar a API do Figma a cada vez. Cada tela sai em 780 × 1688px; `00-quadro-completo.png` é o quadro inteiro em escala 0,5, com as notas de design.

Os PNGs das telas saem **sem** as notas: cada frame é exportado sozinho, e os post-its são nós irmãos no quadro.

## `composicoes/`: tela + nota

37 PNGs de **1000 × 2520**, cada um com a tela e o post-it de **Notas de Design** dela, sobre o mesmo fundo escuro do quadro. Tamanho único e topo alinhado, para as telas ficarem na mesma posição ao passar de um slide para o outro.

As 7 telas sem nota não entram aqui. O PNG solto delas está na pasta de cima.

```sh
export FIGMA_TOKEN=figd_xxx
python3 compor.py            # precisa de Pillow: pip install pillow
```

O script busca as posições na API, renderiza cada tela e cada nota como nós separados e monta as duas respeitando o respiro que elas têm no quadro. Se alguma nota crescer a ponto de não caber, ele avisa qual e qual tamanho seria preciso, em vez de cortar em silêncio.

**Fonte da verdade continua sendo o Figma.** Estes arquivos são um retrato datado. Se o quadro mudar, rode `./exportar.sh` de novo.

As mesmas 44 telas com o design system aplicado estão em [`../mockups/`](../mockups/), com os mesmos nomes de arquivo: `01-o0-home.png` existe nas duas pastas.

[Abrir no Figma →](https://www.figma.com/design/LUp4aT7fVYH4cD8ZwrHIfd/Reembolso-SulAmerica?node-id=33-5)

## Como reexportar

```sh
export FIGMA_TOKEN=figd_xxx   # figma.com > Settings > Security > Personal access tokens
./exportar.sh                 # escala 2 (padrão); ./exportar.sh 3 para 3x
```

Precisa de `jq`. O script lê `frames.tsv`, que mapeia `nodeId → arquivo → nome do frame`; para incluir uma tela nova, acrescente uma linha lá e rode de novo.

## Índice

| # | Arquivo | Frame no Figma | Node |
|---|---|---|---|
| 00 | `00-quadro-completo.png` | Página wireframes (quadro inteiro) | `33:5` |
| 01 | `01-o0-home.png` | Tela O.0 · Home (ponto de entrada) | `112:2` |
| 02 | `02-o1-boas-vindas.png` | Tela O.1 · Boas-vindas ao Reembolso | `112:56` |
| 03 | `03-o2a-confirma-conta.png` | Tela O.2a · Confirmação dos dados bancários | `113:2` |
| 04 | `04-o2b-cadastra-conta.png` | Tela O.2b · Cadastro dos dados bancários | `142:2` |
| 05 | `05-o3-termo.png` | Tela O.3 · Termo de Ciência | `113:50` |
| 06 | `06-o4a-face-id.png` | Tela O.4a · Identidade (Face ID) | `115:2` |
| 07 | `07-o4b-selfie.png` | Tela O.4b · Identidade (selfie · fallback) | `115:30` |
| 08 | `08-o5-onboarding-concluido.png` | Tela O.5 · Onboarding concluído | `115:63` |
| 09 | `09-tela1-inicio.png` | Tela 1 · Início da solicitação | `85:2` |
| 10 | `10-tela2-captura.png` | Tela 2 · Captura da nota fiscal | `97:2` |
| 11 | `11-tela2a-ocr.png` | Tela 2A · Conferência dos campos (OCR) | `110:2` |
| 12 | `12-tela3-tratamento.png` | Tela 3 · Detalhes do tratamento | `111:5` |
| 13 | `13-tela4-documentos.png` | Tela 4 · Upload de documentos | `90:2` |
| 14 | `14-tela5-revisao.png` | Tela 5 · Revisão dos dados | `92:2` |
| 15 | `15-tela6-confirmacao.png` | Tela 6 · Confirmação de envio | `92:69` |
| 16 | `16-tela7-status.png` | Tela 7 · Acompanhar status | `116:2` |
| 17 | `17-tela8-historico.png` | Tela 8 · Histórico de solicitações | `116:62` |
| 18 | `18-sheetA-tutorial-govbr.png` | Sheet A · Tutorial gov.br | `138:2` |
| 19 | `19-sheetB-exemplo-pedido-medico.png` | Sheet B · Exemplo · pedido médico | `138:85` |
| 20 | `20-sheetB-exemplo-nota-fiscal.png` | Sheet B · Exemplo · nota fiscal | `187:2` |
| 21 | `21-sheetB-exemplo-comprovante.png` | Sheet B · Exemplo · comprovante | `187:91` |
| 22 | `22-sheetC-editar-conta.png` | Sheet C · Editar conta bancária | `138:170` |
| 23 | `23-overlay-visualizador.png` | Overlay · Visualizador de documento | `185:2` |
| 24 | `24-estado-home-primeiro-acesso.png` | Estado · Home no primeiro acesso | `125:67` |
| 25 | `25-estado-tela1-sem-historico.png` | Estado · Primeiro acesso (Tela 1 sem histórico) | `125:2` |
| 26 | `26-estado-loading-skeleton.png` | Estado · Loading com skeleton | `118:2` |
| 27 | `27-estado-empty-state.png` | Estado · Empty state (sem histórico) | `118:47` |
| 28 | `28-estado-erro-de-rede.png` | Estado · Erro de rede | `118:66` |
| 29 | `29-estado-2-de-3-documentos.png` | Estado · 2 de 3 documentos (Tela 4) | `185:23` |
| 30 | `30-estado-documentos-completos.png` | Estado · Documentos completos (Tela 4) | `182:2` |
| 31 | `31-estado-retomada-rascunho.png` | Estado · Retomada de rascunho (Tela 5) | `186:2` |
| 32 | `32-estado-preenchimento-manual.png` | Estado · Preenchimento manual (Tela 2A vazia) | `186:76` |
| 33 | `33-erro-data-fora-do-prazo.png` | Erro · Data fora do prazo (Tela 3) | `131:2` |
| 34 | `34-erro-campos-alerta-e-erro.png` | Erro · Campos com alerta e erro (Tela 2A) | `131:66` |
| 35 | `35-erro-solicitacao-com-pendencia.png` | Erro · Solicitação com pendência (Tela 7) | `134:2` |
| 36 | `36-tela2-camera.png` | Tela 2 · Câmera (guia de enquadramento) | `135:2` |
| 37 | `37-estado-lendo-nota-fiscal.png` | Estado · Lendo sua nota fiscal | `135:27` |
| 38 | `38-modal-retomar.png` | Modal · Retomar de onde parou? | `134:65` |
| 39 | `39-tela9-detalhe-pago.png` | Tela 9 · Detalhe da solicitação paga | `195:2` |
| 40 | `40-sheetD-filtrar-historico.png` | Sheet D · Filtrar histórico | `196:2` |
| 41 | `41-sheetE-quem-fez-procedimento.png` | Sheet E · Quem fez o procedimento? | `197:2` |
| 42 | `42-sheetF-buscar-banco.png` | Sheet F · Buscar banco | `197:107` |
| 43 | `43-estado-protocolo-copiado.png` | Estado · Protocolo copiado (Tela 6) | `198:2` |
| 44 | `44-sheetG-ajuda-da-etapa.png` | Sheet G · Ajuda desta etapa | `199:2` |
