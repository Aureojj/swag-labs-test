from pytest_bdd import scenarios, given, when, then
from pages.login_page import LoginPage
from utils.constants import TEST_URL, TEST_USER, TEST_PASSWORD


scenarios("../../features/login.feature")


@given("I am on the login page")
def login_page(driver):
    login_page = LoginPage(driver)
    login_page.go_to_login_page(TEST_URL)


@when("I enter the username")
def input_username(driver):
    login_page = LoginPage(driver)
    login_page.input_username(TEST_USER)


@when("I enter the password")
def input_password(driver):
    login_page = LoginPage(driver)
    login_page.input_password(TEST_PASSWORD)


@when("I click the login button")
def login_button(driver):
    login_page = LoginPage(driver)
    login_page.click_login_button()


@then("I should be redirected to the inventory page")
def redirect_to_inventory_page(driver):
    assert driver.current_url == "https://www.saucedemo.com/inventory.html"
