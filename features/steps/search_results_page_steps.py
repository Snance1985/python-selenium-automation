from behave import when, then
from selenium.webdriver.support import expected_conditions as EC

@when('Click on Add to Cart button')
def click_add_to_cart(context, ADD_TO_CART_BTN, SIDE_NAV_ADD_TO_CART_BTN):
    context.driver.wait.until(
        EC.element_to_be_clickable(ADD_TO_CART_BTN),
        message='Add To Cart button not clickable'
    ).click()

    context.driver.wait.until(
        EC.element_to_be_clickable(SIDE_NAV_ADD_TO_CART_BTN),
        message='Side navigation Add To Cart Btn not clickable'
    )


@when('Store product name')
def store_product_name(context):
    context.app.search_results_page.store_product_name(context)


@when('Confirm Add to Cart button from side navigation')
def side_nav_click_add_to_cart(context):
    context.app.search_results_page.confirm_side_nav_add_to_cart()


@then('Search results for {expected_product} are shown')
def verify_search_results(context, expected_product):
    context.app.search_results_page.verify_search_results(expected_product)