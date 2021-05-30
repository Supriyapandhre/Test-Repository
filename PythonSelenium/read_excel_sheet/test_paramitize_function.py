from selenium import  webdriver
from time import  sleep
import pytest
from .read_excel_file import get_cell_data

driver = webdriver.Chrome(executable_path="C:\\drivers\\chromedriver_win32\\chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.sqatools.in/2020/08/loginform.html")

def generate_login_credentials():
    data_list = []
    for row in range(1, 6):
        username = get_cell_data(row, 1)
        password = get_cell_data(row, 2)
        print(username, password)
        data_list.append((username, password))

    return data_list

input_data = generate_login_credentials()

def login(username, password):
    driver.find_element_by_id("usrname").clear()
    driver.find_element_by_id("usrname").send_keys(username)
    driver.find_element_by_id("psw").clear()
    driver.find_element_by_id("psw").send_keys(password)
    driver.find_element_by_xpath("//input[@id='psw']//following-sibling::input[@type='submit']").click()

@pytest.mark.parametrize("username, password", input_data)
def test_login_functionality(username, password):
    login(username, password)
    sleep(5)

@pytest.mark.skip
def test_new_functionality():
    driver.find_element_by_link_text('Code Practice').click()
