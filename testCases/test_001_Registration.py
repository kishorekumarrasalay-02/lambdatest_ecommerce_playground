from pageObjects.RegistrationPage import RegistrationPage
from pageObjects.HomePage import HomePage
from utilities import randomString
from utilities.testDataStore import TestDataStore
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from datetime import datetime
import os

class Test_001_Reg:

    def test_account_reg_with_error_capture(self, setup):
        driver = setup
        wait = WebDriverWait(driver, 2)

        try:
            # STEP 1: Open site
            driver.get("https://ecommerce-playground.lambdatest.io/")

            # STEP 2: Accept cookies
            home = HomePage(driver)
            home.acceptCookies()

            # STEP 3: Go to Register page
            driver.get("https://ecommerce-playground.lambdatest.io/index.php?route=account/register")

            # STEP 4: Wait until First Name is visible
            wait.until(EC.visibility_of_element_located((By.NAME, "firstname")))

            reg = RegistrationPage(driver)

            # STEP 5: Generate random data
            email = randomString.random_string_geneartor() + "@gmail.com"
            password = "Test@123"

            TestDataStore.email = email
            TestDataStore.password = password

            # STEP 6: Fill form WITH INVALID EMAIL to cause real validation error
            reg.setFirstName("Kishore")
            reg.setLastName("Kumar")
            # reg.setEmail("invalid-email")  # ❌ intentionally wrong
            reg.setEmail(email)
            reg.setTelephone("9876543210")
            reg.setPassword(password)
            reg.setConfirmPassword(password)
            reg.subscribeNewsletter("no")
            reg.acceptPrivacyPolicy()
            reg.clickContinue()

            # STEP 7: Check if any error messages appear
            errors = driver.find_elements(By.CSS_SELECTOR, "div.text-danger")
            if errors:
                timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
                screenshot_path = f"screenshots/registration_error_{timestamp}.png"
                driver.save_screenshot(screenshot_path)
                print(f"Validation error captured. Screenshot saved at: {screenshot_path}")
                for e in errors:
                    print("Error message:", e.text)
                assert False, "Form validation failed. See screenshot."

            # STEP 8: Optional: Check success message if no errors
            msg = reg.getConfirmationMsg()
            assert "Your Account Has Been Created!" in msg

        except Exception as e:
            # Catch unexpected errors and take screenshot
            if not os.path.exists("screenshots"):
                os.makedirs("screenshots")
            timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
            screenshot_path = f"screenshots/registration_exception_{timestamp}.png"
            driver.save_screenshot(screenshot_path)
            print(f"Test failed: {str(e)}. Screenshot saved at {screenshot_path}")
            raise
