import pytest
from automation_code.modules.bus.bus_booking_page import BusBooking
from time import sleep
import logging

log = logging.getLogger(__name__)

@pytest.mark.usefixtures("setup")
class TestBusBooking:
    
    def test_book_bus_and_verify(self):
        log.info('test_book_bus_and_verify execution started')
        bus_page = BusBooking(self.driver)
        bus_page.select_source()
        sleep(5)
        log.info('test_book_bus_and_verify execution finished')
        