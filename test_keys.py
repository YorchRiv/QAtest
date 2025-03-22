import time  # Librería para manejar retrasos en la ejecución
from selenium import webdriver  # Selenium para automatizar el navegador
from selenium.webdriver.chrome.service import Service  # Configuración del servicio del WebDriver
from selenium.webdriver.common.by import By  # Localización de elementos en la página
from selenium.webdriver.support.ui import WebDriverWait  # Manejo de esperas explícitas
from selenium.webdriver.support import expected_conditions as EC  # Condiciones esperadas para las esperas
from selenium.webdriver.common.keys import Keys  # Para manejar teclas especiales como TAB

# Configurar el WebDriver especificando la ruta del ChromeDriver
service = Service(r"C:\drivers\chromedriver.exe")

try:
    driver = webdriver.Chrome(service=service)
    driver.get("https://demoqa.com/text-box")
    wait = WebDriverWait(driver, 10)
    nom = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='userName']")))
    nom.clear()
    nom.send_keys("Usuario_Unico")
    nom.send_keys(Keys.TAB + "CORREO@CORREO.COM" + Keys.TAB + "Direccion 1" + Keys.TAB + "Direccion 1" + Keys.TAB +Keys.ENTER)
    time.sleep(5)

except Exception as e:
    # Captura cualquier excepción y la imprime
    print(f"Se produjo un error: {e}")

finally:
    # Cierra el navegador si está abierto
    if driver:
        driver.quit()