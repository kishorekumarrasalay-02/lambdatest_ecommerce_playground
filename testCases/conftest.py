import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from datetime import datetime
import os
import logging

# =======================
# Create necessary folders
# =======================
if not os.path.exists("logs"):
    os.makedirs("logs")

if not os.path.exists("reports"):
    os.makedirs("reports")

# =======================
# Logging Configuration
# =======================
log_file = f"logs/automation_{datetime.now().strftime('%d-%m-%Y_%H-%M-%S')}.log"

logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%d-%m-%Y %H:%M:%S"
)

def log_info(message):
    logging.info(message)
    print(f"[INFO] {message}")

def log_error(message):
    logging.error(message)
    print(f"[ERROR] {message}")

# =======================
# Browser Fixture
# =======================
@pytest.fixture()
def setup():
    options = Options()
    options.add_argument("--incognito")
    options.add_argument("--start-maximized")

    service = Service(r"C:\drivers\Chromedriver\chromedriver.exe")
    driver = webdriver.Chrome(service=service, options=options)

    log_info("Chrome browser launched successfully")
    yield driver
    driver.quit()
    log_info("Chrome browser closed")

# =======================
# Screenshot & Logging on Failure
# =======================
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.failed:
        driver = item.funcargs.get("setup")
        if driver:
            screenshot_name = f"reports/{item.name}_{datetime.now().strftime('%d-%m-%Y_%H-%M-%S')}.png"
            driver.save_screenshot(screenshot_name)
            log_error(f"Test failed: {item.name}, screenshot saved: {screenshot_name}")
        else:
            log_error(f"Test failed: {item.name}, no driver available")
    elif rep.passed:
        log_info(f"Test passed: {item.name}")

# =======================
# Add Metadata to HTML Report (pytest-html >= 4)
# =======================
def pytest_configure(config):
    # Add metadata
    if hasattr(config, "_metadata"):
        config._metadata["Project Name"] = "Lambdatest"
        config._metadata["Module Name"] = "Ecommerce Automation"
        config._metadata["Tester"] = "Kishore Kumar"

    # Automatically generate HTML report
    if not hasattr(config, "_html"):
        config.option.htmlpath = "reports/report.html"
        config.option.self_contained_html = True
    report_path = os.path.abspath("reports/report.html")
    print(f"\nHTML report generated at: {report_path}\n")


