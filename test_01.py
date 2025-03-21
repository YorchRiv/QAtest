import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
service = Service(r"C:\drivers\chromedriver.exe")
driver = None

try:
    driver = webdriver.Chrome(service=service)
    driver.get("https://demoqa.com/text-box")
    #driver.maximize_window() #Maximizar ventana

    nom = driver.find_element(By.XPATH, "//input[@id='userName']")
    nom.send_keys("Rodrigo")
    time.sleep(1)

    corr=driver.find_element(By.XPATH, "//*[@id='userEmail']")
    corr.send_keys("test@test.com")
    time.sleep(1)

    curr = driver.find_element(By.XPATH, "//textarea[@id='currentAddress']")
    curr.send_keys("direccion_test")
    time.sleep(1)

    perm = driver.find_element(By.XPATH, "//textarea[@id='permanentAddress']")
    perm.send_keys("direccion_permanente_test")
    time.sleep(1)

    driver.execute_script("window.scrollTo(0,500)")
    time.sleep(2)
    driver.find_element(By.XPATH, "//button[@id='submit']").click()
    time.sleep(5)

    print("Primer test")



except Exception as e:
    print(f"Se produjo un error: {e}")

finally:
    if driver:
        driver.quit()