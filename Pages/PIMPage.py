from time import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException


class PIMPage:
    def __init__(self, driver):
        self.driver = driver
        # Locator for the PIM menu
        self.pim_menu_locator = (By.LINK_TEXT, "PIM")
        # Locator for the Add Employee button
        self.add_employee_button_locator = (By.XPATH, "//button[normalize-space()='Add']")
        # Locators for the employee details fields on the Add Employee page
        self.first_name_locator = (By.NAME, "firstName")
        self.middle_name_locator = (By.NAME, "middleName")
        self.last_name_locator = (By.NAME, "lastName")
        self.employee_id_locator = (By.XPATH, "//label[text()='Employee Id']/parent::div/following-sibling::div/input")
        self.save_button_locator = (By.XPATH, "(//button[normalize-space()='Save'])[1]")
        self.success_message_locator = (By.CSS_SELECTOR, ".oxd-text--toast-message")
        # Locator for the Employee ID search field on the Employee List page
        self.employee_id_search_locator = (By.XPATH, "//div[@class='oxd-form-row']//label[text()='Employee Id']/parent::div/following-sibling::div/input")
        self.search_button_locator = (By.XPATH, "//button[normalize-space()='Search']")
        # Locator for the ID cell in the first row of the results table
        self.first_id_cell_locator = (By.XPATH, "//div[@class='oxd-table-card'][1]//div[@role='cell'][2]")
        # Locator for the name search field on the Employee List page and delete employee
        self.name_search_locator = (By.XPATH, "(//input[@placeholder='Type for hints...'])[1]")
        self.delete_button_locator = (By.XPATH, "//div[@class='oxd-table-body']//div[1]//div[@class='oxd-table-cell-actions']//button[i[contains(@class, 'bi-trash')]]")
        self.confirm_delete_button_locator = (By.CSS_SELECTOR, "button[class='oxd-button oxd-button--medium oxd-button--label-danger orangehrm-button-margin']")
        self.record_count_span = (By.XPATH, "//div[contains(@class, 'orangehrm-horizontal-padding')]//span")
        
    def click_pim_menu(self):
        self.driver.find_element(*self.pim_menu_locator).click()

    def click_add_employee(self):
        self.driver.find_element(*self.add_employee_button_locator).click()
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(self.first_name_locator))

    def enter_first_name(self, first_name):
        self.driver.find_element(*self.first_name_locator).clear()
        self.driver.find_element(*self.first_name_locator).send_keys(first_name)
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(self.first_name_locator))

    def enter_middle_name(self, middle_name):
        self.driver.find_element(*self.middle_name_locator).clear()
        self.driver.find_element(*self.middle_name_locator).send_keys(middle_name)
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(self.middle_name_locator))

    def enter_last_name(self, last_name):
        self.driver.find_element(*self.last_name_locator).clear()
        self.driver.find_element(*self.last_name_locator).send_keys(last_name)
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(self.last_name_locator))

    def enter_employee_id(self, employee_id):
        element = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.employee_id_locator))
        # Use Ctrl+A and Backspace to ensure the field is cleared, as .clear() can be flaky on dynamic forms
        element.send_keys(Keys.CONTROL + "a")
        element.send_keys(Keys.BACK_SPACE)
        element.send_keys(employee_id)

    def get_employee_id_value(self):
        element = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(self.employee_id_locator))
        return element.get_attribute("value")

    
    def click_save(self):
        save_btn = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.save_button_locator))
        try:
            save_btn.click()
        except:
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", save_btn)
            self.driver.execute_script("arguments[0].click();", save_btn)
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(self.success_message_locator))
            
    def is_personal_details_visible(self):
        # Wait first for URL change
        return WebDriverWait(self.driver, 20).until(EC.url_contains("viewPersonalDetails"))
       
    
    def get_success_message(self):
        success_message = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(self.success_message_locator))
        return success_message.text
  
    
    def search_employee_by_id(self, employee_id):
        # Wait for the search field to be clickable before interacting
        search_field = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.employee_id_search_locator))
        # Clear the field using Ctrl+A + Backspace to ensure no previous text remains
        search_field.send_keys(Keys.CONTROL + "a")
        search_field.send_keys(Keys.BACK_SPACE)
        search_field.send_keys(employee_id)
        # It's more reliable to click the explicit search button
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.search_button_locator)).click()

     
    def get_employee_id_from_search_result(self, expected_id=None):
        # If expected_id is provided, wait for the cell text to match it.
        # This prevents reading stale data from the table before the search completes.
        if expected_id:
            WebDriverWait(self.driver, 20).until(
                EC.text_to_be_present_in_element(self.first_id_cell_locator, expected_id)
            )
        # Wait for the search results to load and the cell to be visible
        id_cell = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(self.first_id_cell_locator)
        )
        return id_cell.text
    
    def get_no_records_message(self):
        no_records_locator = (By.CSS_SELECTOR, "span[class='oxd-text oxd-text--span']")
        no_records_message = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(no_records_locator)
        )
        return no_records_message.text
    
    def search_employee_by_name(self, name):
        search_field = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(self.name_search_locator)
        )
        search_field.send_keys(Keys.CONTROL + "a")
        search_field.send_keys(Keys.BACK_SPACE)
        search_field.send_keys(name)
        self.driver.find_element(*self.employee_id_locator).clear()  # Clear the Employee ID field to ensure only name is used for search
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.search_button_locator)).click()

    def click_delete_button(self):
        from selenium.common.exceptions import StaleElementReferenceException
        # Wait for the table to load and the delete button to be visible before clicking
        # WebDriverWait(self.driver, 10).until(
        # EC.visibility_of_element_located(By.CLASS_NAME, "oxd-table-card"))
        try:
            WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.delete_button_locator)).click()
        except StaleElementReferenceException:
            # If the element becomes stale, it means the page has refreshed. We should try to find it again.
            WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.delete_button_locator)).click()
        
    def click_confirm_delete_button(self):
        # Wait for the confirm delete button to be clickable before clicking
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.confirm_delete_button_locator)).click()
        
    def get_success_message_after_delete(self):
        return WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(self.success_message_locator)).text
    
    def is_employee_list_visible(self):
           return WebDriverWait(self.driver, 20).until(EC.url_contains("viewEmployeeList"))
    
        