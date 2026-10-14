#!/usr/bin/env bash
# Reexporta os PNGs dos wireframes direto da API do Figma.
#
#   export FIGMA_TOKEN=figd_xxx     # figma.com > Settings > Security > Personal access tokens
#   ./exportar.sh                   # escala 2 (padrão)
#   ./exportar.sh 3                 # outra escala
#
# Lê frames.tsv (nodeId <TAB> nome-do-arquivo <TAB> nome do frame no Figma).
# O quadro completo (00) sai em escala 0.5, porque em 2x passaria de 100 MB.

set -euo pipefail
cd "$(dirname "$0")"

FILE_KEY=LUp4aT7fVYH4cD8ZwrHIfd
SCALE="${1:-2}"

[ -n "${FIGMA_TOKEN:-}" ] || { echo "Defina FIGMA_TOKEN primeiro." >&2; exit 1; }
command -v jq >/dev/null || { echo "Precisa do jq: brew install jq" >&2; exit 1; }

baixa() {           # $1 = escala, $2... = nodeIds
  local escala="$1"; shift
  local ids; ids=$(IFS=,; echo "$*")
  local resp
  resp=$(curl -sf -H "X-Figma-Token: $FIGMA_TOKEN" \
    "https://api.figma.com/v1/images/$FILE_KEY?ids=$ids&format=png&scale=$escala")

  local err; err=$(jq -r '.err // empty' <<<"$resp")
  [ -z "$err" ] || { echo "Figma respondeu: $err" >&2; exit 1; }

  while IFS=$'\t' read -r id url; do
    local nome
    nome=$(awk -F'\t' -v i="$id" '$1==i{print $2}' frames.tsv)
    [ -n "$nome" ] || continue
    [ "$url" != "null" ] || { echo "sem URL: $nome"; continue; }
    curl -sfL -o "$nome.png" "$url" && echo "ok  $nome.png"
  done < <(jq -r '.images | to_entries[] | [.key, .value] | @tsv' <<<"$resp")
}

# telas, na escala pedida; quadro completo à parte, reduzido
telas=()
while IFS= read -r id; do telas+=("$id"); done \
  < <(awk -F'\t' '$1!="33:5"{print $1}' frames.tsv)
baixa "$SCALE" "${telas[@]}"
# o quadro inteiro; se a API recusar renderizar uma página, segue sem ele
baixa 0.5 33:5 || echo "aviso: não consegui renderizar o quadro completo (00); as telas acima estão ok" >&2

echo "pronto: $(ls -1 ./*.png | wc -l | tr -d ' ') arquivos"
