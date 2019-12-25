from selenium.webdriver.common.by import By
from selenium import webdriver
import time
from Pages.Home.HomePage import HomePage

class LoginPage():
    def __init__(self,driver):
        self.driver = driver

        #Locators
    _txtEmail="/html/body/div[2]/div/div/div/div/div[2]/div/form/div[1]/input"
    _txtPassword = "/html/body/div[2]/div/div/div/div/div[2]/div/form/div[2]/input"
    _btnLogin = "/html/body/div[2]/div/div/div/div/div[2]/div/form/div[3]/button"
    _btnClose = "/html/body/div[2]/div/div/button"
    _btnExistingUser = "/html/body/div[2]/div/div/div/div/div[2]/div/form/div[2]/a"
    _txtSignUp = "/html/body/div[2]/div/div/div/div/div[1]/span/span"

    def getUsername(self,userName):
        return self.driver.find_element(By.XPATH,self._txtEmail).send_keys(userName)

    def getPassword(self,password):
        return self.driver.find_element(By.XPATH,self._txtPassword).send_keys(password)

    def enterUsername(self, userName):
        return self.driver.find_element( By.XPATH, self._txtEmail ).send_keys( userName )

    def enterPassword(self, password):
        return self.driver.find_element( By.XPATH, self._txtPassword ).send_keys( password )

    def clickOnCloseBtn(self):
        self.driver.find_element(By.XPATH,self._btnClose).click()
        return HomePage(self.driver)

    def clickOnLoginBtn(self):
        self.driver.find_element(By.XPATH,self._btnLogin).click()
        time.sleep(10)

   # def clickLogin(self,email):
    #    self.getUsername().send_keys(email)

    def login(self, userName, password):
       # usernameTxt= self.driver.find_element
        print(userName + password)
        self.getUsername(userName)
        self.getPassword(password)
        self.clickOnLoginBtn()
        time.sleep(3)
        return True

    def clickOnExistingCustomer(self):
        self.driver.find_element(By.XPATH,self._btnExistingUser).click()
        time.sleep(2)
        return True

    def verifySignUpPage(self):
        return self.driver.find_element(By.XPATH,self._txtSignUp).text
