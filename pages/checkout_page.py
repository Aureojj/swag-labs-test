from selenium.webdriver.common.by import By


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver

    def click_checkout_button(self):
        self.driver.find_element(By.ID, "checkout").click()

    def enter_first_name(self, first_name):
        self.driver.find_element(By.CSS_SELECTOR, '[data-test="firstName"]').send_keys(
            first_name
        )

    def enter_last_name(self, last_name):
        self.driver.find_element(By.CSS_SELECTOR, '[data-test="lastName"]').send_keys(
            last_name
        )

    def enter_postal_code(self, postal_code):
        self.driver.find_element(By.CSS_SELECTOR, '[data-test="postalCode"]').send_keys(
            postal_code
        )

    def click_continue_button(self):
        self.driver.find_element(By.CSS_SELECTOR, '[data-test="continue"]').click()

    def click_finish_button(self):
        self.driver.find_element(By.CSS_SELECTOR, '[data-test="finish"]').click()

    def get_checkout_container(self):
        return self.driver.find_element(
            By.CSS_SELECTOR, '[data-test="checkout-complete-container"]'
        ).is_displayed()

    def complete_message(self):
        return self.driver.find_element(
            By.CSS_SELECTOR, '[data-test="complete-header"]'
        ).text
