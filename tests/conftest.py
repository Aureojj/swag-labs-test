import pytest
from pytest_bdd import given, when
from selenium import webdriver
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from utils.constants import TEST_URL, TEST_USER, TEST_PASSWORD


@pytest.fixture
def driver():
    driver = webdriver.Remote(
        "http://localhost:4444/wd/hub", options=webdriver.ChromeOptions()
    )
    yield driver
    driver.quit()


@given("I am logged in as a standard_user", target_fixture="logged_as_standard_user")
def logged_as_standard_user(driver):
    login_page = LoginPage(driver)
    login_page.go_to_login_page(TEST_URL)
    login_page.input_username(TEST_USER)
    login_page.input_password(TEST_PASSWORD)
    login_page.click_login_button()


@given("I access the inventory page")
@when("I access the inventory page")
def access_inventory_page(driver):
    access_inventory_page = InventoryPage(driver)
    access_inventory_page.access_inventory()


@given("I add an item to the cart")
@when("I add an item to the cart")
def add_item_on_the_cart(driver):
    cart_page = CartPage(driver)
    cart_page.add_item()


@given("I access the cart page")
@when("I access the cart page")
def view_cart_page(driver):
    cart_page = CartPage(driver)
    cart_page.view_cart_page()
