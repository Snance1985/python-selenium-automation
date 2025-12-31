from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep


# Setup Chrome in Incognito mode
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")
driver_path = ChromeDriverManager().install()
service = Service(driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.maximize_window()


# open the url
driver.get("https://stackoverflow.com/users/signup")


#find locators
#"Create your account" header
driver.find_element(By.CSS_SELECTOR, "h1.fs-headline1")
#"Terms of Service" and "Privacy Policy" box
driver.find_element(By.CSS_SELECTOR, "div.js-terms")
#Email field
driver.find_element(By.ID, "email")
#Password field
driver.find_element(By.ID, "password")
#Reveal Password button
driver.find_element(By.CSS_SELECTOR, "svg.js-show-password")
#Signup button
driver.find_element(By.ID, "submit-button")
#Signup with Google button
driver.find_element(By.CSS_SELECTOR, "button.s-btn__icon.s-btn__google")
#Signup with Github button
driver.find_element(By.CSS_SELECTOR, "button.s-btn__icon.s-btn__github")
#Stack Overflow for Teams
driver.find_element(By.CSS_SELECTOR, 'a[href*="stackoverflow.com/teams"]')

#sleep
sleep(7)


driver.quit()