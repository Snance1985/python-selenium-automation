Feature: Tests for search

  Scenario Outline: User can search for a product
    Given Open Target main page
    When Search for <product>
    Then Search results for <product_result> are shown

    Examples:
      |product  |product_result  |
      |tea      |tea             |
      |coffee   |coffee          |
      |xbox     |xbox            |
      |tv       |tv              |