# Acidentes de trânsito em Fortaleza (2015-2024)

Trabalho de ciência de dados sobre os sinistros de trânsito registrados pela AMC em Fortaleza. A ideia é descobrir onde, quando e como os acidentes acontecem.

Base de dados: https://dados.fortaleza.ce.gov.br/dataset/sinistros-transito (cerca de 130 mil registros e 28 colunas)

## Perguntas que o trabalho responde

1. Quais regiões de Fortaleza concentram mais acidentes?
2. Quais horários têm mais acidentes?
3. Quais dias da semana têm mais acidentes?
4. Como os acidentes variam ao longo dos anos?
5. Quais tipos de veículos aparecem mais?
6. As regiões com mais acidentes também têm mais acidentes graves?
7. Que características têm os locais com mais acidentes?

## O que tem em cada pasta

```
notebooks/   os cadernos (arquivos .ipynb) com a análise, em ordem
src/         código que os notebooks usam em comum (caminhos e constantes)
data/raw/    a base baixada do site (NÃO vai pro GitHub)
data/processed/   arquivos gerados pelos notebooks (NÃO vai pro GitHub)
figuras/     gráficos e mapas salvos pelos notebooks
requirements.txt   lista das bibliotecas Python que o projeto usa
```

A pasta `data/` fica de fora do GitHub porque a base é grande. Por isso **cada pessoa baixa a base no próprio computador** (passo 6).

## Os notebooks

Rodam sempre nessa ordem, porque cada um usa o arquivo que o anterior salvou:

| Notebook | O que faz |
|---|---|
| `01_carga_dados` | Lê a base bruta, mostra como ela é e salva uma cópia rápida (parquet) |
| `02_limpeza` | Tira duplicados, arruma data e hora, remove coordenadas erradas, cria colunas novas |
| `03_analise_temporal` | Acidentes por ano, mês, dia da semana e hora |
| `04_veiculos_severidade` | Veículos envolvidos, mortos, feridos, natureza dos acidentes |
| `05_analise_espacial` | Ruas com mais acidentes, mapas de pontos, grade e mapa de calor |
| `06_locais_criticos` | Compara concentração com gravidade e olha as características dos locais críticos |

---

# Passo a passo (do zero)

Feito pensando em Windows. Siga na ordem e não pule nenhum passo.

## Passo 1 - Instalar os programas

Você precisa de 3 programas. Se já tem algum, pule ele.

**Python**
- Baixe em https://www.python.org/downloads/
- Na primeira tela do instalador, marque a caixinha **Add python.exe to PATH** (fica lá embaixo). Se esquecer disso, nada funciona depois.
- Clique em Install Now.
- Para conferir, abra o terminal (passo 2) e digite `python --version`. Tem que aparecer um número, tipo `Python 3.12.4`.

**Git**
- Baixe em https://git-scm.com/downloads
- Instale clicando em Next até o fim. As opções padrão servem.

**VS Code**
- Baixe em https://code.visualstudio.com/
- Instale clicando em Next até o fim.

## Passo 2 - Abrir o terminal

Um terminal é uma tela preta onde você digita comandos. Para abrir:
- Aperte a tecla **Windows**, digite `PowerShell` e aperte Enter.

Dentro do VS Code também tem um: aperte **Ctrl + '** (a aspa simples, abaixo do Esc). A partir do passo 4 é melhor usar o do VS Code.

## Passo 3 - Baixar o projeto do GitHub

No terminal, vá para a Área de Trabalho e baixe o projeto:

```bash
cd Desktop
git clone https://github.com/CaririLeticia/acidente_transito.git
cd acidente_transito
```

Isso cria a pasta `acidente_transito` na sua Área de Trabalho.

Se pedir login do GitHub, entre com a sua conta. Se der erro de permissão, peça pra quem criou o repositório te adicionar como colaborador (Settings > Collaborators).

## Passo 4 - Abrir a pasta no VS Code

1. Abra o VS Code.
2. Clique em **File** > **Open Folder**.
3. Escolha a pasta `acidente_transito` e clique em Selecionar pasta.
4. Se aparecer "Do you trust the authors", clique em **Yes, I trust the authors**.

Para abrir o terminal do VS Code, aperte **Ctrl + '**. Ele já abre dentro da pasta do projeto.

## Passo 5 - Instalar as extensões do VS Code

1. Aperte **Ctrl + Shift + X** (abre as Extensões).
2. Procure `Python` e instale a que tem **Microsoft** embaixo do nome.
3. Procure `Jupyter` e instale a que tem **Microsoft** embaixo do nome.
4. Feche o VS Code e abra de novo na mesma pasta.

## Passo 6 - Criar o ambiente e instalar as bibliotecas

O ambiente (chamado de `.venv`) é uma pasta com as bibliotecas só desse projeto, pra não bagunçar o resto do computador. Você faz isso **uma vez só**.

No terminal do VS Code, rode um comando de cada vez:

```bash
python -m venv .venv
```

```bash
.venv\Scripts\activate
```

Quando der certo, aparece `(.venv)` no começo da linha do terminal.

```bash
pip install -r requirements.txt
```

Esse último demora alguns minutos. É normal. Se aparecer um aviso amarelo falando de "cache" ou de nova versão do pip, pode ignorar.

**Se o `activate` der erro de "execução de scripts desabilitada":** rode isso uma vez e tente de novo:

