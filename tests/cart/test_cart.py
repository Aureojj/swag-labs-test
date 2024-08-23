from pytest_bdd import scenarios, given, when, then
from pages.cart_page import CartPage

scenarios("../../features/cart.feature")


@then("the cart quantity should show 1")
def show_cart_quantity(driver):
    cart_page = CartPage(driver)
    assert cart_page.get_cart_quantity() == "1"


@then("the shopping cart icon should show 1 item")
def show_cart_icon_quantity(driver):
    cart_page = CartPage(driver)
    assert cart_page.get_cart_icon_quantity() == "1"


@when("I remove the item from the cart")
def remove_item_from_cart(driver):
    cart_page = CartPage(driver)
    cart_page.remove_item()


@then("the item in the cart is not displayed")
def show_cart_item(driver):
    cart_page = CartPage(driver)
    assert cart_page.get_cart_item() == False


@then("the shopping cart icon should not show an item")
def show_cart_item(driver):
    cart_page = CartPage(driver)
    assert cart_page.get_cart_badge() == False
