from selenium import  webdriver
from automation_code.data.session_data import *
from selenium.webdriver.chrome.options import Options

class WebdriverFactory:

    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def get_driver_instance(self):
        driver = None
        if self.browser.lower() == "chrome":
            option = Options()
            option.add_argument('--headless')
            driver = webdriver.Chrome(executable_path=chrome_driver, options=option)
        elif self.browser.lower() == "firefox":
            driver = webdriver.Firefox(executable_path=firefox_driver)
        driver.get(self.url)
        driver.maximize_window()
        driver.implicitly_wait(10)

        return driver
