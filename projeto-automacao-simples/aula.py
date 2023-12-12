import os
from tkinter.filedialog import askdirectory

pasta_origem = askdirectory(title="Pasta Origem")
print(pasta_origem)
pasta_destino = askdirectory(title="Pasta Destino")
print(pasta_destino)

regras_arquivos = {
    "jan": "Janeiro",
    "fev": "Fevereiro",
    "mar": "março"
} 

lista_arquivos = os.listdir(pasta_origem)
print(lista_arquivos)

for nome_arquivo in lista_arquivos:
    for chave in regras_arquivos.keys():
        if chave in nome_arquivo:
            #"C:\Users\RAMON\Downloads"
            nova_pasta = regras_arquivos[chave]
            
            nome_completo_original = os.path.join(pasta_origem, nome_arquivo)
            nome_completo_final = os.path.join(pasta_destino, nova_pasta, nome_arquivo)
            
            #verificar se existe a pasta nova_pasta no destino
            caminho_nova_pasta = os.path.join(pasta_destino, nova_pasta)
            if not os.path.exists(caminho_nova_pasta):
                os.mkdir(caminho_nova_pasta) 
                   
            os.rename(nome_completo_original, nome_completo_final)