import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def input(driver):
    driver.get("http://the-internet.herokuapp.com/login")

    input_user = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((
            By.ID, 'username')))
    input_user.send_keys("tomsmith")
    time.sleep(3)

    input_password = driver.find_element(By.ID, 'password')
    input_password.send_keys("SuperSecretPassword!")
    time.sleep(3)

    login_button = driver.find_element(By.XPATH, '//*[@id="login"]/button/i')
    login_button.click()
    time.sleep(5)


chrome_driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()))
input(chrome_driver)
chrome_driver.quit()


firefox_driver = webdriver.Firefox(
    service=FirefoxService(GeckoDriverManager().install()))
input(firefox_driver)
firefox_driver.quit()
