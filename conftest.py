from Driver.webdriver_factory import GetWebdriverInstance
import pytest

@pytest.fixture(scope="class")
def setup(request, browser):
    wdf = GetWebdriverInstance(browser)
    driver = wdf.getbrowserInstance()

    if request.cls is not None:
        request.cls.driver = driver
    yield driver
    driver.quit()

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")
