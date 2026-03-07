# OrangeHRM Automation Framework

A professional-grade automated testing suite for the **OrangeHRM Open
Source** platform, developed using **Python** and **Selenium
WebDriver**. This project follows the **Page Object Model (POM)** design
pattern to ensure test scripts remain **clean, readable, and
maintainable**.

------------------------------------------------------------------------

##  Tech Stack

-   **Language:** Python 3.12+
-   **Framework:** Pytest
-   **Library:** Selenium WebDriver
-   **Driver Management:** WebDriver Manager (Chrome)
-   **Design Pattern:** Page Object Model (POM)

------------------------------------------------------------------------

##  Project Status

###  Completed & Verified

**Smoke Test** - Connectivity check to verify the application URL is
reachable. - Confirms the browser initializes correctly.

**Login Functionality** - Automated **Admin login workflow**.

**Framework Enhancements** - Integrated **Pytest Fixtures
(`conftest.py`)** to manage browser lifecycle (Setup / Teardown). -
Implemented **Explicit Waits** for reliable element interaction.

------------------------------------------------------------------------

##  Roadmap (Next Steps)

### PIM: Add New Employee

-   Automate the **end-to-end creation of new employee records**
-   Handle:
    -   Form inputs
    -   Dropdown selections
    -   Save confirmation

### PIM: Search Existing Employee

-   Verify employee data by searching using **Employee ID**
-   Handle **dynamic web tables**
-   Validate that created records exist in the system

------------------------------------------------------------------------

##  Project Structure

    orangehrm_automation/
    │
    ├── Pages/                # Page Object classes
    │   └── LoginPage.py      # Login locators and action methods
    │
    ├── tests/                # Functional test scripts
    │   └── test_login.py     # Login test cases
    │
    ├── venv/                 # Virtual environment (ignored by Git)
    │
    ├── conftest.py           # Pytest fixtures for driver initialization
    │
    └── requirements.txt      # Project dependencies

------------------------------------------------------------------------

##  Getting Started

###  Clone the Repository

``` bash
git clone https://github.com/amrutha-tester/orangehrm_automation
cd orangehrm_automation
```

------------------------------------------------------------------------

###  Setup and Activate Virtual Environment

``` bash
python -m venv venv
```

**Windows**

``` bash
.\venv\Scripts\activate
```

**Mac / Linux**

``` bash
source venv/bin/activate
```

------------------------------------------------------------------------

###  Install Dependencies

``` bash
pip install -r requirements.txt
```

------------------------------------------------------------------------

###  Run the Tests

``` bash
pytest tests/test_login.py
```

------------------------------------------------------------------------

##  Future Improvements

-   Add Employee (PIM Module) automation
-   Search Employee automation
-   Test reports (Pytest HTML / Allure)
-   CI/CD integration (GitHub Actions)
-   Screenshot capture on test failure

------------------------------------------------------------------------

##  Author

**Amrutha**

Automation testing practice project using **Python + Selenium + Pytest**
to build a scalable automation framework.
