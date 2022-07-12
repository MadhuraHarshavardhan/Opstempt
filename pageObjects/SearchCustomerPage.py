from selenium.webdriver.common.by import By

class SearchCustomer:
    txtEmail_Xpath = "//input[@id='SearchEmail']"
    txtFirstName_Xpath ="//input[@id='SearchFirstName']"
    txtLastName_Xpath = "//input[@id='SearchLastName']"
    btnSearch_Xpath = "//button[@id='search-customers']"

    tblSearchResults_xpath = "//table[@role='grid']"
    table_xpath = "//table[@id='customers-grid']"
    tableRows_xpath = "//table[@id='customers-grid']//tbody/tr"
    tableColumns_xpath = "//table[@id='customers-grid']//tbody/tr/td"

    def __init__(self, driver):
        self.driver = driver

    def setEmail(self, email):
        self.driver.find_element(By.XPATH, self.txtEmail_Xpath).clear()
        self.driver.find_element(By.XPATH, self.txtEmail_Xpath).send_keys(email)

    def setFirstName(self, fname):
        self.driver.find_element(By.XPATH, self.txtFirstName_Xpath).clear()
        self.driver.find_element(By.XPATH, self.txtFirstName_Xpath).send_keys(fname)

    def setLastName(self, lname):
        self.driver.find_element(By.XPATH, self.txtFirstName_Xpath).clear()
        self.driver.find_element(By.XPATH, self.txtLastName_Xpath).send_keys(lname)

    def clickSearch(self):
        self.driver.find_element(By.XPATH, self.btnSearch_Xpath).click()

    def getNoOfRows(self):
        return len(self.driver.find_elements(By.XPATH, self.tableRows_xpath))

    def getNoOfColumns(self):
        return len(self.driver.find_elements(By.XPATH, self.tableColumns_xpath))

    def searchCustomerByEmail(self, email):
        flag = False
        for r in range(1, self.getNoOfRows()+1):
            table = self.driver.find_element(By.XPATH, self.table_xpath)
            emailid = table.find_element(By.XPATH, "//table[@id='customers-grid']/tbody/tr["+str(r)+"]/td[2]").text
            if emailid == email:
                flag = True
                break
        return flag

    def searchCustomerByName(self, Name):
        flag = False
        for r in range(1, self.getNoOfRows() + 1):
            table = self.driver.find_element(By.XPATH, self.table_xpath)
            name = table.find_element(By.XPATH, "//table[@id='customers-grid']/tbody/tr["+str(r)+"]/td[3]").text
            if name == Name:
                flag = True
                break

        return flag