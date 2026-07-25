# QA Concepts, Functional Testing & Defect Lifecycle

## Hands-On 1: QA Concepts, Functional Testing & Defect Lifecycle

---

# Task 1: Map Testing Types to a Real System

## 1. Testing Types for the Course Management API

### Unit Testing

**Definition:** Unit testing verifies a single function or method in isolation without involving external components such as databases or APIs.

**Test Case:**

* Test the `validate_course_code()` function.
* Input: `CS101`
* Expected Result: Function returns `True`.

**Testing Type:** Functional Testing

---

### Integration Testing

**Definition:** Integration testing verifies that two or more components work correctly together.

**Test Case:**

* Send a `POST /api/courses/` request with valid course details.
* Verify that:

  * The API returns HTTP Status Code **201 Created**.
  * The course record is successfully stored in the database.

**Testing Type:** Functional Testing

---

### System Testing

**Definition:** System testing validates the complete application as a whole.

**Test Case:**
Perform the complete workflow:

1. Create a course.
2. Retrieve the created course.
3. Update the course details.
4. Delete the course.
5. Verify that the course is removed successfully.

**Testing Type:** Functional Testing

---

### User Acceptance Testing (UAT)

**Definition:** User Acceptance Testing ensures that the software satisfies business requirements from the end user's perspective.

**Test Case:**
A College Administrator:

* Logs into the system.
* Creates a new course.
* Confirms the course appears in the course list.
* Updates the course information.
* Deletes the course successfully.

**Testing Type:** Functional Testing

---

## 2. Functional vs Non-Functional Testing

### Functional Testing

Functional testing verifies **what the system does** and ensures that each feature works according to the specified requirements.

**Examples**

* Create Course
* Update Course
* Delete Course
* View Course Details

---

### Non-Functional Testing

Non-functional testing verifies **how well the system performs**.

**Example: Performance Testing**

* Send 500 concurrent requests to `GET /api/courses/`.
* Verify that:

  * Average response time is less than 2 seconds.
  * No server crashes occur.
  * All responses are returned successfully.

This is a **Non-Functional Test** because it measures system performance rather than functionality.

---

## 3. Black-Box Testing vs White-Box Testing

| Black-Box Testing                                     | White-Box Testing                                      |
| ----------------------------------------------------- | ------------------------------------------------------ |
| Tests the software without knowing the internal code. | Tests the internal code, logic, and program structure. |
| Focuses on inputs and outputs.                        | Focuses on code paths, conditions, and logic.          |
| No programming knowledge is required.                 | Programming knowledge is required.                     |
| Usually performed by QA Engineers.                    | Usually performed by Developers.                       |

### Example

**Black-Box Testing**

* Send a request to `POST /api/courses/`.
* Verify the response without knowing how the code is implemented.

**White-Box Testing**

* Test the `validate_course_code()` function by checking every logical condition and code branch.

**Typically Performed By**

* **QA Tester:** Black-Box Testing
* **Developer:** White-Box Testing

---

## 4. Formal Test Cases for POST /api/courses/

| Test Case ID | Description                                   | Preconditions                            | Test Steps                                                                    | Expected Result                                                      | Actual Result | Pass/Fail |
| ------------ | --------------------------------------------- | ---------------------------------------- | ----------------------------------------------------------------------------- | -------------------------------------------------------------------- | ------------- | --------- |
| TC001        | Create a course with valid data               | API server is running                    | 1. Send POST request with valid course details.<br>2. Submit the request.     | HTTP 201 Created. Course is stored successfully in the database.     |               |           |
| TC002        | Create a course with missing required field   | API server is running                    | 1. Send POST request without the course name.<br>2. Submit the request.       | HTTP 422 Validation Error. Appropriate error message is returned.    |               |           |
| TC003        | Create a course using an existing course code | Course with the same code already exists | 1. Send POST request using an existing course code.<br>2. Submit the request. | API rejects the duplicate request with an appropriate error message. |               |           |

---

# Task 2: Defect Lifecycle & Severity Classification

## 5. Defect Lifecycle

```
                 +----------------+
                 |      NEW       |
                 +----------------+
                          |
                          v
                 +----------------+
                 |    ASSIGNED    |
                 +----------------+
                          |
                          v
                 +----------------+
                 |      OPEN      |
                 +----------------+
                          |
                          v
                 +----------------+
                 |     FIXED      |
                 +----------------+
                          |
                          v
                 +----------------+
                 |    RETEST      |
                 +----------------+
                          |
                +---------+---------+
                |                   |
                v                   v
        +---------------+    +--------------+
        |   VERIFIED    |    |    REOPEN    |
        +---------------+    +--------------+
                |                   |
                v                   |
        +---------------+-----------+
        |     CLOSED    |
        +---------------+
```

### Additional Paths

**Rejected**

* The reported issue is not considered a valid defect.

**Deferred**

* The defect is acknowledged but scheduled to be fixed in a future release.

---

## 6. Severity and Priority Classification

| Bug                                                                   | Severity | Priority | Justification                                                                           |
| --------------------------------------------------------------------- | -------- | -------- | --------------------------------------------------------------------------------------- |
| POST /api/courses/ returns 500 Internal Server Error for all requests | Critical | P1       | Core functionality is completely broken and must be fixed immediately.                  |
| Course names longer than 150 characters are silently truncated        | Medium   | P2       | Data integrity issue affecting users, but the application still functions.              |
| Typo in Swagger (/docs) page                                          | Low      | P4       | Cosmetic issue with minimal impact on functionality.                                    |
| Login occasionally returns 401 on the first attempt                   | High     | P1       | Intermittent login failures impact user experience and may indicate system instability. |

---

## 7. Defect Report

**Defect ID:** BUG-001

**Title:** POST /api/courses/ returns HTTP 500 Internal Server Error

**Environment**

* Windows 11
* Python 3.11
* FastAPI
* PostgreSQL
* Google Chrome

**Build Version**

* v1.0

**Severity**

* Critical

**Priority**

* P1

**Steps to Reproduce**

1. Start the application.
2. Open Swagger UI.
3. Navigate to `POST /api/courses/`.
4. Enter valid course details.
5. Click **Execute**.

**Expected Result**

* HTTP Status Code **201 Created**.
* Course should be stored successfully.

**Actual Result**

* HTTP Status Code **500 Internal Server Error**.
* Course is not created.

**Attachments**

* Screenshot of 500 Internal Server Error.

---

## 8. Difference Between Severity and Priority

### Severity

Severity indicates **how much impact a defect has on the application**.

Example:
If users cannot create a course because the API crashes, the defect has **Critical Severity**.

---

### Priority

Priority indicates **how urgently the defect should be fixed**.

Example:
A spelling mistake on the CEO's dashboard has **Low Severity** because it does not affect functionality. However, it may have **High Priority (P1)** because it is highly visible during an important business presentation.

---

## Conclusion

This hands-on demonstrated:

* Different software testing levels.
* Functional and Non-Functional Testing.
* Black-Box and White-Box Testing.
* Professional test case documentation.
* Complete defect lifecycle.
* Severity and Priority classification.
* Professional defect reporting.

These concepts form the foundation of Quality Assurance and are essential for both manual testing and Selenium automation.
