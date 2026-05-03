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


# Imprimir/exibir os dados
print(dados_csv)


# In[ ]:




