def inverter_string(texto):
    return texto[::-1]

def calcular_fatorial(numero):
    return 1 if numero == 0 else numero * calcular_fatorial(numero-1)

def eh_palindromo(palavra):
    return palavra == palavra[::-1]

def calcular_media(lista):
    return sum(lista) / len(lista) if len(lista) > 0 else 0

def ordenar_lista(lista):
    return sorted(lista)

def eh_primo(numero):
    return numero > 1 and all(numero % i != 0 for i in range(2, int(numero**0.5) + 1))

def celsius_para_faheneit(celsius):
    return (celsius * 9/5) * 32

def contador_de_palavras(frase):
    palavras = frase.split()
    return len(palavras)

import random
def gerador_numero_aleatorios(inicio, fim):
    return random.randint(inicio, fim)

import re
def validar_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email) is not None

    
#print(inverter_string('Fernando'))
#print(calcular_fatorial(3))
# print(eh_palindromo('ramon'))
# print(eh_palindromo('Amor'))
# lista_notas = [8,9,10]
# print(calcular_media(lista_notas))
# lista_notas = [6,7,6,6]
# print(calcular_media(lista_notas))
# lista_nomes = ['uva', 'açai', 'banana', 'caju']
# print(ordenar_lista(lista_nomes))
# print(celsius_para_faheneit(30))
# print(celsius_para_faheneit(45))
# frase = 'O ramon esta programando sdsdsds sdsaad'
# print(contador_de_palavras(frase))
# print(gerador_numero_aleatorios(1, 100))
# print(gerador_numero_aleatorios(1, 20000))
print(validar_email('ramon'))
print(validar_email('ramon@gmail.com'))