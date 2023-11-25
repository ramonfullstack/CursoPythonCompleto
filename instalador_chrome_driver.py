from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
s = Service('chromedriver/chromedriver96.exe')
driver = webdriver.Chrome(service=s, options=options)