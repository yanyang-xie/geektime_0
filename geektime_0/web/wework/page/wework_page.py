from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from geektime_0.web.wework.framework.base_page import BasePage
from geektime_0.web.wework.page.contact_page import ContactPage


class WeWorkPage(BasePage):
    def __init__(self, driver=None):
        # 绕过扫码认证直接进入后台，如果以后要使用多浏览器，可以用cookie复用代替
        super().__init__(driver)
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame#index')

    def contact(self):
        # 显式等待的高级用法，使用复杂行为解决点击不生效问题
        def loop_click(driver):
            self.click(By.LINK_TEXT, '通讯录')
            return len(self.driver.find_elements(By.LINK_TEXT, '删除')) > 0

        WebDriverWait(self.driver, 10).until(loop_click)

        return ContactPage(self.driver)

    def portal(self):
        # self.driver.find_element(By.LINK_TEXT, '首页').click()

        self.click(By.LINK_TEXT, '首页')
        return self
