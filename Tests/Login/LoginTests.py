from selenium import webdriver
from Pages.Login.LoginPage import LoginPage
from Pages.Home.HomePage import HomePage
import unittest
import time

class LoginTests(unittest.TestCase):

    #def __init__(self):
     #   baseURL = "https://www.flipkart.com/"
      #  global driver
       # driver = webdriver.Chrome( "C:\\Users\\Hp\\PycharmProjects\\pySelenium\\lib\\chromedriver.exe" )
       # driver.maximize_window()
       # driver.implicitly_wait(3)
       # driver.get(baseURL)

    def test_validSearch(self):
       baseURL = "https://www.flipkart.com/"
       global driver
       driver = webdriver.Chrome( "C:\\Users\\Hp\\PycharmProjects\\pySelenium\\lib\\chromedriver.exe" )
       driver.maximize_window()
       driver.implicitly_wait(3)
       driver.get(baseURL)

   # def test_validateLogin(self):
    #    lp=LoginPage(driver)
    #    lp.enterUsername("sampleuser@gmail.com")
    #    lp.enterPassword("samplepassword")
    #    lp.clickOnLoginBtn()
       # lp.login("abc.g","huho")

    def test_validateLogin(self):
        loginPage=LoginPage(driver)
        time.sleep(1)
        global homePage
        homePage = loginPage.clickOnCloseBtn()
        time.sleep(1)
       # homePage.enterSearchText("Samsung TV")
       # time.sleep(3)

    def test_validateSearch(self):
        homePage.enterSearchText("iPhone")
        global searchPage
        searchPage = homePage.clickOnSearchBtn()
        searchPage.clickOnLink()
        time.sleep(1)



