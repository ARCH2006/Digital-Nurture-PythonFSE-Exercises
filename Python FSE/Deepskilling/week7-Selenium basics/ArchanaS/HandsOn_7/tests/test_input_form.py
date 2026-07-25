from pages.input_form_page import InputFormPage


def test_input_form_submit(driver):

    page = InputFormPage(driver)

    page.navigate_to(
        "https://www.lambdatest.com/selenium-playground/input-form-demo"
    )

    page.fill_form(
        "Rohith",
        "rohith@example.com",
        "9876543210",
        "Chennai"
    )

    page.submit_form()

    assert "success" in page.get_success_message().lower()