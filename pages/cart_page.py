from selenium.webdriver.common.by import By


class CartPage:
    def __init__(self, driver):
        self.driver = driver

    def view_cart(self):
        self.driver.find_element(
            By.CSS_SELECTOR,
            ".shopping_cart_link").click()

    def checkout(self):
        self.driver.find_element(By.ID, "checkout").click()

    def is_cart_page(self):
        return self.driver.find_element(
            By.ID, "cart_contents_container").is_displayed()

    def is_checkout_page(self):
        return self.driver.find_element(
            By.ID, "checkout_info_container").is_displayed()
