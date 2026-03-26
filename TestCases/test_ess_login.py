import sys
import os
import time
from selenium.webdriver.common.by import By
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


import allure
import logging
from Pages.LoginPage import LoginPage
from Pages.PersonalDetailsPage import PersonalDetailsPage
from Pages.PIMPage import PIMPage
from Pages.AdminPage import AdminPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

unique_username = f"Admin_{int(time.time())}"

@allure.feature("PIM")
@allure.story("Add User")
@allure.severity(allure.severity_level.NORMAL)
def test_add_user(login_admin):
    add_user = PIMPage(login_admin)
    add_user.click_pim_menu()
    add_user.click_add_employee()
    add_user.enter_first_name("Tester")
    add_user.enter_middle_name("User")        
    add_user.enter_last_name("345")
    add_user.enter_employee_id(str(int(time.time())))
    add_user.click_save()
    assert add_user.get_success_message() == "Successfully Saved"
    assert add_user.is_personal_details_visible()
    logging.info("Employee added successfully with name: Tester User 345")
# Add ESS user role for the created employee
    
    add_ess_user = AdminPage(login_admin)
    add_ess_user.click_admin_menu()
    add_ess_user.navigate_to_users()
    add_ess_user.click_add_user_button()
    add_ess_user.select_user_role("ESS")
    add_ess_user.enter_employee_name("Tester User 345")
    add_ess_user.select_status("Enabled")
    add_ess_user.enter_username(unique_username)
    add_ess_user.enter_password("Test@1234")
    add_ess_user.enter_confirm_password("Test@1234")
    add_ess_user.click_save()
    assert add_ess_user.get_success_message() == "Successfully Saved"
    assert add_ess_user.is_system_user_page_displayed()
    logging.info("ESS user created successfully with username: testuser345")
    
    add_ess_user.logout()

@allure.feature("ESS")
@allure.story("Update My Info")
@allure.severity(allure.severity_level.NORMAL)


def test_ess_update_my_info(driver):
    # Credentials as created in test_ess_login.py
    username = unique_username
    password = "Test@1234"

    # Login as ESS User
    login_page = LoginPage(driver)
    login_page.enter_username(username)
    login_page.enter_password(password)
    login_page.click_login_button()

    WebDriverWait(driver, 20).until(EC.url_contains("dashboard"))

    # 2. Navigate to 'My Info'
    personal_details = PersonalDetailsPage(driver)
    personal_details.click_my_info_menu()

    # 3. Update Personal Details
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located(personal_details.save_button_locator))

    personal_details.select_nationality("French")
    
    # 4. Save and Verify
    personal_details.click_save()

    assert "Successfully Updated" in personal_details.get_success_update_message()

    logging.info("Successfully updated personal details for ESS user.")