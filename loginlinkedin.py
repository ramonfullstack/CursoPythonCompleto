from navegador.browser import browser
from selenium.webdriver.common.by import By
import time

instance = browser()  

info_login_oficial = {
    'user': "ramonss.bque@gmail.com",
    'senha': "Ramon@@1995"
} 

info_login_teste = {
    'user': "ramonss.bque@gmail.com",
    'senha': "Ramon@@1995"
} 

urls = {
    'urlbaselinkedin': 'https://www.linkedin.com/',
    'urlJobs': 'https://www.linkedin.com/jobs/s'
}

def faca_login_linkedin():
    url = "https://www.linkedin.com/"
    instance.open_window_maximized(url)
    
    input_email = '//*[@id="session_key"]'
    elemento_email = instance.driver.find_element(By.XPATH, input_email)
    elemento_email.send_keys(info_login_oficial['user'])
    
    input_senha = '//*[@id="session_password"]'
    elemento_senha = instance.driver.find_element(By.XPATH, input_senha)
    elemento_senha.send_keys(info_login_oficial['senha'])

    botao = '//*[@id="main-content"]/section[1]/div/div/form/div[2]/button'
    botao_login = instance.driver.find_element(By.XPATH, botao)
    botao_login.click()
    time.sleep(10)
    
def clica_botao_pesquisavaga():
    #clica no campo de pesquisa de vagas
    #campo_pesquisa = instance.driver.find_element(By.XPATH, '//*[@id="jobs-search-box-keyword-id-ember25"]')
    campo_pesquisa = instance.driver.find_element(By.TAG_NAME, 'input')
    time.sleep(2)
    
    campo_pesquisa.click()
    time.sleep(2)
    campo_pesquisa.send_keys('developer + senior')
    time.sleep(2)
    
    #Clica no botão pesquisa vagas
    botao_pesquisa = instance.driver.find_element(By.XPATH, '//*[@id="global-nav-search"]/div/div[2]/button[1]')
    botao_pesquisa.click()
    time.sleep(3)
    #Filtra somente easy apply, vagas fáceis de se candidatar
    filtro_easy_apply = instance.driver.find_element(By.CSS_SELECTOR, '[aria-label="Easy Apply filter."]')
    filtro_easy_apply.click()
    time.sleep(3)
    
def procure_vagas():
    time.sleep(5)
    
    urlJobs = urls.get('urlJobs')
    
    instance.driver.get(urlJobs)
    time.sleep(5)
    clica_botao_pesquisavaga()
    
def percorre_as_vagas():
    time.sleep(2)
    vagas_emprego_id_elemento = instance.driver.find_elements(By.XPATH, '//*[@data-job-id]')
    time.sleep(5)
    
    # Iterar sobre os elementos e fazer algo
    for elemento in vagas_emprego_id_elemento:
        
        atributo_id = elemento.get_attribute("data-job-id")
        try:
            print(atributo_id)
            elemento.click()
            time.sleep(8)
            
            #botao_easy_apply = instance.driver.find_element(By.CSS_SELECTOR, '//*[contains(@aria-label, "Easy Apply to")]')
            botao_easy_apply = instance.driver.find_element(By.XPATH, '//*[contains(@aria-label, "Easy Apply to")]')
            botao_easy_apply.click()
            time.sleep(5)
            
            #clica no botão next step
            botao_next1 = instance.driver.find_element(By.XPATH, '//*[contains(@aria-label, "Continue to next step")]')
            botao_next1.click()
            time.sleep(5)
            botao_next1.click()
            time.sleep(5)
            
            #clica no botão review
            botao_review = instance.driver.find_element(By.XPATH, '//*[contains(@aria-label, "Review")]')
            botao_review.click()
            time.sleep(5)
            
            #clica no botão para enviar a review
            botao_submit = instance.driver.find_element(By.XPATH, '//*[contains(@aria-label, "Submit")]')
            botao_submit.click()
            time.sleep(5)
            
            #clica no botão done
            botao_done =  instance.driver.find_element(By.XPATH, '//html/body/div[3]/div/div/div[3]/button')
            botao_done.click()
            time.sleep(2)
                
        except Exception as e:
            print(f"Erro no atributo: {atributo_id} Erro {e}")
       
try:
    faca_login_linkedin()
   
    #procura vagas no linkedin
    procure_vagas()
    
    #percorre as vagas
    percorre_as_vagas()
    
except Exception as e:
    print(f"Erro: {e}")

finally:
    # Fechar o navegador
    instance.driver.quit()
