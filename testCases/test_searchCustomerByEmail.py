import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from pageObjects.AddcustomerPage import AddCustomer
from utilities.customLogger import LogGen
from pageObjects.SearchCustomerPage import SearchCustomer

class Test_SearchCustomerByEmail_004:
    baseurl = ReadConfig.getApplicationURL() #"https://admin-demo.nopcommerce.com/"
    username = ReadConfig.getUseremail() #"admin@yourstore.com"
    password = ReadConfig.getPassword() #)"admin"

    logger = LogGen.loggen()


    @pytest.mark.regression
    def test_searchCustomerByEmail(self, setup):
        self.logger.info("*********SearchCustomerByEmail_004*********")
        self.driver = setup
        self.driver.get(self.baseurl)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPaswword(self.password)
        self.lp.clickLogin()
        self.logger.info("*********Login Successful*********")
        self.logger.info("*********Starting Search Customer By Email*********")

        self.addcust = AddCustomer(self.driver)
        self.addcust.clickOnCustomerMenu()
        self.addcust.clickOnCustomerMenuItem()

        self.logger.info("*********Searching Customer By Email ID*********")
        searchcust = SearchCustomer(self.driver)
        searchcust.setEmail("victoria_victoria@nopCommerce.com")
        searchcust.clickSearch()
        sleep(5)
        status = searchcust.searchCustomerByEmail("victoria_victoria@nopCommerce.com")
        assert True==status
        self.logger.info("*************TC_SearchCustomerByEmail_004 Finished****************")
        self.driver.close()

