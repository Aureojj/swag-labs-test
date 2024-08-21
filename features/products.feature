Feature: Products
  As a logged-in user
  I want to view and verify product details
  So that I can make informed purchasing decisions

  Scenario: View products
    Given I am logged in as "standard_user" with password "secret_sauce"
    When I view the products
    Then I should be on the products page
    And the products page should be displayed
    And the URL should be "https://www.saucedemo.com/inventory.html"

  Scenario: Verify product details
    Given I am logged in as "standard_user" with password "secret_sauce"
    And I am on the products page
    When I get the product list
    Then each product should have a name
    And each product should have a description
    And each product should have a price
