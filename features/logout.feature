Feature: Logout
  As a logged-in user
  I want to log out of the Sauce Demo site
  So that I can end my session

  Scenario: Successful logout
    Given I am logged in as a standard user
    When I click the menu button
    And I click the logout button
    Then I should be redirected to the login page
