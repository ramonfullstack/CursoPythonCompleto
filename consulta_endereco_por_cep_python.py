#!/usr/bin/env python
# coding: utf-8

# In[8]:


import requests

cep = "89.052-100/"

cep = cep.replace("-", "").replace(".", "").replace(" ", "")

if len(cep) == 8 :
    link = f'https://viacep.com.br/ws/{cep}/json/'

    requisicao = requests.get(link)

    print(requisicao)

    resposta = requisicao.json()

    uf = resposta['uf']
    cidade = resposta['localidade']
    bairro = resposta['bairro']
    ibge = resposta['ibge']
    comp = resposta['complemento']
    print(uf, cidade, bairro, ibge, comp)
else :
    print('Cep Inválido')


# In[ ]:




