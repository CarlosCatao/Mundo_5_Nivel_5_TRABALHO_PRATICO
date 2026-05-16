#!/usr/bin/env python
# coding: utf-8

# In[162]:


# Importando as Bibliotecas de Trabalho

import pandas as pd
import numpy as np


# In[163]:


# Criando a Variável para armazenar o arquivo

dados_csv = None


# In[164]:


# Leitura do Arquivo CSV atribuindo as informacoes lidas para a variavel ja definida

dados_csv = pd.read_csv(
    './data/picoweb.csv',  # caminho do arquivo
    sep=';',               # separador de colunas
    engine='python',       # engine
    encoding='utf-8'       # encoding
)


# In[165]:


# Listagem do arquivo original para efeito de comparacoes futuras

print("="*65)
print("      LISTAGEM DO ARQUIVO ORIGINAL PARA BASE DE COMPARAÇÕES"+"\n")
print(dados_csv)
print("="*65)


# In[166]:


# Verificando a importacao dos dados

print("="*65)
print("    INFORMAÇÕES GERAIS PARA VERIFICAR A IMPORTAÇÃO DOS DADOS"+"\n")
print(dados_csv.info())
print("\n===> PRIMEIRAS 5 LINHAS"+"\n")
print(dados_csv.head())
print("\n===> ÚLTIMAS 5 LINHAS"+"\n")
print(dados_csv.tail())
print("="*65)


# In[167]:


# Criando uma nova variável com cópia dos dados

dados_csv_copia = dados_csv.copy()


# In[168]:


# Substituindo os valores nulos da coluna 'Calories' por 0

dados_csv_copia['Calories'] = dados_csv_copia['Calories'].fillna(0)

# Imprimindo os novos valores apos a substituico

print("="*65)
print("***  DESAFIO 01 - SUBSTITUIÇÃO DE <Calories> NULOS POR 0 (ZERO)"+"\n")

print("===> APÓS SUBSTITUIR NULOS POR 0")
print(dados_csv_copia)
print("="*65)


# Se observarmos as linhas 18 e 28 poderemos ver as substituições efetuadas.

# In[169]:


# Substituindo os valores nulos da coluna 'Date' por '1900/01/01'

dados_csv_copia['Date'] = dados_csv_copia['Date'].fillna("'1900/01/01'")

# Imprimindo os novos valores apos a substituico

print("="*65)
print("***  DESAFIO 02 - SUBSTITUIÇÃO DE <Date> NULOS POR ‘1900/01/01’"+"\n")

print("===> APÓS SUBSTITUIR NULOS POR ‘1900/01/01’")
print(dados_csv_copia)
print("="*65)


# Se observarmos a linha 22 poderemos ver a substituição efetuada.

# In[170]:


# Transformar a coluna Date para datetime

print("="*65)
print("***  DESAFIO 03 - TRANSFORMAÇÃO DA COLUNA <Date> em DATETIME’"+"\n")

try:
    dados_csv_copia['Date'] = pd.to_datetime(dados_csv_copia['Date'], format='%Y/%m/%d')
except Exception as e:
    print(f"===> NA TENTATIVA DE TRANSFORMAÇÃO OCORREU <ERRO>\n\n {e}")

print("\nEste ERRO se deve ao fato de que os valores de data estão entre aspas simples.")
print("Para resolver será nesárioces retirar as aspas.")
print("="*65)


# No arquivo original todas as datas encontram-se entre aspas simples.

# In[171]:


# Revertendo na coluna ‘Date’, o valor ‘1900/01/01’ por ‘NaN’

dados_csv_copia['Date'] = dados_csv_copia['Date'].replace("'1900/01/01'", np.nan)

print("="*65)
print("***  DESAFIO 03 - REVERTENDO O VALOR DE <Date> DE ‘1900/01/01’ PARA NULO’"+"\n")
print(dados_csv_copia)
print("="*65)


# In[172]:


