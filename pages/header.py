from selenium.webdriver.common.by import By
from pages.base_page import Page

class Header(Page):

    CART_ICON = (By.CSS_SELECTOR, "[data-test='@web/CartIcon']")
    SEARCH_FIELD = (By.ID, 'search')
    SEARCH_ICON = (By.CSS_SELECTOR, "[data-test='@web/Search/SearchButton']")

    ACCOUNT_ICON = (By.XPATH, "//*[@data-test='@web/AccountLink']")
    SIDE_NAV_SIGN_IN = (By.XPATH, "//*[@data-test='accountNav-signIn']")

    HEADER_LINKS = (By.CSS_SELECTOR, "[data-test*='@web/GlobalHeader/UtilityHeader/']")

    def search(self, product):
        self.input_text(product, *self.SEARCH_FIELD)
        self.click(*self.SEARCH_ICON)

    def click_cart(self):
        self.wait_until_clickable_click(*self.CART_ICON)

    def click_account(self):
        self.wait_until_clickable_click(*self.ACCOUNT_ICON)

    def click_side_nav_sign_in(self):
        self.wait_until_clickable_click(*self.SIDE_NAV_SIGN_IN)

    def verify_header_links_count(self, expected_amount):
        links = self.driver.find_elements(*self.HEADER_LINKS)
        assert len(links) == expected_amount, \
            f'Expected {expected_amount} header links, but got {len(links)}'

