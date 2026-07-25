"""
Checkbox Demo Page Object.
Targets: https://www.lambdatest.com/selenium-playground/checkbox-demo

The LambdaTest checkbox demo page has two sections:
  1. Single Checkbox Demo – a single checkbox with id="isAgeSelected"
  2. Multiple Checkbox Demo – four checkboxes labelled "Option 1" … "Option 4"

This page object uses the standard Bootstrap form-check-input CSS class and
falls back to a generic CSS selector if needed.
"""

from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException

from pages.base_page import BasePage


class CheckboxPage(BasePage):
    """
    Page Object for the LambdaTest Checkbox Demo page.
    """

    # ── Locators ──────────────────────────────────────────────────────────

    # Primary: using Bootstrap's stable CSS class
    CHECKBOXES = (By.CSS_SELECTOR, "input.form-check-input[type='checkbox']")

    # Fallback: generic checkbox locator (in case site updates class names)
    FALLBACK_CHECKBOXES = (By.CSS_SELECTOR, "input[type='checkbox']")

    # Single checkbox – it has a stable id
    SINGLE_CHECKBOX = (By.ID, "isAgeSelected")

    # Text element that shows after single checkbox is clicked
    SINGLE_CHECKBOX_TEXT = (By.ID, "txtAge")

    # ── Page Navigation ───────────────────────────────────────────────────

    def navigate(self):
        """Navigate to the Checkbox Demo page."""
        self.navigate_to(
            "https://www.lambdatest.com/selenium-playground/checkbox-demo"
        )

    # ── Visible Checkbox Helpers ──────────────────────────────────────────

    def _get_visible_checkboxes(self):
        """
        Collect only VISIBLE, enabled checkboxes.
        Uses the primary locator first; falls back to the generic one.
        Returns a list of WebElements.
        """

        # Try primary locator
        for locator in (self.CHECKBOXES, self.FALLBACK_CHECKBOXES):
            try:
                elements = self.wait_for_elements(locator, timeout=5)
                # Filter to only visible, enabled elements
                visible = [el for el in elements if el.is_displayed() and el.is_enabled()]
                if visible:
                    return visible
            except (TimeoutException, StaleElementReferenceException):
                continue

        # Last resort: use find_elements directly with a short implicit-style check
        elements = self.driver.find_elements(*self.FALLBACK_CHECKBOXES)
        visible = [el for el in elements if el.is_displayed() and el.is_enabled()]
        return visible

    def get_checkbox(self, index):
        """
        Return the (index)th visible, enabled checkbox.
        Raises IndexError if fewer checkboxes are available.
        """
        checkboxes = self._get_visible_checkboxes()
        if index >= len(checkboxes):
            raise IndexError(
                f"Checkbox index {index} is out of range. "
                f"Only {len(checkboxes)} visible checkbox(es) found."
            )
        return checkboxes[index]

    # ── Single Checkbox ───────────────────────────────────────────────────

    def click_single_checkbox(self):
        """Click the single checkbox using its stable ID."""
        self.click_element(self.SINGLE_CHECKBOX)

    def is_single_checkbox_selected(self):
        """
        Check whether the single checkbox is selected.
        Returns True if selected, False otherwise.
        """
        element = self.wait_for_element(self.SINGLE_CHECKBOX)
        return element.is_selected()

    def get_single_checkbox_message(self):
        """
        Return the text displayed after clicking the single checkbox.
        (Hidden if the checkbox is not checked.)
        """
        try:
            return self.get_text(self.SINGLE_CHECKBOX_TEXT)
        except TimeoutException:
            return ""

    # ── Multiple Checkboxes ──────────────────────────────────────────────

    def check_option(self, index):
        """
        Click the (index)th visible checkbox to check it.
        Does nothing if it is already checked.
        """
        checkbox = self.get_checkbox(index)
        if not checkbox.is_selected():
            self.driver.execute_script("arguments[0].scrollIntoView(true);", checkbox)
            try:
                checkbox.click()
            except Exception:
                # Fall back to JS click if intercepted
                self.driver.execute_script("arguments[0].click();", checkbox)

    def uncheck_option(self, index):
        """
        Click the (index)th visible checkbox to uncheck it.
        Does nothing if it is already unchecked.
        """
        checkbox = self.get_checkbox(index)
        if checkbox.is_selected():
            self.driver.execute_script("arguments[0].scrollIntoView(true);", checkbox)
            try:
                checkbox.click()
            except Exception:
                # Fall back to JS click if intercepted
                self.driver.execute_script("arguments[0].click();", checkbox)

    def is_option_checked(self, index):
        """
        Check whether the (index)th visible checkbox is selected.
        Returns True if selected, False otherwise.
        """
        return self.get_checkbox(index).is_selected()

