Feature: Login
  As a standard user
  I want to log in to the Sauce Demo site
  So that I can access the inventory page

  Scenario: Successful login
    Given I am on the login page
    When I enter the username
    And I enter the password
    And I click the login button
    Then I should be redirected to the inventory page
