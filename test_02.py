import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Configurar el WebDriver
service = Service(r"C:\drivers\chromedriver.exe")

try:
    driver = webdriver.Chrome(service=service)
    driver.get("https://demoqa.com/text-box")
    
    # Set zoom level to 55%
    driver.execute_script("document.body.style.zoom='55%'")
    time.sleep(1)  # Short wait to allow zoom to take effect

    # Esperar a que el campo "userName" sea interactuable
    wait = WebDriverWait(driver, 10)
    
    for i in range(1, 31):  # Ciclo para repetir la prueba 30 veces
        print(f"Ingresando datos para el usuario {i}...")

        nom = wait.until(EC.presence_of_element_located((By.ID, "userName")))
        nom.clear()
        nom.send_keys(f"nombre{i}")

        corr = driver.find_element(By.ID, "userEmail")
        corr.clear()
        corr.send_keys(f"usuario{i}@test.com")

        curr = driver.find_element(By.ID, "currentAddress")
        curr.clear()
        curr.send_keys(f"Direccion actual {i}")

        perm = driver.find_element(By.ID, "permanentAddress")
        perm.clear()
        perm.send_keys(f"Direccion permanente {i}")

        # Scroll dinámico para visibilizar el botón antes de hacer clic
        submit_button = driver.find_element(By.ID, "submit")
        driver.execute_script("arguments[0].scrollIntoView();", submit_button)

        # Esperar a que el botón sea clickeable y hacer clic
        wait.until(EC.element_to_be_clickable((By.ID, "submit"))).click()

    print("Prueba completada con éxito")
    time.sleep(5)  # Esperar 5 segundos al final de la prueba

except Exception as e:
    print(f"Se produjo un error: {e}")

finally:
    if driver:
        driver.quit()
