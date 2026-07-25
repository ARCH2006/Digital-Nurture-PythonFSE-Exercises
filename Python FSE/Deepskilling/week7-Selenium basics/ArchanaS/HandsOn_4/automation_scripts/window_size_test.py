from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install())
)

driver.get("https://www.lambdatest.com/selenium-playground")

# Get current window size
print("Current Size:", driver.get_window_size())

# Set a consistent window size
driver.set_window_size(1280, 800)

print("New Size:", driver.get_window_size())

# A consistent window size helps ensure UI elements appear
# in predictable locations across test runs, which is important
# for responsive web applications.

driver.quit()