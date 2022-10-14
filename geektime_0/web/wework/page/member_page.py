from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from geektime_0.web.wework.framework.base_page import BasePage
from geektime_0.web.wework.page.member import Member


class MemberPage(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)

        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(
                (By.CLASS_NAME, 'member_display_cover_detail_name')))

    def get_name(self):
        ...

    def get_account(self):
        ...

    def save_member(self, member):
        ...

    def get_member(self):
        member = Member()
        member.name = self.find(
            By.CLASS_NAME, 'member_display_cover_detail_name').text

        member.account = self.driver.find_elements(
            By.CSS_SELECTOR, '.member_display_cover_detail_bottom')[1].text.replace('帐号：', '')

        member.mail = self.find(
            By.CSS_SELECTOR, '.member_display_item_Email .member_display_item_right').text

        member.phone = self.find(
            By.CSS_SELECTOR,
            '.member_display_item_Phone .member_display_item_right').text

        # .member_display_item_Phone .member_display_item_right
        # //*[contains(@class, "member_display_item_Phone")]//*[contains(@class, "member_display_item_right")]

        return member
