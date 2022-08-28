#!/usr/bin/env python
# coding: utf-8

# In[5]:


nome = "Ramon da Silva Santos"
print(type(nome))
print(nome)
print(nome[0])
print(nome[1])


# In[8]:


print(nome[0:5])
print(nome[-3])


# In[9]:


print(id(nome))


# In[13]:


print(len(nome))
tamanho = len(nome)
print("O tamanho do meu nome é", tamanho)


# In[23]:


nome = "silva"
sobrenome = "Silva"
print(nome + " " + sobrenome)


# In[24]:


if (nome == sobrenome):
    print("O nome é igual ao sobrenome")
else:
    print("O nome não é igual ao sobrenome")


# In[25]:


if (nome is sobrenome):
    print("O nome é igual ao sobrenome")
else:
    print("O nome não é igual ao sobrenome")


# In[28]:


texto = "Nos estamos aprendendo python nessa aula"
textoRecuperado = texto.find("python")
if(textoRecuperado > 0):
    print("O texto procurado foi encontrado com sucesso")


# In[29]:


texto = texto.replace("python", "java")
print(texto)


# In[30]:


arrayDeTexto = texto.split(' ')
print(arrayDeTexto)


# In[31]:


nome = nome.upper()
print(nome)


# In[32]:


nome = nome.lower()
print(nome)


# In[35]:


# coding: utf-8
nome = "João da Silva"
print(nome)


# In[ ]:




