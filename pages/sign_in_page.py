from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep

class SignInPage(Page):

    TC_LINK = (By.CSS_SELECTOR, "a[aria-label*='terms & conditions']")
    SIGN_IN_HEADER = (By.XPATH, "//h1[text()='Sign in or create account']")

    def verify_sign_in_page_opened(self):
        self.wait_until_element_present(*self.SIGN_IN_HEADER)

    def open_target_signin(self):
        self.open_url('/orders?lnk=acct_nav_my_account')
        sleep(1)

    def click_tc_link(self):
        self.wait_until_clickable_click(*self.TC_LINK)