import pytest
from Automation_Framework.Modules.dynamic_page import Dynamic
from Automation_Framework.Base.Selenium_code import selenium_driver
from pytest_html_reporter import attach
from Automation_Framework.Data.dynamic_data import *
import logging
from time import sleep

log = logging.getLogger(__name__)

@pytest.mark.usefixtures("class_setup")
class TestDynamic:

    def test_select_dynamic(self):
        self.driver.get(college_list_url)

        obj = Dynamic(self.driver)
        obj.select_dynamic_checkbox(collge_id)
        sleep(5)

    def test_select_multiple_checkboz(self):
        for id in collge_id_list:
            obj = Dynamic(self.driver)
            obj.select_dynamic_checkbox(id)
        sleep(5)