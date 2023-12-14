from navegador.browser import browser
from selenium.webdriver.common.by import By
import time

instance = browser()   

try:
    
    url = "https://www.linkedin.com/"
    instance.open_window_maximized(url)
    
    input_email = '//*[@id="session_key"]'
    elemento_email = instance.driver.find_element(By.XPATH, input_email)
    elemento_email.send_keys("ramonss.bque@outlook.com")
    
    input_senha = '//*[@id="session_password"]'
    elemento_senha = instance.driver.find_element(By.XPATH, input_senha)
    elemento_senha.send_keys("teste1995")

    botao = '//*[@id="main-content"]/section[1]/div/div/form/div[2]/button'
    botao_login = instance.driver.find_element(By.XPATH, botao)
    botao_login.click()
    
except Exception as e:
    print(f"Erro: {e}")

finally:
    # Fechar o navegador
    instance.driver.quit()
