from pytest_bdd import scenarios, when, then, parsers
from pages.checkout_page import CheckoutPage


scenarios("../../features/checkout.feature")


@when("I click the checkout button")
def go_to_checkout(driver):
    checkout_page = CheckoutPage(driver)
    checkout_page.click_checkout_button()


@when(parsers.parse('I enter my first name "{first_name:l}"'))
def enter_first_name(driver, first_name):
    checkout_page = CheckoutPage(driver)
    checkout_page.enter_first_name(first_name)


@when(parsers.parse('I enter my last name "{last_name:l}"'))
def enter_last_name(driver, last_name):
    checkout_page = CheckoutPage(driver)
    checkout_page.enter_last_name(last_name)


@when(parsers.parse('I enter my postal code "{postal_code:d}"'))
def enter_postal_code(driver, postal_code):
    checkout_page = CheckoutPage(driver)
    checkout_page.enter_postal_code(postal_code)


@when("I click the continue button")
def click_continue_button(driver):
    checkout_page = CheckoutPage(driver)
    checkout_page.click_continue_button()


@when("I click the finish button")
def click_continue_button(driver):
    checkout_page = CheckoutPage(driver)
    checkout_page.click_finish_button()


@then("I should see the order confirmation page")
def get_checkout_container(driver):
    checkout_page = CheckoutPage(driver)
    assert checkout_page.get_checkout_container() == True
    assert checkout_page.complete_message() == "Thank you for your order!"
