from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.sqatools.in/2020/08/alerts.html")

# Locators
alert_boc_id = 'btnShowMsg'
confirm_box_id = 'button'
prompt_box = 'promptbtn'
confirm_msg_id = 'demo'
prompt_msg_id = 'prompt'

# input data
ok_press_msg = 'You pressed OK!'
cancel_press_msg = 'You pressed Cancel!'
user_input = 'John'
prompt_msg = f'Hello {user_input}! How are you today?'
prompt_dismiss_msg = 'User cancelled the prompt.'

# function
def handle_alert_box(wd):
    wd.find_element_by_id(alert_boc_id).click()
    alert1 = wd.switch_to.alert
    sleep(3)
    alert1.accept()
    sleep(3)
    print("executed complete , test cases passed")

def handle_confirm_alert_box(wd, input):
    sleep(5)
    wd.find_element_by_id(confirm_box_id).click()
    alert2 = wd.switch_to.alert
    if input == 'accept':
        alert2.accept()
        ui_msg = wd.find_element_by_id(confirm_msg_id).text
        print("ui_msg:", ui_msg)
        assert ui_msg == ok_press_msg
    elif input == 'dismiss':
        alert2.dismiss()
        ui_msg = wd.find_element_by_id(confirm_msg_id).text
        print("ui_msg:", ui_msg)
        assert ui_msg == cancel_press_msg
    print("executed complete , test cases passed")

def handle_prompt_alert(wd, accept_input, prompt_input):
    sleep(5)
    wd.find_element_by_id(prompt_box).click()
    alert3 = wd.switch_to.alert
    if accept_input == 'accept':
        alert3.send_keys(prompt_input)
        alert3.accept()
        accept_msg = wd.find_element_by_id(prompt_msg_id).text
        assert accept_msg == prompt_msg
    elif accept_input == 'dismiss':
        alert3.dismiss()
        dismiss_msg = wd.find_element_by_id(prompt_msg_id).text
        assert dismiss_msg == prompt_dismiss_msg

    print("executed complete , test cases passed")



# test cases
#test cases1 : accept alert box and confirm
handle_alert_box(driver)

#test cases2 : accept confirm box and verify msg
#import pdb; pdb.set_trace()
handle_confirm_alert_box(driver, 'accept')

# test cases3 : dismiss confirm box and verify msg
handle_confirm_alert_box(driver, 'dismiss')

# test cases 4: provide input to the prompt and verify msg
handle_prompt_alert(driver, 'accept', user_input)

# test cases 4: provide input to the prompt, dismiss and  verify cancel msg
handle_prompt_alert(driver, 'dismiss', user_input)


driver.close()

