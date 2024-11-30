from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC


class ProductsPage(BasePage):

    PAGE_URL = Links.PRODUCTS_PAGE

    BACKPACK = ("id", "add-to-cart-sauce-labs-backpack")
    T_SHIRT = ("id", "add-to-cart-sauce-labs-bolt-t-shirt")
    ONESIE = ("id", "add-to-cart-sauce-labs-onesie")

    def add_backpack(self):
        self.wait.until(EC.element_to_be_clickable(self.BACKPACK)).click()

    def add_t_shirt(self):
        self.wait.until(EC.element_to_be_clickable(self.T_SHIRT)).click()

    def add_onesie(self):
        self.wait.until(EC.element_to_be_clickable(self.ONESIE)).click()
