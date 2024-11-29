import pytest

from pages.login_page import LoginPage
from pages.product_page import ProductsPage
from pages.checkout_page import CheckoutPage
from pages.overview_page import OverviewPage
from pages.cart_page import CartPage


class BaseTest:

    login_page: LoginPage
    product_page: ProductsPage
    checkout_page: CheckoutPage
    overview_page: OverviewPage
    cart_page: CartPage

    @pytest.fixture(autouse=True)
    def setup(self, request, driver):
        request.cls.driver = driver
        request.cls.login_page = LoginPage(driver)
        request.cls.product_page = ProductsPage(driver)
        request.cls.checkout_page = CheckoutPage(driver)
        request.cls.overview_page = OverviewPage(driver)
        request.cls.cart_page = CartPage(driver)
