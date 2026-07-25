# Selenium Page Object Model (POM) Framework

A hands-on project that demonstrates how to structure automated web UI tests using the Page Object Model design pattern. The tests are written in Python using Selenium WebDriver and Pytest, and run against the LambdaTest Selenium Playground.

## Objective

The goal is to learn how to organize test automation code using the Page Object Model pattern. This involves creating separate page classes for each web page, writing reusable interaction methods, and keeping test cases clean and readable.

## Concepts Covered

- Page Object Model (POM) design pattern
- Explicit waits using WebDriverWait
- Selenium locator strategies (ID, Name, CSS Selector, XPath)
- Pytest fixture setup and teardown
- HTML report generation with pytest-html
- Automated WebDriver management with webdriver-manager
- Testing form inputs, checkboxes, and dropdowns

## Technologies Used

- Python
- Selenium WebDriver
- Pytest
- Pytest-HTML
- WebDriver Manager
- Google Chrome

## Project Structure

```
Hands-on-07/
├── pages/                          # Page Object classes
│   ├── __init__.py                 # Package init
│   ├── base_page.py                # Base class with common Selenium methods
│   ├── simple_form_page.py         # Page object for Simple Form Demo
│   ├── checkbox_page.py            # Page object for Checkbox Demo
│   ├── dropdown_page.py            # Page object for Select Dropdown Demo
│   └── input_form_page.py          # Page object for Input Form Demo
│
├── tests/                          # Pytest test files
│   ├── __init__.py                 # Package init
│   ├── test_simple_form.py         # Test for simple form submission
│   ├── test_checkbox.py            # Test for checkbox selection
│   ├── test_dropdown.py            # Test for dropdown selection
│   └── test_input_form.py          # Test for input form submission
│
├── conftest.py                     # Pytest fixtures (WebDriver setup/teardown)
├── requirements.txt                # Python dependencies
├── TODO.md                         # Progress tracker
└── README.md                       # This file
```

### Folder and File Descriptions

**pages/** - Contains all Page Object classes. Each page of the application under test has its own class with locators and interaction methods.

- `base_page.py` - Parent class for all page objects. Provides reusable methods like `click_element()`, `type_text()`, `get_text()`, `wait_for_element()`, etc.
- `simple_form_page.py` - Page object for the Simple Form Demo page. Contains methods to enter a message and submit it.
- `checkbox_page.py` - Page object for the Checkbox Demo page. Supports single and multiple checkbox interactions.
- `dropdown_page.py` - Page object for the Select Dropdown Demo page. Provides dropdown selection and verification.
- `input_form_page.py` - Page object for the Input Form Demo page. Handles form filling and submission.

**tests/** - Contains all test files. Tests are written using Pytest and use the shared `driver` fixture from conftest.py.

- `test_simple_form.py` - Verifies that entering a message and clicking submit displays the correct output.
- `test_checkbox.py` - Verifies checking and unchecking a checkbox works correctly.
- `test_dropdown.py` - Verifies selecting a value from a dropdown and reading the confirmation message.
- `test_input_form.py` - Verifies filling an input form with multiple fields and checking the success message.

**conftest.py** - Defines the `driver` fixture that creates a Chrome WebDriver instance before each test and quits it after the test completes.

**requirements.txt** - Lists all Python packages needed to run the project.

## Setup Instructions

1. **Create a virtual environment:**

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

   On Windows:

   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

2. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

## Running Tests

Run all tests:

```bash
pytest
```

Run all tests with verbose output:

```bash
pytest -v
```

Run tests from a specific file:

```bash
pytest tests/
```

Run tests and generate an HTML report:

```bash
pytest --html=report.html --self-contained-html
```

Run a single test file:

```bash
pytest tests/test_simple_form.py -v
```

## Expected Output

When you run `pytest -v`, all four tests should pass. The output should look similar to this:

```
tests/test_checkbox.py::test_checkbox_demo PASSED
tests/test_dropdown.py::test_dropdown_selection PASSED
tests/test_input_form.py::test_input_form_submit PASSED
tests/test_simple_form.py::test_simple_form_submission PASSED
```

Each test performs the following:

- **test_simple_form_submission** - Opens the Simple Form Demo page, types "Hello Selenium" into the message field, clicks the submit button, and verifies that the displayed message matches the input.
- **test_checkbox_demo** - Opens the Checkbox Demo page, checks the first checkbox, verifies it is checked, unchecks it, and verifies it is unchecked.
- **test_dropdown_selection** - Opens the Select Dropdown Demo page, selects "Monday" from the dropdown, and verifies that the confirmation message contains "Monday".
- **test_input_form_submit** - Opens the Input Form Demo page, fills in the name, email, phone, and address fields, submits the form, and verifies that a success message appears.

## Framework Design

This project follows the **Page Object Model (POM)** design pattern.

Each web page is represented by a separate class that contains:

- Locators for the elements on that page
- Methods that perform actions on those elements

The `BasePage` class provides common methods that all page objects inherit. This includes explicit waits, click, type, and text retrieval operations.

Test files are kept separate from page objects. Tests use page object methods to interact with the application and Pytest assertions to verify outcomes. This separation means that if the UI changes, only the page object needs to be updated, not the test itself.

The `conftest.py` file provides a `driver` fixture using Pytest's fixture mechanism. The fixture is automatically called before each test and the WebDriver is quit after the test finishes. The `webdriver-manager` library handles downloading the correct version of ChromeDriver.

## Notes

- The tests run against the **LambdaTest Selenium Playground**, which is a third-party website. The site layout, element IDs, CSS classes, and XPaths may change over time. If a test fails unexpectedly, inspect the page to check if locators need to be updated.
- The tests are written for **Google Chrome**. If you use a different browser, you will need to update the WebDriver setup in `conftest.py`.
- The `webdriver-manager` library automatically matches the ChromeDriver version to your installed Chrome browser. If you run into driver compatibility issues, make sure both Chrome and webdriver-manager are up to date.
- This is a learning project. It is not designed for production CI/CD pipelines.

## Learning Outcome

After completing this hands-on, you will be able to:

- Structure a Selenium project using the Page Object Model pattern
- Write reusable base page classes with common interaction methods
- Create page-specific classes with custom locators and actions
- Use Pytest fixtures for WebDriver setup and teardown
- Write clean, maintainable test cases that are independent of page structure
- Generate test reports with pytest-html
- Manage WebDriver binaries automatically using webdriver-manager
