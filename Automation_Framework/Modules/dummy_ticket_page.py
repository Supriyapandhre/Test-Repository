from Automation_Framework.Base.Selenium_code import selenium_driver
from Automation_Framework.Data.dummy_ticket_page_data import *


class DummyTicket(selenium_driver):
    def __init__(self, driver):
        super().__init__(driver)

    def enter_first_name(self, first_name):
        self.input_text(first_name_field, first_name)

    def enter_lastname(self, lastname):
        self.input_text(last_name_field, lastname)

    def select_dob(self, month, year):
        self.click_element(dob_calender)
        self.select_value_from_dropdown(month_dropdown, month)
        self.select_value_from_dropdown(year_dropdown, year)
        self.click_element(date_link)

    def select_male_gender(self):
        self.click_element(gender_button)

    def select_more_passenger(self, value):
        self.click_element(add_more_passenger_checkbox)
        self.select_value_from_dropdown(add_more_pass_dropdown, value)

