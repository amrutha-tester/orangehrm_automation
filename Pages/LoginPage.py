
from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_field = self.driver.find_element(By.NAME, "username")
        self.password_field = self.driver.find_element(By.NAME, "password")
        self.login_button = self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']")

    def enter_username(self, username):
        self.username_field.clear()
        self.username_field.send_keys(username)

    def enter_password(self, password):
        self.password_field.clear()
        self.password_field.send_keys(password)

    def click_login_button(self):
        self.login_button.click()