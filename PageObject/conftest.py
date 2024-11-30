# файл для хранения фикстур
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


# фикстура которая инициализирует драйвер для тестов
# autouse=True позволяет использовать её автоматически для каждого теста
# scope="function" создает экземпляр драйвера для каждого теста отдельно
@pytest.fixture(scope="function", autouse=True)
def driver(request):
    options = Options()
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()
