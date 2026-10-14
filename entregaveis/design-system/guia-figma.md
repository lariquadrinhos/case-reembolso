# Guia de construção no Figma

Como montar a biblioteca a partir deste sistema. Cada valor aqui existe em
`fundamentos.md`, `componentes.md` ou `estados.md`, com a marca de origem.

**Nada deste guia introduz valor novo.** Se um número aparecer aqui e não estiver
naqueles documentos, é erro deste arquivo.

## Ordem

A ordem importa: variável não se liga a componente que ainda não existe, e componente
refeito depois de instanciado quebra as instâncias.

1. Variáveis de cor, nos dois modos
2. Variáveis numéricas
3. Text styles
4. Effect styles
5. Ícones
6. Componentes, na ordem da Parte 4
7. Publicar

---

# Parte 1 · Variáveis de cor

Uma coleção, **`Color`**, com **dois modos: `Claro` e `Escuro`**. O modo é o que faz
o modo escuro funcionar sem componente duplicado: a mesma instância troca de paleta
ao mudar o modo do frame.

## 1.1 Primitivas

Grupo `ramp/`, sem exceção e sem atalho. São as rampas publicadas pela SulAmérica,
de 50 a 950, para `gray`, `blue`, `orange`, `green`, `red` e `yellow`. Os valores
estão em `extracao/tokens-site.json`.

**Quatro semânticas declaradas não têm degrau em rampa nenhuma**, verificado em
`extracao/11-rampas.py`: `text-link` e `feedback-informational`, as duas `#1355B4`,
mais `brand-tertiary-1` `#1769E0` e a superfície `on-body-feedback-info` `#DFEAFC`.
Elas viram primitivas próprias, `ramp/link/500`, `ramp/link/100` e
`ramp/tertiary/500`, em vez de serem forçadas no degrau mais próximo, que está a 49
de distância e mudaria a cor.

Todas as outras semânticas caem exatamente sobre um degrau, distância zero. É o que
sustenta a arquitetura de duas camadas: a rampa não é decoração, é de onde a
semântica sai.

Nos dois modos a primitiva tem **o mesmo valor**. Rampa não muda com o tema: quem
muda é a semântica que aponta para ela.

> Não use primitiva direto no componente. Ela existe para a semântica apontar.

## 1.2 Semânticas

Grupo `color/`, cada uma apontando para uma primitiva, com valor diferente por modo:

| Variável | Claro | Escuro |
|---|---|---|
| `color/surface/body` | `ramp/gray/50` | `ramp/gray/950` |
| `color/surface/on-body` | `ramp/gray/100` | `ramp/gray/900` |
| `color/surface/raised` | `ramp/gray/50` | `ramp/gray/800` |
| `color/surface/disabled` | `ramp/gray/200` | `ramp/gray/800` |
| `color/text/primary` | `ramp/gray/800` | `ramp/gray/100` |
| `color/text/secondary` | `ramp/gray/700` | `ramp/gray/400` |
| `color/text/disabled` | `ramp/gray/500` | `ramp/gray/600` |
| `color/text/on-brand` | `ramp/gray/50` | `ramp/gray/50` |
| `color/brand/primary` | `ramp/orange/500` | `ramp/orange/500` |
| `color/brand/primary-pressed` | `ramp/orange/600` | `ramp/orange/600` |
| `color/brand/on-surface` | `ramp/orange/500` | `ramp/orange/400` |
| `color/brand/secondary` | `ramp/blue/600` | `ramp/blue/400` |
| `color/feedback/error` | `ramp/red/500` | `ramp/red/400` |
| `color/feedback/alert` | `ramp/yellow/500` | `ramp/yellow/400` |
| `color/feedback/success` | `ramp/green/500` | `ramp/green/400` |
| `color/feedback/info` | `ramp/link/500` | `ramp/blue/400` |
| `color/text/link` | `ramp/link/500` | `ramp/blue/400` |

**Repare em `brand/primary` e `brand/on-surface`.** São dois tokens porque fazem
coisas diferentes: o primeiro preenche superfície e não muda no escuro, o segundo é
laranja **de texto e ícone** e clareia. Um token só para os dois casos forçaria a
escolher entre botão fraco no escuro e texto vibrando. Ver `estados.md`, 4.3.

## 1.3 Superfícies de feedback

| Variável | Claro | Escuro |
|---|---|---|
| `color/surface/error` | `ramp/red/100` | `ramp/red/950` |
| `color/surface/alert` | `ramp/yellow/100` | `ramp/yellow/950` |
| `color/surface/success` | `ramp/green/100` | `ramp/green/950` |
| `color/surface/info` | `ramp/link/100` | `ramp/blue/950` |

---

# Parte 2 · Variáveis numéricas

Coleção **`Number`**, modo único. Não tem tema: espaçamento não muda com a paleta.

## 2.1 Espaçamento

`space/4` `space/8` `space/12` `space/16` `space/20` `space/24` `space/32`

## 2.2 Raio

