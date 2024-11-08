from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By


def modal_window(driver):
    driver.get("http://the-internet.herokuapp.com/entry_ad")

    sleep(3)

    close_button = driver.find_element(
        By.XPATH, "//*[@id='modal']/div[2]/div[3]/p")
    close_button.click()


chrome_driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()))
modal_window(chrome_driver)
sleep(2)
chrome_driver.quit()

firefox_driver = webdriver.Firefox(
    service=FirefoxService(GeckoDriverManager().install()))
modal_window(firefox_driver)
sleep(2)
firefox_driver.quit()
