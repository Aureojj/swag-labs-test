from selenium.webdriver.common.by import By


class InventoryPage:
    def __init__(self, driver):
        self.driver = driver

    def access_inventory(self):
        self.driver.get("https://www.saucedemo.com/inventory.html")

    def get_inventory_items(self):
        inventory_items = self.driver.find_elements(By.CSS_SELECTOR, ".inventory_item")
        list_items = []
        for item in inventory_items:
            dictionary = {
                "name": item.find_element(By.CSS_SELECTOR, ".inventory_item_name").text,
                "description": item.find_element(
                    By.CSS_SELECTOR, ".inventory_item_desc"
                ).text,
                "price": item.find_element(
                    By.CSS_SELECTOR, ".inventory_item_price"
                ).text,
            }
            list_items.append(dictionary)
        return list_items
