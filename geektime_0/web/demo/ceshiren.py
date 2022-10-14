import os

import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from geektime_0.web.demo.search import Search


class Ceshiren:
    def open(self):
        # 打开浏览器
        browser = os.getenv('browser')
        if browser == 'chrome':
            options = webdriver.ChromeOptions()
        elif browser == 'firefox':
            options = webdriver.FirefoxOptions()
        else:
            options = webdriver.ChromeOptions()

        # self.driver = webdriver.Remote('http://docker.hogwarts.ceshiren.com:14444/wd/hub', options=options)
        self.driver = webdriver.Remote('http://192.168.64.3:4444/wd/hub', options=options)
        print("xieyanyang=================")
        #self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.get('https://ceshiren.com/')
        allure.attach(body=self.driver.get_screenshot_as_png(), attachment_type=allure.attachment_type.PNG)

    def open_search(self):
        self.driver.find_element(By.ID, 'search-button').click()
        allure.attach(body=self.driver.get_screenshot_as_png(), attachment_type=allure.attachment_type.PNG)

        search = Search(self.driver)
        return search

    def close(self):
        self.driver.quit()
