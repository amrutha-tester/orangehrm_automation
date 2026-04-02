import allure

@allure.feature("Smoke Test")
@allure.story("Verify Application Reachability")
def test_open_orangehrm(driver):
    """
    Smoke test to verify that the OrangeHRM page loads correctly.
    The 'driver' fixture handles setup, navigation to the base URL, and teardown.
    """
    # Print the page title for visibility in console output
    print(f"The page title is: {driver.title}")
    
    # Validation: Assert that the title contains the expected brand name
    assert "OrangeHRM" in driver.title, f"Expected title to contain 'OrangeHRM', but got '{driver.title}'"