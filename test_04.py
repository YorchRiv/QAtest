#Test con WAIT

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()

try:
    driver.get("https://demoqa.com/text-box")
    driver.maximize_window() # Maximizar la ventana del navegador
    driver.implicitly_wait(10)  # Espera implícita de 10 segundos

    nom = driver.find_element(By.XPATH, "//input[@id='userName']").send_keys("Jorge Mejicanos")    


    time.sleep(5)
    print("Página cargada correctamente.")

except Exception as e:
    print(f"Se produjo un error: {e}")

finally:
    if driver:
        driver.quit()