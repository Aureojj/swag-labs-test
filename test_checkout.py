from pages.checkout_page import CheckoutPage
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from selenium.webdriver.common.by import By
from utils.constants import TEST_USER, TEST_PASSWORD, CHECKOUT_FORM_DATA


def login(driver):
    """Login with a valid username and password."""
    login_page = LoginPage(driver)
    login_page.login(TEST_USER, TEST_PASSWORD)


def add_product(driver):
    """Add a product to the cart"""
    products_page = ProductsPage(driver)
    products_page.add_product_to_cart()


def view_cart(driver):
    """View product in the cart."""
    cart_page = CartPage(driver)
    cart_page.view_cart()
    cart_page.checkout()


def test_fill_checkout_form(driver):
    """Test the completion of the checkout form."""
    login(driver)
    checkout_page = CheckoutPage(driver)
    checkout_page.go_direct_to_checkout()
    checkout_page.fill_checkout_form(**CHECKOUT_FORM_DATA)
    checkout_page.next_checkout_step()
    assert checkout_page.is_on_checkout_step_two()


def test_complete_checkout(driver):
    """Test the complete checkout flow."""
    login(driver)
    add_product(driver)
    view_cart(driver)
    checkout_page = CheckoutPage(driver)
    checkout_page.fill_checkout_form(**CHECKOUT_FORM_DATA)
    checkout_page.next_checkout_step()
    assert checkout_page.is_on_checkout_step_two()
    # Check the values on the checkout page
    inventory_name = driver.find_element(By.CSS_SELECTOR, ".inventory_item_name")
    item_value = driver.find_element(By.CSS_SELECTOR, ".inventory_item_price")
    tax_value = driver.find_element(By.CSS_SELECTOR, ".summary_tax_label")
    total_value = driver.find_element(By.CSS_SELECTOR, ".summary_total_label")
    assert "Sauce Labs Backpack" == inventory_name.text
    assert "29.99" in item_value.text
    assert "2.40" in tax_value.text
    assert "32.39" in total_value.text
    checkout_page.finish_checkout()
    assert checkout_page.is_on_checkout_complete()
