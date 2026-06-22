import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from Pages.LoginPage import LoginPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_page_title(driver):
    assert driver.title == "OrangeHRM"

def test_orangehrm_login(driver):
    login = LoginPage(driver)
    login.enter_username("Admin")
    login.enter_password("admin123")
    login.click_login_button()

    # Wait for the URL to change to the dashboard URL. This is more reliable
    # than time.sleep() and makes the test more robust.
    WebDriverWait(driver, 10).until(EC.url_contains("dashboard"))

    # The assertion is now simpler and clearer.
    assert "dashboard" in driver.current_url

   
