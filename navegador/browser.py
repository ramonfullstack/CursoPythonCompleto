from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from chromedriver_py import binary_path
import time

class browser:
    def __init__(self) -> None:
        print('Configuração iniciada')
        chrome_options = Options()
        svc = webdriver.ChromeService(executable_path=binary_path, Options=chrome_options)
        self.driver = webdriver.Chrome(service=svc)
        
    def configura_browser(self):
        print ("configura_browser")
        
    def open_window_maximized(self, url):
        try:
            # Abrir uma URL qualquer
            self.driver.get(url)
            print("Abriu navegador")

            # Maximizar a janela
            self.driver.maximize_window()
            time.sleep(5)  # Aguarda por 15 segundos (você pode ajustar conforme necessário)
        except Exception as e:
            print(f"Erro ao abrir a janela maximizada: {e}")
        finally:
            # Fechar o navegador ao finalizar
            #self.driver.quit()
            print('Terminou')
            