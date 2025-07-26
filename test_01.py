import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# Set up Chrome WebDriver service
service = Service(r"C:\drivers\chromedriver.exe")
driver = None

try:
    # Initialize Chrome WebDriver
    driver = webdriver.Chrome(service=service)
    # Navigate to the test page
    driver.get("https://demoqa.com/text-box")

    # Loop to fill the form 5 times
    for i in range(5):
        # Find and fill the Full Name field
        nom = driver.find_element(By.XPATH, "//input[@id='userName']")
        nom.clear()  # Clear previous input
        nom.send_keys(f"Rodrigo_{i+1}")
        time.sleep(1)

        # Find and fill the Email field
        corr = driver.find_element(By.XPATH, "//*[@id='userEmail']")
        corr.clear()  # Clear previous input
        corr.send_keys(f"test{i+1}@test.com")
        time.sleep(1)

        # Find and fill the Current Address field
        curr = driver.find_element(By.XPATH, "//textarea[@id='currentAddress']")
        curr.clear()  # Clear previous input
        curr.send_keys(f"direccion_test_{i+1}")
        time.sleep(1)

        # Find and fill the Permanent Address field
        perm = driver.find_element(By.XPATH, "//textarea[@id='permanentAddress']")
        perm.clear()  # Clear previous input
        perm.send_keys(f"direccion_permanente_test_{i+1}")
        time.sleep(1)

        # Scroll down the page to make the submit button visible
        driver.execute_script("window.scrollTo(0,500)")
        time.sleep(2)
        # Click the submit button
        driver.find_element(By.XPATH, "//button[@id='submit']").click()
        time.sleep(5)

        print(f"Test iteration {i+1} completed")

    print("All tests completed successfully")

except Exception as e:
    # Handle any exceptions that occur during test execution
    print(f"Se produjo un error: {e}")

finally:
    # Clean up by closing the browser
    if driver:
        driver.quit()