| Variável | Valor | Uso |
|---|---|---|
| `radius/sm` | 4 | esqueleto de carregamento |
| `radius/md` | 8 | caixa de status |
| `radius/lg` | 12 | card |
| `radius/sheet` | 16 | topo de bottom sheet |
| `radius/full` | 999 | botão e chip |

**`radius/full` é 999 de propósito.** O botão é pílula, e pílula quer raio igual à
metade da altura. O Figma corta o raio na metade da menor dimensão, então um número
grande produz a pílula em qualquer altura, e o componente continua correto se a
altura mudar. Raio fixo de 24 quebraria isso.

## 2.3 Tamanho

| Variável | Valor |
|---|---|
| `size/tap-target` | 44 |
| `size/button-height` | 48 |
| `size/row-height` | 58 |
| `size/nav-height` | 44 |
| `size/field-height` | 48 |
| `size/icon` | 24 |

## 2.4 Traço

`stroke/hairline` = 1 · `stroke/emphasis` = 2

---

# Parte 3 · Text styles

Família **Figtree** em todos. Confirmada por sobreposição de forma contra dez
candidatas, ver `fundamentos.md`, 2.1.

| Style | Corpo | Peso | Entrelinha |
|---|---|---|---|
| `Title/Screen` | 20 | Bold | 130% |
| `Title/Section` | 20 | Bold | 130% |
| `Title/Nav` | 16 | Semibold | 130% |
| `Body` | 16 | Regular | 145% |
| `Body/Emphasis` | 16 | Semibold | 145% |
| `Button` | 16 | Semibold | 100% |
| `Caption` | 14 | Regular | 140% |
| `Label` | 12 | Medium | 130% |

`Title/Screen` e `Title/Section` têm o mesmo valor hoje. Ficam separados porque
respondem a perguntas diferentes e vão divergir quando aparecer uma tela que precise
dos dois na mesma vista. Fundi-los agora obrigaria a desfazer depois em cada
instância.

> **`Button` não desce de 16.** A medição do app deu 15,4, mas branco sobre laranja
> dá 3,54:1, que só passa em AA como texto grande. Em 16 Semibold ele entra nessa
> regra. Ver `fundamentos.md`, 1.6.

---

# Parte 4 · Effect styles

| Style | Valor | Uso |
|---|---|---|
| `elevation/raised` | `0 2 8`, preto 12% | modal, sheet |
| `scrim/modal` | preenchimento preto a 40% | véu atrás de modal |

**Não crie sombra de card.** O sistema separa card do fundo por superfície tonal.
Ver `estados.md` e a medição que mostrou a sombra atual variando 3 em 255.

---

# Parte 5 · Componentes

Ordem de construção. Cada um só depende dos anteriores.

## 5.1 Button

Um component set. Propriedades:

| Propriedade | Tipo | Valores |
|---|---|---|
| `Hierarquia` | variante | `Primário`, `Secundário`, `Texto` |
| `Estado` | variante | `Ativo`, `Pressionado`, `Desabilitado`, `Carregando` |
| `Rótulo` | texto | |
| `Ícone` | booleano | |

Base: auto layout horizontal, altura fixa `size/button-height`, largura preenchendo,
alinhamento central, raio `radius/full`, texto `Button`.

| Hierarquia e estado | Preenchimento | Rótulo | Contorno |
|---|---|---|---|
| Primário · Ativo | `brand/primary` | `text/on-brand` | nenhum |
| Primário · Pressionado | `brand/primary-pressed` | `text/on-brand` | nenhum |
| Primário · Desabilitado | `surface/disabled` | `text/disabled` | nenhum |
| Secundário · Ativo | nenhum | `brand/on-surface` | 1,5 `brand/primary` |
| Texto · Ativo | nenhum | `brand/on-surface` sublinhado | nenhum |

`Carregando` esconde o rótulo e mostra o spinner, **mantendo a largura**. No Figma,
troque a visibilidade em vez de remover a camada: remover encolhe o botão.

## 5.2 Input

| Propriedade | Tipo | Valores |
|---|---|---|
| `Estado` | variante | `Vazio`, `Preenchido`, `Foco`, `Erro`, `Desabilitado`, `Leitura` |
| `Rótulo`, `Valor`, `Mensagem` | texto | |
| `Sufixo` | instance swap | ícone de select ou calendário |

Auto layout vertical, `space/4` entre rótulo e valor. Linha inferior de
`stroke/hairline`, exceto em `Foco` e `Erro`, que usam `stroke/emphasis`.

## 5.3 Card

Dois componentes distintos, e não variantes do mesmo:

**`Card/Row`**: linha de lista, altura mínima `size/row-height`, ícone opcional,
título `Body/Emphasis`, subtítulo `Caption`, chevron. Separador entre linhas.

**`Card/Content`**: bloco, raio `radius/lg`, contorno `stroke/hairline` em
`surface/disabled`, preenchimento interno `space/16`.

São coisas diferentes: uma navega, a outra contém. Juntá-las num component set faria
a troca de variante mudar o significado, não a aparência.

## 5.4 Radio e Checkbox

Propriedades `Estado` (`Marcado`, `Vazio`, `Desabilitado`) e `Rótulo`.
Linha inteira com altura mínima `size/tap-target`, e o alvo é a linha, não a marca.

