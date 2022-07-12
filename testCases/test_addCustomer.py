import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from pageObjects.AddcustomerPage import AddCustomer
from utilities.customLogger import LogGen
import string
import random

class Test_003_Addcustomer:
    baseurl = ReadConfig.getApplicationURL() #"https://admin-demo.nopcommerce.com/"
    username = ReadConfig.getUseremail() #"admin@yourstore.com"
    password = ReadConfig.getPassword() #)"admin"

    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_addCustomer(self, setup):
        self.logger.info("*********TEST_003_AddCustomer*********")
        self.driver = setup
        self.driver.get(self.baseurl)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPaswword(self.password)
        self.lp.clickLogin()
        self.logger.info("*********Login Successful*********")
        self.logger.info("*********Starting Add Customer Test*********")

        self.addcust=AddCustomer(self.driver)
        self.addcust.clickOnCustomerMenu()
        self.addcust.clickOnCustomerMenuItem()

        self.addcust.clickOnAddnew()
        self.logger.info("*********Providing Customer Info*********")

        self.email = random_generator() + "@gmail.com"
        self.addcust.setEmail(self.email)
        self.addcust.setPassword("test123")
        self.addcust.setCustomerRoles("Guests")
        self.addcust.setManagerOfVendor("Vendor 2")
        self.addcust.setGender("Female")
        self.addcust.setFirstName("Madhura")
        self.addcust.setLastName("Harshavardhan")
        self.addcust.setDob("06/25/1990")
        self.addcust.setCompanyName("BusyQA")
        self.addcust.setAdminContent("This is for testing.......")
        self.addcust.clickOnSave()

        self.logger.info("*********Saving customer Info*********")
        self.logger.info("*********Add customer validation started*********")
        self.msg = self.driver.find_element(By.TAG_NAME, "body").text

        #print(self.msg)

        if 'customer has been added successfully' in self.msg:
            assert True == True
            self.logger.info("*********Add customer test passed*********")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_addCustomer_scr.png")
            self.logger.error("*********Add customer tset failed*********")
            assert True == False

        self.driver.close()
        self.logger.info("*********Ending Home page title test*********")


def random_generator(size = 8, chars = string.ascii_lowercase + string.digits):
    return "".join(random.choice(chars) for x in range(size))