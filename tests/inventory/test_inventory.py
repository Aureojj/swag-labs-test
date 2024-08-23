from pytest_bdd import scenarios, when, then
from pages.inventory_page import InventoryPage

scenarios("../../features/inventory.feature")


@then("I should see a list of inventory items")
def list_inventory(driver):
    inventory_page = InventoryPage(driver)
    list_items = inventory_page.get_inventory_items()
    assert len(list_items) > 0


@then("each item should have a name")
def list_inventory(driver):
    inventory_page = InventoryPage(driver)
    list_items = inventory_page.get_inventory_items()
    for item in list_items:
        assert isinstance(item["name"], str)


@then("each item should have a description")
def list_inventory(driver):
    inventory_page = InventoryPage(driver)
    list_items = inventory_page.get_inventory_items()
    for item in list_items:
        assert isinstance(item["description"], str)


@then("each item should have a price")
def list_inventory(driver):
    inventory_page = InventoryPage(driver)
    list_items = inventory_page.get_inventory_items()
    for item in list_items:
        assert float(item["price"].replace("$", ""))
