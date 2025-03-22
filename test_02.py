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

    # Esperar a que el campo "userName" sea interactuable
    wait = WebDriverWait(driver, 10)

    nom = wait.until(EC.presence_of_element_located((By.ID, "userName")))
    nom.send_keys("Rodrigo")

    corr = driver.find_element(By.ID, "userEmail")
    corr.send_keys("test@test.com")

    curr = driver.find_element(By.ID, "currentAddress")
    curr.send_keys("direccion_test")

    perm = driver.find_element(By.ID, "permanentAddress")
    perm.send_keys("direccion_permanente_test")

    # Scroll dinámico para visibilizar el botón antes de hacer clic
    submit_button = driver.find_element(By.ID, "submit")
    driver.execute_script("arguments[0].scrollIntoView();", submit_button)

    # Esperar a que el botón sea clickeable
    wait.until(EC.element_to_be_clickable((By.ID, "submit"))).click()

    print("Test completado con éxito")
    time.sleep(5)

except Exception as e:
    print(f"Se produjo un error: {e}")

finally:
    if driver:
        driver.quit()
