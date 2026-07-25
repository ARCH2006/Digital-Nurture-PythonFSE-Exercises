# Test Automation Process, Lifecycle & Framework Types

## Hands-On 3: Automation Strategy for Course Management System

# Task 1: Automation Decision and Test Case Selection

## 17. Criteria for Deciding Whether a Test Should Be Automated

### Criterion 1: Repetitive Execution

Tests executed frequently are strong candidates for automation because automation reduces manual effort and saves time.

**Application to POST /api/courses/**

The course creation endpoint is tested repeatedly during every build and regression cycle. Therefore, automating this test is beneficial.

**Decision:** Automate.

---

### Criterion 2: Regression Testing

Regression tests verify that existing functionality still works after code changes. Since they run repeatedly, they provide excellent automation ROI.

**Application to POST /api/courses/**

Every backend update can impact course creation. The test must be executed after every release.

**Decision:** Automate.

---

### Criterion 3: High Business Risk

Critical features that directly affect users should be automated to ensure reliability.

**Application to POST /api/courses/**

If course creation fails, students cannot enroll and administrators cannot manage courses.

**Decision:** Automate.

---

### Criterion 4: Data-Driven Scenarios

Tests requiring multiple combinations of inputs are ideal for automation.

**Application to POST /api/courses/**

Different combinations of valid course names, credits, departments, and course codes can be tested efficiently through automated scripts.

**Decision:** Automate.

---

### Criterion 5: Stable Functionality

Features with stable requirements are good automation candidates because scripts remain maintainable.

**Application to POST /api/courses/**

Course creation is a core feature and its behavior is unlikely to change frequently.

**Decision:** Automate.

---

## Final Automation Decision

The test case:

> Verify that POST /api/courses/ returns HTTP 201 and stores the correct course data when valid input is provided.

meets all five automation criteria and should be automated.

---

## 18. Manual vs Automated Test Selection

| Test Case                                                    | Decision | Justification                                                             |
| ------------------------------------------------------------ | -------- | ------------------------------------------------------------------------- |
| Regression testing for all CRUD APIs after every code change | Automate | Executed frequently and ideal for regression automation.                  |
| Exploratory testing of a new search feature                  | Manual   | Human creativity and investigation are required.                          |
| Performance test with 100 concurrent users                   | Automate | Performance testing requires tools and large-scale execution.             |
| UI login test                                                | Automate | Login is a critical and repetitive workflow.                              |
| Verify Swagger documentation accuracy                        | Manual   | Documentation review often requires human validation and interpretation.  |
| Smoke test after deployment                                  | Automate | Quick automated validation ensures the system is reachable after release. |

---

## 19. Test Automation ROI

### Definition

Test Automation ROI (Return on Investment) measures whether the time and cost spent creating and maintaining automation are lower than the effort required for repeated manual execution.

---

### Given

Automation development effort = **4 hours**

Manual execution time = **30 minutes (0.5 hours)**

Maintenance overhead after the 10th run = **20% of manual execution time**

20% of 0.5 hours = **0.1 hours**

---

### Break-Even Calculation

Manual effort after N runs:

```text
Manual Cost = 0.5 × N hours
```

Automation cost for the first 10 runs:

```text
Automation Cost = 4 hours
```

Break-even:

```text
4 ÷ 0.5 = 8 runs
```

Therefore, automation pays for itself after **8 executions**.

After the 10th run:

```text
Automation Cost = 4 + (0.1 × additional runs)
```

Even with maintenance overhead, automation remains significantly cheaper than repeated manual execution.

---

## 20. Flaky Tests

### Definition

A flaky test is a test that sometimes passes and sometimes fails without any actual change in the application.

Flaky tests reduce confidence in the automation suite and create false failures.

---

### Example

A Selenium script clicks the Login button immediately after page load.

Sometimes the button loads quickly and the test passes.

Sometimes the button loads slowly and the test fails with:

```text
ElementNotInteractableException
```

The application is correct, but the test is unreliable.

---

### Strategies to Prevent Flaky Tests

### 1. Use Explicit Waits

Avoid `time.sleep()` and use `WebDriverWait()`.

---

### 2. Use Stable Locators

Prefer:

* ID
* Name
* CSS Selectors

Avoid fragile absolute XPath expressions.

---

### 3. Ensure Test Isolation

Each test should create and clean its own data so tests do not affect one another.

---

# Task 2: Compare Automation Framework Types

## 21. Framework Comparison

### Linear Framework

#### Description

The Linear Framework executes scripts sequentially in a single file. Test data, logic, and locators are all written together.

#### Advantage

Simple and easy for beginners.

#### Disadvantage

Poor maintainability and almost no reusability.

#### Course Management Example

Suitable only for a very small prototype with a few API tests.

---

### Modular Framework

#### Description

The application is divided into reusable modules. Common actions such as login or course creation are written once and reused.

#### Advantage

High reusability.

#### Disadvantage

Managing large amounts of test data becomes difficult.

#### Course Management Example

Separate modules:

* Login Module
* Course Module
* Enrollment Module
* Student Module

---

### Data-Driven Framework

#### Description

Test data is separated from test scripts and stored externally in CSV, JSON, Excel, or databases.

#### Advantage

One script can execute many test scenarios.

#### Disadvantage

Data management becomes more complex.

#### Course Management Example

Run the login test using 50 different username and password combinations.

---

### Keyword-Driven Framework

#### Description

Tests are written using predefined keywords such as Login, Click, EnterText, or Logout.

#### Advantage

Non-technical users can create test scenarios.

#### Disadvantage

Initial setup is complex.

#### Course Management Example

Business analysts define:

```text
Login
Create Course
Verify Course
Logout
```

without writing Selenium code.

---

### Hybrid Framework

#### Description

Hybrid Framework combines Modular, Data-Driven, and Keyword-Driven approaches to maximize maintainability, scalability, and reusability.

#### Advantage

Highly scalable and suitable for enterprise applications.

#### Disadvantage

Requires more planning and architecture.

#### Course Management Example

A large Selenium framework supporting multiple modules, external data files, reusable page objects, and keyword execution.

---

## Framework Comparison Table

| Framework      | Reusability | Data Support | Easy for Non-Technical Users | Scalability |
| -------------- | ----------- | ------------ | ---------------------------- | ----------- |
| Linear         | Low         | Low          | No                           | Low         |
| Modular        | High        | Medium       | No                           | Medium      |
| Data-Driven    | High        | High         | No                           | High        |
| Keyword-Driven | Medium      | High         | Yes                          | High        |
| Hybrid         | Very High   | Very High    | Yes                          | Very High   |

---

## 22. Recommended Framework

### Requirement Analysis

The team needs:

* 50 login combinations.
* Reusable login functionality.
* Support for technical and non-technical users.
* Long-term maintainability.

### Recommendation

A **Hybrid Framework** combining:

* Modular Framework
* Data-Driven Framework
* Keyword-Driven Framework

### Justification

* Modular supports reusable login methods.
* Data-Driven supports 50 credential combinations.
* Keyword-Driven allows non-technical members to write scenarios.
* Hybrid provides scalability and maintainability for future growth.

Therefore, Hybrid is the most suitable framework.

---

## 23. Hybrid Framework Folder Structure

```text
CourseManagementAutomation/

│
├── config/
│   ├── config.yaml
│   └── environment.py
│
├── test_data/
│   ├── login_data.csv
│   ├── courses.json
│   └── users.xlsx
│
├── pages/
│   ├── login_page.py
│   ├── course_page.py
│   ├── student_page.py
│   └── enrollment_page.py
│
├── keywords/
│   ├── login_keywords.py
│   ├── course_keywords.py
│   └── common_keywords.py
│
├── utilities/
│   ├── driver_factory.py
│   ├── logger.py
│   ├── waits.py
│   └── screenshots.py
│
├── tests/
│   ├── test_login.py
│   ├── test_courses.py
│   ├── test_students.py
│   └── test_enrollment.py
│
├── reports/
│
├── screenshots/
│
├── conftest.py
│
└── requirements.txt
```

### Purpose of Each Folder

* **config/** – Environment settings and configuration files.
* **test_data/** – CSV, Excel, JSON test data.
* **pages/** – Page Object Model classes.
* **keywords/** – Reusable keyword implementations.
* **utilities/** – Common helper functions.
* **tests/** – Actual test cases.
* **reports/** – HTML or Allure reports.
* **screenshots/** – Failure screenshots.

This architecture supports maintainability, reusability, scalability, and collaboration between both technical and non-technical team members.

---

# Conclusion

This automation strategy identifies suitable automation candidates, explains automation ROI, addresses flaky tests, compares framework architectures, recommends a Hybrid Framework, and defines a scalable enterprise-level Selenium framework structure for the Course Management system.
