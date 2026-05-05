#!/usr/bin/env python
# coding: utf-8

# In[12]:


import pandas as pd


# In[13]:


# Define max_rows para 9999
pd.set_option('display.max_rows', 9999)


# In[14]:


# Criar uma variável
dados_csv = None

# Ler o conteúdo do arquivo CSV
dados_csv = pd.read_csv(
    './data/picoweb.csv',  # caminho do arquivo
    sep=';',               # separador de colunas
    engine='python',       # engine
    encoding='utf-8'       # encoding
)


# In[15]:


print("=== INFORMAÇÕES GERAIS DO DATASET ===")
print("="*65)
print(dados_csv.describe())
print("="*65 + "\n")


# In[16]:


# Informações completas do dataset
print("=== INFORMAÇÕES COMPLETAS DO DATASET ===")
print("="*65)
print(dados_csv.info())
print("="*65)


# In[19]:


# TOTAL DE LINHAS
print("\n" + "="*65)
print("1. TOTAL DE LINHAS:")
print(f"Total de linhas de dados: {len(dados_csv) - 1}")
print(f"Total de linhas no arquivo: {len(dados_csv)}")
print("="*65)


# In[8]:


# TOTAL DE COLUNAS
print("\n" + "="*65)
print("2 TOTAL DE COLUNAS:")
print(f"O dataset possui {len(dados_csv.columns)} colunas")
print(f"Colunas: {dados_csv.columns.tolist()}")
print("="*65)


# In[9]:


# QUANTIDADE DE DADOS NULOS
print("\n" + "="*65)
print("3. DADOS NULOS POR COLUNA:")
nulos_por_coluna = dados_csv.isnull().sum()
print("Nulos por coluna:")
print(nulos_por_coluna)
print(f"\nTOTAL de valores nulos no dataset: {dados_csv.isnull().sum().sum()}")
print("="*65)


# In[10]:


# TIPO DE DADO DE CADA COLUNA
print("\n" + "="*65)
print("4. TIPO DE DADO POR COLUNA:")
print(dados_csv.dtypes)

# Explicação detalhada dos tipos
print("\nDetalhamento dos tipos encontrados:")
for coluna in dados_csv.columns:
    tipo = dados_csv[coluna].dtype
    if tipo == 'int64':
        print(f"  - {coluna}: Inteiro (int64) - valores inteiros")
    elif tipo == 'float64':
        print(f"  - {coluna}: Decimal/Ponto flutuante (float64) - permite valores decimais e NaN")
    elif tipo == 'object':
        print(f"  - {coluna}: Texto/String (object) - valores alfanuméricos")
print("="*65)


# In[11]:


# QUANTIDADE DE MEMÓRIA UTILIZADA
print("\n" + "="*65)
print("5. MEMÓRIA UTILIZADA:")

# Memória detalhada por coluna
memoria_detalhada = dados_csv.memory_usage(deep=True)
print("Memória por coluna:")
for coluna in dados_csv.columns:
    memoria_bytes = memoria_detalhada[coluna]
    memoria_kb = memoria_bytes / 1024
    print(f"  - {coluna}: {memoria_bytes:>10,} bytes ({memoria_kb:.2f} KB)")

# Memória total
memoria_total_bytes = memoria_detalhada.sum()
memoria_total_kb = memoria_total_bytes / 1024
memoria_total_mb = memoria_total_kb / 1024

print(f"\nMEMÓRIA TOTAL:")
print(f"  - Bytes: {memoria_total_bytes:,} bytes")
print(f"  - Kilobytes (KB): {memoria_total_kb:.2f} KB")
print(f"  - Megabytes (MB): {memoria_total_mb:.4f} MB")
print("="*65)


# In[ ]:




