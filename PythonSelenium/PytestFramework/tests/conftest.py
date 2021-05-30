import pytest
from selenium import  webdriver
from .data_file import *

driver = webdriver.Chrome(executable_path="C:\\drivers\\chromedriver_win32\\chromedriver.exe")

@pytest.fixture(scope='session')
def setup():
    driver.get(url)
    driver.maximize_window()
    driver.implicitly_wait(10)
    return driver
