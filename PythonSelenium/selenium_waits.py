"""
1. implicit wait : this is maximum wait that will apply on all the elements on the webpage.
                   in this condition task can be complete with in 1 sec or mini time, and it
                   can complete in max time as e.g 10 sec as well.
2. Explicit wait : This kind of wait will apply on specific element and we can defined
                   expected condition to be completed within time frame.

3. Fluent wait
4. static wait
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

driver = webdriver.Chrome()

driver.maximize_window()
driver.implicitly_wait(10)


driver.get("https://www.google.co.in/")

driver.find_element_by_name('q').send_keys('Selenium')
driver.find_element_by_name('btnK').click()
print("Execution successful")

driver.close()