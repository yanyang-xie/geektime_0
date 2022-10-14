import allure
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from geektime_0.web.wework.framework.base_page import BasePage
from geektime_0.web.wework.page.member import Member
from geektime_0.web.wework.page.member_page import MemberPage


class ContactPage(BasePage):
    def __init__(self, driver: WebDriver):
        # 接受外部传入的driver，用于自己的自动化测试
        super().__init__(driver)

        WebDriverWait(self.driver, 10) \
            .until(expected_conditions.visibility_of_element_located(
            (By.LINK_TEXT, '立即邀请')
        )
        )

    def add_member(self, memeber: Member):
        # 如果控件发生了变化或者重绘，需要显式等待合理的状态
        self.click(By.LINK_TEXT, '添加成员')
        allure.attach(body=self.driver.get_screenshot_as_png(), attachment_type=allure.attachment_type.PNG)
        self.find(By.NAME, 'username').send_keys(memeber.name)
        self.find(By.NAME, 'acctid').send_keys(memeber.account)

        mail_element = self.find(By.NAME, 'biz_mail')
        mail_element.clear()
        mail_element.send_keys(memeber.mail + Keys.ENTER)

        self.find(By.NAME, 'mobile').send_keys(memeber.phone)
        allure.attach(body=self.driver.get_screenshot_as_png(), attachment_type=allure.attachment_type.PNG)

        self.find(By.LINK_TEXT, '保存').click()
        allure.attach(body=self.driver.get_screenshot_as_png(), attachment_type=allure.attachment_type.PNG)

        WebDriverWait(self.driver, 10) \
            .until(expected_conditions.visibility_of_element_located(
            (By.LINK_TEXT, '立即邀请')
        )
        )
        allure.attach(body=self.driver.get_screenshot_as_png(), attachment_type=allure.attachment_type.PNG)

        return self

    def import_contact(self, path):
        return self

    def export_contact(self):
        ...

    def delete_member(self):
        return self

    def search_member(self, keyword):
        self.find(By.ID, 'memberSearchInput').send_keys(keyword)
        return MemberPage(self.driver)
