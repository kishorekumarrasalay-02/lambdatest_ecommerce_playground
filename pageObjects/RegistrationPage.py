from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class RegistrationPage:

    # ===== Locators =====
    txt_firstname_locator = (By.NAME, "firstname")
    txt_lastname_locator = (By.NAME, "lastname")
    txt_email_locator = (By.NAME, "email")
    txt_telephone_locator = (By.NAME, "telephone")
    txt_password_locator = (By.NAME, "password")
    txt_confirm_password_locator = (By.NAME, "confirm")
    radio_newsletter_yes_locator = (By.CSS_SELECTOR, "input#input-newsletter-yes + label")
    radio_newsletter_no_locator = (By.CSS_SELECTOR, "input#input-newsletter-no + label")
    chk_privacy_policy_locator = (By.CSS_SELECTOR, "input#input-agree + label")
    btn_continue_locator = (By.CSS_SELECTOR, "input[value='Continue']")
    msg_confirmation_locator = (By.TAG_NAME, "h1")

    # ===== Constructor =====
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    # ===== Actions =====
    def setFirstName(self, fname):
        element = self.wait.until(EC.presence_of_element_located(self.txt_firstname_locator))
        element.clear()
        element.send_keys(fname)

    def setLastName(self, lname):
        element = self.wait.until(EC.presence_of_element_located(self.txt_lastname_locator))
        element.clear()
        element.send_keys(lname)

    def setEmail(self, email):
        element = self.wait.until(EC.presence_of_element_located(self.txt_email_locator))
        element.clear()
        element.send_keys(email)

    def setTelephone(self, phone):
        element = self.wait.until(EC.presence_of_element_located(self.txt_telephone_locator))
        element.clear()
        element.send_keys(phone)

    def setPassword(self, pwd):
        element = self.wait.until(EC.presence_of_element_located(self.txt_password_locator))
        element.clear()
        element.send_keys(pwd)

    def setConfirmPassword(self, cpwd):
        element = self.wait.until(EC.presence_of_element_located(self.txt_confirm_password_locator))
        element.clear()
        element.send_keys(cpwd)

    def subscribeNewsletter(self, choice):
        if choice.lower() == "yes":
            self.wait.until(EC.element_to_be_clickable(self.radio_newsletter_yes_locator)).click()
        else:
            self.wait.until(EC.element_to_be_clickable(self.radio_newsletter_no_locator)).click()

    def acceptPrivacyPolicy(self):
        self.wait.until(EC.element_to_be_clickable(self.chk_privacy_policy_locator)).click()

    def clickContinue(self):
        self.wait.until(EC.element_to_be_clickable(self.btn_continue_locator)).click()

    def getConfirmationMsg(self):
        wait = WebDriverWait(self.driver, 15)
        confirmation = wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "div#content h1"))
        )
        return confirmation.text





