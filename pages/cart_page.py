from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class CartPage:
    def __init__(self, driver):
        self.driver = driver

    def add_item(self):
        self.driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()

    def view_cart_page(self):
        self.driver.find_element(By.CSS_SELECTOR, ".shopping_cart_link").click()

    def get_cart_quantity(self):
        return self.driver.find_element(By.CSS_SELECTOR, ".cart_quantity").text

    def get_cart_icon_quantity(self):
        return self.driver.find_element(By.CSS_SELECTOR, ".shopping_cart_badge").text

    def remove_item(self):
        self.driver.find_element(By.ID, "remove-sauce-labs-backpack").click()

    def get_cart_item(self):
        try:
            self.driver.find_element(By.CSS_SELECTOR, ".cart_item")
        except NoSuchElementException:
            return False

    def get_cart_badge(self):
        try:
            self.driver.find_element(By.CSS_SELECTOR, ".shopping_cart_badge")
        except NoSuchElementException:
            return False
