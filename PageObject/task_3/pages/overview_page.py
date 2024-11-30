from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC


class OverviewPage(BasePage):

    PAGE_URL = Links.OVERVIEW_PAGE

    TOTAL_VALUE = ("xpath", "//div[@data-test='total-label']")

    def get_total(self):
        self.wait.until(EC.text_to_be_present_in_element(self.TOTAL_VALUE, ""))

        total_text = self.driver.find_element(*self.TOTAL_VALUE).text

        if '$' in total_text:
            total_value = total_text.split('$')[1]
            return total_value
        else:
            print("Символ '$' не найден в тексте.")
            return None
