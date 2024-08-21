from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class ProductsPage:
    def __init__(self, driver):
        self.driver = driver

    def view_products(self):
        self.driver.find_element(By.ID, "inventory_container").click()

    def add_product_to_cart(self):
        self.driver.find_element(
            By.ID, "add-to-cart-sauce-labs-backpack").click()

    def remove_product_from_cart(self):
        self.driver.find_element(By.ID, "remove-sauce-labs-backpack").click()

    def is_products_page(self):
        return self.driver.find_element(
            By.ID, "inventory_container").is_displayed()

    def get_product(self):
        return self.driver.find_elements(By.CSS_SELECTOR, ".inventory_item")

    def is_product_in_cart(self):
        try:
            element = self.driver.find_element(
                By.CSS_SELECTOR, "#shopping_cart_container .shopping_cart_badge")
            return element.is_displayed()
        except NoSuchElementException:
            return False
