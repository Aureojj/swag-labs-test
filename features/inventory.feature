Feature: Inventory
  As a logged-in user
  I want to view the inventory items
  So that I can choose items to add to my cart

  Scenario: View inventory items
    Given I am logged in as a standard_user
    When I access the inventory page
    Then I should see a list of inventory items
    And each item should have a name
    And each item should have a description
    And each item should have a price
