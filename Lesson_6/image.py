from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()))
wait = WebDriverWait(driver, 15)

driver.get(
    "https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

wait.until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#text'), "Done!"))

container = driver.find_elements(By.CSS_SELECTOR, "#image-container img")
print(container[2].get_attribute("src"))

driver.quit()
