from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import logging

log = logging.getLogger(__name__)

class SeleniumCode:
    def __init__(self, driver):
        logging.info("browser initiated")
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)


    def get_locator_type(self, locator_type):
        if locator_type.lower() == "xpath":
            return By.XPATH
        elif locator_type.lower() == "name":
            return By.NAME
        elif locator_type.lower() == "id":
            return By.ID
        elif locator_type.lower() == "css":
            return By.CSS_SELECTOR
        elif locator_type.lower() == "link":
            return By.LINK_TEXT

    def click_element(self, element):
        log.info(f"this element is picked to configure : {element}")
        element_locator = element[0]
        locator_type = self.get_locator_type(element[1])
        web_element = self.wait.until(ec.element_to_be_clickable((locator_type, element_locator)))
        web_element.click()

    def input_text(self, element, value):
        log.info(f"this element is picked to configure : {element}")
        element_locator = element[0]
        locator_type = self.get_locator_type(element[1])
        web_element = self.wait.until(ec.element_to_be_clickable((locator_type, element_locator)))
        web_element.clear()
        web_element.send_keys(value)



