Feature: Target Circle page

  Scenario: User can see Target Circle benefits
    Given Open Target Circle page
    Then At least 10 benefit cells are shown
    #Note that in some instances less than 10 benefits will be visible depending on the user's
    #market and Target's discretion.
    #In such instances the test case will fail.