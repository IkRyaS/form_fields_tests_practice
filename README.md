# Form fields tests practice
form_fields_tests_practice
![Python](https://img.shields.io/badge/Python-3.10-blue.svg)
![Selenium](https://img.shields.io/badge/Selenium-4.15.0-green.svg)
![Pytest](https://img.shields.io/badge/Pytest-7.4.0-yellow.svg)
![Allure](https://img.shields.io/badge/Allure-2.13.2-orange.svg)

A comprehensive UI automation testing project for web forms using Python, Selenium WebDriver, and modern design patterns.

## Project Overview

This project automates testing of web forms on [Form Fields](https://practice-automation.com/form-fields/) page. It implements both positive and negative test scenarios using industry-standard automation practices and design patterns.

## Features

- **Form Automation** - Text fields, passwords, checkboxes, radio buttons, dropdowns
- **Positive & Negative Testing** - Valid and invalid data scenarios
- **Dynamic Calculations** - Automatic element counting and message generation
- **Detailed Reporting** - Allure Framework integration for comprehensive reports
- **Cross-browser Support** - Multi-browser compatibility via Selenium WebDriver

## Design Patterns

- **Page Object Model (POM)** - Page logic encapsulation
- **Fluent Interface** - Method chaining for better readability
- **Page Factory** - Automatic element initialization

## Technology Stack

- **Python 3.10** - Programming language
- **Selenium WebDriver 4.15.0** - Browser automation
- **Pytest 7.4.0** - Testing framework
- **Allure Framework 2.13.2** - Reporting system
- **WebDriver Manager** - Automatic driver management
- **Chrome Driver** - Chrome browser driver

## Project Structure
 
```
form_fields_tests_practice/
├── other/
│   └── chromedriver.exe
├── pages/
│   ├── __init__.py
│   ├── base_page.py
│   ├── form_page.py
│   └── form_builder.py
├── tests/
│   ├── __init__.py
│   ├── test_form.py
│   └── test_form_with_patterns.py
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md
```

## Installation & Setup
### Prerequisites
- Python 3.10 or higher
- Google Chrome browser
- Git

### Installation Steps
1. **Clone the repository:**
```bash
git clone https://github.com/IkRyaS/form_fields_tests_practice.git
cd form_fields_tests_practice
```

2. **Create virtual environment:**
```bash
python -m venv .venv

# Activate on Windows
.venv\Scripts\activate

# Activate on Linux/MacOS
source .venv/bin/activate
```

3. **Install dependencies:**
```bash
pip install -r requirements.txt
```

### Allure Installation on Windows
#### Method 1: Via Scoop (Recommended)
```bash
# Install Scoop if not present
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
irm get.scoop.sh | iex

# Install Allure
scoop install allure
```

#### Method 2: Via Chocolatey
```bash
# Install Chocolatey if not present
Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))

# Install Allure
choco install allure
```

#### Method 3: Manual Installation
1. **Download Allure:**
   - Go to https://github.com/allure-framework/allure2/releases
   - Download `allure-2.24.1.zip`

2. **Install:**
   - Extract to `C:\allure\`
   - Add `C:\allure\bin\` to PATH environment variable

3. **Verify installation:**
```bash
allure --version
```

## Running Tests
### Basic Test Execution
```bash
# Run all tests
pytest tests/ -v

# Run specific test file
pytest tests/test_form.py -v

# Run with detailed output
pytest tests/test_form.py -v -s
```

### Test with Allure Reports
```bash
# Generate test results
pytest tests/ --alluredir=./allure-results

# Serve Allure report
allure serve allure-results

# Generate static report
allure generate allure-results -o reports --clean
allure open reports
```

### Specific Test Scenarios
```bash
# Run positive test only
pytest tests/test_form.py::TestFormFields::test_successful_form_submission -v

# Run calculation test
pytest tests/test_form.py::TestFormFields::test_message_calculation -v

# Run design pattern tests
pytest tests/test_form_with_patterns.py -v
```

## 🎯 Test Results
- **Total Tests:** 9
- **Passed:** 9 (100%)
- **Execution Time:** ~1:44 minutes
- **Design Patterns Implemented:** Page Object Model, Fluent Interface, Page Factory
- **Reporting:** Allure Framework
  <img alt="Отчет" height="750" src="https://github.com/IkRyaS/form_fields_tests_practice/blob/main/other/result_allure.png?raw=true" width="700"/>

## Test Scenarios
### ✅ Positive Tests
- Complete form submission with valid data
- Successful alert message verification
- Form Builder pattern implementation
- Fluent interface method chaining

### ❌ Negative Tests
- Empty required fields validation
- Missing message field handling
- Form validation without calculation

### 🔧 Functional Tests
- Message calculation logic
- Individual field functionality
- Checkbox and radio button states
- Selector type verification (ID, CSS, XPath)

## Configuration
### Browser Configuration (conftest.py)
- Automatic ChromeDriver detection
- Browser window settings
- Timeouts and waits configuration
- Screenshot on failure

### Pytest Configuration (pytest.ini)
- Test paths and patterns
- Plugin configurations
- Reporting settings
- Marker definitions

## Design Pattern Implementation
### Page Object Model
```python
class FormPage(BasePage):
    def enter_name(self, name: str) -> "FormPage":
        self._name_field.clear()
        self._name_field.send_keys(name)
        return self
```

### Fluent Interface
```python
# Method chaining example
(form_page.enter_name("User")
         .enter_password("Pass123")
         .select_drinks(["Milk"])
         .submit())
```

### Page Factory
```python
class BasePage:
    def __init__(self, driver):
        self.driver = driver
        PageFactory.init_elements(driver, self)
```

### Form Builder Pattern
```python
form_builder = (FormBuilder(form_page)
               .with_name("User")
               .with_email("test@example.com")
               .build())
```

## Reporting
### Allure Reports Features
- Test list with status indicators
- Execution timing
- Screenshots on failures
- Detailed test steps
- Charts and metrics

### Report Generation
```bash
# Generate results
pytest --alluredir=allure-results

# Create HTML report
allure generate allure-results -o reports --clean

# Open report
allure open reports
```

## Development
### Adding New Tests
1. Create methods in `FormPage` for new functionality
2. Add test methods in `test_form.py`
3. Use Allure decorators for documentation
4. Follow type hints and code standards

### Code Standards
- PEP 8 compliance
- Type hints implementation
- Single-line docstrings
- Logical naming conventions

## Troubleshooting
### Common Issues
- AMD Video Processor errors don't affect test execution
- DEPRECATED_ENDPOINT warnings are ChromeDriver related
- Ensure Chrome browser is updated
- Verify internet connection for WebDriver Manager

### ChromeDriver Issues
If ChromeDriver fails to start:
1. Download ChromeDriver manually from https://chromedriver.chromium.org/
2. Place `chromedriver.exe` in project root
3. Ensure Chrome version matches ChromeDriver version

## License
This project is created for demonstrating test automation skills and knowledge of design patterns.

## Author
IkRyaS - [GitHub Profile](https://github.com/IkRyaS)
