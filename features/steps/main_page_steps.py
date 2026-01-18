from behave import given

@given('Open Target main page')
def open_main(context):
    print("Opening Target main page...")
    context.app.main_page.open_main_page()