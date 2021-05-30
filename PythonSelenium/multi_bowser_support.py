from selenium import  webdriver
from time import sleep
import sys
#browser = 'edge'
browser = sys.argv[1]
driver = None
if browser == 'chrome':
    driver = webdriver.Chrome()
elif browser == 'firefox':
    # For firefox browser we need geckodriver.
    driver = webdriver.Firefox(executable_path="E:\\driver\\geckodriver.exe")
elif browser == 'edge':
    driver = webdriver.Edge(executable_path="C:\\drivers\\edgedriver_win32\\msedgedriver.exe")

driver.maximize_window()
driver.implicitly_wait(10)

driver.get('https://www.google.co.in')

driver.find_element_by_name('q').send_keys("Python")
sleep(2)
driver.find_element_by_name('btnK').click()
sleep(2)
driver.close()

