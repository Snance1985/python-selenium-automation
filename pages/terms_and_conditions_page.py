from pages.base_page import Page

class TermsAndConditionsPage(Page):

    def verify_page_opened(self):
        self.verify_url_contains('terms-conditions')