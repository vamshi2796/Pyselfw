from selenium import webdriver
from Pages.Login.LoginPage import LoginPage
import unittest
import pytest

@pytest.mark.usefixtures("oneTimeSetUp")
class LoginTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)

    @pytest.mark.run(order=2)
    def test_validLogin(self):
       self.lp.login("test@email.com", "abcabc")
       result = self.lp.verifySignUpPage()
       print("Value ----" + result)
       assert result == "Sign up"
       #result = self.lp.verifyLoginSuccessful()


    @pytest.mark.run(order=1)
    def test_invalidLogin(self):
        self.lp.login("test@email.com", "abcabcabc")
        result = self.lp.clickOnExistingCustomer()
       # result = self.lp.verifyLoginFailed()
        assert result == True