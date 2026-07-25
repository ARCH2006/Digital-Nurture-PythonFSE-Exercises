"""
Hands-On 4
Task 1

Selenium Components

1. WebDriver
   WebDriver is the Selenium component that directly communicates with
   the browser using browser-specific drivers like ChromeDriver.

2. Selenium Grid
   Selenium Grid allows tests to run on multiple machines, browsers,
   and operating systems simultaneously.

3. Selenium IDE
   Selenium IDE is a browser extension used to record and playback
   browser actions and generate automation scripts.
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Configure Chrome options
options = webdriver.ChromeOptions()

# Run browser in headless mode
options.add_argument("--headless")

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
)

# Implicit wait
# Implicit wait applies globally to all element searches.
# It is generally not recommended because it can make tests slower
# and may interfere with explicit waits, which are more precise.
driver.implicitly_wait(10)

# Open website
driver.get("https://www.lambdatest.com/selenium-playground/")

# Print page title
print("Title:", driver.title)

# Close browser
driver.quit()