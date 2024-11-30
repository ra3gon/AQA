import pytest
from calculator import Calculator
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

SPINNER = ("id", "spinner")
RESULT_FIELD = ("xpath", "//*[@id='calculator']/div[1]/div")


@pytest.mark.page_object
def test_calculator(driver):
    operation = Calculator(driver)
    operation.open()
    operation.clear()
    operation.enter_delay(45)
    operation.button_7()
    operation.sum()
    operation.button_8()
    operation.equals()

    WebDriverWait(driver, 45).until(
        EC.invisibility_of_element_located(SPINNER))

    result_field = driver.find_element(*RESULT_FIELD)

    assert result_field.text == "15", \
        f"Ожидался результат 15, но был {result_field.text}"
