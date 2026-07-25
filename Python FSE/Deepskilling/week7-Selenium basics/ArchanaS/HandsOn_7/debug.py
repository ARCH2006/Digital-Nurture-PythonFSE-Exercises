from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://www.lambdatest.com/selenium-playground/select-dropdown-demo")

print("Current URL:", driver.current_url)
print("Title:", driver.title)

print("\nFirst 500 characters of page source:\n")
print(driver.page_source[:500])

input("Press Enter to close...")
driver.quit()