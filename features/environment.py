from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def before_scenario(context, scenario):
    # Chrome options
    options = Options()
    options.add_argument("--start-maximized")
    # options.add_argument("--incognito")  # optional, can add if you want

    # Start Chrome
    service = Service(ChromeDriverManager().install())
    context.driver = webdriver.Chrome(service=service, options=options)

def after_scenario(context, scenario):
    # Close the browser
    context.driver.quit()