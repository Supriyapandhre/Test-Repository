from selenium import webdriver
from time import  sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

college_url = 'https://www.collegedekho.com/engineering/colleges-in-india/'

driver.get(college_url)

college_list_element = driver.find_elements_by_xpath("//div[@class='row collegeBlock']//div[@class='title']/a")
college_link = []
for element in college_list_element:
    try:
        link= element.get_attribute('href')
        print(link)
        college_link.append(link)
    except:
        pass

for link in college_link:
    driver.execute_script(f"window.open('{link}');")
    driver.switch_to.window(driver.window_handles[1])
    sleep(3)
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    sleep(3)

driver.close()