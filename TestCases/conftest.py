from ast import Add

import pytest
from selenium import webdriver
import configparser
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException
import time
import allure

# Function to read the config file
def read_config():
    config = configparser.ConfigParser()
    # Construct the absolute path to config.ini
    # This makes the test runner location-independent
    config_path = os.path.join(os.path.dirname(__file__), '..', 'config.ini')
    if not os.path.exists(config_path):
        print(f"\nWARNING: Config file not found at: {config_path}")
    
    config.read(config_path)
    return config

@pytest.fixture(scope="session")
def config():
    """Fixture to read the config file once per session."""
    return read_config()

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")

@pytest.fixture(scope="function")
def driver(config, request):
    """Fixture to set up and tear down the WebDriver for each test."""
    
    browser = request.config.getoption("--browser").lower()
    # Priority: 1. Environment Variable (Docker), 2. Config file (Local override), 3. None
    grid_url = os.getenv("SELENIUM_GRID_URL") or config.get('common', 'grid_url', fallback=None)

    options = None
    
    # Setup WebDriver options based on the selected browser
    if browser == "chrome":
        options = webdriver.ChromeOptions()
    elif browser == "edge":
        options = webdriver.EdgeOptions()
    elif browser == "firefox":
        options = webdriver.FirefoxOptions()
    else:
        raise ValueError(f"Unsupported browser: '{browser}'")
    
    # Add stability flags for Docker/Linux environments
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    # Remote execution on Selenium Grid
    if grid_url:
        print(f"Running tests on Selenium Grid: {grid_url}")
       # Try to connect 5 times with a 5-second sleep in between
        for i in range(5):
            try:
                driver = webdriver.Remote(command_executor=grid_url, options=options)
                break 
            except Exception as e:
                if i == 4: raise e # Crash only if all 5 attempts fail
                print(f"Waiting for Selenium Hub to wake up... (Attempt {i+1}/5)")
                time.sleep(5)
    else:
        # Local execution
        print("Running tests locally.")
        if browser == "chrome":
            driver = webdriver.Chrome(options=options)
        elif browser == "firefox":
            driver = webdriver.Firefox(options=options)
        elif browser == "edge":
            driver = webdriver.Edge(options=options)

    driver.implicitly_wait(10)
    driver.maximize_window()

    # Navigate to the page using the URL from config.ini
    driver.get(config.get('common', 'base_url'))

    # Yield the driver to the test
    yield driver

    # Teardown: Close the browser
    driver.quit()

@pytest.fixture
def login_admin(driver, config):
    """Fixture to log in as admin before each test that requires authentication."""
    from Pages.LoginPage import LoginPage
    login_page = LoginPage(driver)
    # Use credentials from config.ini
    login_page.enter_username(config.get('credentials', 'username'))
    login_page.enter_password(config.get('credentials', 'password'))
    login_page.click_login_button()

    # Wait for the dashboard page to load to ensure login was successful
    # and the page is ready for the next action. This prevents race conditions.
    WebDriverWait(driver, 10).until(EC.url_contains("dashboard"))

    yield driver

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Hook to take a screenshot on test failure.
    This hook is executed for each test phase (setup, call, teardown).
    """
    # Execute all other hooks to obtain the report object
    outcome = yield
    report = outcome.get_result()

    # We only care about the 'call' phase and only if it failed
    if report.when == 'call' and report.failed:
        # Check if the 'driver' fixture is used by the test
        if 'driver' in item.fixturenames:
            driver = item.funcargs['driver']
            
            # Create screenshots directory if it doesn't exist
            screenshots_dir = os.path.join(os.path.dirname(__file__), '..', 'screenshots')
            os.makedirs(screenshots_dir, exist_ok=True)
            
            # Create a unique filename for the screenshot
            test_name = item.nodeid.replace("::", "_").replace("/", "_")
            timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
            screenshot_file = os.path.join(screenshots_dir, f"{test_name}_{timestamp}.png")
            driver.save_screenshot(screenshot_file)

            # Attach screenshot to Allure report
            allure.attach(
                driver.get_screenshot_as_png(),
                name=f"failure_{test_name}",
                attachment_type=allure.attachment_type.PNG
            )
            
            # Attach screenshot to pytest-html report if the plugin is installed
            # Handle both 'extras' (pytest-html 4.x+) and 'extra' (older versions)
            extra_attr = 'extras' if hasattr(report, 'extras') else 'extra'
            extra_content = getattr(report, extra_attr, [])
            try:
                import pytest_html
                extra_content.append(pytest_html.extras.image(screenshot_file))
            except ImportError:
                pass
            setattr(report, extra_attr, extra_content)
