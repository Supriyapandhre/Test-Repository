from Automation_Framework.Base.Selenium_code import selenium_driver
from Automation_Framework.Data.google_search_page_data import *

class GoogleSearch(selenium_driver):
    def __init__(self, driver):
        super().__init__(driver)

    def search_content(self):
        self.input_text(search_field, search_data)
        self.click_element(search_button)