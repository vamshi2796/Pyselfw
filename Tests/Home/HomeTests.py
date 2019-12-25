from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest


class HomeTests(unittest.TestCase):

    def test_validSearch(self):
        baseURL = "https://www.flipkart.com/"
        driver = webdriver.Chrome( "C:\\Users\\Hp\\PycharmProjects\\pySelenium\\lib\\chromedriver.exe" )
        driver.maximize_window()
        driver.implicitly_wait( 3 )
        driver.get( baseURL )

        loginLink = driver.find_element( By.LINK_TEXT, "Login" )
        loginLink.click()

        emailField = driver.find_element( By.ID, "user_email" )
        emailField.send_keys( "test@email.com" )

        passwordField = driver.find_element( By.ID, "user_password" )
        passwordField.send_keys( "abcabc" )

        loginButton = driver.find_element( By.NAME, "commit" )
        loginButton.click()

        userIcon = driver.find_element( By.XPATH, ".//*[@id='navbar']//span[text()='User Settings']" )
        if userIcon is not None:
            print( "Login Successful" )
        else:
            print( "Login Failed" )

            driver.find_element_by_xpath( "/html/body/div[2]/div/div/button" ).click()
            time.sleep( 2 )
            driver.find_element_by_xpath( "//*[@id='container']/div/div[2]/div/ul/li[1]/span" ).click()
            time.sleep( 1 )
            driver.find_element_by_xpath(
                "//*[@id='container']/div/div[2]/div/ul/li[1]/ul/li/ul/li[1]/ul/li[3]/a" ).click()
            time.sleep( 3 )
            print( "Checkbox value --> " + str( driver.find_element_by_xpath(
                "//*[@id='container']/div/div[3]/div[2]/div/div[1]/div/div[1]/div/section[3]/div[1]/label/input" ).is_selected() ) )
            driver.find_element_by_xpath(
                "//*[@id='container']/div/div[3]/div[2]/div/div[1]/div/div[1]/div/section[3]/div[1]/label/div[1]" ).click()
            time.sleep( 2 )
            print( "Checkbox value --> " + str( driver.find_element_by_xpath(
                "//*[@id='container']/div/div[3]/div[2]/div/div[1]/div/div[1]/div/section[3]/div[1]/label/input" ).is_selected() ) )
            print( "Checkbox attribute--> " + str( driver.find_element_by_xpath(
                "//*[@id='container']/div/div[3]/div[2]/div/div[1]/div/div[1]/div/section[3]/div[1]/label/input" ).get_attribute(
                "type" ) ) )

            # select = driver.find_element_by_id("toll")
            # element = Select(select)
            # element.select_by_value("5")
            # element.select_by_index(5)
            # element.select_by_visible_text("For calls when in Australia: 1800 247 463")
            # time.sleep( 5 )

            # sel = driver.find_element_by_xpath("//*[@id='root']/div/div[2]/div/div[1]/ul/li[1]").is_selected()
            # print("State of One way --> "+ str(sel))
            # driver.close()
            driver.quit()
            # time.sleep( 2 )

            # driver.find_element_by_xpath("/html/body/div[2]/div/div/button").click()
            # driver.delete_all_cookies()
            # print("")
            # textValue = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div[1]/div[5]/div[1]/div[3]/div").text
            # print("Text = "+ textValue)


cc = HomeTests()
cc.test_validSearch()
