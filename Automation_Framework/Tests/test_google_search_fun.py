import pytest
from Automation_Framework.Modules.google_search_page import GoogleSearch
from Automation_Framework.Base.Selenium_code import selenium_driver


@pytest.mark.usefixtures("class_setup")
class TestGoogleSearch:

    def test_search_data_google(self):
        gc = GoogleSearch(self.driver)
        gc.search_content()

    def test_click_on_link(self):
        try:
            dr = selenium_driver(self.driver)
            dr.click_element(("Welcome to Python.org", "link1"))
        except Exception as e:
            attach(data=self.driver.get_screenshot_as_png())
            raise e
