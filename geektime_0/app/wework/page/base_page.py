import allure
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage():
    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    def find(self, by, value):
        self.driver.find_element(AppiumBy.XPATH, '')
        allure.attach(body=self.driver.get_screenshot_as_png(), attachment_type=allure.attachment_type.PNG)
        return self.driver.find_element(by, value)


