# Created by lana at 12/27/25
Feature: Test cases for Cart

  Scenario: User sees empty cart message
    Given Open Target main page
    When Click on Cart icon
    Then Your cart is empty message is shown