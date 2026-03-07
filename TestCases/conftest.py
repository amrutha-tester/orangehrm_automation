import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="function")
def driver():
    """Fixture to set up and tear down the WebDriver for each test."""
    # Setup: Create and configure the WebDriver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    driver.maximize_window()

    # Navigate to the page
    driver.get("https://opensource-demo.orangehrmlive.com/")

    # Yield the driver to the test
    yield driver

    # Teardown: Close the browser
    driver.quit()

@pytest.fixture
def login_admin(driver):
    """Fixture to log in as admin before each test that requires authentication."""
    from Pages.LoginPage import LoginPage
    login_page = LoginPage(driver)
    login_page.enter_username("Admin")
    login_page.enter_password("admin123")
    login_page.click_login_button()
    yield driver