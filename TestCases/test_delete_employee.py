import sys
import os
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import allure

from Pages.PIMPage import PIMPage
import logging

@allure.feature("PIM")
@allure.story("Delete Employee")
@allure.severity(allure.severity_level.NORMAL)

def test_delete_employee(login_admin):
    delete_employee = PIMPage(login_admin)
    # Add a new employee
    delete_employee.click_pim_menu()
    delete_employee.click_add_employee()
    delete_employee.enter_first_name("Test")
    delete_employee.enter_middle_name("User")        
    delete_employee.enter_last_name("123")
    # Generate a unique employee ID using the current timestamp to prevent "ID already exists" errors.
    employee_id = str(int(time.time()))
    delete_employee.enter_employee_id(employee_id)
    
    delete_employee.click_save()
    assert delete_employee.get_success_message() == "Successfully Saved"
    assert delete_employee.is_personal_details_visible()

    # Navigate back to the employee list to perform the search using the unique ID.
    delete_employee.click_pim_menu()  
    delete_employee.search_employee_by_id(employee_id) # Ensure we're on the Employee List page

    # Wait for the search results to update to the correct employee before deleting.
    delete_employee.get_employee_id_from_search_result(employee_id)

    # Delete the employee and verify deletion
    delete_employee.click_delete_button()
    delete_employee.click_confirm_delete_button()
    success_text = delete_employee.get_success_message_after_delete()
    assert "Successfully Deleted" in success_text
    logging.info("Successfully deleted employee.")

    # Wait for the success toast to disappear
    delete_employee.wait_for_success_toast_to_disappear()

    # Navigate back to the PIM page (Employee List) to ensure we are on the correct page
    delete_employee.click_pim_menu()
    # Wait for a key element on the PIM list page to be visible, ensuring the page is loaded
    WebDriverWait(delete_employee.driver, 20).until(EC.visibility_of_element_located(delete_employee.employee_id_search_locator))

    # verfication after deletion
    delete_employee.search_employee_by_id(employee_id)
    delete_employee.wait_for_no_records_found()
    assert delete_employee.get_no_records_message() == "No Records Found"

    logging.info("Successfully verified employee deletion.")