import time
import csv
import os
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
import traceback
from datetime import datetime

options = Options()
options.add_argument("--log-level=3")  # Minimiza logs de Chrome
driver = webdriver.Chrome(options=options)

def clear_console():
    # Para Windows
    if os.name == 'nt':
        os.system('cls')
    # Para Linux/macOS
    else:
        os.system('clear')


def comparar_csv_filtrado(reference_path, test_path):
    df_ref = pd.read_csv(reference_path)
    df_test = pd.read_csv(test_path)

    # Campos que usas para filtrar (los inputs controlables)
    campos_control = ["Categoria", "Monto", "Meses"]

    # Campos de salida que quieres comparar
    campos_salida = [col for col in df_ref.columns if col not in campos_control]

    # Recorremos cada fila de test para buscar el registro correspondiente en referencia
    errores = []
    for idx_test, fila_test in df_test.iterrows():
        filtro = (
            (df_ref["Categoria"] == fila_test["Categoria"]) &
            (df_ref["Monto"] == fila_test["Monto"]) &
            (df_ref["Meses"] == fila_test["Meses"])
        )
        df_ref_match = df_ref[filtro]

        if df_ref_match.empty:
            errores.append(f"Registro de test sin coincidencia en referencia: fila {idx_test}")
            continue

        # Si hay más de una coincidencia, tomamos la primera
        fila_ref = df_ref_match.iloc[0]

        # Comparamos los campos de salida
        for campo in campos_salida:
            val_ref = fila_ref[campo]
            val_test = fila_test[campo]
            if pd.isna(val_ref) and pd.isna(val_test):
                continue  # ambos NaN, OK
            if val_ref != val_test:
                errores.append(
                    f"Diferencia en fila test {idx_test}, campo '{campo}': referencia={val_ref} vs test={val_test}"
                )

    if errores:
        print("Se encontraron diferencias o problemas:")
        for e in errores:
            print("-", e)
    else:
        print("Todos los datos coinciden para los registros encontrados.")

def set_slider_monto(driver, valor):
    """
    Cambia el valor del slider de monto de forma segura.
    valor: debe estar entre 1000 y 1000000, múltiplos de 1000
    """
    if valor < 1000 or valor > 1000000 or valor % 1000 != 0:
        raise ValueError("El valor debe estar entre 1000 y 1000000 en pasos de 1000")
    
    slider = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "monto"))
    )

    # Ejecuta JS para cambiar el valor y disparar los eventos necesarios
    driver.execute_script("""
        let slider = arguments[0];
        slider.value = arguments[1];
        slider.dispatchEvent(new Event('input'));
        slider.dispatchEvent(new Event('change'));
    """, slider, str(valor))

def scroll(option_xpath):
    option = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, option_xpath))
    )
    # Scroll al elemento usando JS
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", option)
    # Ahora clickea
    option.click()

def select_category(num):
    select_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "select")))
    select = Select(select_element)
    select.select_by_index(num)  # El segundo elemento (índice empieza en 0)

def add_amount():
    boton = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div[1]/div[2]/div[1]/div[2]/button[2]")).click()
    )

def select_month(num):
    match num:
        case 0:
            boton = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div[1]/div[2]/div[2]/div[2]/div[1]"))).click()
        case 1:
            boton = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div[1]/div[2]/div[2]/div[2]/div[2]"))).click()
        case 2:
            boton = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div[1]/div[2]/div[2]/div[2]/div[3]"))).click()
        case 3:
            boton = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div[1]/div[2]/div[2]/div[2]/div[4]"))).click()
        case 4:
            boton = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div[1]/div[2]/div[2]/div[2]/div[5]"))).click()
        case 5:
            boton = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div[1]/div[2]/div[2]/div[2]/div[6]"))).click()
        case 6:
            boton = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div[1]/div[2]/div[2]/div[2]/div[7]"))).click()

