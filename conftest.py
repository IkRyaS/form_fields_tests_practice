import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import os


@pytest.fixture
def browser():
    """Fixture to initialize and cleanup browser instance"""
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])

    # Set up ChromeDriver
    chromedriver_path = os.path.join(os.path.dirname(__file__), 'other/chromedriver.exe')

    if os.path.exists(chromedriver_path):
        service = Service(chromedriver_path)
    else:
        service = Service(ChromeDriverManager().install())

    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Hook to take screenshot on test failure"""
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        try:
            if "browser" in item.funcargs:
                browser = item.funcargs["browser"]
                screenshot = browser.get_screenshot_as_png()
                allure.attach(
                    screenshot,
                    name="screenshot_on_failure",
                    attachment_type=allure.attachment_type.PNG
                )
        except Exception as e:
            print(f"Failed to capture screenshot: {e}")