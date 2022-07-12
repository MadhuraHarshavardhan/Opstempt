from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from time import sleep


class AddCustomer():
    #Add customer page
    lnkCustomers_menu_xpath = "//a[@href='#']//p[contains(text(),'Customers')]"
    lnkCustomers_menuitem_xpath = "//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]"
    btnAddnew_xpath = "//a[normalize-space()='Add new']"
    txtEmail_xpath = "//input[@id='Email']"
    txtPassword_xpath = "//input[@id='Password']"
    txtFirstName_xpath = "//input[@id='FirstName']"
    txtLastName_xpath = "//input[@id='LastName']"
    txtCustomerRoles_xpath = "//div[@class='k-multiselect-wrap k-floatwrap']"
    rdMale_Gender_id = "Gender_Male"
    rdFemale_Gender_id = "Gender_Female"
    txtDob_xpath = "//input[@id='DateOfBirth']"
    txtCompanyName_xpath = "//input[@id='Company']"
    txt_Newsletter_xpath = "//ul[@id='SelectedNewsletterSubscriptionStoreIds_taglist']/parent::div"
    li_Newsletter_Yourstorename_xpath = "//li[contains(text(), 'Your store name')]"
    li_Newsletter_Teststore2_xpath ="//li[contains(text(), 'Test store 2')]"
    txt_CustomerRoles_xpath = "//div[@class='input-group-append input-group-required']//div[@role='listbox']"
    li_CustomerRoles_Adminstrators_xpath = "//li[contains(text(), 'Administrators')]"
    li_CustomerRoles_ForumModerators_xpath = "//li[contains(text(), 'Forum Moderators')]"
    li_CustomerRoles_Guests_xpath = "//li[contains(text(), 'Guests')]"
    li_CustomerRoles_Registerd_xpath = "//li[contains(text(), 'Registered')]"
    li_CustomerRoles_Vendors_xpath = "//li[contains(text(), 'Vendors')]"
    drpmgrOfVendor_xpath = "//*[@id='VendorId']"
    txtAdminContent_xpath = "//textarea[@class='form-control']"
    btn_save_xpath = "//button[@name='save']"

    def __init__(self, driver):
        self.driver = driver

    def clickOnCustomerMenu(self):
        self.driver.find_element(By.XPATH, self.lnkCustomers_menu_xpath).click()

    def clickOnCustomerMenuItem(self):
        self.driver.find_element(By.XPATH, self.lnkCustomers_menuitem_xpath).click()

    def clickOnAddnew(self):
        self.driver.find_element(By.XPATH, self.btnAddnew_xpath).click()

    def setEmail(self, email):
        self.driver.find_element(By.XPATH, self.txtEmail_xpath).send_keys(email)

    def setPassword(self, password):
        self.driver.find_element(By.XPATH, self.txtPassword_xpath).send_keys(password)

    def setCustomerRoles(self,role):
        self.driver.find_element(By.XPATH, self.txtCustomerRoles_xpath).click()
        sleep(3)
        if role == 'Registered':
            self.listitem = self.driver.find_element(By.XPATH, self.li_CustomerRoles_Registerd_xpath)
        elif role == 'Administrators':
            self.listitem = self.driver.find_element(By.XPATH, self.li_CustomerRoles_Adminstrators_xpath)
        elif role == 'Guests':
            sleep(3)
            self.driver.find_element(By.XPATH,"//span[@title='delete']")
            self.listitem = self.driver.find_element(By.XPATH, self.li_CustomerRoles_Guests_xpath)
        elif role == 'Forum Moderators':
            self.listitem = self.driver.find_element(By.XPATH, self.li_CustomerRoles_ForumModerators_xpath)
        elif role == 'Vendors':
            self.listitem = self.driver.find_element(By.XPATH, self.li_CustomerRoles_Vendors_xpath)
        else:
            self.listitem = self.driver.find_element(By.XPATH, self.li_CustomerRoles_Guests_xpath)
        sleep(3)
        #self.listitem.click()
        self.driver.execute_script("arguments[0].click;", self.listitem)

    def setManagerOfVendor(self,value):
        drp = Select(self.driver.find_element(By.XPATH, self.drpmgrOfVendor_xpath))
        drp.select_by_visible_text(value)


    def setGender(self, gender):
        if gender == 'Male':
            self.driver.find_element(By.ID, self.rdMale_Gender_id)
        elif gender == 'Female':
            self.driver.find_element(By.ID, self.rdFemale_Gender_id)
        else:
            self.driver.find_element(By.ID, self.rdFemale_Gender_id)

    def setFirstName(self, fname):
        self.driver.find_element(By.XPATH, self.txtFirstName_xpath).send_keys(fname)

    def setLastName(self, lname):
        self.driver.find_element(By.XPATH, self.txtLastName_xpath).send_keys(lname)

    def setDob(self, dob):
        self.driver.find_element(By.XPATH, self.txtDob_xpath).send_keys(dob)

    def setCompanyName(self, comname):
        self.driver.find_element(By.XPATH, self.txtCompanyName_xpath).send_keys(comname)

    def setAdminContent(self, content):
        self.driver.find_element(By.XPATH, self.txtAdminContent_xpath).send_keys(content)

    def clickOnSave(self):
        self.driver.find_element(By.XPATH, self.btn_save_xpath).click()