```bash
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

## Passo 7 - Baixar a base de dados

1. Entre em https://dados.fortaleza.ce.gov.br/dataset/sinistros-transito
2. Baixe os arquivos da base (se tiver um por ano, baixe todos de 2015 a 2024).
3. Coloque dentro da pasta `data/raw/` do projeto.

O notebook 01 lê arquivos `.geojson`, `.shp`, `.gpkg` e `.csv`, e junta tudo se tiver mais de um. Se vier um `.zip`, descompacte antes.

## Passo 8 - Rodar os notebooks

1. No VS Code, na lista de arquivos à esquerda, abra a pasta `notebooks`.
2. Dê dois cliques em `01_carga_dados.ipynb`.
3. No canto de cima à direita, clique em **Select Kernel**.
4. Clique em **Python Environments** e escolha o que tem **.venv** no nome.
   - Se não aparecer: aperte **Ctrl + Shift + P**, digite `Python: Select Interpreter` e escolha o `.venv`.
5. O notebook é feito de células (caixas). Clique numa caixa de código e aperte **Shift + Enter**. Ela roda e pula pra próxima.
6. Faça isso até o fim do notebook. A saída (tabela, gráfico) aparece logo abaixo da célula.
7. Quando terminar, abra o `02_limpeza.ipynb` e repita (escolhe o kernel de novo se pedir). Depois o 03, 04, 05 e 06.

Caixas de texto (markdown) editam com dois cliques. **Shift + Enter** fecha.

Para rodar um notebook inteiro de uma vez, use o botão **Run All** na barra de cima.

---

# Trabalhando em grupo

Todo mundo mexe no mesmo repositório, então precisa de organização para não sobrescrever o trabalho dos outros.

## Regras

- **Ninguém mexe direto na `main`.** Cada pessoa cria uma branch (uma cópia pra trabalhar) e depois junta.
- **Avisem no grupo** quando forem mexer num notebook. Dois mexendo no mesmo `.ipynb` dá conflito e é muito chato de resolver.
- Divisão sugerida: uma pessoa por notebook, ou por pergunta.
- Antes de commitar, use **Clear All Outputs** no notebook (barra de cima). Isso apaga os gráficos salvos dentro do arquivo e deixa o commit pequeno.
  - Os gráficos finais ficam salvos como imagem na pasta `figuras/`, então não perde nada.

## Fluxo de todo dia

**1. Antes de começar, pegar o que os outros fizeram:**

```bash
git checkout main
git pull
```

**2. Criar a sua branch** (troque pelo seu nome e assunto):

```bash
git checkout -b maria/analise-temporal
```

**3. Trabalhar nos notebooks normalmente.**

**4. Salvar o trabalho (commit).** Pelo terminal:

```bash
git add .
git commit -m "adiciona grafico de acidentes por hora"
```

Ou pelo VS Code: clique no ícone de **Source Control** (terceiro da barra da esquerda, ou **Ctrl + Shift + G**), escreva a mensagem na caixa e clique em **Commit**.

A mensagem deve dizer o que mudou, de forma curta: "corrige limpeza de coordenadas", "adiciona mapa de calor". Nada de "atualização" ou "mudanças".

**5. Mandar pro GitHub:**

```bash
git push -u origin maria/analise-temporal
```

(Nas próximas vezes na mesma branch, basta `git push`.)

**6. Abrir o Pull Request.** Entre no repositório no GitHub. Vai aparecer um botão verde **Compare & pull request**. Clique, escreva uma frase dizendo o que fez e crie. Alguém do grupo olha e aprova com **Merge pull request**.

**7. Depois que juntou**, volte pra `main` e atualize:

```bash
git checkout main
git pull
```

---

# Problemas comuns

**`python` não é reconhecido como comando**
O Python foi instalado sem marcar "Add python.exe to PATH". Reinstale marcando essa caixa, e abra um terminal novo.

**`pip install` falha em alguma biblioteca**
Confira se o `(.venv)` aparece no começo da linha do terminal. Se não aparecer, rode o `activate` de novo (passo 6). Se continuar, copie a mensagem de erro e mande no grupo.

**O notebook diz `ModuleNotFoundError: No module named 'geopandas'`**
O kernel errado está selecionado. Clique em **Select Kernel** e escolha o `.venv` (passo 8).

**`ModuleNotFoundError: No module named 'src'`**
Abra o VS Code na **pasta do projeto** (`acidente_transito`), e não numa pasta de dentro. Os notebooks precisam estar dentro de `notebooks/` para achar a pasta `src`.

**O notebook 01 diz que não achou arquivos**
A pasta `data/raw/` está vazia. Volte ao passo 7.

**O notebook 02, 03... dá erro dizendo que não acha um arquivo `.parquet`**
Você pulou um notebook. Rode na ordem, começando pelo 01.

**O notebook ficou lento ou travou**
Na barra de cima do notebook, clique em **Restart** e rode de novo do começo.

**`git push` foi rejeitado**
Alguém mandou algo antes de você. Rode `git pull` e tente o push de novo.

**Conflito no `.ipynb`**
Se der, chame quem sabe de git no grupo antes de mexer. Não escolha "aceitar tudo" sem olhar.

**Esqueci de criar a branch e já commitei na `main`**
Não faça push. Rode `git checkout -b nome-da-branch` (leva o commit junto) e siga o fluxo normal.
