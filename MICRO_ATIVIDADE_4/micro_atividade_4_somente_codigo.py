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


# In[4]:


#imprime as primeiras 10 linhas
print("=== 10 ptimeiras linhas ===")
print(dados_csv.head(10))


# In[5]:


# imprime as últimas 10 linhas
print("=== 10 ultimas linhas ===")
print(dados_csv.tail(10))

