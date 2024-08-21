Feature: Login
  As a user
  I want to log in to the application
  So that I can access the inventory page

  Scenario: Successful login
    Given I am on the login page
    When I enter username "standard_user" and password "secret_sauce"
    And I click the login button
    Then I should be logged in
    And I should be on the inventory page
