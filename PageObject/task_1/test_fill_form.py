import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from main_page import MainPage


@pytest.mark.page_object
@pytest.mark.parametrize(
        "first_name, last_name, \
        address, city, country, email, phone, \
        job_position, company",
        [("Иван", "Петров", "Ленина, \
           55-3", "Россия", "Москва", "test@skypro.com",
            "+7985899998787", "QA", "SkyPro"),])
def test_form_fill(first_name, last_name, address, city, country,
                   email, phone, job_position, company):
    driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()))
    form = MainPage(driver)
    form.open()
    form.enter_first_name(first_name)
    form.enter_last_name(last_name)
    form.enter_address(address)
    form.enter_city(city)
    form.enter_country(country)
    form.enter_email(email)
    form.enter_phone(phone)
    form.enter_job_position(job_position)
    form.enter_company(company)
    form.submit()
    assert driver.find_element(
        "css selector", "#zip-code").value_of_css_property(
            'background-color') == 'rgba(248, 215, 218, 1)'
    elements = driver.find_elements("css selector", ".col-md-4.col-md-3")
    for element in elements:
        assert element.value_of_css_property(
            'background-color') == 'rgba(209, 231, 221, 1)'
    driver.quit()