def print_data(month):

    categorias_tarjeta = {
    0: "Clasica",
    1: "Oro",
    2: "Platinum",
    3: "Infinite",
    4: "Master black",     # MasterCard Black
    5: "Business"
    }

    monto = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div[1]/div[2]/div[1]/div[1]/span"))).text
    cuota = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div[2]/div/div[1]/span"))).text
    comision = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div[2]/div/div[2]/div[1]/span"))).text
    seguro = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div[2]/div/div[2]/div[2]/span"))).text
    primeraCuota = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div[2]/div/div[2]/div[3]/span"))).text
    meses = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div[1]/div[2]/div[2]/div[1]/span"))).text
    print(f"{categorias_tarjeta[month]} | Monto: {monto} | Cuota: {cuota} | Comisión: {comision} | Seguro: {seguro} | Primera Cuota: {primeraCuota} | Meses: {meses}")

def get_data(month):
    categorias_tarjeta = {
        0: "Clasica",
        1: "Oro",
        2: "Platinum",
        3: "Infinite",
        4: "Master black",
        5: "Business"
    }

    def clean_monto(text):
        # Quita "L. ", "L ", y cualquier espacio, deja solo números
        return float(text.replace("L. ", "").replace("L ", "").replace(",", "").strip())

    def clean_meses(text):
        # Quita la palabra "meses", espacios y devuelve solo el número
        return float(text.lower().replace("meses", "").strip())

    monto = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div[1]/div[2]/div[1]/div[1]/span"))
    ).text

    cuota = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div[2]/div/div[1]/span"))
    ).text

    comision = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div[2]/div/div[2]/div[1]/span"))
    ).text

    seguro = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div[2]/div/div[2]/div[2]/span"))
    ).text

    primera_cuota = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div[2]/div/div[2]/div[3]/span"))
    ).text

    meses = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div[1]/div[2]/div[2]/div[1]/span"))
    ).text

    # Limpiar valores
    monto = clean_monto(monto)
    cuota = clean_monto(cuota)
    comision = clean_monto(comision)
    seguro = clean_monto(seguro)
    primera_cuota = clean_monto(primera_cuota)
    meses = clean_meses(meses)

    return {
        "Categoria": categorias_tarjeta[month],
        "Monto": monto,
        "Cuota Mensual": cuota,
        "Comision": comision,
        "Seguro": seguro,
        "Primera Cuota": primera_cuota,
        "Meses": meses
    }

def save_data(month, filename="resultados_test/resultados.csv"):
    data = get_data(month) 
    
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    file_exists = os.path.isfile(filename)

    with open(filename, mode="a", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=data.keys())

        # Escribir encabezado solo si el archivo no existía
        if not file_exists:
            writer.writeheader()

        writer.writerow(data)



try:
    driver.get("https://www.corporacionbi.com/hn/banpais/tarjetas-de-credito-y-debito/extra-financiamiento-solicitar-tarjetas-de-credito-y-debito/")
    driver.maximize_window() # Maximizar la ventana del navegador    
    iframe = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "calculadora-financiamiento")))
    driver.switch_to.frame(iframe)

    now = datetime.now()
    timestamp = now.strftime("%Y%m%d_%H%M%S")  # e.g. 20250801_211530
    filename = f"resultados_test/resultados_{timestamp}.csv"

    scroll("/html/body/div[@class='container']/div[@class='calc-container']")

    total_iter = 6 * 7 * 100  # total de iteraciones
    count = 0

    for j in range(0, 6):  # categoria
        select_category(j)

        for k in range(0, 7):  # meses
            select_month(k)

            for i in range(1, 11):  # monto
                set_slider_monto(driver, i * 100000)
                save_data(j, filename)
                print_data(j)
                # count += 1
                # porcentaje = (count / total_iter) * 100
                # clear_console()
                # print(f"Progreso del test: {porcentaje:.2f}%")

    time.sleep(2)
    comparar_csv_filtrado("resultados_test/referencia.csv", filename)    
    print("Página cargada correctamente.") #Final test

except Exception as e:
    print("Se produjo un error:")
    traceback.print_exc()

finally:
    if driver:
        driver.quit()