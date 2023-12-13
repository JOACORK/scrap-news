# Instalar automaticamente chromedriver
from webdriver_manager.chrome import ChromeDriverManager
# Driver Selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
# Para modificar las opciones de webdriver en Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# Para esperar
from selenium.webdriver.support.ui import WebDriverWait

# para esperar que aparezca un elemento
from selenium.webdriver.support import expected_conditions as EC



def iniciar_chrome():
    """Setear parámetros"""

    ruta = ChromeDriverManager().install()
    options = Options()

    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    options.add_argument(f"user-agent={user_agent}") # Define user agent personalizado
    # Para setear como iniciar ventana
    options.add_argument("--headless") # para ejecutar selenium sin abrir navegador

    options.add_argument("--start-maximized") # para maximizar la ventana
    options.add_argument("--disable-web-security") # deshabilita política del mismo origen
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-notifications")
    options.add_argument("--ignore-certificate-errors") # ignorar aviso "su conexion no es privada"
    options.add_argument("--no-sandbox")
    options.add_argument("--log-level=3") # Para que chromedriver no muestre nada en terminal
    options.add_argument("--allow-running-insecure-content") # desactiva el aviso de "contenido no seguro"
    options.add_argument("--no-default-browser-check") # Evita el aviso que Chrome no es el navegador por defecto
    options.add_argument("--no-first-run")
    options.add_argument("--no-proxy-server")
    options.add_argument("--disable-blink-features=AutomationControlled") # eVITA QUE SELENIUM SEA DETECTADO COMO BOT

    # PARAMETROS A OMITIR EN EL INICIO DE CHROMEDRIVER
    exp_opt = [
        'enable-automation', #evitar que se muestre notificacion sobre software automatizado de pruebas
        'ignore-certificate-errors',
        'enable-logging'
    ]
    options.add_experimental_option("excludeSwitches",exp_opt)

    # PARAMETROS QUE DEFINEN PREFERENCIAS EN CHROMEDRIVER
    prefs={
        "profile.default_content_setting_values.notifications": 2, # evitar notificaciones
        "intl.accept_languages":["es-ES","es"],
        "credentials_enable_service": False # Evitar notificacion para guardar contraseña
    }

    options.add_experimental_option("prefs",prefs)


    # instanciamos servicio
    s = Service(ruta)

    driver = webdriver.Chrome(service=s, options=options)

    return driver

