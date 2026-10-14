# Mockups exportados

PNGs em **@2x** das 44 telas com o design system aplicado. Cada tela sai em 780 × 1688px; `00-quadro-completo.png` é o quadro inteiro reduzido.

**Os nomes de arquivo são os mesmos da pasta `wireframes/`**, de propósito. `01-o0-home.png` existe nas duas, e isso permite abrir a mesma tela lado a lado e ver o que a cor mudou e o que ela não mudou.

**Seis frames da página não estão aqui, de propósito.** A página `mockups` tem 50
frames: estas 44 telas mais seis **telas de apoio do protótipo**, que são versões
alternativas de telas que já estão na lista (`Tela 3 · Detalhes` vazia, `O.2b`
preenchida, `O.3` aceita, `Preenchimento manual` preenchido,
`Estado · Validando identidade` e `Estado · Home após o onboarding`). Elas existem porque protótipo não digita: o toque
num campo precisa levar a uma tela já preenchida. Exportá-las quebraria a paridade
de nomes com `wireframes/`, que é justamente o que torna a comparação possível. Para
vê-las, use o protótipo ou o Figma. A razão de cada uma está em `anotacoes-ux.md`,
seção *Protótipo · primeiro acesso*.

**Fonte da verdade continua sendo o Figma.** Estes arquivos são um retrato datado. Se o quadro mudar, rode `./exportar.sh` de novo.

