from selenium import webdriver

# Substitua '/caminho/para/chromedriver' pelo caminho real para o seu executável do ChromeDriver
chrome_driver_path = '.\chromedriver'

# Substitua 'C:\\Users\\SeuUsuario\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 1' pelo caminho real
profile_path = 'C:\\Users\\RAMON\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 1'

# Configurar opções do Chrome para usar o perfil especificado
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument(f'--user-data-dir={profile_path}')
chrome_options.add_argument('--profile-directory=Profile 1')

# Criar instância do WebDriver usando as opções configuradas
driver = webdriver.Chrome(executable_path=chrome_driver_path, options=chrome_options)

try:
    # Abrir uma URL qualquer
    driver.get("https://www.google.com")

    # Realizar outras operações, se necessário

except Exception as e:
    print(f"Erro: {e}")

finally:
    # Fechar o navegador
    driver.quit()
