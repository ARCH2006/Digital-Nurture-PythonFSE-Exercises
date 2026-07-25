from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import os

BASE_URL = "https://www.lambdatest.com/selenium-playground/"


def _save_debug_evidence(driver, test_name):
    """Save screenshot and page source on failure for debugging."""
    os.makedirs("debug_output", exist_ok=True)
    screenshot_path = f"debug_output/{test_name}_failure.png"
    html_path = f"debug_output/{test_name}_failure.html"
    driver.save_screenshot(screenshot_path)
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(driver.page_source)
    print(f"\n[DEBUG] Screenshot saved → {screenshot_path}")
    print(f"[DEBUG] Page source saved → {html_path}")
    print(f"[DEBUG] Current URL: {driver.current_url}")
    print(f"[DEBUG] Page title: {driver.title}")


def test_simple_form_submission(driver):
    driver.get(BASE_URL + "simple-form-demo")

    message = "Hello Selenium"

    try:
        input_box = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.ID, "user-message"))
        )
    except TimeoutException:
        _save_debug_evidence(driver, "simple_form_input")
        raise

    input_box.clear()
    input_box.send_keys(message)

    driver.find_element(By.ID, "showInput").click()

    try:
        displayed_message = WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located((By.ID, "message"))
        )
    except TimeoutException:
        _save_debug_evidence(driver, "simple_form_message")
        raise

    assert displayed_message.text == message


def test_checkbox_demo(driver):
    driver.get(BASE_URL + "checkbox-demo")

    checkbox = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "input[type='checkbox']")
        )
    )

    checkbox.click()
    assert checkbox.is_selected()

    checkbox.click()
    assert not checkbox.is_selected()
