from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.maximize_window()

CSS1 = "input[name='travname']"
CSS2 =  "input[id='travname']"
CSS3 = "p[id='travname_field']>input"
CSS4 = "div[class='col-1']>div>p[id='travname_field']>input"

driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")

#CSS1
#driver.find_element_by_css_selector(CSS1).send_keys("Rahul Sharma")

#CSS2
#driver.find_element_by_css_selector(CSS2).send_keys("Rahul Sharma")

#CSS3
#driver.find_element_by_css_selector(CSS3).send_keys("Vipin")

#CSS4
driver.find_element_by_css_selector(CSS4).send_keys("Zafar")


sleep(5)
driver.close()