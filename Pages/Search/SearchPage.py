from selenium.webdriver.common.by import By
from selenium import webdriver
import time

class SearchPage():
    def __init__(self,driver):
        self.driver = driver

    _lnkTxt="//*[@id='container']/div/div[3]/div[2]/div[1]/div[2]/div[2]/div/div/div/a/div[1]/div[1]/div/div/img"

    def clickOnLink(self):
        self.driver.find_element(By.XPATH,self._lnkTxt).click()