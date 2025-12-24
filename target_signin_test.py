from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Setup Chrome in Incognito mode
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")

driver_path = ChromeDriverManager().install()
service = Service(driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.maximize_window()

# 1. Open Target homepage
driver.get("https://www.target.com/")

# 2. Navigate directly to Sign-In page
driver.get("https://www.target.com/account/signin")

# 3. Verify Sign In page opened
sign_in_text = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located(
        (By.XPATH, "//h1[contains(text(),'Sign in or create account')]")
    )
).text
print(sign_in_text)

# Verify Sign In button exists
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
        (By.XPATH, "//button[contains(text(),'Sign in')]")
    )
)

print("Test case passed: Sign In page opened successfully")

# 4. Quit browser
driver.quit()