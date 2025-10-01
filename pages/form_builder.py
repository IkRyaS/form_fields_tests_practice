import allure
from pages.form_page import FormPage


class FormBuilder:
    """Fluent Interface Builder for form filling scenarios"""

    def __init__(self, form_page: FormPage) -> None:
        self.form_page = form_page
        self._name = None
        self._password = None
        self._email = None
        self._drinks = []
        self._color = None
        self._automation_preference = "yes"
        self._calculate_message = True

    @allure.step("Set name: {name}")
    def with_name(self, name: str) -> "FormBuilder":
        self._name = name
        return self

    @allure.step("Set password")
    def with_password(self, password: str) -> "FormBuilder":
        self._password = password
        return self

    @allure.step("Set email: {email}")
    def with_email(self, email: str) -> "FormBuilder":
        self._email = email
        return self

    @allure.step("Add drinks: {drinks}")
    def with_drinks(self, drinks: list) -> "FormBuilder":
        self._drinks = drinks
        return self

    @allure.step("Set color: {color}")
    def with_color(self, color: str) -> "FormBuilder":
        self._color = color
        return self

    @allure.step("Set automation preference: {preference}")
    def with_automation_preference(self, preference: str) -> "FormBuilder":
        self._automation_preference = preference
        return self

    @allure.step("Disable message calculation")
    def without_message(self) -> "FormBuilder":
        self._calculate_message = False
        return self

    @allure.step("Build and fill form")
    def build(self) -> FormPage:
        """Execute the form filling with configured parameters"""

        if self._name:
            self.form_page.enter_name(self._name)
        if self._password:
            self.form_page.enter_password(self._password)
        if self._drinks:
            self.form_page.select_drinks(self._drinks)
        if self._color:
            self.form_page.select_color(self._color)
        if self._automation_preference:
            self.form_page.select_automation(self._automation_preference)
        if self._email:
            self.form_page.enter_email(self._email)
        if self._calculate_message:
            self.form_page.calculate_and_enter_message()
        return self.form_page