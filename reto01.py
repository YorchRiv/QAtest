import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import pandas as pd


options = Options()
options.add_argument("--log-level=3")  # Minimiza logs de Chrome

driver = webdriver.Chrome(options=options)

def select_option_with_scroll(option_xpath):
    option = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, option_xpath))
    )
    # Scroll al elemento usando JS
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", option)
    # Ahora clickea
    option.click()

def textbox(input, xpath):
    elemento = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
    elemento.clear()
    elemento.send_keys(input)

def button(xpath):
    elemento = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
    elemento.click()

def checkbox_gender(gender):
    if gender == "Male":
        xpath = '//label[@for="gender-radio-1"]'
    elif gender == "Female":
        xpath = '//label[@for="gender-radio-2"]'
    elif gender == "Other":
        xpath = '//label[@for="gender-radio-3"]'
    else:
        xpath = '//label[@for="gender-radio-3"]'
    
    check_box = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
    check_box.click()
    return check_box

def set_date(fecha, xpath):
    campo_fecha = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
    campo_fecha.click()
    campo_fecha.send_keys(Keys.CONTROL + "a")  # Selecciona todo el texto actual
    campo_fecha.send_keys(fecha)
    campo_fecha.send_keys(Keys.ENTER)

def add_subjects(subjects, xpath='//*[@id="subjectsInput"]'):
    input_subject = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
    for subject in subjects:
        input_subject.send_keys(subject)
        # Espera que aparezca la opción desplegable
        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.CLASS_NAME, 'subjects-auto-complete__menu'))
        )
        input_subject.send_keys(Keys.ENTER)

def select_hobbies(hobbies_list):
    # Mapea los nombres visibles con sus atributos "for"
    hobby_map = {
        "Sports": "hobbies-checkbox-1",
        "Reading": "hobbies-checkbox-2",
        "Music": "hobbies-checkbox-3"
    }

    for hobby in hobbies_list:
        if hobby in hobby_map:
            xpath = f'//label[@for="{hobby_map[hobby]}"]'
            checkbox = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, xpath))
            )
            checkbox.click()

def sendFile(file, xpath='//*[@id="uploadPicture"]'):
    file_input = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
    file_input.send_keys(file)
    return file_input

def select_state_and_city(state, city):
    select_option_with_scroll('//*[@id="stateCity-label"]')

    # Click en el campo de State
    state_field = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'state')))
    state_field.click()

    # Espera y selecciona el estado
    state_option = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, f'//div[contains(@id,"react-select-3-option") and text()="{state}"]')))
    state_option.click()

    # Click en el campo de City
    city_field = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "city")))
    city_field.click()

    # Espera y selecciona la ciudad
    city_option = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, f'//div[contains(@id,"react-select-4-option") and text()="{city}"]')))
    city_option.click()

def imprimir_datos_confirmacion(driver, timeout=10):
    modal_tabla = WebDriverWait(driver, timeout).until(
        EC.visibility_of_element_located((By.XPATH, '/html/body/div[5]/div/div/div[2]/div/table'))
    )

    filas = modal_tabla.find_elements(By.TAG_NAME, "tr")

    datos = {}

    for fila in filas:
        celdas = fila.find_elements(By.TAG_NAME, "td")
        if len(celdas) == 2:
            etiqueta = celdas[0].text.strip()
            valor = celdas[1].text.strip()
            datos[etiqueta] = valor

    print("Datos del formulario enviados correctamente:")
    for etiqueta, valor in datos.items():
        print(f"{etiqueta}: {valor}")

def limpiar_formulario():
    # Scroll arriba
    driver.execute_script("window.scrollTo(0, 0);")
    
    # Limpia campos de texto
    campos_texto = [
        '//*[@id="firstName"]',
        '//*[@id="lastName"]',
        '//*[@id="userEmail"]',
        '//*[@id="userNumber"]',    
        '//*[@id="subjectsInput"]',
        '//*[@id="currentAddress"]'
    ]
    for xpath in campos_texto:
        try:
            elem = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, xpath)))
            elem.clear()
        except:
            pass
    
    # Deseleccionar hobbies (checkboxes)
    for hobby_id in ["hobbies-checkbox-1", "hobbies-checkbox-2", "hobbies-checkbox-3"]:
        checkbox = driver.find_element(By.ID, hobby_id)
        if checkbox.is_selected():
            label = driver.find_element(By.XPATH, f'//label[@for="{hobby_id}"]')
            label.click()
    
    # Resetear género: no estándar, lo más seguro es dejarlo para cuando setees el nuevo
    
    # Limpiar State y City (más complicado, quizás recargar sea mejor aquí)


try:
    driver.get("https://demoqa.com/automation-practice-form")
    driver.maximize_window() # Maximizar la ventana del navegador    
    file_path = os.path.abspath("subjets.txt")
    df = pd.read_csv("datos_demoqa.csv")  # Usa ruta absoluta si está en otro lugar
    
    for _, fila in df.iterrows():
        try:
            limpiar_formulario()        
            select_option_with_scroll('//*[@id="firstName"]')
            textbox(fila["firstName"], '//*[@id="firstName"]')
            textbox(fila["lastName"], '//*[@id="lastName"]')
            textbox(fila["email"], '//*[@id="userEmail"]')
            checkbox_gender(fila["gender"])
            textbox(str(fila["mobile"]), '//*[@id="userNumber"]')
            set_date(fila["birthDate"], '//*[@id="dateOfBirthInput"]')

            subjects = [s.strip() for s in fila["subjects"].split(",")]
            add_subjects(subjects)

            hobbies = [h.strip() for h in fila["hobbies"].split(",")]
            select_hobbies(hobbies)

            sendFile(file_path)
            textbox(fila["address"], '//*[@id="currentAddress"]')
            select_state_and_city(fila["state"], fila["city"])
            
            button('//*[@id="submit"]')

            print(f"Registro exitoso: {fila['firstName']} {fila['lastName']} - {fila['email']}")

            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "closeLargeModal"))).click()
            WebDriverWait(driver, 10).until(EC.invisibility_of_element((By.CLASS_NAME, "modal-content")))

        except Exception as fila_error:
            print(f"Error en fila {fila.to_dict()}: {fila_error}")

    #time.sleep(5)
    print("Página cargada correctamente.") #Final test

except Exception as e:
    print(f"✘ Error al procesar {fila['firstName']} {fila['lastName']}: {e}")

finally:
    if driver:
        driver.quit()