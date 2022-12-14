nome = input('Digite o nome: ')
idade = input('Digite a sua idade: ')

if nome and idade:
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {nome[::-1]}')

    if ' ' in nome:
        print('Seu nome contém espaços')
    else:
        print('Seu nome não contém espaços')

    quantidade_letras_no_nome = len(nome)
    print(f'A quantidade de letras no nome é {quantidade_letras_no_nome}')

    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A ultima letra do seu nome é {nome[-1]}')
else:
    print('Descupe não foi informado nada')

MAIOR_DE_IDADE = 18
idade_int = int(idade)
if idade_int > MAIOR_DE_IDADE:
    print(f'O {nome} é maior de idade')
else:
    print(f'O {nome} não é maior de idade')