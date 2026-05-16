## Limpeza e Tratamento de Dados com Python e Pandas
[![GitHub](https://img.shields.io/badge/GitHub-Repositório-black?logo=github)](https://github.com/CarlosCatao/Mundo_5_Nivel_5_TRABALHO_PRATICO)
## 💻 Autor

Carlos Altomare Catão

## 📌 Descrição do Projeto

Este projeto foi desenvolvido como parte de uma atividade prática para um curso de Análise de Dados. O objetivo principal é realizar a limpeza e transformação de um conjunto de dados fornecido em formato CSV, tornando-o apto para tarefas de mineração e análise de dados.

Foram aplicadas técnicas de tratamento de valores nulos, conversão de tipos de dados, correção de formatos inconsistentes e remoção de registros inválidos utilizando a linguagem **Python** e a biblioteca **Pandas**.

## 📋 Requisitos

Antes de executar o projeto, certifique-se de possuir:

- ![Python](https://img.shields.io/badge/Python-3.x-blue)
- ![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-green)
- Jupyter Notebook, JupyterLab ou Google Colab

## 📊 Conjunto de Dados Utilizado

- **Arquivo:** `picoweb.csv` (fornecido no material da atividade)
- **Colunas originais:**
  - `ID`
  - `Duration`
  - `Date`
  - `Pulse`
  - `Maxpulse`
  - `Calories`

## 🧰 Ferramentas e Tecnologias

- Python 3.x
- Pandas
- Jupyter Notebook / JupyterLab / Google Colab (recomendado)
- Ambiente de desenvolvimento (VS Code, PyCharm, etc.)

## 📁 Estrutura do Projeto

```text
├── .ipynb_checkpoints/
├── data/
│   └── picoweb.csv
├── Trabalho_Pratico.ipynb
├── Trabalho_Pratico_Resultado_Execucao.pdf
└── trabalho_pratico_somente_codigo.py
```

## 🔧 Etapas Realizadas

### 1. Leitura dos dados
O arquivo CSV foi importado utilizando `pandas.read_csv()`, com atenção aos parâmetros de separador, encoding e engine.

### 2. Verificação inicial
- Exibição das informações gerais do DataFrame (`.info()`)
- Exibição das primeiras e últimas linhas (`.head()` e `.tail()`)

### 3. Cópia dos dados
Uma cópia independente do conjunto original foi criada para preservar os dados brutos.

### 4. Tratamento de valores nulos

| Coluna     | Ação                                                                 |
|------------|----------------------------------------------------------------------|
| `Calories` | Substituição de valores nulos por `0`                                |
| `Date`     | Substituição temporária de valores inválidos para permitir a padronização e posterior conversão para datetime. |

### 5. Conversão para datetime
- Tentativa de converter a coluna `Date` para o tipo `datetime`
- Identificação de valores com formato incorreto, como `"20201226"`
- Correção utilizando `replace()` combinado com `to_datetime()`

### 6. Remoção de registros nulos
- Remoção da linha 22 (registro com `Date` nulo após as transformações)
- Uso do método `.dropna()` baseado na coluna `Date`

### 7. Verificação final
Exibição do Dataset final para confirmar que todas as transformações foram aplicadas com sucesso.

## ▶️ Como Executar o Projeto

1. Clone este repositório ou faça o download dos arquivos.
2. Instale a biblioteca Pandas (caso não tenha):
   ```bash
   pip install pandas

3. Execute o script Python ou abra o notebook no Jupyter/Colab.
4. Certifique-se de que o arquivo picoweb.csv está no mesmo diretório do script.

## 📄 Arquivos do Projeto

| Arquivo                                    | Descrição                                                                 |
|--------------------------------------------|---------------------------------------------------------------------------|
| `Trabalho_Pratico.ipynb`                  | Notebook Jupyter com todo o código, documentação e saídas intermediárias. |
| `trabalho_pratico_somente_codigo.py`      | Versão em script Python contendo apenas o código (sem markdown).          |
| `Trabalho_Pratico_Resultado_Execucao.pdf` | PDF com os prints/saídas da execução do notebook.                         |
| `.ipynb_checkpoints/`                     | Pasta gerada automaticamente pelo Jupyter para backups.                   |
| `data/`                                   | Pasta contendo o(s) arquivo(s) de dados utilizados no projeto.            |


## ✅ Resultados Obtidos

Ao final do processo, o Dataset resultante:

- Não contém valores nulos nas colunas essenciais
- Possui a coluna `Date` no formato `datetime64`
- Está pronto para análises estatísticas, visualizações ou modelagem preditiva

## 📚 Referências

- Documentação oficial do Pandas:
  https://pandas.pydata.org/docs/

- Documentação oficial do Python:
  https://docs.python.org/3/

