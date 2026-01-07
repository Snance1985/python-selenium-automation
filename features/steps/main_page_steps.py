from behave import given

@given('Open Target main page')
def open_main(context):
    print("Opening Target main page...")
    context.driver.get('https://www.target.com/')