from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")


element = driver.find_element_by_id('addmorepax')

# Verify the checkbox is enabled, then click on that
if element.is_enabled():
    element.click()
    sleep(2)
    driver.find_element_by_id('select2-addpaxno-container').click()
    sleep(2)
    driver.find_element_by_xpath("//li[contains(text(),'add 3 more passengers')]").click()
    sleep(2)

sleep(5)

# interact with calender date of birth
driver.find_element_by_id('dob4').click()
sleep(2)
driver.find_element_by_xpath("//a[text()='20']").click()
sleep(2)
# close() : this method close the current running instance of the browser.
driver.close()