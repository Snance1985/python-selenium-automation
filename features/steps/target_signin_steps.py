from selenium.webdriver.common.by import By
from behave import when, then

@when('Click on Account icon')
def click_account(context):
    context.driver.find_element(By.XPATH, "//*[@data-test='@web/AccountLink']").click()

@when('Click on Sign In from navigation menu')
def click_sign_in(context):
    context.driver.find_element(By.XPATH, "//*[@data-test='accountNav-signIn']").click()

@then('Sign In form is opened')
def verify_sign_in(context):
    header = context.driver.find_element(
        By.XPATH, "//h1[text()='Sign in or create account']"
    )
    assert header.is_displayed(), "Sign In page did not open"