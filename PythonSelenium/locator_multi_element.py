from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.maximize_window()



driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")


#element_list = driver.find_elements_by_xpath("//a[@class='nav-item']")
element_list = driver.find_elements_by_xpath("//ul[@id='checkout-products']//input")

print(len(element_list))

for element in element_list:
    sleep(5)
    element.click()
    sleep(5)
    #driver.back()
    #@sleep(5)

driver.close()