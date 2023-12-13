"""from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
# import pandas as pd 
import requests
"""
# Instalar automaticamente chromedriver
# Driver Selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

# Para esperar
from selenium.webdriver.support.ui import WebDriverWait

# para esperar que aparezca un elemento
from selenium.webdriver.support import expected_conditions as EC
from logic.tools import iniciar_chrome



if __name__ == "__main__":
    driver = iniciar_chrome()
    url="https://www.eldestapeweb.com"
    driver.get(url)

    wait = WebDriverWait(driver, 10)
    elemento = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.data")))
    elementos = driver.find_elements(By.CSS_SELECTOR,"div.data")
    titulo_nota = elemento.text
    print(titulo_nota)

    driver.quit()