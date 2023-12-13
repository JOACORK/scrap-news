from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
# import pandas as pd 
import requests

from logic.tools import iniciar_chrome, WebDriverWait, EC,By



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