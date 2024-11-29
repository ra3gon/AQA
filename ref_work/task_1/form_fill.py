from selenium.webdriver.common.by import By


class Form_fill:
    def __init__(self, driver):
        self.driver = driver
        self.driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    def fill_form(self, first_name, last_name, address, city, country, email,
                  phone, job_title, company):
        self.driver.find_element(
            By.CSS_SELECTOR, 'input[name="first-name"]').send_keys(first_name)
        self.driver.find_element(
            By.CSS_SELECTOR, 'input[name="last-name"]').send_keys(last_name)
        self.driver.find_element(
            By.CSS_SELECTOR, 'input[name="address"]').send_keys(address)
        self.driver.find_element(
            By.CSS_SELECTOR, 'input[name="city"]').send_keys(city)
        self.driver.find_element(
            By.CSS_SELECTOR, 'input[name="country"]').send_keys(country)
        self.driver.find_element(
            By.CSS_SELECTOR, 'input[name="e-mail"]').send_keys(email)
        self.driver.find_element(
            By.CSS_SELECTOR, 'input[name="phone"]').send_keys(phone)
        self.driver.find_element(
            By.CSS_SELECTOR, 'input[name="job-position"]').send_keys(job_title)
        self.driver.find_element(
            By.CSS_SELECTOR, 'input[name="company"]').send_keys(company)

    def submit(self):
        self.driver.find_element(
            By.CSS_SELECTOR, 'button[type="submit"]').click()
