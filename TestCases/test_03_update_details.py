import sys
import os
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from Pages.PIMPage import PIMPage
from Pages.PersonalDetailsPage import PersonalDetailsPage
import logging

def test_update_personal_details(login_admin):
    update_details = PIMPage(login_admin)
    update_details.click_pim_menu()
    # Add a new employee
    update_details.click_add_employee()
    update_details.enter_first_name("Test")
    update_details.enter_middle_name("User")        
    update_details.enter_last_name("345")
    update_details.enter_employee_id(str(int(time.time())))  # Use a unique employee ID based on the current timestamp
    update_details.click_save()
    # Verification after saving the new employee
    assert update_details.get_success_message() == "Successfully Saved"
    assert update_details.is_personal_details_visible()
    # Fill in personal details
    personal_details = PersonalDetailsPage(login_admin)
    personal_details.select_nationality("French")
    personal_details.enter_date_of_birth("1995-01-01")
    personal_details.select_gender("Female")
    personal_details.click_save()
    # Verification after updating personal details
    assert personal_details.get_success_update_message() == "Successfully Updated"
    logging.info("Successfully updated personal details.")