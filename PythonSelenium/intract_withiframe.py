from selenium import  webdriver
from time import sleep


driver = webdriver.Chrome()

driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://the-internet.herokuapp.com/iframe")

driver.switch_to.frame('mce_0_ifr')

sleep(2)
driver.find_element_by_id('tinymce').send_keys("Learning Selenium is Fun")


driver.switch_to.default_content()
sleep(2)
driver.find_element_by_xpath("//span[text()='File']").click()
sleep(5)
driver.close()