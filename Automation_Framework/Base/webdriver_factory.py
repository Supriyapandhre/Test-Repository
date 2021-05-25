from selenium import webdriver
from Automation_Framework.Data import session_data as data


class WebdriverFactory:
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def get_driver_instance(self):
        if self.browser.lower() == 'chrome':
            self.driver = webdriver.Chrome(executable_path=data.chrome_driver_path)
        elif self.browser.lower() == 'firefox':
            self.driver = webdriver.Firefox()
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        return self.driver




