from selenium.webdriver.common.by import By
from behave import given, then
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


COLOR_OPTIONS = (By.CSS_SELECTOR, "a[aria-label^='color']")
SELECTED_COLOR = (
    By.CSS_SELECTOR,
    "a[aria-current='true'][aria-label^='color']"
)

@given('Open target product A-87903492 page')
def open_target(context):
    context.driver.get(
        "https://www.target.com/p/alpine-swiss-mens-fashion-sneakers-lightweight-knit-tennis-shoes/-/A-87903492?preselect=88146116#lnk=sametab"
    )
    WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located(COLOR_OPTIONS)
    )

@then('Verify user can click through colors')
def click_and_verify_colors(context):
    expected_colors = {'black', 'gray', 'olive', 'white'}
    actual_colors = set()

    wait = WebDriverWait(context.driver, 15)

    color_elements = context.driver.find_elements(*COLOR_OPTIONS)
    print(f"Found {len(color_elements)} color swatches")

    assert len(color_elements) >= 4, "Not enough color options found"

    for i in range(len(color_elements)):
        # Re-find elements to avoid stale element issues
        color_elements = context.driver.find_elements(*COLOR_OPTIONS)
        color_elements[i].click()

        selected = wait.until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "a[aria-current='true'][aria-label^='color']")
            )
        )

        label = selected.get_attribute("aria-label")
        color = label.split(", ")[1].lower()

        print("Selected color:", color)
        actual_colors.add(color)

    print("Actual colors found:", actual_colors)

    assert actual_colors == expected_colors, \
        f"Expected {expected_colors}, but got {actual_colors}"