[Abrir no Figma →](https://www.figma.com/design/LUp4aT7fVYH4cD8ZwrHIfd/Reembolso-SulAmerica?node-id=33-6)

## Como reexportar

```sh
export FIGMA_TOKEN=figd_xxx   # figma.com > Settings > Security > Personal access tokens
./exportar.sh                 # escala 2 (padrão)
```

Precisa de `jq`. O script lê `frames.tsv`, que mapeia `nodeId → arquivo → nome do frame`.

## O que mudou do wireframe para o mockup

| | Wireframe | Mockup |
|---|---|---|
| Paleta | 5 cinzas | 14 cores do sistema |
| Cor | valores soltos | 2.564 ligações a variável, e zero soltas |
| Ícones | quadrados cinza e glifos de texto | 148 instâncias do conjunto `Icon` |
| Anotação | notas de design e indicador de rolagem | nenhuma |

As anotações ficaram só no wireframe de propósito: mockup com nota por cima não serve para julgar a tela.

## Índice

| # | Arquivo | Frame no Figma | Node |
|---|---|---|---|
| 00 | `00-quadro-completo.png` | Página mockups (quadro inteiro) | `33:6` |
| 01 | `01-o0-home.png` | Tela O.0 · Home (ponto de entrada) | `235:2587` |
| 02 | `02-o1-boas-vindas.png` | Tela O.1 · Boas-vindas ao Reembolso | `235:2655` |
| 03 | `03-o2a-confirma-conta.png` | Tela O.2a · Confirmação dos dados bancários | `235:2696` |
| 04 | `04-o2b-cadastra-conta.png` | Tela O.2b · Cadastro dos dados bancários | `235:1561` |
| 05 | `05-o3-termo.png` | Tela O.3 · Termo de Ciência | `235:426` |
| 06 | `06-o4a-face-id.png` | Tela O.4a · Identidade (Face ID) | `235:469` |
| 07 | `07-o4b-selfie.png` | Tela O.4b · Identidade (selfie · fallback) | `235:498` |
| 08 | `08-o5-onboarding-concluido.png` | Tela O.5 · Onboarding concluído | `235:535` |
| 09 | `09-tela1-inicio.png` | Tela 1 · Início da solicitação | `235:2` |
| 10 | `10-tela2-captura.png` | Tela 2 · Captura da nota fiscal | `235:241` |
| 11 | `11-tela2a-ocr.png` | Tela 2A · Conferência dos campos (OCR) | `235:281` |
| 12 | `12-tela3-tratamento.png` | Tela 3 · Detalhes do tratamento | `235:358` |
| 13 | `13-tela4-documentos.png` | Tela 4 · Upload de documentos | `235:63` |
| 14 | `14-tela5-revisao.png` | Tela 5 · Revisão dos dados | `235:122` |
| 15 | `15-tela6-confirmacao.png` | Tela 6 · Confirmação de envio | `235:197` |
| 16 | `16-tela7-status.png` | Tela 7 · Acompanhar status | `235:565` |
| 17 | `17-tela8-historico.png` | Tela 8 · Histórico de solicitações | `235:627` |
| 18 | `18-sheetA-tutorial-govbr.png` | Sheet A · Tutorial gov.br | `235:1284` |
| 19 | `19-sheetB-exemplo-pedido-medico.png` | Sheet B · Exemplo · pedido médico | `235:1370` |
| 20 | `20-sheetB-exemplo-nota-fiscal.png` | Sheet B · Exemplo · nota fiscal | `235:1914` |
| 21 | `21-sheetB-exemplo-comprovante.png` | Sheet B · Exemplo · comprovante | `235:2003` |
| 22 | `22-sheetC-editar-conta.png` | Sheet C · Editar conta bancária | `235:1456` |
| 23 | `23-overlay-visualizador.png` | Overlay · Visualizador de documento | `235:1685` |
| 24 | `24-estado-home-primeiro-acesso.png` | Estado · Home no primeiro acesso | `235:844` |
| 25 | `25-estado-tela1-sem-historico.png` | Estado · Primeiro acesso (Tela 1 sem histórico) | `235:778` |
| 26 | `26-estado-loading-skeleton.png` | Estado · Loading com skeleton | `235:666` |
| 27 | `27-estado-empty-state.png` | Estado · Empty state (sem histórico) | `235:712` |
| 28 | `28-estado-erro-de-rede.png` | Estado · Erro de rede | `235:732` |
| 29 | `29-estado-2-de-3-documentos.png` | Estado · 2 de 3 documentos (Tela 4) | `235:1708` |
| 30 | `30-estado-documentos-completos.png` | Estado · Documentos completos (Tela 4) | `235:1624` |
| 31 | `31-estado-retomada-rascunho.png` | Estado · Retomada de rascunho (Tela 5) | `235:1768` |
| 32 | `32-estado-preenchimento-manual.png` | Estado · Preenchimento manual (Tela 2A vazia) | `235:1847` |
| 33 | `33-erro-data-fora-do-prazo.png` | Erro · Data fora do prazo (Tela 3) | `235:901` |
| 34 | `34-erro-campos-alerta-e-erro.png` | Erro · Campos com alerta e erro (Tela 2A) | `235:971` |
| 35 | `35-erro-solicitacao-com-pendencia.png` | Erro · Solicitação com pendência (Tela 7) | `235:1054` |
| 36 | `36-tela2-camera.png` | Tela 2 · Câmera (guia de enquadramento) | `235:1192` |
| 37 | `37-estado-lendo-nota-fiscal.png` | Estado · Lendo sua nota fiscal | `235:1219` |
| 38 | `38-modal-retomar.png` | Modal · Retomar de onde parou? | `235:1116` |
| 39 | `39-tela9-detalhe-pago.png` | Tela 9 · Detalhe da solicitação paga | `235:2089` |
| 40 | `40-sheetD-filtrar-historico.png` | Sheet D · Filtrar histórico | `235:2149` |
| 41 | `41-sheetE-quem-fez-procedimento.png` | Sheet E · Quem fez o procedimento? | `235:2235` |
| 42 | `42-sheetF-buscar-banco.png` | Sheet F · Buscar banco | `235:2346` |
| 43 | `43-estado-protocolo-copiado.png` | Estado · Protocolo copiado (Tela 6) | `235:2448` |
| 44 | `44-sheetG-ajuda-da-etapa.png` | Sheet G · Ajuda desta etapa | `235:2495` |
