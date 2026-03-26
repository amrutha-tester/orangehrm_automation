from time import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException
import allure

class AdminPage:
    def __init__(self, driver):
        self.driver = driver
        # Locator for Navigation to User menu
        self.admin_menu_locator = (By.LINK_TEXT, "Admin")
        self.user_management_locator = (By.XPATH, "//span[contains(text(),'User Management')]")
        self.users_submenu_locator = (By.XPATH, "//ul[@class='oxd-dropdown-menu']//a[text()='Users']")

        # Locators for adding a new user
        self.add_user_button_locator = (By.CSS_SELECTOR, "button[class='oxd-button oxd-button--medium oxd-button--secondary']")
        self.user_role_select_locator = (By.XPATH, "(//div[@class='oxd-select-text oxd-select-text--active'])[1]")
        # self.user_role_options_locator = (By.CSS_SELECTOR, "div[role='listbox'] div[role='option']")
        self.employee_name_locator = (By.CSS_SELECTOR, "input[placeholder='Type for hints...']")
        # This targets the dynamic suggestion list that appears after typing
        self.employee_suggestion_locator = (By.XPATH, "//div[@role='listbox']//div[@role='option']")
        self.status_select_locator = (By.XPATH, "(//div[@class='oxd-select-text oxd-select-text--active'])[2]")
        # self.status_options_locator = (By.CSS_SELECTOR, "div[role='listbox'] div[role='option']")
        self.username_locator = (By.XPATH, "(//input[@class='oxd-input oxd-input--active'])[2]")
        self.password_locator = (By.CSS_SELECTOR, "div[class='oxd-grid-item oxd-grid-item--gutters user-password-cell'] div[class='oxd-input-group oxd-input-field-bottom-space'] div input[type='password']")
        self.confirm_password_locator = (By.CSS_SELECTOR, "div[class='oxd-grid-item oxd-grid-item--gutters'] div[class='oxd-input-group oxd-input-field-bottom-space'] div input[type='password']")
        self.save_button_locator = (By.XPATH, "//button[normalize-space()='Save']")
        self.success_message_locator = (By.CSS_SELECTOR, ".oxd-text--toast-message")
        self.logout_dropdown_locator = (By.CSS_SELECTOR, ".oxd-userdropdown-tab")
        self.logout_button_locator = (By.LINK_TEXT, "Logout")

    @allure.step("Click Admin menu")
    def click_admin_menu(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.admin_menu_locator)).click()

    @allure.step("Navigate to Users section")
    def navigate_to_users(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.user_management_locator)).click()
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.users_submenu_locator)).click()

    @allure.step("Click Add User button")
    def click_add_user_button(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.add_user_button_locator)).click()  

    @allure.step("Select user role: {1}")
    def select_user_role(self, role_name):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.user_role_select_locator)).click()
        role_xpath = (By.XPATH, f"//div[@role='listbox']//span[text()='{role_name}']")
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(role_xpath)).click()

    @allure.step("Enter employee name: {1}")
    def enter_employee_name(self, name):
        element = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.employee_name_locator))
        element.send_keys(Keys.CONTROL + "a")  # Select all existing text
        element.send_keys(Keys.DELETE)  # Clear the field
        element.send_keys(name)
        # Wait for the suggestion list to appear and click the correct employee from the suggestions
        # Use a specific locator that matches the text we typed to ensure the correct option is selected
        suggestion_locator = (By.XPATH, f"//div[@role='listbox']//div[@role='option'][contains(., '{name}')]")
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(suggestion_locator)).click()
        

    @allure.step("Select status: {1}")
    def select_status(self, status_name):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.status_select_locator)).click()
        status_xpath = (By.XPATH, f"//div[@role='listbox']//span[text()='{status_name}']")
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(status_xpath)).click()

    @allure.step("Enter username: {1}")
    def enter_username(self, username):
        self.driver.find_element(*self.username_locator).clear()
        self.driver.find_element(*self.username_locator).send_keys(username)
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(self.username_locator))

    @allure.step("Enter password")
    def enter_password(self, password):
        self.driver.find_element(*self.password_locator).clear()
        self.driver.find_element(*self.password_locator).send_keys(password)
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(self.password_locator))
    
    @allure.step("Confirm password")
    def enter_confirm_password(self, password):
        self.driver.find_element(*self.confirm_password_locator).clear()
        self.driver.find_element(*self.confirm_password_locator).send_keys(password)
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(self.confirm_password_locator))

    @allure.step("Click Save button")
    def click_save(self):
        try:
            WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.save_button_locator)).click()
        except ElementClickInterceptedException:
            # Fallback: use JavaScript click if the element is intercepted by an overlay (like a toast message)
            self.driver.execute_script("arguments[0].click();", self.driver.find_element(*self.save_button_locator))
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(self.success_message_locator))

    @allure.step("Verify if System User page is displayed")
    def is_system_user_page_displayed(self):
        return WebDriverWait(self.driver, 20).until(EC.url_contains("/admin/viewSystemUsers"))

    @allure.step("Get success message text")
    def get_success_message(self):
        return WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(self.success_message_locator)).text
    
    @allure.step("Logout from application")
    def logout(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.logout_dropdown_locator)).click()
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.logout_button_locator)).click()