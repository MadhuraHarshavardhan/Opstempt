import pytest
from selenium import webdriver

@pytest.fixture
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome(r"C:\Users\Madhura\PycharmProjects\pythonProject2\Opstempt\Drivers\chromedriver.exe")
        print("Launching Chrome browser")
    elif browser == 'firefox':
        driver = webdriver.Firefox(r"C:\Users\Madhura\PycharmProjects\pythonProject2\Opstempt\Drivers\geckodriver.exe")
        print("Launching Firefox browser")
    else:
        driver = webdriver.Ie()
        print("Launching Edge browser")
    return driver

def pytest_addoption(parser): #this will get the value from CLI
    parser.addoption("--browser")

@pytest.fixture()
def browser(request): #This will return the browser value to set up method
    return request.config.getoption("--browser")

########pyTest html report ########

#it is a hook for adding environment info to HTML Report
def pytest_configure(config):
    config._metadata['Project Name'] = "nop Commerce"
    config._metadata['Module Name'] = "Customers"
    config._metadata['Test Engineer'] = "Madhura"

#it is a hook for deleting/modifying environment info to HTML report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins",None)
