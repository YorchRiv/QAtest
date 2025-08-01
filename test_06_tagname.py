import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()

try:
    driver.get("https://unicostarjetasbi.com/")
    driver.maximize_window() # Maximizar la ventana del navegador    
    
    links = driver.find_elements(By.TAG_NAME, "a")
    for link in links:
        print(link.get_attribute("href"))

    time.sleep(5)
    print("Página cargada correctamente.") #Final test

except Exception as e:
    print(f"Se produjo un error: {e}")

finally:
    if driver:
        driver.quit()