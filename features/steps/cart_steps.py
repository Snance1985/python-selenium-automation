from selenium.webdriver.common.by import By
from behave import when, then
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

# Empty cart
EMPTY_CART_TEXT = (By.XPATH, "//*[text()='Your cart is empty']")

# Search results
FIRST_PRODUCT = (By.CSS_SELECTOR, "[data-test='productTile']")

# PDP (Product Detail Page)
ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "[id^='addToCartButton']")

# Cart
VIEW_CART_BUTTON = (By.CSS_SELECTOR, "[data-test='viewCartBtn']")
CART_ITEMS = (By.CSS_SELECTOR, "[data-test='cartItem']")

# Cart icon
CART_ICON = (By.XPATH, "//*[@data-test='@web/CartLink']")


@when('Click on Cart icon')
def click_cart(context):
    context.driver.find_element(*CART_ICON).click()


@then('Your cart is empty message is shown')
def verify_empty_cart(context):
    empty_msg = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located(EMPTY_CART_TEXT)
    )
    assert empty_msg.is_displayed(), "Empty cart message not displayed"


@when('Click on the first product in results')
def click_first_product(context):
    first_product = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable(FIRST_PRODUCT)
    )
    first_product.click()
    sleep(5)

@when('Add product to cart')
def add_product_to_cart(context):
    sleep(15)
    add_to_cart = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable(ADD_TO_CART_BUTTON)
    )
    add_to_cart.click()
    sleep(5)

@when('Click view cart and checkout')
def click_view_cart_and_checkout(context):
    view_cart = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable(VIEW_CART_BUTTON)
    )
    view_cart.click()
    sleep(5)

@then('Verify the cart has at least 1 item')
@then('Verify cart has product in it')
def verify_cart_has_product(context):
    items = WebDriverWait(context.driver, 10).until(
        EC.presence_of_all_elements_located(CART_ITEMS)
    )
    assert len(items) >= 1, f"Expected at least 1 cart item, found {len(items)}"
