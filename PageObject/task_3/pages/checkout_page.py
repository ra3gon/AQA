from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage(BasePage):

    PAGE_URL = Links.CHECKOUT_PAGE

    FIRSTNAME_FIELD = ("id", "first-name")
    LASTNAME_FIELD = ("id", "last-name")
    POSTALCODE_FIELD = ("id", "postal-code")
    SUBMIT_BUTTON = ("id", "continue")

    def enter_firstname(self, firstname):
        self.wait.until(
            EC.element_to_be_clickable(
                self.FIRSTNAME_FIELD)).send_keys(firstname)

    def enter_lastname(self, lastname):
        self.wait.until(
            EC.element_to_be_clickable(
                self.LASTNAME_FIELD)).send_keys(lastname)

    def enter_postalcode(self, postalcode):
        self.wait.until(
            EC.element_to_be_clickable(
                self.POSTALCODE_FIELD)).send_keys(postalcode)

    def click_submit_button(self):
        self.wait.until(
            EC.element_to_be_clickable(
                self.SUBMIT_BUTTON)).click()
