from links import Links
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

DELAY = ("id", "delay")
SEVEN = ("xpath", "//*[@id='calculator']/div[2]/span[1]")
EIGHT = ("xpath", "//*[@id='calculator']/div[2]/span[2]")
SUM = ("xpath", "//*[@id='calculator']/div[2]/span[4]")
EQUALS = ("xpath", "//*[@id='calculator']/div[2]/span[15]")


class Calculator:

    PAGE_URL = Links.MAIN

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10, poll_frequency=1)
        self.driver.maximize_window()

    def open(self):
        self.driver.get(self.PAGE_URL)

    def clear(self):
        self.wait.until(
            EC.presence_of_element_located((DELAY))).clear()

    def enter_delay(self, value):
        self.wait.until(
            EC.presence_of_element_located((DELAY))).send_keys(value)

    def button_7(self):
        self.wait.until(
            EC.presence_of_element_located((SEVEN))).click()

    def sum(self):
        self.wait.until(
            EC.presence_of_element_located((SUM))).click()

    def button_8(self):
        self.wait.until(
            EC.presence_of_element_located((EIGHT))).click()

    def equals(self):
        self.wait.until(
            EC.presence_of_element_located((EQUALS))).click()
