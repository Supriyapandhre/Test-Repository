from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.maximize_window()

#Get method helps to launch url on the browser
driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")

element = driver.find_element_by_id('travname')

# Through get attribute method we can get any attribute value   of the element
class_name = element.get_attribute('class')

print(class_name)

driver.get("https://www.sqatools.in/p/manual-testing.html")

list_elements = driver.find_elements_by_tag_name('a')

for element in list_elements:
    # Get attribute value using get_attribute method
    print(element.get_attribute('href'))

    # Get text of any element using text method
    print(element.text)