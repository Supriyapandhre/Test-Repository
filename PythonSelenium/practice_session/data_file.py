browser = 'chrome'
url = 'https://www.goibibo.com/'


############ input data #############
source_location_search = 'Pune'
select_source = 'Pune, India(PNQ)'
destination_location_search = 'Delhi'
select_destination = 'Delhi, India(DEL)'
depart_date = '20'
return_date = '21'

adult = 2
child = 2
infant = 2
flight_type = 'First class'

############# locators ##############
source_field_id = 'gosuggest_inputSrc'
source_drop_values = "//ul[contains(@id,'react-autosuggest')]//div"
destination_field_id = 'gosuggest_inputDest'
date_xpath = "//div[text()='date']"
return_calendar_xpath = "//input[@id='returnCalendar']"
passenger_section_id = "pax_link_common"
add_adults_id = 'adultPaxPlus'
add_child_id =  'childPaxPlus'
add_infant_id = 'infantPaxPlus'
flight_type_dropdown = 'gi_class'
search_button_id = 'gi_search_btn'