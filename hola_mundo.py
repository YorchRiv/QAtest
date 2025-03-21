from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

# Especificar la ruta del ChromeDriver
service = Service(r"C:\drivers\chromedriver.exe")
driver = None

try:
    driver = webdriver.Chrome(service=service)
    # Abrir la página
    driver.get("https://demoqa.com/text-box")
    
    # Imprimir el título de la página
    print("PRIMER TESTING (OBTENER TITULO): ")
    print(driver.title)

except Exception as e:
    print(f"Se produjo un error: {e}")

finally:
    if driver:
        # Cerrar el navegador
        driver.quit()
