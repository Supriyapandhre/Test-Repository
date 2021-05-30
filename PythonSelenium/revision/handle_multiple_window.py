from selenium import webdriver
from time import sleep

driver = webdriver.Chrome(executable_path="C:\\drivers\\chromedriver_win32\\chromedriver.exe")

driver.implicitly_wait(10)
driver.maximize_window()

driver.get("https://www.sqatools.in/p/manual-testing.html")


driver.find_element_by_link_text('What is Software Testing').click()
windows_handles = driver.window_handles

driver.switch_to.window(windows_handles[1])


driver.find_element_by_name('q').send_keys('python')
driver.find_element_by_xpath("//input[@type='submit' and @title='search']").click()

driver.close()

driver.switch_to.window(windows_handles[0])

driver.find_element_by_link_text('Code Practice').click()


sleep(5)

driver.close()





