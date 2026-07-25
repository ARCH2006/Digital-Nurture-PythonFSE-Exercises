from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install())
)

driver.get("https://www.lambdatest.com/selenium-playground")

driver.save_screenshot("./screenshots/playground_screenshot.png")

print("Screenshot Saved")

print(driver.get_window_size())      # e.g. {'width': 964, 'height': 832}
driver.set_window_size(1280, 800)


driver.quit()