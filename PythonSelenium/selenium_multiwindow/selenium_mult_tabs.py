from selenium import webdriver
from time import sleep
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

# we are playing with multiple browser tab.
driver.get("https://www.sqatools.in/p/manual-testing.html")

# Open link in new tab
driver.find_element_by_xpath("//a[contains(text(), 'What is Software Testing')]").click()

# Get the list tabs on the browser
windows = driver.window_handles
print("total windows :", len(windows))

#Switch to new browser window
driver.switch_to.window(windows[1])

# verify one element on new tab
tar_element = driver.find_element_by_xpath("//h3[contains(text(), 'Software Testing')]")
assert tar_element is not None
sleep(5)

# search content in new tab
driver.find_element_by_name('q').send_keys('Python')

#click in search button on new tab
driver.find_element_by_xpath("//input[@value='Search']").click()
sleep(5)

#close new tab
driver.close()

#switch back to default tab
driver.switch_to.window(windows[0])

sleep(2)
#click on home button
driver.find_element_by_xpath("//div[@class='widget-content']//a[contains(text(), 'Home')]").click()
sleep(5)

# close the remaining tab as well
driver.close()