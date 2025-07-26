import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Configurar el WebDriver
service = Service(r"C:\drivers\chromedriver.exe")
driver = None

try:
    options = webdriver.ChromeOptions()
    options.add_argument("--log-level=3")  # Menos mensajes en consola
    options.add_experimental_option('excludeSwitches', ['enable-logging'])

    driver = webdriver.Chrome(service=service, options=options)
    driver.get("https://demoqa.com/text-box")
    time.sleep(5)
    print("Página cargada correctamente.")

except Exception as e:
    print(f"Se produjo un error: {e}")

finally:
    if driver:
        driver.quit()
