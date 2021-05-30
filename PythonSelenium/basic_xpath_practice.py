from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.maximize_window()

XPATH1 = "//input[@id='travname']"
XPATH2 = "//input[@name='travname']"
XPATH3 = "//*[@name='travname']"
XPATH4 = "//p//*[@name='travname']"
XPATH5 = "//p//input[@name='travname']"
XPATH6 = "//p[@id='travname_field']//input"
XPATH7 = "//*[@id='travname_field']//input"
XPATH8 = "//div[@id='customer_details']//input[@id='travname']"
XPATH9 = "//div[@class='wcopc']//input[@id='travname']"

driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
#XPATH1
#driver.find_element_by_xpath(XPATH1).send_keys("user1")

#XPATH2
#driver.find_element_by_xpath(XPATH1).send_keys("user2")

#XAPTH3
driver.find_element_by_xpath(XPATH2).send_keys("user3")

sleep(5)

driver.close()