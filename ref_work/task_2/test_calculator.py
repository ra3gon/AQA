import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    yield driver
    driver.quit()


@pytest.mark.smoke
def test_calculator(driver):
    delay_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "delay")))

    delay_field.clear()
    delay_field.send_keys("45")

    driver.find_element(
        "xpath", '//*[@id="calculator"]/div[2]/span[1]').click()
    driver.find_element(
        "xpath", '//*[@id="calculator"]/div[2]/span[4]').click()
    driver.find_element(
        "xpath", '//*[@id="calculator"]/div[2]/span[2]').click()
    driver.find_element(
        "xpath", '//*[@id="calculator"]/div[2]/span[15]').click()

    WebDriverWait(driver, 45).until(
        EC.invisibility_of_element_located((By.ID, "spinner")))

    result_field = driver.find_element(
        "xpath", '//*[@id="calculator"]/div[1]/div')

    assert result_field.text == "15", \
        f"Ожидался результат 15, но был {result_field.text}"
