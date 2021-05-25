from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from datetime import datetime
from selenium.webdriver.support.select import Select
from Automation_Framework.Data.session_data import *
import logging

log = logging.getLogger(__name__)

class selenium_driver:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver,  10)

    def get_locator_type(self, locator):
        if locator.lower() == "xpath":
            return By.XPATH
        elif locator.lower() == "id":
            return By.ID
        elif locator.lower == 'css':
            return By.CSS_SELECTOR
        elif locator.lower() == 'link':
            return By.LINK_TEXT
        elif locator.lower() == 'name':
            return By.NAME


    def click_element(self, element):
        try :
            web_element = element[0]
            element_type = self.get_locator_type(element[1])
            elem = self.wait.until(ec.element_to_be_clickable((element_type,  web_element)))
            if elem is None:
                filename = datetime.now().strftime("%d_%m_%y_%H_%M_%S")
                self.driver.save_screenshot(f"{log_path}\\{filename}_{str(element)}.png")
            else:
                elem.click()
        except Exception as e:
            filename = datetime.now().strftime("%d_%m_%y_%H_%M_%S")
            self.driver.save_screenshot(f"{log_path}\\{filename}_{str(element)}.png")
            raise e

    def input_text(self,  element, value):
        try:
            web_element = element[0]
            element_type = self.get_locator_type(element[1])
            elem = self.wait.until(ec.visibility_of_element_located((element_type, web_element)))
            if elem is None:
                filename = datetime.now().strftime("%d_%m_%y_%H_%M_%S")
                self.driver.save_screenshot(f"{log_path}\\{filename}_{str(element)}.png")
            else:
                elem.send_keys(value)
        except Exception as e:
            filename = datetime.now().strftime("%d_%m_%y_%H_%M_%S")
            self.driver.save_screenshot(f"{log_path}\\{filename}_{str(element)}.png")
            raise e

    def get_element(self, locator):
        web_element = locator[0]
        element_type = self.get_locator_type(locator[1])
        elem = self.wait.until(ec.element_to_be_clickable((element_type, web_element)))
        return elem

    def select_value_from_dropdown(self, locator, value):
        element = self.get_element(locator)
        select_obj = Select(element)
        select_obj.select_by_visible_text(value)

    def get_element_text(self, locator):
        element = self.get_element(locator)
        return element.text

    def get_attribute(self,locator, attribute):
        element = self.get_element(locator)
        return element.get_attribute(attribute)

    def switch_to_windows(self):
        window_handle = self.driver.windows_hanldes()
        self.driver.switch_to.window(window_handle[1])