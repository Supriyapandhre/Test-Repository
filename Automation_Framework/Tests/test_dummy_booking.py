import pytest
from Automation_Framework.Modules.dummy_ticket_page import DummyTicket
from Automation_Framework.Data.dummy_ticket_page_data import *
from time import sleep

@pytest.mark.usefixtures("dummy_setup")
class TestDummyBooking:

    @pytest.mark.sanity
    def test_provide_passenger_entry(self):
        global dm
        dm = DummyTicket(self.driver)
        dm.enter_first_name(user_name)
        dm.enter_lastname(last_name)

    @pytest.mark.sanity
    def test_select_date_of_birth_and_other_info(self):
        dm.select_dob(dob_month, dob_year)
        dm.select_male_gender()
        sleep(2)

    def test_select_more_passenger(self):
        dm.select_more_passenger(extra_passenger)
        sleep(5)
