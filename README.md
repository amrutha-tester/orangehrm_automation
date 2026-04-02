# OrangeHRM Professional Test Automation Framework

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Selenium](https://img.shields.io/badge/Selenium-WebDriver-green)
![Docker](https://img.shields.io/badge/Docker-Containerized-blue)
![Jenkins](https://img.shields.io/badge/Jenkins-CI%2FCD-red)
![Pytest](https://img.shields.io/badge/Pytest-Framework-yellow)
![Allure](https://img.shields.io/badge/Reporting-Allure-purple)

------------------------------------------------------------------------

##  Overview

This repository contains a **System-level Functional Automation
Framework** designed for the OrangeHRM platform. It leverages **Selenium
Grid** and **Docker** for containerized browser orchestration and is
fully integrated into a **CI/CD Pipeline with Jenkins** for automated
quality assurance.

------------------------------------------------------------------------

##  Architecture

### Framework Design

-   **Test Layer →** Pytest test scenarios
-   **Page Layer →** Page Object Model (POM)
-   **Execution Layer →** Selenium Grid
-   **Infrastructure Layer →** Docker Compose
-   **Pipeline Layer →** Jenkins CI/CD
-   **Reporting Layer →** Allure Reports

------------------------------------------------------------------------

##  Infrastructure Highlights

### Distributed Execution

Runs tests across multiple browsers:

-   Chrome
-   Firefox
-   Edge

Using Selenium Grid Hub & Nodes.

### Containerization

Docker Compose orchestrates:

-   Selenium Hub
-   Browser Nodes
-   Test Runner Container

This guarantees reproducible execution environments.

### CI/CD Integration

Jenkins pipeline automatically:

1 Build project\
2 Start containers\
3 Execute tests\
4 Generate reports\
5 Archive results

### Parallel Execution

Uses:

pytest‑xdist

To run tests in parallel workers and reduce execution time.

------------------------------------------------------------------------

## Test Scenarios

The suite validates the full **CRUD (Create, Read, Update, Delete)**
lifecycle and persona‑based access across these scenarios:

### OHRM_1: Employee Lifecycle (Admin Path)

**Validates:**

-   Login functionality
-   Add employee workflow
-   PIM module integration

### OHRM_2: Data Integrity & Search (Positive)

**Validates:**

-   Employee search
-   Correct record retrieval
-   Database/UI consistency

### OHRM_3: Negative Testing & Edge Cases

**Validates:**

-   Invalid employee search
-   System stability
-   UI error handling

**Assertion:**

"No Records Found" state is displayed.

### OHRM_4: Asynchronous Modal & Delete Workflow

**Technical validations:**

-   Async modal handling
-   Confirmation dialog automation
-   Record deletion validation
-   UI refresh synchronization

### OHRM_5: Self‑Service (ESS Persona)

**Validates:**

-   Role based access
-   Restricted modules
-   Profile updates
-   My Info module

------------------------------------------------------------------------

##  Tech Stack

  Category        Technology
  --------------- ----------------------------
  Language         Python
  Framework        Pytest
  Automation       Selenium WebDriver
  Grid             Selenium Grid
  Containers       Docker
  CI/CD            Jenkins
  Reporting        Allure
  Design Pattern   Page Object Model

------------------------------------------------------------------------

##  Project Structure

    orangehrm_automation
    ├── Pages/             # Page Object Model locators and actions
    ├── TestCases/         # Pytest test scripts
    ├── allure-results/    # Generated test data for reporting
    ├── Dockerfile         # Python environment configuration
    ├── docker-compose.yml # Selenium Grid & Service orchestration
    ├── Jenkinsfile        # CI/CD Pipeline definition
    ├── config.ini         # Environment & URL configurations
    └── requirements.txt   # Project dependencies

------------------------------------------------------------------------

##  Execution Guide

### 1. One‑Command Run (Docker)

The most efficient way to run the suite is via Docker Compose. This
spins up the Hub, Nodes, and Test container automatically.

``` bash
docker-compose up --build
```

Framework automatically:

✔ Starts Selenium Grid\
✔ Starts browsers\
✔ Waits for Hub health\
✔ Executes tests\
✔ Generates reports

### 2. Manual Execution (Local)

If running without Docker, ensure you have the requirements installed:

Install dependencies:

``` bash
pip install -r requirements.txt
```

Run tests:

``` bash
pytest TestCases/ --alluredir=allure-results
```

### 3. Reporting

To view the interactive graphical dashboard:

``` bash
allure serve allure-results
```

------------------------------------------------------------------------

##  Engineering Capabilities

### Smart Wait Strategy

Uses:

WebDriverWait + Expected Conditions

To handle:

-   Dynamic tables
-   Async popups
-   DOM refreshes

### Data Driven Testing

Uses:

pytest parametrize

Allows:

Multiple datasets Reusable workflows

### Stability Engineering

Framework includes:

-   Retry connection logic
-   Scroll into view fallback
-   JavaScript click fallback
-   Element visibility guards

### Maintainability

Uses Page Object Model:

Separates:

Test logic UI locators Business actions

Improves maintainability and readability.

------------------------------------------------------------------------

##  Key Benefits

-   Scalable distributed test execution
-   Containerized infrastructure
-   CI/CD ready automation framework
-   Parallel execution support
-   Professional reporting with Allure
-   Maintainable design using Page Object Model

------------------------------------------------------------------------

##  Future Improvements

Possible enhancements:

-   API testing integration
-   Performance testing
-   GitHub Actions pipeline
-   Slack notifications
-   Test analytics dashboard

