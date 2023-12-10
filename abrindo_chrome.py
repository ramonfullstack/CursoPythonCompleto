from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from chromedriver_py import binary_path
import time

# Configurar opções do Chrome para usar o perfil especificado
chrome_options = Options()

svc = webdriver.ChromeService(executable_path=binary_path, Options=chrome_options)
driver = webdriver.Chrome(service=svc)

try:
    # Abrir uma URL qualquer
    url = "https://www.google.com"
    driver.get(url)

    driver.maximize_window()
    time.sleep(15)

except Exception as e:
    print(f"Erro: {e}")

finally:
    # Fechar o navegador
    driver.quit()
