from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By


def run_test(driver):
    driver.get("http://the-internet.herokuapp.com/add_remove_elements/")

    add_element = driver.find_element(
        By.CSS_SELECTOR, "button[onclick='addElement()']")

    for i in range(5):
        add_element.click()

    remove_element = driver.find_elements(
        By.CSS_SELECTOR, "button[onclick='deleteElement()']")
    print(len(remove_element))

    sleep(3)


chrome_driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()))
chrome_driver.maximize_window()
run_test(chrome_driver)
chrome_driver.quit()

firefox_driver = webdriver.Firefox(
    service=FirefoxService(GeckoDriverManager().install()))
firefox_driver.maximize_window()
run_test(firefox_driver)
firefox_driver.quit()
