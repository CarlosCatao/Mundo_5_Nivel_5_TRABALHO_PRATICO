#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


# Define max_rows para 9999
pd.set_option('display.max_rows', 9999)


# In[3]:


# Criar uma variável
dados_csv = None

# Ler o conteúdo do arquivo CSV
dados_csv = pd.read_csv(
    './data/picoweb.csv',  # caminho do arquivo
    sep=';',               # separador de colunas
    engine='python',       # engine
    encoding='utf-8'       # encoding
)


# In[5]:


# Imprimir o conjunto de dados original usando to_string()
print("=== Dados originais completos (to_string) ===")
print(dados_csv.to_string())


# In[7]:


# Ver os nomes das colunas disponíveis
print("Colunas disponíveis no dataset:")
print(dados_csv.columns.tolist())


# In[8]:


# Seleciona 3 colunas quaisquer
subconjunto_dados = dados_csv[['ID', 'Pulse', 'Maxpulse']]


# In[9]:


# Imprimir/exibir o novo subconjunto usando to_string()
print(subconjunto_dados.to_string())

