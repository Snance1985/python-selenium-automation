from selenium.webdriver.common.by import By
from pages.base_page import Page


class CartPage(Page):
    EMPTY_CART_MSG = (By.CSS_SELECTOR, "[data-test='boxEmptyMsg']")
    CART_ITEM_NAME = (By.CSS_SELECTOR, "[data-test='cartItem-title']")
    CART_TOTAL_TEXT = (By.CSS_SELECTOR, "h2 [class*='styles_cart-summary-span']")

    empty_cart_msg = 'Your cart is empty'

    def open_cart_page(self):
        self.open_url('/cart')

    def verify_empty_cart_msg(self):
        self.verify_partial_text(self.empty_cart_msg, *self.EMPTY_CART_MSG)

    def verify_cart_items(self, amount):
        self.wait_until_element_present(*self.CART_TOTAL_TEXT)
        cart_summary = self.find_element(*self.CART_TOTAL_TEXT).text
        assert f'{amount} item' in cart_summary, f"Expected {amount} items but got {cart_summary}"

    def verify_product_in_cart(self, expected_product):
        product_in_cart = self.find_element(*self.CART_ITEM_NAME).text
        assert product_in_cart[:20] == expected_product[:20], \
            f'Expected product {expected_product[:20]} but got {product_in_cart[:20]}'