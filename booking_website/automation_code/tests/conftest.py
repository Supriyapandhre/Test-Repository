import pytest
from automation_code.base.webdriver_factory import WebdriverFactory
from automation_code.data import  session_data as sd
from datetime import  datetime

@pytest.fixture(scope="class")
def setup(request):
    wf = WebdriverFactory(sd.browser, sd.url)
    global driver
    driver = wf.get_driver_instance()
    request.cls.driver = driver
    yield driver
    driver.quit()


def pytest_configure(config):
    """ Create a log file if log_file is not mentioned in *.ini file"""
    if not config.option.log_file:
        timestamp = datetime.strftime(datetime.now(), '%Y-%m-%d_%H-%M-%S')
        config.option.log_file = 'debug_'+ timestamp + '.log'


