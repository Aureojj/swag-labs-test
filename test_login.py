from pages.login_page import LoginPage
from utils.constants import TEST_USER, TEST_PASSWORD


def test_login_success(driver):
    """Test to validate the login flow."""
    login_page = LoginPage(driver)
    login_page.login(TEST_USER, TEST_PASSWORD)
    assert login_page.is_logged_in()
    assert driver.current_url == "https://www.saucedemo.com/inventory.html"
