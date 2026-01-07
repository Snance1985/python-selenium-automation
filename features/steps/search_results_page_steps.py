from selenium.webdriver.common.by import By
from behave import when, then

# Locators
SEARCH_FIELD = (By.ID, 'search')
SEARCH_ICON = (By.CSS_SELECTOR, "[data-test='@web/Search/SearchButton']")
SEARCH_RESULTS_TEXT = (By.XPATH, "//div[contains(@class,'styles_listingPageResultsCount')]")

@when('Search for {product}')
def search_product(context, product):
    print(f"Searching for {product}...")
    search_box = context.driver.find_element(*SEARCH_FIELD)
    search_box.clear()
    search_box.send_keys(product)
    context.driver.find_element(*SEARCH_ICON).click()

@then('Search results for {product_result} are shown')
def verify_search_results(context, product_result):
    actual_text = context.driver.find_element(*SEARCH_RESULTS_TEXT).text
    print(f"Search results found: {actual_text}")
    assert product_result in actual_text, \
        f'Expected text "{product_result}" not in actual text "{actual_text}"'