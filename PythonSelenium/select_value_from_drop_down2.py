from selenium import webdriver
from selenium.webdriver.support.ui import Select
from time import sleep

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")

date_of_birth_element_id ='dob'
month_dropdown_xpath = "//select[@class='ui-datepicker-month']"
year_dropdown_xpath = "//select[@class='ui-datepicker-year']"
add_more_passenger_checkbox_id = 'addmorepax'
add_more_passenger_dropown_id = "addpaxno"
#Select month and year in calendar.
driver.find_element_by_id(date_of_birth_element_id).click()
sleep(5)
select_month = Select(driver.find_element_by_xpath(month_dropdown_xpath))
select_month.select_by_visible_text('Aug')
sleep(5)
select_year = Select(driver.find_element_by_xpath(year_dropdown_xpath))
select_year.select_by_visible_text('1990')

driver.find_element_by_xpath("//a[text()='24']").click()

sleep(5)

# click on add more passenger checkbox
driver.find_element_by_id(add_more_passenger_checkbox_id).click()

# Select value from checkbox
select_passe = Select(driver.find_element_by_id(add_more_passenger_dropown_id))
sleep(2)
select_passe.select_by_visible_text('add 2 more passengers')


sleep(5)


driver.close()


