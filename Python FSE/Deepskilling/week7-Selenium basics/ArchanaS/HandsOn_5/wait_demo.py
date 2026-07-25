import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, WebDriverException

def run_task_2_demo():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    # Selenium Manager (bundled with Selenium) locates a compatible ChromeDriver.
    # This avoids webdriver-manager modifying its cache in ~/.wdm at startup.
    driver = webdriver.Chrome(options=options)
    
    try:
        try:
            driver.get("https://www.lambdatest.com/selenium-playground/bootstrap-alert-messages-demo")
        except WebDriverException as e:
            print("\n Network Connection Error: Could not reach the test website.")
            print("Please check your internet connection and try again.")
            return

        wait = WebDriverWait(driver, 10)
        success_btn_xpath = "//button[contains(text(), 'Normal Success')]"
        success_btn = driver.find_element(By.XPATH, success_btn_xpath)

        # --- STEP 36 & 37: TIMING EXPLICIT WAIT VS TIME.SLEEP ---
        print("--- Step 36 & 37: Speed Comparison ---")
        success_btn.click()
        
        start_explicit = time.time()
        # Target the success alert by its semantic CSS class rather than its
        # display text, which the demo site has changed over time.
        alert_text_xpath = "//div[contains(@class, 'alert') and contains(@class, 'success') and not(contains(@style, 'display: none'))]"
        alert = wait.until(EC.visibility_of_element_located((By.XPATH, alert_text_xpath)))
        end_explicit = time.time()
        
        explicit_time = end_explicit - start_explicit
        print(f"✓ Explicit Wait caught alert in: {explicit_time:.4f} seconds")
        assert "success" in alert.text.lower()

        # Compare with time.sleep
        driver.refresh()
        success_btn = wait.until(EC.element_to_be_clickable((By.XPATH, success_btn_xpath)))
        success_btn.click()
        
        start_sleep = time.time()
        time.sleep(3)  # Hard sleep pause
        alert_sleep = driver.find_element(By.XPATH, alert_text_xpath)
        end_sleep = time.time()
        
        sleep_time = end_sleep - start_sleep
        print(f"✗ time.sleep(3) forced script to pause for: {sleep_time:.4f} seconds")
        print(f"Result: Explicit wait was {sleep_time - explicit_time:.2f} seconds faster!")

        print("\n--- Step 38: Clickable Check ---")
        driver.get("https://www.lambdatest.com/selenium-playground/bootstrap-alert-messages-demo")
        
        clickable_btn = wait.until(EC.element_to_be_clickable((By.XPATH, success_btn_xpath)))
        clickable_btn.click()
        print("✓ Element clicked securely using EC.element_to_be_clickable()")

        print("\n--- Step 39: Fluent Wait Dynamic Table Polling ---")
        driver.get("https://www.lambdatest.com/selenium-playground/table-data-download-demo")
        
        fluent_wait = WebDriverWait(driver, timeout=10, poll_frequency=0.5, ignored_exceptions=[NoSuchElementException])
        first_row = fluent_wait.until(EC.visibility_of_element_located((By.XPATH, "//table[@id='example']/tbody/tr[1]")))
        print("✓ Fluent Wait successfully polled and located the dynamic data table rows.")

    finally:
        driver.quit()

if __name__ == "__main__":
    run_task_2_demo()
