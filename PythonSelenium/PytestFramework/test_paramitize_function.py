from selenium import  webdriver
from time import  sleep
import pytest

@pytest.mark.parametrize("num1, num2, sum", [(2, 3, 5), (30, 50, 80), (40, 40, 90)])
def test_addition(num1, num2, sum):
    assert num1+num2 == sum

driver = webdriver.Chrome(executable_path="C:\\drivers\\chromedriver_win32\\chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://www.sqatools.in/2020/08/loginform.html")

def login(username, password):
    driver.find_element_by_id("usrname").clear()
    driver.find_element_by_id("usrname").send_keys(username)
    driver.find_element_by_id("psw").clear()
    driver.find_element_by_id("psw").send_keys(password)
    driver.find_element_by_xpath("//input[@id='psw']//following-sibling::input[@type='submit']").click()


@pytest.mark.parametrize("username, password", [('user##', 'password1'), ('P@@@@user2', 'password2'), ('user3&&^^&^', 'password3')])
def test_login_functionality(username, password):
    login(username, password)
    sleep(5)


@pytest.mark.skip
def test_new_functionality():
    driver.find_element_by_link_text('Code Practice').click()
