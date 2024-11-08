from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By


def run_test(driver):
    driver.get("http://uitestingplayground.com/dynamicid")

    sleep(1)

    blue_button = driver.fine_element((By.CSS_SELECTOR, '.btn-primary'))
    blue_button.click()

    sleep(3)


chrome_driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()))
chrome_driver.maximize_window()

for i in range(3):
    run_test(chrome_driver)
chrome_driver.quit()


firefox_driver = webdriver.Firefox(
    service=FirefoxService(GeckoDriverManager().install()))
firefox_driver.maximize_window()

for i in range(3):
    run_test(firefox_driver)
firefox_driver.quit()
