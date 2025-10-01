import pytest
import allure
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support.ui import Select
from selenium.webdriver.remote.webdriver import WebDriver
from pages.form_page import FormPage


@allure.feature("Form Fields Testing")
class TestFormFields:
    """Test suite for form fields functionality"""

    @allure.title("Positive test: Successful form submission")
    def test_successful_form_submission(self, browser: WebDriver) -> None:
        """Test complete form submission with valid data"""
        form_page = FormPage(browser)
        form_page.open()

        form_page.fill_all_required_fields(
            name="Test User",
            password="TestPassword123",
            email="test@example.com"
        )

        form_page.submit()
        alert_text = form_page.get_alert_text()
        assert "success" in alert_text.lower() or "received" in alert_text.lower()

    @allure.title("Negative test: Empty required fields")
    def test_empty_required_fields(self, browser: WebDriver) -> None:
        """Test form submission behavior when required fields are empty"""
        form_page = FormPage(browser)
        form_page.open()

        form_page.calculate_and_enter_message()
        form_page.submit()

        try:
            browser.implicitly_wait(3)
            alert = browser.switch_to.alert
            alert_text = alert.text
            alert.accept()
            assert "success" not in alert_text.lower()
        except NoAlertPresentException:
            assert True
        finally:
            browser.implicitly_wait(10)

    @allure.title("Test message calculation logic")
    def test_message_calculation(self, browser: WebDriver) -> None:
        """Test the automated message calculation functionality"""
        form_page = FormPage(browser)
        form_page.open()
        form_page.calculate_and_enter_message()

        message_text = form_page._message_field.get_attribute("value")
        assert message_text

        parts = message_text.split(" ", 1)
        assert len(parts) == 2
        assert parts[0].isdigit()
        assert int(parts[0]) > 0
        assert parts[1]

    @allure.title("Test individual field functionality")
    def test_individual_fields(self, browser: WebDriver) -> None:
        """Test individual form field interactions and validations"""
        form_page = FormPage(browser)
        form_page.open()

        form_page.enter_name("Individual Test")
        name_value = form_page._name_field.get_attribute("value")
        assert name_value == "Individual Test"

        form_page.enter_password("TestPass123")
        password_value = form_page._password_field.get_attribute("value")
        assert password_value == "TestPass123"

        form_page.enter_email("test@example.com")
        email_value = form_page._email_field.get_attribute("value")
        assert email_value == "test@example.com"

        form_page.select_drinks(["Milk", "Coffee"])
        assert form_page._milk_checkbox.is_selected()
        assert form_page._coffee_checkbox.is_selected()

        form_page.select_color("Yellow")
        assert form_page._yellow_radio.is_selected()

        form_page.select_automation("yes")
        select = Select(form_page._automation_select)
        selected_option = select.first_selected_option
        assert selected_option.get_attribute("value") == "yes"

    @allure.title("Negative test: Missing required fields")
    def test_missing_message_field(self, browser: WebDriver) -> None:
        """Test form submission behavior when message field is empty"""
        form_page = FormPage(browser)
        form_page.open()

        # Fill all fields except message
        form_page.enter_name("Test User")
        form_page.enter_password("TestPassword123")
        form_page.select_drinks(["Milk", "Coffee"])
        form_page.select_color("Yellow")
        form_page.select_automation("yes")
        form_page.enter_email("test@example.com")
        form_page.submit()

        try:
            browser.implicitly_wait(3)
            alert = browser.switch_to.alert
            alert_text = alert.text
            alert.accept()
            assert "message" in alert_text.lower() or "required" in alert_text.lower()
        except NoAlertPresentException:
            assert True
        finally:
            browser.implicitly_wait(10)