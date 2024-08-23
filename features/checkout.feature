Feature: Checkout
  As a logged-in user
  I want to complete the checkout process
  So that I can purchase the items in my cart
  
  Background: Login and go to checkout
    Given I am logged in as a standard_user
    And I access the inventory page
    And I add an item to the cart
    And I access the cart page

  Scenario: Complete checkout
    When I click the checkout button
    And I enter my first name "John"
    And I enter my last name "Doe"
    And I enter my postal code "12345"
    And I click the continue button
    And I click the finish button
    Then I should see the order confirmation page
