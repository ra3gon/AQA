import pytest
from base.base_tect import BaseTest


class TestCart(BaseTest):

    @pytest.mark.page_object
    def test_cart_total(self):
        self.login_page.open()
        self.login_page.enter_login("standard_user")
        self.login_page.enter_password("secret_sauce")
        self.login_page.click_submit_button()
        self.product_page.add_backpack()
        self.product_page.add_t_shirt()
        self.product_page.add_onesie()
        self.checkout_page.open()
        self.checkout_page.enter_firstname("Aleksey")
        self.checkout_page.enter_lastname("Razgon")
        self.checkout_page.enter_postalcode(123)
        self.checkout_page.click_submit_button()

        # получаем общую сумму
        overview_page = self.overview_page
        total_value = overview_page.get_total()

        # проверка
        expected_total_value = "58.29"
        assert total_value == expected_total_value, \
            f"Expected {expected_total_value}, but got {total_value}"
