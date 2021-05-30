from selenium import  webdriver
from time import  sleep
import pytest

driver = webdriver.Chrome(executable_path="C:\\drivers\\chromedriver_win32\\chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(10)

@pytest.mark.smoke
@pytest.mark.sanity
def test_launch_url_and_verify():
    driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
    element = driver.find_element_by_xpath("//h2[@class='fg-text-dark ffb-h2-1']/p[2]")
    expected_title = "Dummy ticket booking"
    heading = element.text
    assert  expected_title == heading

@pytest.mark.sanity
def test_provide_user_surname():
    driver.find_element_by_name('travname').send_keys("John")
    driver.find_element_by_name('travlastname').send_keys("Jony")
    sleep(3)


@pytest.mark.smoke
def test_passenger_details():
    driver.find_element_by_id("traveltype_1").click()
    driver.find_element_by_name("fromcity").send_keys("Pune")
    driver.find_element_by_name("tocity").send_keys("Mumbai")
    sleep(3)


@pytest.mark.sanity
def test_Add_bill_name():
    driver.find_element_by_id("billname").send_keys("john")
    driver.find_element_by_id("billing_phone").send_keys("4567889")
    driver.find_element_by_id("billing_email").send_keys("john_test@gmail.com")

@pytest.mark.sanity
@pytest.mark.smoke
def test_close_browser():
    driver.close()