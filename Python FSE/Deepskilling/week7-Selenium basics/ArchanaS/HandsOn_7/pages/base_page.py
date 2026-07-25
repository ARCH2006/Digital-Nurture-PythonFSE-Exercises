"""
Base Page class using Selenium 4 and Page Object Model.
Provides core, reusable interaction methods with explicit waits.
"""

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException


class BasePage:
    """
    Parent class for all page objects.
    Every page inherits from this class.
    """

    def __init__(self, driver):
        self.driver = driver
        self.default_wait = 15

    def _wait(self, timeout=None):
        """Return a WebDriverWait instance with the given or default timeout."""
        return WebDriverWait(self.driver, timeout or self.default_wait)

    def navigate_to(self, url):
        """Navigate to the given URL and wait for the page to load."""
        self.driver.get(url)
        self._wait_for_page_ready()

    def _wait_for_page_ready(self, timeout=15):
        """Wait until document.readyState is 'complete'."""
        WebDriverWait(self.driver, timeout).until(
            lambda d: d.execute_script("return document.readyState") == "complete"
        )

    def get_title(self):
        """Return the current page title."""
        return self.driver.title

    def get_current_url(self):
        """Return the current page URL."""
        return self.driver.current_url

    def wait_for_element(self, locator, timeout=None):
        """
        Wait until a single element is visible in the DOM and return it.
        Raises TimeoutException if the element does not become visible.
        """
        wait = self._wait(timeout)
        return wait.until(EC.visibility_of_element_located(locator))

    def wait_for_elements(self, locator, timeout=None):
        """
        Wait until at least one element matching the locator is visible.
        Returns a list of visible elements.
        Raises TimeoutException if no elements become visible.
        """
        wait = self._wait(timeout)
        return wait.until(EC.visibility_of_all_elements_located(locator))

    def wait_for_element_to_be_clickable(self, locator, timeout=None):
        """
        Wait until an element is both visible and enabled for clicking.
        Returns the element.
        """
        wait = self._wait(timeout)
        return wait.until(EC.element_to_be_clickable(locator))

    def click_element(self, locator, timeout=None):
        """
        Wait for element to be clickable and click it.
        Handles StaleElementReferenceException by retrying once.
        """
        try:
            element = self.wait_for_element_to_be_clickable(locator, timeout)
            element.click()
        except StaleElementReferenceException:
            element = self.wait_for_element_to_be_clickable(locator, timeout)
            element.click()

    def type_text(self, locator, text, timeout=None):
        """
        Wait for element, clear it, and type text into it.
        """
        element = self.wait_for_element(locator, timeout)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator, timeout=None):
        """
        Wait for element to be visible and return its visible text.
        """
        element = self.wait_for_element(locator, timeout)
        return element.text

    def is_element_displayed(self, locator, timeout=5):
        """
        Quickly check if an element is displayed.
        Returns True/False without throwing TimeoutException.
        """
        try:
            return self.wait_for_element(locator, timeout).is_displayed()
        except (TimeoutException, StaleElementReferenceException):
            return False

