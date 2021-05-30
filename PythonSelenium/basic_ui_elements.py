from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.maximize_window()

#Get method helps to launch url on the browser
driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")


#Intract with text box
"""
sleep(3)
# send_keys : this method help to enter data to text box or any text area.
driver.find_element_by_id('travname').send_keys("John")

sleep(3)
# clear() : This method clear the existing content from the text box.
driver.find_element_by_id('travname').clear()

sleep(3)

# last name in the field.
driver.find_element_by_id('travlastname').send_keys('Hamilton')

#Put data to the text area
driver.find_element_by_id('order_comments').send_keys("We are booking ticket to go home")
sleep(3)
"""

# interact with radio button

element = driver.find_element_by_id('sex_1')


# is_selected() : this method check particular element is selected or not and return status as
#   True and False
#   Can be used to check if a checkbox or radio button is selected.
print("I radio button is selected:", element.is_selected())
element.click()
print("I radio button is selected:", element.is_selected())
# is_displayed() : check the target element is displayed on the UI or not.
# is_enabled() : check particular target element is enabled to perform operation


print("is_displayed :", element.is_displayed())
print("is_enabled :", element.is_enabled())
element.click()
sleep(3)

################################################################




# close() : this method close the current running instance of the browser.
driver.close()