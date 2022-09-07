#!/usr/bin/env python
# coding: utf-8

# In[ ]:




numero1 = input("Digite o número 1 para calcular")
numero2 = input("Digite o número 2 para calcular")
operacao = input("Escolha a operação a ser realizada (+, -, * ou /)")
resultado = 0

if(operacao == "+"):
    resultado = soma(numero1, numero2)
elif(operacao == "-"):
    resultado = menos(numero1, numero2)
elif(operacao == "/"):
    resultado = divisao(numero1, numero2)
elif(operacao == "*"):
    resultado = mult(numero1, numero2)

print("A operação escolhida foi: " + (operacao))
print("O resultado foi: " + str(resultado))

def soma(n1, n2):
    return (int(n1) + int(n2))

def menos(n3, n4):
    return (int(n3) - int(n4))

def divisao(n3, n4):
    return (int(n3) / int(n4))

def mult(n3, n4):
    return (int(n3) * int(n4))





# In[26]:





# In[ ]:





# In[ ]:




