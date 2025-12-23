from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        # Login fields
        self.txt_email_id = (By.ID, "input-email")
        self.txt_password_id = (By.ID, "input-password")
        self.btn_login_xpath = (By.XPATH, "//input[@value='Login']")

        # My Account & Logout
        self.my_account_menu = (By.XPATH, "//span[text()='My Account']")
        self.logout_link = (By.XPATH, "//a[text()='Logout']")

    def setEmail(self, email):
        self.wait.until(EC.visibility_of_element_located(self.txt_email_id)).send_keys(email)

    def setPassword(self, password):
        self.wait.until(EC.visibility_of_element_located(self.txt_password_id)).send_keys(password)

    def clickLogin(self):
        self.wait.until(EC.element_to_be_clickable(self.btn_login_xpath)).click()

    def clickLogout(self):
        # Step 1: Open My Account menu
        self.wait.until(EC.element_to_be_clickable(self.my_account_menu)).click()
        # Step 2: Click Logout
        self.wait.until(EC.element_to_be_clickable(self.logout_link)).click()
