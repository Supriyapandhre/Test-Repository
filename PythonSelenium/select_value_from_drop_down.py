from selenium import webdriver
from selenium.webdriver.support.ui import Select
from time import sleep

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://www.sqatools.in/2020/08/dropdown.html")
"""
select_obj = Select(driver.find_element_by_id("cars"))
sleep(5)
#select_obj.select_by_visible_text("BMW Sport Car")

#select_obj.select_by_value('jaguar')

select_obj.select_by_index(0)

sleep(5)
"""

def select_value_from_dropdown(locator, value):
    select_obj = Select(driver.find_element_by_id(locator))
    sleep(5)
    select_obj.select_by_visible_text(value)
    sleep(5)

select_value_from_dropdown('cars', 'Jaguar Laxury')
select_value_from_dropdown('cars', 'Land Rover')
select_value_from_dropdown('cars', 'BMW Sport Car')


driver.close()


