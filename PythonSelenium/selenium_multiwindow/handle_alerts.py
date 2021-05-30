from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://www.sqatools.in/2020/08/alerts.html")

""""
#alert_box_1
driver.find_element_by_id('btnShowMsg').click()

alert_msg = driver.switch_to.alert

# Get text on the alert
print(alert_msg.text)
sleep(5)
# Accept the alert
alert_msg.accept()
sleep(5)
"""
#################################################
#ALERT_BOX2
"""
verification_msg = 'You pressed OK!'
cancel_mg = 'You pressed Cancel!'

driver.find_element_by_id('button').click()

alert2 = driver.switch_to.alert

# print alert message
print(alert2.text)

sleep(5)
"""
"""
# accept alert
alert2.accept()
# verify message after clicking
ui_msg = driver.find_element_by_id('demo').text
assert ui_msg == verification_msg
"""

# dismiss the confirmation box
"""
alert2.dismiss()
sleep(5)
ui_msg = driver.find_element_by_id('demo').text
assert ui_msg == cancel_mg
"""

##############################################
# Handle aAlert 3, which need user input.
user_input = 'SQA Tools'
confirm_msg = f'Hello {user_input}! How are you today?'

driver.find_element_by_id("promptbtn").click()

alert3 = driver.switch_to.alert
sleep(5)
alert3.send_keys(user_input)
sleep(2)
alert3.accept()

ui_msg = driver.find_element_by_id("prompt").text
assert ui_msg == confirm_msg

sleep(5)


sleep(5)
driver.close()