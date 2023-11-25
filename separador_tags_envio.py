import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from chromedriver_py import binary_path # this will get you the path variable
from selenium.webdriver.common.by import By  # Importe a classe By

#tags = input('Informe as tags para separar e enviar...')
tags = "teste, teste2"
print(tags)
arrayTags = tags.split(',')
tagsFormatadasComQuebra = '\n'.join(arrayTags)

print('...............')
print(tagsFormatadasComQuebra)

#chrome_driver_path = r'C:\Temp2\chromedriver.exe'
chrome_driver_path = './chromedriver.exe'
#chrome_driver_path = '.\\chromedriver'

if(os.path.exists(chrome_driver_path)):
    print(r'Caminho existente: ' + chrome_driver_path)

try:
    
    # chrome_options.add_argument(f'--webdriver.chrome.driver={chrome_driver_path}')

    # driver = webdriver.Chrome(options=chrome_options)
    profile_path = r'C:\Users\RAMON\AppData\Local\Google\Chrome\User Data\Profile 4'
    chrome_options = Options()
    chrome_options.add_argument(f'--user-data-dir={profile_path}')
    chrome_options.add_argument('--profile-directory=Profile 4')
    svc = webdriver.ChromeService(executable_path=binary_path, Options=chrome_options)
    driver = webdriver.Chrome(service=svc)

    print("WebDriver iniciado com sucesso.")

    #url = "https://web.telegram.org/"
    url = "https://gmail.com/"

    # Abre o site
    driver.get(url)

    driver.maximize_window()
    time.sleep(15)

    

    xpathBotaoLogin = '/html/body/div[1]/div/div[2]/div[3]/div/div[2]/button[1]/div'
    botaoLogin = driver.find_element(By.XPATH, xpathBotaoLogin)
    botaoLogin.click()

    time.sleep(5)

    xpathInputNumero = '/html/body/div[1]/div/div[2]/div[2]/div/div[3]/div[2]/div[1]'
    numeroTelefone = '63981311589'
    campoTelefone = driver.find_element(By.XPATH, xpathInputNumero)
    campoTelefone.send_keys(numeroTelefone)

    xpathOkLogin = '/html/body/div[1]/div/div[2]/div[2]/div/div[3]/button[1]/div'
    botaoOkLogin = driver.find_element(By.XPATH, xpathOkLogin)
    botaoOkLogin.click()

except Exception as e:
    print(f"Erro: {e}")
finally:
    # No bloco finally, mesmo se houver um erro, fecharemos o navegador
    if 'driver' in locals():
        time.sleep(200)
        driver.quit()
        print("WebDriver fechado.")