# Removendo as aspas para eliminar o ERRO

dados_csv_copia['Date'] = dados_csv_copia['Date'].str.strip("'")

print("="*65)
print("***  DESAFIO 04 - REMOVENDO AS ASPAS E TENTANDO NOVAMENTE A TRANSFORMAÇÃO DA COLUNA <Date> EM DATETIME’"+"\n")

# Agora tentar converter para datetime novamente
try:
    dados_csv_copia['Date'] = pd.to_datetime(dados_csv_copia['Date'], format='%Y/%m/%d')
    print("\n\nConversão bem sucedida!")
except Exception as e:
    print(f"===> NA NOVA TENTATIVA DE TRANSFORMAÇÃO OCORREU <ERRO>\n\n {e}")

print('\nEste ERRO se deve ao fato de que na linha 26 a data nao está separada por "/".')
print("="*65)    


# In[173]:


# Combinando replace e to_datetime
dados_csv_copia['Date'] = dados_csv_copia['Date'].replace(
    '20201226', 
    pd.to_datetime('2020/12/26', format='%Y/%m/%d').date()
)

print("="*65)
print("***  DESAFIO 05 - CONVERTENDO A DATA 20201226 PARA 2020/12/26’"+"\n")
print(dados_csv_copia)
print("="*65)


# Na linha 26 podemos observar a data separada por -. Isso acontece porque o pandas, por padrão, exibe datas no formato ISO 8601 que é YYYY-MM-DD (com hífens), independentemente do formato que você usou na conversão.

# In[174]:


print("="*65)
print("***  DESAFIO 06 - FAZENDO A CONVERSÕ DE TODOS OS DADOS DA COLUNA <Date> PARA DATETIME’"+"\n")

# Agora tentar converter para datetime novamente
try:
    dados_csv_copia['Date'] = pd.to_datetime(dados_csv_copia['Date'], format='%Y/%m/%d')
    print("\nConversão bem sucedida!\n")
except Exception as e:
    print(f"===> NA NOVA TENTATIVA DE TRANSFORMAÇÃO OCORREU <ERRO>\n\n {e}")

print(dados_csv_copia)
print("="*65)


# In[175]:


# Verificar e remover registros com valores nulos em QUALQUER coluna

print("***  DESAFIO 07 - VERIFICANDO VALORES NULOS EM TODAS AS COLUNAS"+"\n")
print(f"Total de registros antes da remoção: {len(dados_csv_copia)}")

# Verificar valores nulos em todas as colunas
print("\n✅ CONTAGEM DE VALORES NULOS POR COLUNA")
for coluna in dados_csv_copia.columns:
    nulos = dados_csv_copia[coluna].isna().sum()
    if nulos > 0:
        print(f"  - {coluna}: {nulos} valor(es) nulo(s)")

# Mostrar quais linhas têm valores nulos em qualquer coluna
linhas_com_nulos = dados_csv_copia[dados_csv_copia.isna().any(axis=1)]
print(f"\n✅ LINHAS QUE CONTÊM VALORES NULOS")
print(f"    Total de linhas com algum valor nulo: {len(linhas_com_nulos)}\n")
print(linhas_com_nulos)

# Remover linhas que tenham QUALQUER valor nulo
dados_csv_copia = dados_csv_copia.dropna()

print(f"\n✅ Total de registros após remoção: {len(dados_csv_copia)}")
print(f"✅ Valores nulos restantes: {dados_csv_copia.isna().sum().sum()}")
print("="*65)


# In[178]:


# Imprimir o dataframe e verificar todas as transformações

print("*** DATAFRAME FINAL APÓS TODAS AS TRANSFORMAÇÕES"+"\n")

# Imprimir o DataFrame completo
print("\n===> DATAFRAME FINAL\n")
print(dados_csv_copia)
print("="*65)


# Como podemos verificar todas as modificações solicitadas foram efetuadas e o registro 22 
# foi removido.
