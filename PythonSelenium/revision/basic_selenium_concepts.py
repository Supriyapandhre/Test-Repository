"""
Implicit wait : this waits on all the element by defaults
Explicit wait : this wait on specific element
static wait : this wait doest not relate to any element, it just stop operation after doing any action on the
web page.
"""
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome(executable_path="C:\\drivers\\chromedriver_win32\\chromedriver.exe")

driver.implicitly_wait(10)
wait = WebDriverWait(driver, 10)


driver.get("https://www.google.co.in")


driver.find_element_by_name('q').send_keys('Python')

#driver.find_element_by_name('btnK').click()

element = wait.until(ec.element_to_be_clickable((By.NAME, 'btnK')))

element.click()
# move back on web page
driver.back()

sleep(5)
# move forward on web page
driver.forward()

# refresh the page
driver.refresh()

#print(element.is_displayed())
#if element.is_enabled():
#    element.click()

# save_screen_shot

driver.save_screenshot("E:\\driver\\google_page.png")

#sleep(10)
driver.close()

