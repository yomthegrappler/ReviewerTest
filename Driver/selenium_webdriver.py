from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class SeleniumDriver:
    def __init__(self, driver):
        self.driver = driver

    def navigate(self, data):
        self.driver.get(data)
        return True

    def getElement(self, locator):
        time.sleep(0.4)
        element = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, locator)))
        return element

    def sendKeys(self, data, locator):
        self.getElement(locator).clear()
        self.getElement(locator).send_keys(data)
        return True

    def elementClick(self, locator):
        self.getElement(locator).click()
        return True
