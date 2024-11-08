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
    driver.get("http://the-internet.herokuapp.com/inputs")

    search_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((
            By.CSS_SELECTOR, '.example [type="number"]')))
    time.sleep(3)
    search_input.send_keys("1000")
    time.sleep(3)
    search_input.clear()
    time.sleep(3)
    search_input.send_keys("999")
    time.sleep(2)


chrome_driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()))
input(chrome_driver)
chrome_driver.quit()


firefox_driver = webdriver.Firefox(
    service=FirefoxService(GeckoDriverManager().install()))
input(firefox_driver)
firefox_driver.quit()
