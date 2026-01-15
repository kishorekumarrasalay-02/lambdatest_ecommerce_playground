# 🛒 Automation Testing Project Lambdatest E-Commerce Web Application

A robust, scalable, and production-ready Test Automation Framework built using **Python**, **Selenium WebDriver**, and **Pytest**. This project automates the [LambdaTest E-Commerce Playground](https://ecommerce-playground.lambdatest.io/) website to demonstrate modern testing practices.

![Python](https://img.shields.io/badge/Python-3.14-blue.svg)
![Selenium](https://img.shields.io/badge/Selenium-WebDriver-green.svg)
![Pytest](https://img.shields.io/badge/Framework-Pytest-yellow.svg)

---

## 🚀 Key Features

* **Page Object Model (POM):** Clearly separates test logic from UI elements (Locators) for better maintenance.
* **Data-Driven Testing:** Capable of running tests against multiple datasets.
* **Robust Utility Functions:** Custom wrapper methods in `utilities/` for handling clicks, explicit waits, and dynamic elements.
* **Smart Logging:** Generates detailed execution logs (timestamps, steps, pass/fail status) in the `logs/` directory.
* **Automatic Screenshots:** Captures screenshots automatically upon test failure for debugging.
* **Rich Reporting:** Generates HTML reports via `pytest-html` and supports Allure reporting.

---

## 🛠️ Tech Stack

* **Language:** Python
* **Automation Tool:** Selenium WebDriver
* **Testing Framework:** Pytest
* **Reporting:** Pytest-HTML / Allure-Pytest
* **Design Pattern:** Page Object Model (POM)

---

## 📂 Project Structure

```text
Lambdatest_ECommerce_Playground/
│
├── configurations/        # Configuration files (URLs, Common Data)
├── logs/                  # Automation execution logs
├── pageObjects/           # Page Classes (Locators & Actions)
│   ├── HomePage.py
│   ├── LoginPage.py
│   └── RegistrationPage.py
├── reports/               # Test Execution Reports (HTML)
├── screenshots/           # Failure screenshots
├── testCases/             # Actual Test Scripts
│   ├── test_001_Registration.py
│   ├── test_002_LoginPage.py
│   └── conftest.py        # Pytest fixtures (Setup/Teardown)
├── testData/              # Excel/JSON files for data-driven testing
├── utilities/             # Reusable components
│   ├── customLogger.py
│   ├── readProperties.py
│   └── testDataStore.py
└── requirements.txt       # Project dependencies

```

---

## ⚙️ How to Install & Run

### 1. Clone the Repository

```bash
git clone [https://github.com/YOUR_USERNAME/Lambdatest_ECommerce_Playground.git](https://github.com/YOUR_USERNAME/Lambdatest_ECommerce_Playground.git)
cd Lambdatest_ECommerce_Playground

```

### 2. Set up Virtual Environment (Optional but Recommended)

```bash
python -m venv .venv
# Activate on Windows:
.venv\Scripts\activate
# Activate on Mac/Linux:
source .venv/bin/activate

```

### 3. Install Dependencies

```bash
pip install -r requirements.txt

```

### 4. Run the Tests

To run all test cases:

```bash
pytest

```

To run a specific test case (e.g., Login):

```bash
pytest testCases/test_002_LoginPage.py

```

To run and generate an HTML report:

```bash
pytest --html=reports/report.html

```

---

## 📊 Reports & Logs

* **HTML Report:** After execution, open `reports/report.html` in any browser to see a graphical summary of passed/failed tests.
* **Logs:** Check the `logs/` folder for detailed step-by-step execution details useful for debugging.

---

## 👤 Author

**Kishore Kumar R**

* 📞Phone: +919490946159
*🔗[LinkedIn Profile](https://www.linkedin.com/in/kishorekumarrasalay/)
*💻 [Github Profile](https://github.com/kishorekumarrasalay-02)

---
