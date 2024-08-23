Feature: Cart
  As a logged-in user
  I want to complete the checkout process
  So that I can purchase the items in my cart
  
  Background: Login and go to inventory page
    Given I am logged in as a standard_user
    And I access the inventory page

  Scenario: Add item in to the cart
    When I add an item to the cart
    And I access the cart page
    Then the cart quantity should show 1
    And the shopping cart icon should show 1 item

  Scenario: Remove item in to the cart
    When I add an item to the cart
    And I access the cart page
    And I remove the item from the cart
    Then the item in the cart is not displayed
    And the shopping cart icon should not show an item
