from time import sleep

from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.remote.webdriver import WebDriver

from geektime_0.app.wework.page.base_page import BasePage


class ContactPage(BasePage):

    def add_contact(self, name, phone):
        self.find(AppiumBy.ID, 'kui').click()
        self.find(AppiumBy.CSS_SELECTOR, '[text="添加成员"]').click()
        self.find(AppiumBy.CSS_SELECTOR, '[text="手动输入添加"]').click()
        el5 = self.find(by=AppiumBy.ID, value="com.tencent.wework:id/buo")
        el5.send_keys(name)
        el6 = self.find(by=AppiumBy.ID, value="com.tencent.wework:id/hva")
        el6.send_keys(phone)
        self.find(AppiumBy.ID, 'hfc').click()
        self.find(AppiumBy.CSS_SELECTOR, '[text="保存"]').click()
        #todo: 用显式等待
        sleep(2)
        self.find(AppiumBy.ID, 'ktu').click()
        self.find(AppiumBy.ID, 'kud').click()

    def back(self):
        self.find(AppiumBy.CSS_SELECTOR, '[text="消息"]').click()
