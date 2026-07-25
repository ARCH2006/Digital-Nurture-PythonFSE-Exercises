from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class InputFormPage(BasePage):

    NAME = (By.NAME, "name")
    EMAIL = (By.NAME, "email")
    PHONE = (By.NAME, "phone")
    ADDRESS = (By.NAME, "address")

    SUBMIT = (By.CSS_SELECTOR, "button[type='submit']")

    SUCCESS_MESSAGE = (
        By.CSS_SELECTOR,
        ".success-msg"
    )

    def fill_form(self, name, email, phone, address):

        self.type_text(self.NAME, name)
        self.type_text(self.EMAIL, email)
        self.type_text(self.PHONE, phone)
        self.type_text(self.ADDRESS, address)

    def submit_form(self):
        self.click_element(self.SUBMIT)

    def get_success_message(self):
        return self.wait_for_element(
            self.SUCCESS_MESSAGE
        ).text