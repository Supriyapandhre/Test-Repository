"""
1: install selenium on machine pip command
    pip install selenium.
2: Download chrome driver and set path in environment variable.
    -> Check your browser version
    -> Download the driver as per browser version
3: Get locator of the element on which we want to perform operation.
"""

from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(executable_path="C:\\drivers\\chromedriver_win32\\chromedriver.exe")

wait = WebDriverWait(driver, 10)

user_locator = ("btnK1", "name")
print(type(By.NAME))

#print(user_locator[1])


def get_locator_type(locator):
    if locator.lower() == 'name':
        return By.NAME
    elif locator.lower() == 'xpath':
        return By.XPATH
    elif locator.lower() == 'id':
        return By.ID

def get_by_element(locator, driver):
    if locator.lower() == 'name':
        return driver.find_element_by_name
    elif locator.lower() == 'xpath':
        return driver.find_element_by_xpath
    elif locator.lower() == 'id':
        return driver.find_element_by_id


driver.get("https://www.google.co.in")
driver.maximize_window()

by_element = get_by_element('name', driver)
by_element('q').send_keys('selenium')

#driver.find_element_by_name('q').send_keys('Selenium')

sleep(2)

#driver.find_element_by_name('btnK').click()
#wait.until(ec.element_to_be_clickable((By.NAME, 'btnK'))).click()
#import pdb;pdb.set_trace()
#locator_type = get_locator_type(user_locator[1])
#print(locator_type)
element = user_locator[0]
print(element)


web_element = wait.until(ec.element_to_be_clickable(('name', element)))
web_element.click()

sleep(5)
driver.close()