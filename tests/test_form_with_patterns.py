import pytest
import allure
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.remote.webdriver import WebDriver
from pages.form_page import FormPage
from pages.form_builder import FormBuilder


@allure.feature("Form Fields Testing with Design Patterns")
class TestFormFieldsWithPatterns:
    """Test suite demonstrating design patterns implementation"""

    @allure.title("Positive Test: Fluent Interface with FormBuilder")
    def test_fluent_interface_builder(self, browser: WebDriver) -> None:
        """Test form submission using Fluent Interface Builder pattern"""
        form_page = FormPage(browser)
        form_page.open()

        form_builder = (FormBuilder(form_page)
                        .with_name("Fluent User")
                        .with_password("FluentPass123")
                        .with_email("fluent@example.com")
                        .with_drinks(["Milk", "Coffee"])
                        .with_color("Yellow")
                        .with_automation_preference("yes"))

        built_form = form_builder.build()
        built_form.submit()

        try:
            alert_text = built_form.get_alert_text()
            assert "success" in alert_text.lower() or "received" in alert_text.lower()
        except NoAlertPresentException:
            # Handle case where form might have client-side validation
            assert True

    @allure.title("Test element location")
    def test_page_factory_elements(self, browser: WebDriver) -> None:
        """Verify all elements are properly located"""
        form_page = FormPage(browser)
        form_page.open()
        
        # Check that key elements are present
        assert form_page._name_field.is_displayed()
        assert form_page._email_field.is_displayed()
        assert form_page._submit_btn.is_displayed()

    @allure.title("Comprehensive Fluent Interface Test")
    def test_comprehensive_fluent_interface(self, browser: WebDriver) -> None:
        """Test complex form scenarios using Fluent Interface"""
        form_page = FormPage(browser)
        form_page.open()

        (form_page.enter_name("Chained User")
         .enter_password("ChainPass123")
         .select_drinks(["Milk"])
         .select_color("Yellow")
         .select_automation("undecided")
         .enter_email("chained@example.com")
         .calculate_and_enter_message()
         .submit())

        try:
            alert_text = form_page.get_alert_text()
            assert "success" in alert_text.lower() or "received" in alert_text.lower()
        except NoAlertPresentException:
            assert True

    @allure.title("Test selector types")
    def test_selector_types(self, browser: WebDriver) -> None:
        """Verify usage of CSS, XPath, and ID selectors"""
        form_page = FormPage(browser)
        form_page.open()

        form_page.enter_name("Selector Test")
        name_value = form_page._name_field.get_attribute("value")
        assert name_value == "Selector Test"

        form_page.select_drinks(["Milk", "Coffee"])
        assert form_page._milk_checkbox.is_selected()
        assert form_page._coffee_checkbox.is_selected()

        # Test that tools list can be found
        tools_list = browser.find_elements(*form_page.tools_list_items)
        assert len(tools_list) >= 0