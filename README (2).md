# OrangeHRM Professional Test Automation Framework

This repository features a robust, end-to-end automation suite for the
OrangeHRM application. Built with Python and Selenium WebDriver, the
project demonstrates advanced framework engineering concepts, including
the Page Object Model (POM), Data-Driven Testing, and Asynchronous UI
handling.

##  Test Scenarios & Portfolio Highlights

The suite validates the full CRUD (Create, Read, Update, Delete)
lifecycle and persona-based access across these scenarios:

### OHRM_1: Employee Lifecycle (Admin Path)

**Functional:** - Validates successful login - Validates Add Employee
workflow in the PIM module

### OHRM_2: Data Integrity & Search (Positive)

**Functional:** - Verifies that searching for a valid Employee ID
returns the correct expected record

### OHRM_3: Negative Testing & Edge Cases

**Robustness:** - Validates system behavior when searching for a
non‑existent ID

**Assertion:** - Confirms the UI correctly displays the **"No Records
Found"** state

### OHRM_4: Asynchronous Modal & Delete Workflow

**Technical Challenge:** - Handles asynchronous confirmation pop‑ups
(modals) to delete a record

**Verification:** - Re‑searches for the deleted ID - Ensures data
removal and UI synchronization

### OHRM_5: Self‑Service (ESS Persona)

**Persona Testing:** - Logs in as an ESS employee - Verifies restricted
access permissions

**Profile Management:** - Validates My Info module - Updates personal
user details

## Scalability: Data‑Driven Testing

**Design:** - Uses @pytest.mark.parametrize to execute Add Employee
tests with multiple datasets such as: - Special characters - Long
names - Edge case inputs

## Key Engineering Features

### Page Object Model (POM)

Centralized locators and reusable actions inside the Pages directory for
better maintainability.

### Wait Strategies

Implements WebDriverWait with expected_conditions to handle: - Success
toast messages - Table refresh delays - Dynamic UI elements

This prevents flaky tests.

### Dynamic Data Handling

Generates unique Employee IDs using timestamps to prevent duplicate ID
failures during repeated executions.

### Robust Interactions

Uses: - JavaScript execution - Scrolling - Click interception handling

To interact with UI elements blocked by overlays.

##  Setup & Execution

### 1. Installation

``` bash
git clone https://github.com/amrutha-tester/orangehrm_automation
cd orangehrm_automation
pip install -r requirements.txt
```

### 2. Run All Tests with Reporting

``` bash
pytest TestCases/ --alluredir=allure-results
```

### 3. Generate Interactive Dashboard

``` bash
allure serve allure-results
```

##  Tech Stack

  Category            Technology
  ------------------- --------------------
  Language            Python 3.x
  Automation          Selenium WebDriver
  Test Runner         Pytest
  Reporting           Allure Reports
  Environment         Webdriver‑Manager
  Framework Pattern   Page Object Model

##  Project Structure

    orangehrm_automation
    │
    ├── Pages/
    ├── TestCases/
    ├── requirements.txt
    ├── pytest.ini
    |── config.ini
    └── README.md

##  Framework Capabilities

-   End‑to‑end automation
-   Data‑driven testing
-   Role‑based testing
-   Negative testing
-   UI synchronization handling
-   Allure reporting
-   Scalable framework design

##  Future Improvements

Possible enhancements:

-   CI/CD integration (GitHub Actions / Jenkins)
-   Docker execution




------------------------------------------------------------------------

⭐ If you found this useful, consider giving the repository a star.
