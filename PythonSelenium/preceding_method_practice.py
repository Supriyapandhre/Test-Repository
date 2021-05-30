from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.maximize_window()

XPATH1 = "//nav[@id='navbar']//a[text()='Blog' and @href='/blog']//preceding::a[text()='Projects']"

driver.get("https://www.selenium.dev/")
#XPATH1
sleep(5)
driver.find_element_by_xpath(XPATH1).click()

sleep(5)

driver.close()