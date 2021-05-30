from selenium import webdriver
from read_json_file import get_json_data
from time import sleep

data = get_json_data()
browser = data['browser']
driver = None

if browser.lower() == "chrome":
    driver = webdriver.Chrome(executable_path="C:\\drivers\\chromedriver_win32\\chromedriver.exe")
elif browser.lower() == 'firefox':
    driver = webdriver.Firefox()

driver.maximize_window()
driver.implicitly_wait(10)
driver.get(data['url'])

driver.find_element_by_id('travname').send_keys(data['pass_name'])
driver.find_element_by_id('travlastname').send_keys(data['pass_surname'])
driver.find_element_by_id('order_comments').send_keys(data['comment'])

sleep(5)
driver.close()