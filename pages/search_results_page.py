from selenium.webdriver.common.by import By
from pages.base_page import Page


class SearchResultsPage(Page):
    SEARCH_RESULTS_TEXT = (By.XPATH, "//div[contains(@class,'styles_listingPageResultsCount')]")
    ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[id*='addToCartButton']")
    SIDE_NAV_ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[data-test='content-wrapper'] [id*='addToCart']")
    SIDE_NAV_PRODUCT_NAME = (By.CSS_SELECTOR, "[data-test='content-wrapper'] h4")

    def verify_search_results(self, expected_product):
        self.verify_partial_text(expected_product, *self.SEARCH_RESULTS_TEXT)

    def click_add_to_cart(self):
        self.wait_until_clickable_click(*self.ADD_TO_CART_BTN)

    def store_product_name(self, context):
        context.product_before_adding = self.find_element(*self.SIDE_NAV_PRODUCT_NAME).text

    def confirm_side_nav_add_to_cart(self):
        self.wait_until_clickable_click(*self.SIDE_NAV_ADD_TO_CART_BTN)