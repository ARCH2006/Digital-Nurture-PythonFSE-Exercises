from pages.dropdown_page import DropdownPage


def test_dropdown_selection(driver):
    page = DropdownPage(driver)

    page.navigate_to(
        "https://www.lambdatest.com/selenium-playground/select-dropdown-demo"
    )

    page.select_day("Monday")

    message = page.get_selected_message()
    assert "Monday" in message, f"Expected 'Monday' in message, got: '{message}'"
