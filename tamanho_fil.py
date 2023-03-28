#!/usr/bin/env python
# coding: utf-8

# In[25]:


caminho = 'C://Users/Ramon/Downloads/'

import os

lista_arquivos = os.listdir(caminho)
#print(lista_arquivos)

def getsize(filename):
    return os.stat(filename).st_size

for arquivo in lista_arquivos:
    nome_completo = caminho + arquivo
    tamanho = getsize(nome_completo)
    print(arquivo)
    print(tamanho)
    


# In[ ]:



      


# In[ ]:




