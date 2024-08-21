from pages.products_page import ProductsPage
from pages.login_page import LoginPage
from selenium.webdriver.common.by import By
from utils.constants import TEST_USER, TEST_PASSWORD


def login(driver):
    """Login with a valid username and password."""
    login_page = LoginPage(driver)
    login_page.login(TEST_USER, TEST_PASSWORD)


def test_view_products(driver):
    """Test to visualise available products."""
    login(driver)
    products_page = ProductsPage(driver)
    products_page.view_products()
    assert products_page.is_products_page()
    assert driver.current_url == "https://www.saucedemo.com/inventory.html"


def test_verify_product_details(driver):
    """Test to view product details."""
    login(driver)
    product_page = ProductsPage(driver)
    get_product = product_page.get_product()
    for item in get_product:
        assert item.find_element(By.CSS_SELECTOR, ".inventory_item_name").text
        assert item.find_element(By.CSS_SELECTOR, ".inventory_item_desc").text
        assert item.find_element(By.CSS_SELECTOR, ".inventory_item_price").text
