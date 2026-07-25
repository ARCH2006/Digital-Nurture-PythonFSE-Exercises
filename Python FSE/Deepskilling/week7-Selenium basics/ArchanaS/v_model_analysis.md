# SDLC vs TDLC – V-Model & Agile QA Integration

## Hands-On 2: SDLC vs TDLC – V-Model & Agile QA Integration

---

# Task 1: V-Model Mapping

## 9. V-Model Diagram

The V-Model (Verification and Validation Model) establishes a relationship between software development phases (SDLC) and corresponding testing phases (TDLC). Testing activities are planned in parallel with development activities.

```text
                 SDLC (Development)                 TDLC (Testing)

               Requirements ---------------------> Acceptance Testing
                    |                                     ^
                    |                                     |
              System Design ----------------------> System Testing
                    |                                     ^
                    |                                     |
          Architecture Design -------------------> Integration Testing
                    |                                     ^
                    |                                     |
             Module Design ----------------------> Unit Testing
                    \                                     /
                     \                                   /
                      \                                 /
                           -------- Coding --------
```

### Phase Mapping

| SDLC Phase          | Corresponding TDLC Phase |
| ------------------- | ------------------------ |
| Requirements        | Acceptance Testing       |
| System Design       | System Testing           |
| Architecture Design | Integration Testing      |
| Module Design       | Unit Testing             |
| Coding              | Implementation           |

---

## 10. Test Artifacts Produced During Development

| SDLC Phase          | Test Artifact Produced                        |
| ------------------- | --------------------------------------------- |
| Requirements        | Acceptance Test Plan, Acceptance Test Cases   |
| System Design       | System Test Plan, System Test Cases           |
| Architecture Design | Integration Test Plan, Integration Test Cases |
| Module Design       | Unit Test Cases, Unit Test Plan               |
| Coding              | Source Code, Unit Test Execution              |

### Explanation

* **Requirements Phase:** QA prepares the Acceptance Test Plan based on business requirements.
* **System Design Phase:** QA prepares System Test Cases to verify complete system functionality.
* **Architecture Design Phase:** QA designs Integration Test Cases to validate interactions between modules.
* **Module Design Phase:** Developers prepare Unit Test Cases for individual modules.
* **Coding Phase:** Developers implement the code and execute unit tests.

---

## 11. Entry Criteria and Exit Criteria

### Unit Testing

**Entry Criteria**

* Module design is completed.
* Source code is implemented.
* Unit test cases are prepared.

**Exit Criteria**

* All unit tests executed successfully.
* No Critical or High severity defects remain.
* Code coverage target is achieved.

---

### Integration Testing

**Entry Criteria**

* Individual modules pass Unit Testing.
* Integration Test Cases are ready.
* Required modules are integrated.

**Exit Criteria**

* All integration test cases pass.
* Interfaces between modules work correctly.
* No Critical integration defects remain.

---

### System Testing

**Entry Criteria**

* Complete application is deployed in the test environment.
* System Test Cases are prepared.
* Integration Testing is completed.

**Exit Criteria**

* All planned System Test Cases are executed.
* Critical and High severity defects are resolved.
* Application meets functional requirements.

---

### Acceptance Testing

**Entry Criteria**

* System Testing is completed successfully.
* Business users are available.
* Acceptance Test Cases are approved.

**Exit Criteria**

* Customer accepts the application.
* Business requirements are satisfied.
* Product is approved for production deployment.

---

## 12. Early QA Engagement Points

For the Course Management API project, QA should participate before testing begins.

### 1. Requirements Review

QA reviews the requirements to ensure they are:

* Clear
* Complete
* Testable
* Free from ambiguity

Example:
QA confirms whether the API should reject duplicate course codes and what response code should be returned.

---

### 2. Design Review

QA participates in design discussions by:

* Reviewing API endpoints
* Validating database design
* Identifying possible edge cases
* Planning Integration and System Test Cases early

Example:
QA verifies how the Course API interacts with the Department and Student modules before implementation begins.

---

# Task 2: Agile QA and Shift-Left Testing

## 13. Problems with Waterfall Testing

In the Waterfall model, testing starts only after development is completed. This creates several challenges.

### Problem 1: Late Defect Detection

Bugs are discovered only after the entire application is developed.

Example:
A duplicate course code validation issue is found after all CRUD APIs are completed, making the fix more expensive.

---

### Problem 2: Higher Cost of Fixing Defects

Fixing defects late requires changes to multiple modules.

Example:
Changing database validation after deployment affects APIs, frontend, and documentation.

---

### Problem 3: Delayed Project Delivery

If many defects are discovered together, release schedules are delayed.

Example:
System Testing uncovers several API failures, postponing the application release.

---

## 14. QA Role in Agile Ceremonies

### Sprint Planning

* Understand user stories.
* Define Acceptance Criteria.
* Estimate testing effort.
* Identify testing risks.

---

### Daily Stand-up

* Share testing progress.
* Report blockers.
* Discuss newly discovered defects.
* Coordinate with developers.

---

### Sprint Review

* Validate completed features.
* Demonstrate functionality.
* Verify user stories meet acceptance criteria.

---

### Sprint Retrospective

* Discuss what worked well.
* Identify testing improvements.
* Suggest process enhancements.
* Reduce recurring defects.

---

## 15. Shift-Left Testing Practices

### A. Review Requirements for Testability

QA reviews requirements before coding begins.

Example:
Verify that the Course Creation API clearly specifies validation rules.

---

### B. Write Test Cases Before Code (TDD/BDD)

QA prepares test scenarios before developers implement the feature.

Example:
Create test cases for:

* Valid course creation
* Duplicate course code
* Missing required fields

---

### C. Static Code Analysis

Developers use static analysis tools to detect coding issues before execution.

Example:
Run code quality checks to identify unused variables, syntax issues, or coding standard violations.

---

### D. API Contract Testing

Verify API request and response formats before integrating services.

Example:
Confirm that `POST /api/courses/` always returns the documented JSON structure and status codes.

---

## 16. Acceptance Criteria (Given–When–Then)

### Scenario 1 – Happy Path

```gherkin
Given the College Admin is logged in
When the Admin enters valid course details
And clicks Create Course
Then the course should be created successfully
And the API should return HTTP 201 Created
```

---

### Scenario 2 – Duplicate Course Code

```gherkin
Given a course with code "CS101" already exists
When the Admin creates another course using "CS101"
Then the API should reject the request
And an appropriate error message should be displayed
```

---

### Scenario 3 – Missing Required Fields

```gherkin
Given the College Admin is on the Create Course page
When the Admin submits the form without the Course Name
Then the API should return HTTP 422 Validation Error
And the validation message should identify the missing field
```

---

# Conclusion

This hands-on demonstrated:

* SDLC and TDLC phase mapping using the V-Model.
* Test artifacts produced during each development phase.
* Entry and Exit Criteria for Unit, Integration, System, and Acceptance Testing.
* Early QA involvement in Requirements and Design phases.
* Problems with the Waterfall model.
* QA responsibilities during Agile ceremonies.
* Shift-Left testing practices.
* Acceptance Criteria written using the Gherkin (Given–When–Then) format.

These concepts help QA engineers identify defects earlier, improve software quality, reduce development costs, and ensure the application meets business requirements before release.
