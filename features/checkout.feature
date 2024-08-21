Feature: Checkout
  As a logged-in user
  I want to complete the checkout process
  So that I can purchase the items in my cart

  Scenario: Fill checkout form
    Given I am logged in as "standard_user" with password "secret_sauce"
    And I am on the checkout page
    When I fill the checkout form with "John", "Doe", and "123 Main St"
    And I click the continue button
    Then I should see the checkout step two page

  Scenario: Complete checkout
    Given I am logged in as "standard_user" with password "secret_sauce"
    And I have added an item to the cart
    And I am on the cart page
    When I click the checkout button
    And I fill the checkout form with "John", "Doe", and "123 Main St"
    And I click the continue button
    Then I should see the overview page with item "Sauce Labs Backpack" and price "29.99"
    And I should see the tax value "2.40"
    And I should see the total value "32.39"
    When I click the finish button
    Then I should see the order confirmation page
