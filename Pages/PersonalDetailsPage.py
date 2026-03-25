from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException


class PersonalDetailsPage:
    def __init__(self, driver):
        self.driver = driver
        # Locators for the Personal Details page
        self.nationality_dropdown = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/i[1]")
       
        self.dob_field = (By.XPATH, "//label[text()='Date of Birth']/parent::div/following-sibling::div//input")
        self.gender_radio = (By.XPATH, "(//div[@class='--gender-grouped-field'])[1]")
        self.save_button_locator = (By.XPATH, "(//button[@type='submit'][normalize-space()='Save'])[1]")
        self.success_update_message_locator = (By.CSS_SELECTOR, ".oxd-text--toast-message")
        self.my_info_menu_locator = (By.LINK_TEXT, "My Info")

    def select_nationality(self, country_name):
        # Click the nationality dropdown to open the options
        nationality_element = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.nationality_dropdown))
        nationality_element.click()
        # Wait for the dropdown options to be visible and click the desired country option
        country_option = (By.XPATH, f"//div[@role='listbox']//span[text()='{country_name}']")
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(country_option)).click()

    def enter_date_of_birth(self, date_of_birth):
        element = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.dob_field))
        element.send_keys(Keys.CONTROL + "a")
        element.send_keys(Keys.BACK_SPACE)
        element.send_keys(date_of_birth)

    def select_gender(self, gender):
        gender_locator = (By.XPATH, f"//div[contains(@class, '--gender-grouped-field')]//label[normalize-space()='{gender}']")
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(gender_locator)).click()

    def click_save(self):
        try:
            WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.save_button_locator)).click()
        except ElementClickInterceptedException:
            # Fallback: use JavaScript click if the element is intercepted by an overlay (like a toast message)
            self.driver.execute_script("arguments[0].click();", self.driver.find_element(*self.save_button_locator))
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(self.success_update_message_locator))

    def get_success_update_message(self):
        return WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(self.success_update_message_locator)).text

    def click_my_info_menu(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.my_info_menu_locator)).click()
