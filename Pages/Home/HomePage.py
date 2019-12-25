from selenium.webdriver.common.by import By
from selenium import webdriver
import time
from Pages.Search.SearchPage import SearchPage


class HomePage():
    def __init__(self,driver):
        self.driver = driver

    _txtSearch = "//*[@id='container']/div/div[1]/div[1]/div[2]/div[2]/form/div/div/input"
    _btnSearch = "//*[@id='container']/div/div[1]/div[1]/div[2]/div[2]/form/div/button"

    def enterSearchText(self, searchText):
        self.driver.find_element(By.XPATH,self._txtSearch).send_keys(searchText)

    def clickOnSearchBtn(self):
        self.driver.find_element(By.XPATH,self._btnSearch).click()
        return SearchPage(self.driver)