import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from form_fill import Form_fill


@pytest.mark.smoke
@pytest.mark.parametrize(
        "browser, first_name, last_name, \
        address, city, country, email, phone, \
        job_title, company",
        [("chrome", "Иван", "Петров", "Ленина, \
           55-3", "Россия", "Москва", "test@skypro.com",
            "+7985899998787", "QA", "SkyPro"),])
def test_form_fill(browser, first_name, last_name, address, city,
                   country, email, phone, job_title, company):
    if browser == "chrome":
        driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()))
    else:
        raise ValueError(f"Unsupported browser: {browser}")
    driver.maximize_window()

    try:
        form = Form_fill(driver)
        form.fill_form(first_name, last_name, address, city,
                       country, email, phone, job_title, company)
        form.submit()
        assert driver.find_element(
            By.CSS_SELECTOR, "#zip-code").value_of_css_property(
                'background-color') == 'rgba(248, 215, 218, 1)'
        elements = driver.find_elements(By.CSS_SELECTOR, ".col-md-4.col-md-3")
        for element in elements:
            assert element.value_of_css_property(
                'background-color') == 'rgba(209, 231, 221, 1)'
    finally:
        driver.quit()
