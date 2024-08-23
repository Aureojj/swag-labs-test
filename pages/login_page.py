from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def go_to_login_page(self, url):
        self.driver.get(url)

    def input_username(self, username):
        self.driver.find_element(By.ID, "user-name").send_keys(username)

    def input_password(self, password):
        self.driver.find_element(By.ID, "password").send_keys(password)

    def click_login_button(self):
        self.driver.find_element(By.ID, "login-button").click()
