Feature: Test cases for Cart

  Scenario: User sees empty cart message
    Given Open Target main page
    When Click on Cart icon
    Then Your cart is empty message is shown

  Scenario: User can add a product to the cart
    Given Open Target main page
    When Search for tea
    And Click on the first product in results
    And Add product to cart
    Then Verify the cart has at least 1 item

  Scenario: User can add a product to the cart and verify the amount of items in the cart
    Given Open Target main page
    When Search for popcorn
    And Click on the first product in results
    And Add product to cart
    And Click on Cart icon
    Then Verify the cart has at least 1 item
    And Verify cart has product in it
