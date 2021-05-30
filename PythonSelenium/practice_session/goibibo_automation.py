from selenium import  webdriver
from PythonSelenium.practice_session.data_file import *
from selenium.webdriver.support.ui import Select
from time import sleep

driver = None
if browser == 'chrome':
    driver = webdriver.Chrome()
elif browser == 'firefox':
    driver = webdriver.Firefox()
elif browser == 'edge':
    driver = webdriver.Edge()

driver.maximize_window()
driver.implicitly_wait(10)
driver.get(url)

# Seach Source location and Select

driver.find_element_by_id(source_field_id).send_keys(source_location_search)

all_elements = driver.find_elements_by_xpath(source_drop_values)

for element in all_elements:
    #print(element.text)
    text_name = element.text
    name = text_name.split("\n")[0]
    # print(name)
    # print(element.tag_name)
    # print("_"*50)
    if name == select_source:
        element.click()
        break
    else:
        continue

# Select Destination
driver.find_element_by_id(destination_field_id).send_keys(destination_location_search)
all_elements_dest = driver.find_elements_by_xpath(source_drop_values)

for element in all_elements_dest:
    #print(element.text)
    text_name = element.text
    name = text_name.split("\n")[0]
    # print(name)
    # print(element.tag_name)
    # print("_"*50)

    if name == select_destination:
        element.click()
        break
    else:
        continue


# Departure date
depart_date_xpath = date_xpath.replace('date', depart_date)
driver.find_element_by_xpath(depart_date_xpath).click()

# Return date
driver.find_element_by_xpath(return_calendar_xpath).click()
return_date_xpath = date_xpath.replace('date', return_date)
driver.find_element_by_xpath(return_date_xpath).click()

#select type of flight and passenger

driver.find_element_by_id(passenger_section_id).click()

#add adult
for i in range(adult):
    driver.find_element_by_id(add_adults_id).click()

#add child
for i in range(child):
    driver.find_element_by_id(add_child_id).click()

#add infant
for i in range(infant):
    driver.find_element_by_id(add_infant_id).click()

# Select flight type
select_obj = Select(driver.find_element_by_id(flight_type_dropdown))
select_obj.select_by_visible_text(flight_type)

sleep(5)
# Click on search button
driver.find_element_by_id(search_button_id).click()

sleep(5)
driver.close()