from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")

driver_path = ChromeDriverManager().install()
service = Service(driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.maximize_window()
driver.get('https://www.amazon.com/')
driver.get('https://www.amazon.com/ap/register')

#Amazon logo
driver.find_element(By.XPATH, '//i[@class="a-icon a-icon-logo"]')

#Email field
driver.find_element(By.ID, 'ap_email_login')

#Continue button
driver.find_element(By.XPATH, "//input[@class='a-button-input']")

#Conditions of use link
driver.find_element(By.XPATH, "//a[text()='Conditions of Use']")

#Privacy Notice link
driver.find_element(By.XPATH, "//a[text()='Privacy Notice']")

#Need help link
driver.find_element(By.XPATH, "//a[contains(text(),'Need help')]")
