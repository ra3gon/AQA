from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


FIRST_NAME = ("name", "first-name")
LAST_NAME = ("name", "last-name")
ADDRESS = ("name", "address")
CITY = ("name", "city")
COUNTRY = ("name", "country")
EMAIL = ("name", "e-mail")
PHONE = ("name", "phone")
JOB_POSITION = ("name", "job-position")
COMPANY = ("name", "company")
SUBMIT_BUTTON = ("css selector", 'button[type="submit"]')


class MainPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10, poll_frequency=1)
        self.driver.maximize_window()

    def open(self):
        self.driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    def enter_first_name(self, first_name):
        self.wait.until(
            EC.presence_of_element_located(
                (FIRST_NAME))).send_keys(first_name)

    def enter_last_name(self, last_name):
        self.wait.until(
            EC.presence_of_element_located(
                (LAST_NAME))).send_keys(last_name)

    def enter_address(self, address):
        self.wait.until(
            EC.presence_of_element_located(
                (ADDRESS))).send_keys(address)

    def enter_city(self, city):
        self.wait.until(
            EC.presence_of_element_located(
                (CITY))).send_keys(city)

    def enter_country(self, country):
        self.wait.until(
            EC.presence_of_element_located(
                (COUNTRY))).send_keys(country)

    def enter_email(self, email):
        self.wait.until(
            EC.presence_of_element_located(
                (EMAIL))).send_keys(email)

    def enter_phone(self, phone):
        self.wait.until(
            EC.presence_of_element_located(
                (PHONE))).send_keys(phone)

    def enter_job_position(self, job_position):
        self.wait.until(
            EC.presence_of_element_located(
                (JOB_POSITION))).send_keys(job_position)

    def enter_company(self, company):
        self.wait.until(
            EC.presence_of_element_located(
                (COMPANY))).send_keys(company)

    def submit(self):
        self.wait.until(
            EC.presence_of_element_located(
                (SUBMIT_BUTTON))).click()
