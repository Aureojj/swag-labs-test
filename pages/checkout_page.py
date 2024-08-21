from selenium.webdriver.common.by import By


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver

    def go_direct_to_checkout(self):
        self.driver.get("https://www.saucedemo.com/checkout-step-one.html")

    def fill_checkout_form(self, first_name, last_name, address):
        self.driver.find_element(By.ID, "first-name").send_keys(first_name)
        self.driver.find_element(By.ID, "last-name").send_keys(last_name)
        self.driver.find_element(By.ID, "postal-code").send_keys(address)

    def next_checkout_step(self):
        self.driver.find_element(By.ID, "continue").click()

    def finish_checkout(self):
        self.driver.find_element(By.ID, "finish").click()

    def is_on_checkout_step_two(self):
        return (
            self.driver.current_url
            == "https://www.saucedemo.com/checkout-step-two.html"
        )

    def is_on_checkout_complete(self):
        return (
            self.driver.current_url
            == "https://www.saucedemo.com/checkout-complete.html"
            and self.driver.find_element(
                By.ID, "checkout_complete_container"
            ).is_displayed()
        )
