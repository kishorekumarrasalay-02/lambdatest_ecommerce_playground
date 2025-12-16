Lambdatest_ECommerce_Playground
---
End-to-end web test automation framework** for the LambdaTest E-Commerce Playground using Python, Selenium WebDriver, and Pytest. Implements **POM, logging, screenshots, and HTML reports** for reliable and maintainable testing.


## 🧰 Built With / Key Technologies

* Python
* Selenium WebDriver
* Pytest
* Pip & Virtual Environment (`requirements.txt`)
* Page Object Model (POM) design pattern
* Data-driven testing
* Explicit waits for reliable UI synchronization
* Custom logging framework
* Automatic screenshot capture on test failures
* Pytest HTML reporting with logs and screenshots


## 🧱 Framework Design

* **Page Object Model (POM)** to separate UI logic from test logic
* **Reusable utility and wrapper methods** for common browser actions
* **Centralized configuration** using `config.ini`
* **Custom logger** for step-level logging and error tracking
* **Pytest fixtures (`conftest.py`)** for setup and teardown
* **Failure handling** with screenshots and detailed reports

---

## 📁 Project Structure

```
lambdatest_ecommerce_playground/
│
├── configurations/            # Environment & application configurations
│   └── config.ini
├── logs/                      # Execution logs
├── pageObjects/               # Page Object classes
│   ├── __init__.py
│   ├── HomePage.py
│   ├── LoginPage.py
│   └── RegistrationPage.py
├── reports/                   # Pytest HTML reports
│   ├── assets/
│   └── *.html
├── screenshots/               # Failure screenshots
├── testCases/                 # Test scripts
│   ├── __init__.py
│   ├── conftest.py
│   ├── test_001_Registration.py
│   └── test_002_LoginPage.py
├── testData/                  # External test data
├── utilities/                 # Reusable utilities
│   ├── __init__.py
│   ├── customLogger.py
│   ├── randomString.py
│   └── readProperties.py
├── requirements.txt           # Project dependencies
└── README.md                  # Project documentation
```

---

## ▶️ Step 1: How to Run Test Cases

1. **Clone the repository**

```bash
git clone https://github.com/<your-github-username>/lambdatest_ecommerce_playground.git
cd lambdatest_ecommerce_playground
```

2. **Create virtual environment**

```bash
python -m venv .venv
```

3. **Activate virtual environment**

* **Windows:**

```bash
.venv\Scripts\activate
```

* **Mac/Linux:**

```bash
source .venv/bin/activate
```

4. **Install dependencies**

```bash
pip install -r requirements.txt
```

5. **Run test cases**

```bash
pytest -v -s
```

---

## ⚙️ Step 2: Driver Configuration

### WebDriver Configuration

This framework supports **both local WebDriver and automatic driver management**.

**Local WebDriver**

* Download the browser driver (Chrome/Edge)
* Place it in a local folder
* Update the driver path in the base setup

**Automatic WebDriver (Recommended)**

* Uses `webdriver-manager`
* Automatically downloads the compatible driver version
* No manual driver setup required

**Driver behavior can be controlled via `config.ini`:**

```ini
driver_type = auto   # auto|local
```

---

## STEP 3: Reports & Screenshots

* HTML Reports → `reports/` directory
* Execution logs → `logs/` directory
* Screenshots on test failures → `screenshots/` directory

---

### 🌐 Application Under Test

**LambdaTest E-Commerce Playground:** [https://ecommerce-playground.lambdatest.io/](https://ecommerce-playground.lambdatest.io/)



