import os

import allure
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait


class TestDemo:

    def setup_class(self):
        caps={
            'platformName': 'android',
            'app': '/Users/seveniruby/ke/app/appium/ApiDemos-debug.apk',
            'udid': os.getenv('udid')
        }
        self.driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub', caps)
        self.driver.implicitly_wait(5)

    def test_demo(self):
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Views').click()
        allure.attach(body=self.driver.get_screenshot_as_png(), attachment_type=allure.attachment_type.PNG)

        for i in range(3):
            self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Buttons').click()
            allure.attach(body=self.driver.get_screenshot_as_png(), attachment_type=allure.attachment_type.PNG)
            self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Normal')
            self.driver.back()
            allure.attach(body=self.driver.get_screenshot_as_png(), attachment_type=allure.attachment_type.PNG)



