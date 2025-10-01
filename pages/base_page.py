from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class BasePage:
    """Base page class"""

    def __init__(self, driver) -> None:
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)