## 5.5 Chip

`Estado`: `Disponível`, `Aplicado`, `Removível`, `Desabilitado`.
Altura `size/tap-target`, raio `radius/full`.
Aplicado usa **preenchimento**, não contorno colorido. Ver `estados.md`, 3.2.

## 5.6 Nav bar

Altura `size/nav-height`, sem padding vertical. Voltar e ação à direita em frames de
`size/tap-target` quadrados. Título centralizado em `Title/Nav`.

## 5.7 Linha de anexo

Ícone `size/icon` **solto**, sem círculo de fundo. Título `Body/Emphasis`, estado
`Caption`, duas ações `Button/Texto` com alvo próprio.

## 5.8 Stepper

Variantes `Passo = 1 a 5`. Rótulo em `Label`, trilho de 4pt em `border/subtle`,
preenchimento em `brand/primary` proporcional ao passo.

**Construa cedo.** Está em 31 das 44 telas, mais que qualquer outro componente
depois da barra de navegação.

## 5.9 Banner

Variantes `Tipo = Info, Alerta, Erro, Sucesso`. Superfície tonal mais glifo, nunca
cor sozinha.

## 5.10 Rodapé fixo

Banner de estado acima do CTA, sombra superior `0 -2 8` a 6%. Os dois no mesmo
contêiner, porque a pendência e a ação que ela trava não podem se separar.

**Montagem na tela.** O rodapé é o último filho do frame de 844, irmão de um
`Conteúdo rolável` com altura fixa e `overflow: vertical`. Não use posição absoluta
com o rodapé por cima: absoluto em auto layout não é o mesmo que fixo na rolagem, e
a propriedade que faria isso (`scrollBehavior`) não está exposta na API de plugin.
A soma dos três blocos precisa fechar exatamente 844.

## 5.11 Bottom sheet

Pega de 36 × 5, `radius/sheet` só no topo, superfície `surface/raised`.

## 5.12 Toast, Skeleton, Tab bar, Timeline e Linha de revisão

Os cinco fecham a cobertura dos padrões que aparecem nas telas. Especificação em
`componentes.md`, seções 21 a 25.

---

# Parte 6 · Ícones

Não havia biblioteca a herdar: as capturas mostram os ícones do app, mas raster não
vira vetor confiável, e nenhum deles podia ser extraído. Foram desenhados do zero.

**36 ícones**, num único conjunto de variantes `Icon`, com propriedade `Nome`:

`chevron-right` `chevron-left` `close` `check` `plus` `camera` `paperclip`
`keyboard` `bell` `map-pin` `video` `doc-check` `shield` `gallery` `home` `grid`
`help` `search` `calendar` `document` `clock` `alert` `info` `share` `download`
`refresh` `edit` `flash` `list` `stethoscope` `activity` `flask` `hospital`
`globe` `apple` `brain`

Os sete últimos vieram das categorias de procedimento da Tela 1, que precisavam de
ícones distintos entre si: uma lista de sete itens com o mesmo ícone genérico não
ajuda ninguém a achar o seu.

Família outline, traço 1,5pt, caixa de `size/icon`. **A cor nunca entra no vetor**,
só por variável, e é isso que faz o conjunto inteiro virar no modo escuro junto com
o resto do sistema.

Regra que vem da medição: **ícone não vai dentro de círculo colorido**. O app faz
isso em dois lugares e em nenhum outro, e é o que faz esses dois destoarem.

---

# Parte 7 · Checklist antes de publicar

- [ ] Nenhuma cor solta: toda cor é variável semântica, nenhuma primitiva aplicada direto
- [ ] Os dois modos trocam sem quebrar nenhum componente
- [ ] Nenhum tamanho de texto fora dos oito text styles
- [ ] Nenhum alvo tocável abaixo de `size/tap-target`
- [ ] Botão em `radius/full`, não em raio fixo
- [ ] Nenhuma sombra em card de lista
- [ ] Contraste conferido nos dois modos com `extracao/10-contraste.py`
- [ ] Todo componente com estado desabilitado e de erro, mesmo os que o app não tem
- [ ] Nenhum padrão recorrente das telas ficou sem componente

O penúltimo item é o que separa esta biblioteca do app atual. As 32 capturas não
mostram esses estados, e é justamente por isso que eles precisam existir na
biblioteca: o que não está no sistema é improvisado na tela.

O último se confere contando. Liste os padrões que se repetem nas telas, conte em
quantas cada um aparece e compare com a biblioteca. Foi assim que o Stepper apareceu
como buraco: estava em 31 telas e em nenhum componente.

---

# Parte 8 · Estrutura do arquivo

```
Página  Foundations     variáveis, text styles, effect styles, amostras
Página  Icons           a biblioteca, em grade
Página  Components      um component set por seção da Parte 5
Página  Patterns        composições recorrentes: formulário, lista, modal
Página  Sandbox         rascunho, nunca publicado
```

`Sandbox` fora da publicação: componente de teste que vaza para a biblioteca aparece
no menu de quem consome e ninguém sabe se pode usar.
