from automation_code.base.selenium_code import SeleniumCode
from automation_code.data.bus.bus_booking_page_data import *
import logging

log = logging.getLogger(__name__)

class BusBooking(SeleniumCode):
    def __init__(self, driver):
        log.info("Bus Booking class initiated")
        super().__init__(driver)
        self.driver = driver

    def select_source(self):
        self.input_text(source_element, source_location)
        log.info(f"entered this text : {source_location}")
        self.click_element(source_dropdown_option)
        log.info(f"clicked on this element : {source_dropdown_option}")