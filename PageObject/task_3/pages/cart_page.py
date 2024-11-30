from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC


class CartPage(BasePage):

    PAGE_URL = Links.CART_PAGE

    CHECKOUT_BUTTON = ("xpath", "//button[text()='Checkout']")

    def click_checkout(self):
        self.wait.until(EC.element_to_be_clickable(
            self.CHECKOUT_BUTTON)).click()
