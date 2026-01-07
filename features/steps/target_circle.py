from selenium.webdriver.common.by import By
from behave import given, then
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

CIRCLE_PAGE = 'https://www.target.com/circle'
BENEFIT_CARDS = (By.CSS_SELECTOR, "div[data-test='@web/SlingshotComponents/common/Storycard']")

@given('Open Target Circle page')
def open_target_circle(context):
    context.driver.get(CIRCLE_PAGE)

@then('At least 10 benefit cells are shown')
def verify_benefit_cards(context):
    WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located(BENEFIT_CARDS)
    )
    cards = context.driver.find_elements(*BENEFIT_CARDS)
    print(f"Found {len(cards)} benefit cards")
    assert len(cards) >= 10, f"Expected at least 10 benefit cards, found {len(cards)}"