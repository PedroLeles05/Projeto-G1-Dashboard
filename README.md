# Mercado de TI no Brasil — Projeto G1

Projeto acadêmico de análise e visualização de dados com Python, Pandas, Matplotlib, Seaborn, Plotly, Streamlit e SQLite/SQLAlchemy.

## Identificação acadêmica

- **Aluno:** Pedro Leles
- **Professor:** Alexandre Neves Louzada
- **Disciplina:** Linguagens de Programação
- **Projeto:** G1 — Mercado de TI no Brasil

## Objetivo

Analisar uma base simulada do mercado de tecnologia brasileiro, identificando padrões de salários e oportunidades segundo período, região, UF, cidade, cargo, senioridade, tecnologia, modalidade, setor e nível de demanda.

## Base de dados

- 4.440 registros
- 14 variáveis
- 120 meses, de janeiro de 2015 a dezembro de 2024
- 37 cidades
- 5 regiões
- Sem valores ausentes na inspeção inicial

> A base é simulada. Portanto, os resultados representam padrões internos ao dataset e não devem ser tratados como estatísticas oficiais do mercado de trabalho brasileiro.

## Requisitos atendidos

### Obrigatórios
- Python
- Pandas
- Matplotlib
- Seaborn
- Streamlit
- GitHub
- Notebook de análise
- Página HTML para GitHub Pages

### Intermediários
- Filtros múltiplos
- KPIs dinâmicos
- Gráficos interativos
- Análise temporal
- Tratamento e preparação dos dados
- Integração com banco de dados
- Dashboard organizado em seções
- Visualizações comparativas

### Avançados escolhidos
1. **Persistência em banco:** SQLite + SQLAlchemy.
2. **Dashboard multipágina:** Streamlit.

Também há análise temporal avançada e correlação no notebook.

## Estrutura

```text
projeto-g1/
├── app.py
├── db.py
├── requirements.txt
├── README.md
├── index.html
├── dados/
│   └── simulacao_mercado_ti_brasil.csv
├── database/
│   └── mercado_ti.db
├── notebooks/
│   └── analise_mercado_ti.ipynb
├── imagens/
└── pages/
    ├── 1_Analise_Salarial.py
    ├── 2_Analise_de_Vagas.py
    └── 3_Analise_Temporal.py
```

## Execução local

### 1. Clonar o repositório

```bash
git clone https://github.com/SEU-USUARIO/projeto-g1.git
cd projeto-g1
```

### 2. Criar ambiente virtual

Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```

Linux/macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Instalar dependências

```bash
pip install -r requirements.txt
```

### 4. Executar o dashboard

```bash
streamlit run app.py
```

O Streamlit abrirá o endereço local informado no terminal, normalmente `http://localhost:8501`.

### 5. Executar o notebook

```bash
jupyter notebook
```

Abra `notebooks/analise_mercado_ti.ipynb` e execute as células em ordem.

## Banco SQLite

O arquivo `database/mercado_ti.db` contém a tabela `mercado_ti`. O módulo `db.py` usa SQLAlchemy para criar a conexão e Pandas para leitura/escrita.

Se o banco não existir, o dashboard o cria automaticamente a partir do CSV.

## Principais perguntas analíticas

- Como o salário médio varia entre regiões?
- Quais cargos apresentam maior remuneração média?
- Como senioridade e tecnologia se relacionam com salário?
- Qual modalidade de trabalho apresenta maior remuneração média?
- Como as vagas evoluem ao longo do tempo?
- Qual região concentra maior volume de vagas?
- Existe correlação relevante entre salário médio e quantidade de vagas?

## Limitações

A base não representa uma amostra oficial do mercado de trabalho. Correlação não implica causalidade e médias agregadas podem esconder diferenças entre combinações de cargo, localidade, tecnologia e senioridade.
