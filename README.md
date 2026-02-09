# 🛒 LambdaTest E-Commerce Playground - Automated Testing Framework

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![Selenium](https://img.shields.io/badge/Selenium-WebDriver-green.svg)](https://www.selenium.dev/)
[![Pytest](https://img.shields.io/badge/Pytest-Framework-orange.svg)](https://pytest.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A **production-ready**, **scalable**, and **maintainable** Test Automation Framework built with **Python**, **Selenium WebDriver**, and **Pytest**. This framework demonstrates industry best practices in test automation by implementing the **Page Object Model (POM)** design pattern, **Data-Driven Testing (DDT)**, and comprehensive reporting mechanisms.

---

## 📋 Table of Contents

- [Project Overview](#-project-overview)
- [Key Features](#-key-features)
- [Technologies Used](#️-technologies-used)
- [Project Architecture](#-project-architecture)
- [Installation & Setup](#️-installation--setup)
- [Running Tests](#-running-tests)
- [Test Scenarios Covered](#-test-scenarios-covered)
- [Reporting & Logs](#-reporting--logs)
- [Project Structure](#-project-structure)
- [Best Practices](#-best-practices)
- [Contributing](#-contributing)
- [Author](#-author)
- [License](#-license)

---

## 🎯 Project Overview

This automation framework is designed to test the **LambdaTest E-Commerce Playground** web application. It validates critical end-to-end user journeys including user registration, login authentication, product search, cart management, and checkout processes.

**Project Goals:**
- Automate repetitive testing tasks to improve efficiency
- Ensure consistent quality across releases
- Enable early defect detection through comprehensive test coverage
- Provide detailed test execution insights through reports and logs

---

## ✨ Key Features

### 🏗️ **Robust Framework Architecture**
- **Page Object Model (POM)**: Clean separation of test logic from UI elements (locators) for enhanced maintainability and reusability
- **Hybrid Framework**: Combines keyword-driven, data-driven, and modular testing approaches
- **Scalable Design**: Easily extensible to accommodate new test cases and pages

### 📊 **Data-Driven Testing**
- Utilizes Pytest fixtures and parameterization for running tests with multiple datasets
- Supports Excel/JSON-based test data management
- Validates diverse scenarios improving overall test coverage

### 🔍 **Advanced Element Handling**
- Implements reliable XPath and CSS selectors
- Uses explicit waits to handle dynamic content and synchronization challenges
- Custom wrapper methods for robust element interactions

### 📝 **Comprehensive Reporting & Logging**
- **HTML Reports**: Rich, graphical test execution summaries via pytest-html
- **Allure Reports**: Interactive and detailed test results visualization (optional)
- **Detailed Logging**: Timestamped execution logs with step-by-step tracking
- **Automatic Screenshots**: Captures failure screenshots for faster debugging

### 🧪 **Flexible Test Execution**
- Run Smoke, Regression, and Functional test suites independently
- Execute specific test cases or complete test modules
- Parallel execution support for faster results (configurable)

### 🔧 **Version Control Integration**
- Complete Git/GitHub integration
- Follows industry-standard branching and commit strategies
- Collaborative development ready

---

## 🛠️ Technologies Used

| Technology | Purpose | Version |
|-----------|---------|---------|
| **Python** | Programming Language | 3.8+ |
| **Selenium WebDriver** | Browser Automation | 4.x |
| **Pytest** | Testing Framework | Latest |
| **pytest-html** | HTML Reporting | Latest |
| **Allure-Pytest** | Advanced Reporting | Latest (Optional) |
| **openpyxl** | Excel Data Handling | Latest |
| **Git & GitHub** | Version Control | - |

---

## 🏛️ Project Architecture

The framework follows the **Page Object Model (POM)** design pattern with a modular structure:

```
┌─────────────────┐
│   Test Cases    │ ◄── High-level test scenarios
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Page Objects   │ ◄── Page-specific locators & actions
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│   Utilities     │ ◄── Reusable functions & helpers
└─────────────────┘
```

**Benefits:**
- **Maintainability**: Changes in UI require updates only in Page Objects
- **Reusability**: Common functions centralized in utilities
- **Readability**: Test cases remain clean and business-focused

---

## ⚙️ Installation & Setup

### Prerequisites
- Python 3.8 or higher installed
- pip (Python package manager)
- Chrome/Firefox/Edge browser
- Git (for cloning repository)

### Step 1: Clone the Repository

```bash
git clone https://github.com/kishorekumarrasalay-02/lambdatest_ecommerce_playground.git
cd lambdatest_ecommerce_playground
```

### Step 2: Set Up Virtual Environment (Recommended)

**Windows:**
```bash
python -m venv .venv
.venv\Scripts\activate
```

**macOS/Linux:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Configure WebDriver

The framework uses Selenium WebDriver. Ensure the appropriate driver (ChromeDriver, GeckoDriver, etc.) is installed and available in your system PATH, or use WebDriver Manager for automatic driver management.

---

## 🚀 Running Tests

### Run All Tests
```bash
pytest
```

### Run Specific Test File
```bash
pytest testCases/test_001_Registration.py
pytest testCases/test_002_LoginPage.py
```

### Run Tests with HTML Report
```bash
pytest --html=reports/report.html --self-contained-html
```

### Run Tests with Allure Report
```bash
pytest --alluredir=reports/allure-results
allure serve reports/allure-results
```

### Run Tests by Markers (Smoke/Regression)
```bash
pytest -m smoke      # Run smoke tests only
pytest -m regression # Run regression tests only
```

### Run Tests with Verbose Output
```bash
pytest -v -s
```

### Run Tests in Parallel (requires pytest-xdist)
```bash
pytest -n 4  # Run with 4 parallel workers
```

---

## 🧪 Test Scenarios Covered

The framework currently automates the following critical e-commerce workflows:

| Test Scenario | Description | Status |
|--------------|-------------|--------|
| **User Registration** | Validates new user account creation with valid/invalid data | ✅ |
| **User Login** | Tests authentication with correct/incorrect credentials | ✅ |
| **Product Search** | Verifies search functionality and result accuracy | ✅ |
| **Add to Cart** | Ensures products are correctly added to shopping cart | ✅ |
| **Checkout Process** | End-to-end checkout flow validation | ✅ |
| **Product Filtering** | Tests category and price filtering options | 🚧 |
| **Wishlist Management** | Add/remove items from wishlist | 🚧 |

**Legend:** ✅ Implemented | 🚧 Planned | ❌ Not Planned

---

## 📊 Reporting & Logs

### HTML Reports
After test execution, open the HTML report for a graphical overview:

```bash
# Report location
reports/report.html
```

**Features:**
- Pass/Fail summary with percentages
- Individual test case results
- Execution time tracking
- Failure screenshots embedded

### Execution Logs
Detailed logs are generated in the `logs/` directory:

```bash
# Log location
logs/automation_YYYY-MM-DD.log
```

**Log Contents:**
- Timestamp for each action
- Step-by-step execution details
- Error messages and stack traces
- Debug information for troubleshooting

### Screenshots
Failure screenshots are automatically captured and saved:

```bash
# Screenshot location
screenshots/test_name_TIMESTAMP.png
```

---

## 📂 Project Structure

```
lambdatest_ecommerce_playground/
│
├── .idea/                      # IDE configuration files
├── configurations/             # Configuration files (URLs, test data)
│   ├── config.ini              # Application URLs and settings
│   └── common_data.py          # Common test data variables
│
├── logs/                       # Automated execution logs
│   └── automation_*.log        # Daily log files
│
├── pageObjects/                # Page Object Model classes
│   ├── HomePage.py             # Home page locators & actions
│   ├── LoginPage.py            # Login page locators & actions
│   ├── RegistrationPage.py    # Registration page locators & actions
│   ├── ProductPage.py          # Product page locators & actions
│   └── CheckoutPage.py         # Checkout page locators & actions
│
├── reports/                    # Test execution reports
│   ├── report.html             # Pytest HTML report
│   └── allure-results/         # Allure report data (if enabled)
│
├── screenshots/                # Failure screenshots
│   └── *.png                   # Auto-captured screenshots
│
├── testCases/                  # Test scripts
│   ├── conftest.py             # Pytest fixtures (setup/teardown)
│   ├── test_001_Registration.py
│   ├── test_002_LoginPage.py
│   ├── test_003_ProductSearch.py
│   ├── test_004_AddToCart.py
│   └── test_005_Checkout.py
│
├── testData/                   # Test data files
│   ├── test_data.xlsx          # Excel-based test data
│   └── test_data.json          # JSON-based test data
│
├── utilities/                  # Reusable utility modules
│   ├── customLogger.py         # Custom logging implementation
│   ├── readProperties.py       # Config file reader
│   ├── testDataStore.py        # Test data management
│   └── XLUtils.py              # Excel utility functions
│
├── .gitignore                  # Git ignore rules
├── LICENSE                     # MIT License
├── README.md                   # Project documentation (this file)
└── requirements.txt            # Python dependencies
```

---

## 💡 Best Practices Implemented

### 1. **Page Object Model (POM)**
- Encapsulates page-specific elements and actions
- Improves code reusability and reduces duplication
- Makes maintenance easier when UI changes

### 2. **Explicit Waits**
- Handles dynamic content loading effectively
- Reduces flaky tests caused by timing issues
- Improves test reliability

### 3. **Data-Driven Testing**
- Separates test data from test logic
- Enables testing with multiple data sets
- Easy to add new test scenarios

### 4. **Logging & Reporting**
- Comprehensive logging for debugging
- Visual HTML reports for stakeholders
- Automatic failure screenshot capture

### 5. **Version Control**
- Clean commit history
- Meaningful commit messages
- Branch-based development workflow

### 6. **Configuration Management**
- Centralized configuration files
- Easy environment switching
- Secure credential handling

---

## 🤝 Contributing

Contributions are welcome! Please follow these guidelines:

1. **Fork the repository**
2. **Create a feature branch** (`git checkout -b feature/AmazingFeature`)
3. **Commit your changes** (`git commit -m 'Add some AmazingFeature'`)
4. **Push to the branch** (`git push origin feature/AmazingFeature`)
5. **Open a Pull Request**

### Code Standards
- Follow PEP 8 Python style guide
- Write meaningful test case names
- Add comments for complex logic
- Update documentation for new features

---

## 👨‍💻 Author

**Kishore Kumar R**

- 📧 Email: [Contact via GitHub](https://github.com/kishorekumarrasalay-02)
- 📞 Phone: +91 9490946159
- 💼 LinkedIn: [Connect with me](https://www.linkedin.com/in/kishore-kumar-rasalay)
- 🐙 GitHub: [@kishorekumarrasalay-02](https://github.com/kishorekumarrasalay-02)

---

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

---

## 📞 Support

If you encounter any issues or have questions:

1. **Check existing issues** in the GitHub repository
2. **Create a new issue** with detailed description
3. **Contact the author** via email or LinkedIn

---

## 🔄 Changelog

### Version 1.0.0 (Current)
- ✅ Initial framework setup
- ✅ Page Object Model implementation
- ✅ Registration & Login test cases
- ✅ Product search & Add to cart functionality
- ✅ HTML reporting integration
- ✅ Logging mechanism
- ✅ Screenshot capture on failure

<div align="center">

**⭐ If you find this project useful, please consider giving it a star! ⭐**

</div>
