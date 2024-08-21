from pages.login_page import LoginPage
from selenium.webdriver.common.by import By
from utils.constants import TEST_USER, TEST_PASSWORD


def test_logout_success(driver):
    """Test to validate the logout flow"""
    login_page = LoginPage(driver)
    login_page.login(TEST_USER, TEST_PASSWORD)
    assert login_page.is_logged_in()

    # Logout using the logout method
    login_page.logout()
    assert driver.current_url == "https://www.saucedemo.com/"
