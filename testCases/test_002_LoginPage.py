from pageObjects.LoginPage import LoginPage
from utilities.testDataStore import TestDataStore

class Test_002_Login:

    def test_login(self, setup):
        driver = setup

        email = TestDataStore.email
        password = TestDataStore.password

        assert email is not None, "Email not found from registration test"

        driver.get("https://ecommerce-playground.lambdatest.io/index.php?route=account/login")

        login = LoginPage(driver)
        login.setEmail(email)
        login.setPassword(password)
        login.clickLogin()

        assert "My Account" in driver.page_source


