from pages.cart_page import CartPage
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from utils.constants import TEST_USER, TEST_PASSWORD


def login(driver):
    """Login with a valid username and password"""
    login_page = LoginPage(driver)
    login_page.login(TEST_USER, TEST_PASSWORD)


def test_add_product_to_cart(driver):
    """Test to validate the flow of adding products"""
    login(driver)
    products_page = ProductsPage(driver)
    products_page.add_product_to_cart()
    assert products_page.is_product_in_cart()


def test_remove_product_from_cart(driver):
    """Test to validate the flow of removing products"""
    login(driver)
    products_page = ProductsPage(driver)
    products_page.add_product_to_cart()
    products_page.remove_product_from_cart()
    assert not products_page.is_product_in_cart()


def test_view_cart(driver):
    """Test to validate the flow cart view"""
    login(driver)
    cart_page = CartPage(driver)
    cart_page.view_cart()
    assert cart_page.is_cart_page()
    assert driver.current_url == "https://www.saucedemo.com/cart.html"


def test_go_to_checkout(driver):
    """Test to validate redirection to checkout"""
    login(driver)
    cart_page = CartPage(driver)
    cart_page.view_cart()
    cart_page.checkout()
    assert cart_page.is_checkout_page()
    assert driver.current_url == "https://www.saucedemo.com/checkout-step-one.html"
