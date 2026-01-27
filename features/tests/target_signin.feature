Feature: Target Sign In

  Scenario: Logged out user can navigate to Sign In
    Given Open Target main page
    When Click on Account icon
    And Click on Sign In from navigation menu
    Then Sign In form is opened

  Scenario: User is able to open Terms and Conditions
    Given Open Target sign in page
    And Store original window
    When Click Target terms and conditions link
    And Switch to new window
    Then Verify Terms and Conditions page opened
    And Close current page
    And Return to original window