from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePage:

    btn_accept_cookies_xpath = "//button[normalize-space()='Accept All']"
    lnk_register_xpath = "//a[normalize-space()='Register']"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 2)

    def acceptCookies(self):
        try:
            self.wait.until(
                EC.element_to_be_clickable((By.XPATH, self.btn_accept_cookies_xpath))
            ).click()
        except:
            pass

    def clickRegister(self):
        self.wait.until(
            EC.element_to_be_clickable((By.XPATH, self.lnk_register_xpath))
        ).click()
