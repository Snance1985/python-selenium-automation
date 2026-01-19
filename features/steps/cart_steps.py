from behave import when, then


@when('Open cart page')
def open_cart(context):
    context.app.cart_page.open_cart_page()


@then('Verify cart has {amount} item(s)')
def verify_cart_items(context, amount):
    context.app.cart_page.verify_cart_items(amount)


@then('Verify product in cart is correct')
def verify_product(context):
    expected = context.product_before_adding
    context.app.cart_page.verify_product_in_cart(expected)


@then('Your cart is empty message is shown')
def verify_empty_cart_msg(context):
    context.app.cart_page.verify_empty_cart_msg()