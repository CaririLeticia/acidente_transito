# Acidentes de trânsito em Fortaleza (2015-2024)

Trabalho de ciência de dados sobre os sinistros de trânsito registrados pela AMC em Fortaleza. A ideia é ver onde, quando e como os acidentes acontecem.

Base: https://dados.fortaleza.ce.gov.br/dataset/sinistros-transito (cerca de 130 mil registros, 28 colunas)

## Perguntas

- Quais regiões concentram mais acidentes?
- Quais horários e dias da semana têm mais ocorrências?
- Como os acidentes variam ao longo dos anos?
- Quais veículos mais aparecem?
- As regiões com mais acidentes também têm mais acidentes graves?
- Que características têm os locais mais críticos?

## Como rodar

Testado com Python 3.14, mas deve funcionar do 3.11 pra cima.

```bash
git clone <url-do-repo>
cd Letucia
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

Baixe os arquivos da base no site acima e coloque em `data/raw/`. A pasta `data/` não vai pro git.

Abra a pasta no VS Code, instale a extensão Jupyter e escolha o kernel `.venv` em cada notebook.

## Notebooks

Rodar na ordem:

1. `01_carga_dados` - lê a base bruta e salva em parquet
2. `02_limpeza` - duplicados, datas, coordenadas, colunas novas
3. `03_analise_temporal` - ano, dia da semana, hora
4. `04_veiculos_severidade` - veículos, mortos e feridos
5. `05_analise_espacial` - ruas críticas, grade e mapas
6. `06_locais_criticos` - concentração x gravidade e características dos hotspots

O código compartilhado (caminhos, constantes) fica em `src/config.py`. Os gráficos saem em `figuras/`.

## Trabalhando em grupo

- Cada um trabalha numa branch (`git checkout -b nome/assunto`) e abre pull request pra `main`.
- Avisem no grupo antes de mexer no mesmo notebook, porque conflito em `.ipynb` é ruim de resolver.
- Antes de commitar, de preferência limpar as saídas dos notebooks (Clear All Outputs) pra diff ficar pequeno.
