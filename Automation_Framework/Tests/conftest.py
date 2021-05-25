import pytest
from Automation_Framework.Base.webdriver_factory import WebdriverFactory
from Automation_Framework.Data import session_data as data
from pytest_html_reporter import attach
from datetime import datetime
import os


@pytest.fixture(scope="session")
def setup():
    web = WebdriverFactory(data.browser, data.url)
    driver = web.get_driver_instance()
    return driver

@pytest.fixture(scope="class")
def class_setup(request):
    web = WebdriverFactory(data.browser, data.url)
    global driver
    driver = web.get_driver_instance()
    request.cls.driver = driver
    yield driver
    driver.quit()

@pytest.fixture(scope="class")
def dummy_setup(request):
    web = WebdriverFactory(data.browser, data.dummy_url)
    global driver
    driver = web.get_driver_instance()
    request.cls.driver = driver
    yield driver
    driver.quit()

def pytest_configure(config):
   """ Create a log file if log_file is not mentioned in *.ini file"""
   if not config.option.log_file:
        timestamp = datetime.strftime(datetime.now(), '%Y-%m-%d_%H-%M-%S')
        config.option.log_file = os.path.join(data.log_path, 'debug_'+ timestamp + '.log')