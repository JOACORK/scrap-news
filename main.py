from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
# from bs4 import BeautifulSoup
# import pandas as pd 
# import requests

print("Iniciando Ruta")
ruta= ChromeDriverManager().install()
print(ruta)
print("hola mundo")

