"""
1. implicit wait : this is maximum wait that will apply on all the elements on the webpage.
                   in this condition task can be complete with in 1 sec or mini time, and it
                   can complete in max time as e.g 10 sec as well.

2. Explicit wait : This kind of wait will apply on specific element and we can defined
                   expected condition to be completed within time frame.

3. Fluent wait : This kind of wait will apply on specific element and we can also defined
                 expected condition to be true in given time, frame, only difference is
                 in explicit wait and fluent wait, we can decide polling frequency on fluent wait.

4. static wait : static wait is hard coded wait, once it is set, then we have to wait till that time
                this wait is not recommended in real time project, it may increase the execution a lot.
                e.g. time.sleep(10)
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from time import sleep

driver = webdriver.Chrome()
driver.maximize_window()

# Explicit wait
wait = WebDriverWait(driver, 10)
# Fluent Wait
wait2 = WebDriverWait(driver, 5, poll_frequency=1)


driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")

# Apply Explicit wait on specific element
first_name_element = wait.until(ec.visibility_of_element_located((By.NAME, 'travname')))

first_name_element.send_keys('John')

# Apply fluent wait on lastname field
#driver.find_element_by_name('travlastname').send_keys('Harry')
last_name_element = wait2.until(ec.element_to_be_clickable((By.NAME, 'travlastname')))

last_name_element.send_keys("Harry")

print("Execution successful")

# static waits
sleep(10)

driver.close()