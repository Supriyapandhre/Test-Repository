from selenium import webdriver
from time import  sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://www.google.co.in")

print(driver.execute_script("return document.URL;"))
print(driver.execute_script("return document.title;"))

text_box = driver.execute_script("return document.getElementsByName('q')[0];")

text_box.send_keys("Selenium")
sleep(5)
search_button = driver.execute_script("return document.getElementsByName('btnK')[0];")

search_button.click()

print(driver.execute_script("return document.URL;"))
print(driver.execute_script("return document.title;"))
sleep(5)
driver.close()


