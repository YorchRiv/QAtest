import time  # Librería para manejar retrasos en la ejecución
from selenium import webdriver  # Selenium para automatizar el navegador
from selenium.webdriver.chrome.service import Service  # Configuración del servicio del WebDriver
from selenium.webdriver.common.by import By  # Localización de elementos en la página
from selenium.webdriver.support.ui import WebDriverWait  # Manejo de esperas explícitas
from selenium.webdriver.support import expected_conditions as EC  # Condiciones esperadas para las esperas

# Configurar el WebDriver especificando la ruta del ChromeDriver
service = Service(r"C:\drivers\chromedriver.exe")

try:
    # Inicia el navegador Chrome con el servicio configurado
    driver = webdriver.Chrome(service=service)
    # Abre la página web especificada
    driver.get("https://demoqa.com/text-box")

    # Configura una espera explícita de hasta 10 segundos
    wait = WebDriverWait(driver, 10)

    # Ciclo para ingresar datos de 50 usuarios
    for i in range(1, 51):
        print(f"Ingresando datos para el usuario {i}...")

        # Localiza el campo "userName" usando XPath, limpia el campo y escribe un nombre
        nom = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='userName']")))
        nom.clear()
        nom.send_keys(f"Usuario_{i}")

        # Localiza el campo "userEmail", limpia el campo y escribe un correo
        corr = driver.find_element(By.XPATH, "//*[@id='userEmail']")
        corr.clear()
        corr.send_keys(f"usuario{i}@test.com")

        # Localiza el campo "currentAddress", limpia el campo y escribe una dirección
        curr = driver.find_element(By.XPATH, "//textarea[@id='currentAddress']")
        curr.clear()
        curr.send_keys(f"Direccion actual {i}")

        # Localiza el campo "permanentAddress", limpia el campo y escribe otra dirección
        perm = driver.find_element(By.XPATH, "//textarea[@id='permanentAddress']")
        perm.clear()
        perm.send_keys(f"Direccion permanente {i}")

        # Realiza un desplazamiento en la página para que el botón "submit" sea visible
        submit_button = driver.find_element(By.XPATH, "//button[@id='submit']")
        driver.execute_script("arguments[0].scrollIntoView();", submit_button)

        # Espera a que el botón sea clickeable y hace clic en él
        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@id='submit']"))).click()

    # Imprime un mensaje indicando que el test se completó
    print("Test completado con éxito")
    time.sleep(5)  # Espera 5 segundos antes de finalizar

except Exception as e:
    # Captura cualquier excepción y la imprime
    print(f"Se produjo un error: {e}")

finally:
    # Cierra el navegador si está abierto
    if driver:
        driver.quit()
