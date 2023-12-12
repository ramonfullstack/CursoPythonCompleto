import openpyxl

#Criar um novo arquivo excel
workbook = openpyxl.Workbook()

sheet = workbook.active

lista_nomes = [ 'Ramon', 'Joao', 'Vinicius']

sheet['A1'] = 'Nome'

# Adicionar dados à folha usando um loop
for index, nome in enumerate(lista_nomes, start=2):
    sheet['A' + str(index)] = nome

    
#salvar o arquivo
workbook.save('exemplo.xlsx')