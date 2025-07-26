import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()

try:
    driver.get("https://demoqa.com/checkbox")
    driver.maximize_window() # Maximizar la ventana del navegador    
    
    arb1 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="tree-node"]/ol/li/span/button'))).click()
    time.sleep(1)
    
    check_box = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="tree-node"]/ol/li/span/label/span[1]'))).click()


    time.sleep(5)
    print("Página cargada correctamente.")

except Exception as e:
    print(f"Se produjo un error: {e}")

finally:
    if driver:
        driver.quit()