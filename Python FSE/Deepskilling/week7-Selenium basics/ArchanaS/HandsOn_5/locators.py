from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install())
)

driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://www.lambdatest.com/selenium-playground/")

driver.find_element(By.LINK_TEXT, "Simple Form Demo").click()

driver.find_element(By.ID, "user-message").send_keys("Using ID")

driver.find_element(By.NAME, "message").clear()
driver.find_element(By.NAME, "message").send_keys("Using Name")

driver.find_element(By.CLASS_NAME, "form-control").clear()
driver.find_element(By.CLASS_NAME, "form-control").send_keys("Using Class")

driver.find_element(By.TAG_NAME, "input").clear()
driver.find_element(By.TAG_NAME, "input").send_keys("Using Tag")

driver.find_element(By.XPATH, "//input[@id='user-message']").clear()
driver.find_element(By.XPATH, "//input[@id='user-message']").send_keys("Using XPath")

driver.find_element(By.CSS_SELECTOR, "#user-message").clear()
driver.find_element(By.CSS_SELECTOR, "#user-message").send_keys("Using CSS")

driver.quit()

"""
Locator Ranking (Best → Worst)

1. ID
   - Unique
   - Fast
   - Readable

2. CSS Selector
   - Fast
   - Flexible
   - Short syntax

3. Name
   - Good if unique

4. Relative XPath
   - Powerful
   - Supports text(), contains(), axes

5. Class Name
   - Classes are often shared

6. Tag Name
   - Usually returns multiple elements

7. Absolute XPath
   - Worst
   - Breaks whenever HTML structure changes
"""