"""
Dropdown Demo Page Object.
Targets: https://www.lambdatest.com/selenium-playground/select-dropdown-demo
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException

from pages.base_page import BasePage


class DropdownPage(BasePage):
    """
    Page Object for the LambdaTest Select Dropdown List Demo page.
    """

    # ── Locators ──────────────────────────────────────────────────────────

    DAY_DROPDOWN = (By.ID, "select-demo")
    SELECTED_DAY_TEXT = (By.XPATH, "//p[contains(text(),'You have selected')]")

    # ── Page Navigation ───────────────────────────────────────────────────

    def navigate(self):
        """Navigate to the Select Dropdown Demo page."""
        self.navigate_to(
            "https://www.lambdatest.com/selenium-playground/select-dropdown-demo"
        )

    # ── Actions ───────────────────────────────────────────────────────────

    def select_day(self, day_name):
        """
        Select a day from the dropdown using its visible text.

        Args:
            day_name: The visible text of the day to select (e.g., "Monday").
        """
        dropdown_element = self.wait_for_element(self.DAY_DROPDOWN)
        Select(dropdown_element).select_by_visible_text(day_name)

    def get_selected_day_text(self):
        """
        Return the visible text of the currently selected option.

        Returns:
            str: The selected option's visible text (e.g., "Monday").
        """
        dropdown_element = self.wait_for_element(self.DAY_DROPDOWN)
        select = Select(dropdown_element)
        return select.first_selected_option.text

    def get_selected_message(self):
        """
        Return the confirmation message displayed after selecting a day.

        Returns:
            str: The message text, or an empty string if not visible.
        """
        try:
            return self.get_text(self.SELECTED_DAY_TEXT)
        except TimeoutException:
            return ""

