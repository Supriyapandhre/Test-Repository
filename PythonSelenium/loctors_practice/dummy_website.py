from selenium import webdriver
from time import sleep

URL = "https://www.dummyticket.com/dummy-ticket-for-visa-application/"
XPATH1 = "//input[@name='travname']"
XPATH2 = "//*[@name='travname']"
XPATH3 = "//*[@id='travname']"
XPATH4 = "//p[@id='travname_field']//input"
XPATH5 = "//p[@id='travname_field']//input[@name='travname']"
XPATH6 = "//*[@id='travname_field']//input[@name='travname']"
XPATH7 = "//div[@class='col2-set']//input[@name='travname']"
XPATH8 = "//div[@id='customer_details']//input[@name='travname']"
XPATH9 = "//*[@id='customer_details']//input[@name='travname']"

driver = webdriver.Chrome(executable_path="C:\\drivers\\chromedriver_win32\\chromedriver.exe")

driver.maximize_window()

driver.get(URL)

#driver.find_element_by_xpath(XPATH1).send_keys("Rahul")
driver.find_element_by_xpath(XPATH2).send_keys("Rahul")
sleep(5)
driver.close()
