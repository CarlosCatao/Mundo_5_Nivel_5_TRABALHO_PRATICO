#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd


# In[5]:


# Criar uma variável
dados_csv = None

# Ler o conteúdo do arquivo CSV
dados_csv = pd.read_csv(
    './data/picoweb.csv',  # caminho do arquivo
    sep=';',               # separador de colunas
    engine='python',       # engine
    encoding='utf-8'       # encoding
)


# In[6]:


# Ver os nomes das colunas disponíveis
print("Colunas disponíveis no dataset:")
print(dados_csv.columns.tolist())


# In[11]:


# Seleciona 3 colunas quaisquer
subconjunto_dados = dados_csv[['ID', 'Pulse', 'Maxpulse']]


# In[13]:


# Imprimir/exibir o novo subconjunto
print(subconjunto_dados)


# In[ ]:




