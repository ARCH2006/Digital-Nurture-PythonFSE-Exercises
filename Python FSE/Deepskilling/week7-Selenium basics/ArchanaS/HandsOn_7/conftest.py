"""
Pytest configuration – Hands-on-07.
Provides the shared `driver` fixture for all tests.
"""

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def driver():
    """
    Fixture that creates a Chrome WebDriver before each test
    and quits it after the test completes.

    Uses webdriver-manager to automatically download and cache
    the correct ChromeDriver version.
    """
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    # Uncomment the line below to run in headless mode:
    # options.add_argument("--headless")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options,
    )

    yield driver

    driver.quit()

