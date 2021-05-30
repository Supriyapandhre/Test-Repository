from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.maximize_window()

XPATH1 = "//p[@id='travlastname_field']//input[contains(@id,'travlastname')]"
XPATH2 = "(//div[@class='col-1']//p[contains(@id, 'trav')]//input[contains(@id,'travlastname')])[1]"
XPATH3 = " //a[text()='Home']"

driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
#XPATH1
#driver.find_element_by_xpath(XPATH1).send_keys("lastname user1")

#XPATH2
#driver.find_element_by_xpath(XPATH2).send_keys("lastname user2")

#XPATH3
driver.find_element_by_xpath(XPATH3).click()

sleep(5)

driver.close()