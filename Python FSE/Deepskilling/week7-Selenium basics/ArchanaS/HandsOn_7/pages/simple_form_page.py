"""
Simple Form Demo Page Object.
Targets: https://www.lambdatest.com/selenium-playground/simple-form-demo
"""

from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class SimpleFormPage(BasePage):
    """
    Page Object for the LambdaTest Simple Form Demo page.
    """

    # ── Locators ──────────────────────────────────────────────────────────

    MESSAGE_INPUT = (By.ID, "user-message")
    SHOW_MESSAGE_BUTTON = (By.XPATH, "//button[contains(text(),'Get Checked Value') or contains(text(),'Show Message')]")
    DISPLAYED_MESSAGE = (By.ID, "message")

    # ── Page Navigation ───────────────────────────────────────────────────

    def navigate(self):
        """Navigate to the Simple Form Demo page."""
        self.navigate_to(
            "https://www.lambdatest.com/selenium-playground/simple-form-demo"
        )

    # ── Actions ───────────────────────────────────────────────────────────

    def enter_message(self, text):
        """
        Type the given text into the message input field.

        Args:
            text: The text to type (e.g., "Hello Selenium")
        """
        self.type_text(self.MESSAGE_INPUT, text)

    def click_submit(self):
        """Click the 'Show Message' / 'Get Checked Value' button."""
        self.click_element(self.SHOW_MESSAGE_BUTTON)

    def get_displayed_message(self):
        """
        Return the visible text of the message display area.

        Returns:
            str: The message text displayed after clicking submit.
        """
        return self.get_text(self.DISPLAYED_MESSAGE)

    # ── Composite Flows ───────────────────────────────────────────────────

    def submit_message(self, text):
        """
        Complete flow: enter message, click submit, and return the result.

        Args:
            text: The message to enter and submit.

        Returns:
            str: The displayed message text.
        """
        self.enter_message(text)
        self.click_submit()
        return self.get_displayed_message()

