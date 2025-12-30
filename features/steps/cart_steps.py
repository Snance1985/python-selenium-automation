from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from behave import when, then

@when('Click on Cart icon')
def click_cart(context):
    context.driver.find_element(By.XPATH, "//*[@data-test='@web/CartLink']").click()

@then('Your cart is empty message is shown')
def verify_empty_cart(context):
    expected_text = 'Your cart is empty'
    actual_text = context.driver.find_element(
        By.XPATH, "//*[text()='Your cart is empty']"
    ).text
    assert expected_text == actual_text, \
        f'Expected "{expected_text}" but got "{actual_text}"'