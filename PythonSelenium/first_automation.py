from selenium import webdriver
from time import sleep

driver  = webdriver.Chrome(executable_path="C:\\drivers\\chromedriver_win32\\chromedriver.exe")

driver.get("https://www.google.co.in")

driver.maximize_window()
sleep(2)
# Name
driver.find_element_by_name('q').send_keys('Selenium')
sleep(5)
#element = driver.execute_script("document.getElementsByName('btnK')[0].click();")

element = driver.execute_script("return document.getElementsByName('btnK')[0];")

element.click()

# CSS SELECTORS
#driver.find_element_by_css_selector("input[name='q']").send_keys('Selenium')

#driver.find_element_by_css_selector("input[title='Search']").send_keys('Selenium')

#driver.find_element_by_css_selector("input[aria-label='Search']").send_keys('Selenium')

#driver.find_element_by_css_selector("div[jsname='gLFyf']>input[name='q']").send_keys('Selenium')

#XPATH




sleep(2)
#driver.find_element_by_name('btnK').click()
sleep(3)

driver.close()

