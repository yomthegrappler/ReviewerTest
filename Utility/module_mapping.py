from Driver.selenium_webdriver import SeleniumDriver

class DriverMapping(SeleniumDriver):

    def execute_keyword(self, keyword, value, objectname):
        if keyword == 'navigate':
            result = None
            result = self.navigate(value)
            return result

        elif keyword == 'input':
            result = None
            result = self.sendKeys(value, objectname)
            return result

        elif keyword == "click":
            result = None
            result = self.elementClick(objectname)
            return result
