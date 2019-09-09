from selenium import webdriver
from Utility.constant import Constant

class GetWebdriverInstance:

    def __init__(self, browser):
        self.browser = browser.lower()
        self.constant = Constant()

    def getbrowserInstance(self):
        if self.browser == 'chrome':

            driverLocation = self.constant.Path_Chrome_Driver
            driver = webdriver.Chrome(executable_path=driverLocation)

            driver.maximize_window()
            driver.implicitly_wait(5)
            driver.delete_all_cookies()
            return driver

        elif self.browser == 'firefox':

            path = self.constant.Path_Firefox_Driver
            driver = webdriver.Firefox(executable_path=path)

            driver.maximize_window()
            driver.implicitly_wait(5)
            driver.delete_all_cookies()
            return driver

        else:
            print("Please make sure selected browser is correct")