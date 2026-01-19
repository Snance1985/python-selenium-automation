from behave import when, then


@when('Click on cart icon')
def click_cart(context):
    context.app.header.click_cart()


@when('Search for {product}')
def search_product(context, product):
    context.app.header.search(product)


@then('Verify {expected_amount} top header links are shown')
def verify_top_links_shown(context, expected_amount):
    context.app.header.verify_header_links_count(int(expected_amount))