from behave import when, then

@when('Click on Account icon')
def click_account(context):
    context.app.header.click_account()

@when('Click on Sign In from navigation menu')
def click_sign_in(context):
    context.app.header.click_side_nav_sign_in()

@then('Sign In form is opened')
def verify_sign_in(context):
    context.app.sign_in_page.verify_sign_in_page_opened()
