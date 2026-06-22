import sys
import os
import time
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from Pages.PIMPage import PIMPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging

def test_search_employee_by_id(login_admin):
    verify_employee = PIMPage(login_admin)
    verify_employee.click_pim_menu()
    verify_employee.click_add_employee()
    verify_employee.enter_first_name("John")
    verify_employee.enter_middle_name("Doe")
    verify_employee.enter_last_name("Smith")
    
    # Generate a unique employee ID using the current timestamp to prevent "ID already exists" errors.
    employee_id = str(int(time.time()))
    verify_employee.enter_employee_id(employee_id)
    
    verify_employee.click_save()
    # Wait for the success toast, which confirms the save action.
    # Then, wait for the page to redirect to the new employee's personal details.
    # This ensures the create operation is fully complete before we try to search.
    assert verify_employee.get_success_message() == "Successfully Saved"
    assert verify_employee.is_personal_details_visible()

    # Navigate back to the employee list to perform the search.
    verify_employee.click_pim_menu()  # Ensure we're on the Employee List page
    verify_employee.search_employee_by_id(employee_id)

    # From the search results, get the ID and verify it matches the created one.
    actual_id = verify_employee.get_employee_id_from_search_result(employee_id)
    assert actual_id == employee_id, f"Expected employee ID {employee_id}, but got {actual_id}"
    logging.info(f"Successfully verified employee ID: {actual_id} matches the created ID: {employee_id}")


def test_search_non_existent_employee(login_admin):
    search_employee = PIMPage(login_admin)
    search_employee.click_pim_menu()
    
    non_existent_id = "9999999"
    search_employee.search_employee_by_id(non_existent_id)

    # Wait specifically for the text to be "No Records Found".
    # This handles the race condition where the previous record count is still visible immediately after clicking search.
    WebDriverWait(search_employee.driver, 10).until(
        EC.text_to_be_present_in_element(search_employee.record_count_span, "No Records Found")
    )
    logging.info(f"Successfully verified no records found for ID: {non_existent_id}")