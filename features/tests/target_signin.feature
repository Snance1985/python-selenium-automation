Feature: Target Sign In

  Scenario: Logged out user can navigate to Sign In
    Given Open Target main page
    When Click on Account icon
    And Click on Sign In from navigation menu
    Then Sign In form is opened