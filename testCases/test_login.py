import pytest
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_001_Login:
    baseurl = ReadConfig.getApplicationURL() #"https://admin-demo.nopcommerce.com/"
    username = ReadConfig.getUseremail() #"admin@yourstore.com"
    password = ReadConfig.getPassword() #)"admin"

    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_homePageTitle(self, setup):
        self.logger.info("TEST_001_Login")
        self.logger.info("Verifying Home page Title")
        self.driver = setup
        self.driver.get(self.baseurl)
        act_title = self.driver.title
        if act_title == "Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("Home page Title test is passed")

        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homePageTilte.png")
            self.driver.close()
            self.logger.info("Home page Title test is failed")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self, setup):
        self.logger.info('Verifying Login test')
        self.driver = setup
        self.driver.get(self.baseurl)
        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPaswword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title
        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.logger.info("Login test is passed")
            self.driver.close()

        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
            self.driver.close()
            self.logger.error("Login test is failed")
            assert False



