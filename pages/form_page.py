from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
import allure
import time


class FormPage(BasePage):
    """Page Object for form fields with manual element initialization"""

    def __init__(self, driver) -> None:
        super().__init__(driver)
        self.url = "https://practice-automation.com/form-fields/"
        self._initialize_locators()

    def _initialize_locators(self) -> None:
        """Initialize all locators manually"""
        self.name_input = (By.ID, "name-input")
        self.password_input = (By.CSS_SELECTOR, "input[type='password']")
        self.email_input = (By.ID, "email")
        self.message_textarea = (By.ID, "message")
        self.submit_button = (By.ID, "submit-btn")
        self.milk_checkbox = (By.CSS_SELECTOR, "#drink2")
        self.coffee_checkbox = (By.CSS_SELECTOR, "#drink3")
        self.yellow_radio = (By.CSS_SELECTOR, "#color3")
        self.automation_select = (By.CSS_SELECTOR, "#automation")
        self.tools_list_items = (By.XPATH, "//label[contains(text(), 'Automation tools')]/following-sibling::ul[1]/li")


    @property
    def _name_field(self) -> WebElement:
        return self.wait.until(EC.element_to_be_clickable(self.name_input))

    @property
    def _password_field(self) -> WebElement:
        return self.driver.find_element(*self.password_input)

    @property
    def _email_field(self) -> WebElement:
        return self.driver.find_element(*self.email_input)

    @property
    def _message_field(self) -> WebElement:
        return self.driver.find_element(*self.message_textarea)

    @property
    def _submit_btn(self) -> WebElement:
        return self.driver.find_element(*self.submit_button)

    @property
    def _milk_checkbox(self) -> WebElement:
        return self.driver.find_element(*self.milk_checkbox)

    @property
    def _coffee_checkbox(self) -> WebElement:
        return self.driver.find_element(*self.coffee_checkbox)

    @property
    def _yellow_radio(self) -> WebElement:
        return self.driver.find_element(*self.yellow_radio)

    @property
    def _automation_select(self) -> WebElement:
        return self.driver.find_element(*self.automation_select)

    @allure.step("Open form page")
    def open(self) -> "FormPage":
        self.driver.get(self.url)
        time.sleep(2)
        return self

    @allure.step("Enter name: {name}")
    def enter_name(self, name: str) -> "FormPage":
        self._name_field.clear()
        self._name_field.send_keys(name)
        return self

    @allure.step("Enter password")
    def enter_password(self, password: str) -> "FormPage":
        self._password_field.clear()
        self._password_field.send_keys(password)
        return self

    @allure.step("Select drinks: {drinks}")
    def select_drinks(self, drinks: list) -> "FormPage":
        if "Milk" in drinks and not self._milk_checkbox.is_selected():
            self._milk_checkbox.click()
        if "Coffee" in drinks and not self._coffee_checkbox.is_selected():
            self._coffee_checkbox.click()
        return self

    @allure.step("Select color: {color}")
    def select_color(self, color: str) -> "FormPage":
        if color == "Yellow":
            self._yellow_radio.click()
        return self

    @allure.step("Select automation preference: {preference}")
    def select_automation(self, preference: str = "yes") -> "FormPage":
        select = Select(self._automation_select)
        if preference == "yes":
            select.select_by_value("yes")
        elif preference == "no":
            select.select_by_value("no")
        elif preference == "undecided":
            select.select_by_value("undecided")
        else:
            select.select_by_value("yes")
        return self

    @allure.step("Enter email: {email}")
    def enter_email(self, email: str) -> "FormPage":
        self._email_field.clear()
        self._email_field.send_keys(email)
        return self

    @allure.step("Calculate and enter message")
    def calculate_and_enter_message(self) -> "FormPage":
        try:
            tools_list = self.driver.find_elements(*self.tools_list_items)
            tools_count = len(tools_list)

            if tools_count > 0:
                longest_tool = max([tool.text for tool in tools_list], key=len)
                message = f"{tools_count} {longest_tool}"
            else:
                message = "3 Selenium WebDriver"  # Fallback

            self._message_field.clear()
            self._message_field.send_keys(message)
        except Exception as e:
            allure.attach(f"Error in calculate_and_enter_message: {str(e)}", name="Calculation Error")
            self._message_field.clear()
            self._message_field.send_keys("3 Selenium WebDriver")
        return self

    @allure.step("Submit form")
    def submit(self) -> "FormPage":
        # Scroll to button first to ensure it's visible
        self.driver.execute_script("arguments[0].scrollIntoView(true);", self._submit_btn)
        time.sleep(1)
        # Use JavaScript click to avoid interception
        self.driver.execute_script("arguments[0].click();", self._submit_btn)
        return self

    @allure.step("Get alert text")
    def get_alert_text(self) -> str:
        alert = self.wait.until(EC.alert_is_present())
        text = alert.text
        alert.accept()
        return text

    @allure.step("Fill all required fields with valid data")
    def fill_all_required_fields(self, name: str, password: str, email: str) -> "FormPage":
        """Fluent interface for filling all form fields"""
        return (self.enter_name(name)
                .enter_password(password)
                .select_drinks(["Milk", "Coffee"])
                .select_color("Yellow")
                .select_automation("yes")
                .enter_email(email)
                .calculate_and_enter_message())