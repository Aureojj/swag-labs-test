Feature: Cart
  As a logged-in user
  I want to manage my cart
  So that I can purchase the items I want

  Scenario: Add product to cart
    Given I am logged in as "standard_user" with password "secret_sauce"
    And I am on the products page
    When I add a product to the cart
    Then the product should be in the cart

  Scenario: Remove product from cart
    Given I am logged in as "standard_user" with password "secret_sauce"
    And I am on the products page
    And I have added a product to the cart
    When I remove the product from the cart
    Then the product should not be in the cart

  Scenario: View cart
    Given I am logged in as "standard_user" with password "secret_sauce"
    When I view the cart
    Then I should be on the cart page
    And the cart page should be displayed

  Scenario: Go to checkout
    Given I am logged in as "standard_user" with password "secret_sauce"
    And I am on the cart page
    When I click the checkout button
    Then I should be on the checkout page
    And the checkout page should be displayed
