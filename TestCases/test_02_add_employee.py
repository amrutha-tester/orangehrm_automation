import sys
import os
import time
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


import pytest
from Pages.PIMPage import PIMPage

@pytest.mark.parametrize("first_name, middle_name, last_name", [
    ("Leon", "Doe", "Ray"), 
    ("Jane", "A", "l'orean"), 
    ("Job", "R", "Smith")
])
def test_add_employee(login_admin, first_name, middle_name, last_name):
    new_employee = PIMPage(login_admin)
    new_employee.click_pim_menu()
    new_employee.click_add_employee()
    new_employee.enter_first_name(first_name)
    new_employee.enter_middle_name(middle_name)
    new_employee.enter_last_name(last_name)
    new_employee.enter_employee_id(str(int(time.time())))
   
    new_employee.click_save()
    
    # The success toast is temporary. We should wait for it to appear first,
    # as this confirms the save operation was successful.
   
    success_message = new_employee.get_success_message()
    assert success_message == "Successfully Saved"
    assert new_employee.is_personal_details_visible()
