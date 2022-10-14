from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

from geektime_0.app.wework.page.base_page import BasePage
from geektime_0.app.wework.page.contact_page import ContactPage
from geektime_0.app.wework.page.search_page import SearchPage


class WeWorkApp(BasePage):
    def __init__(self):
        super().__init__()
        caps = {
            "platformName": "android",
            "appium:appPackage": "com.tencent.wework",
            "appium:appActivity": "com.tencent.wework.launch.LaunchSplashActivity",
            "appium:noReset": "true",
            "unicodeKeyboard": True,
            'resetKeyboard': True,

        }
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
        self.driver.implicitly_wait(10)

    def search(self):
        self.find(AppiumBy.ID, 'kuo').click()

        return SearchPage(self.driver)


    def contact(self):
        self.find(AppiumBy.CSS_SELECTOR, '[text="通讯录"]').click()
        return ContactPage(self.driver)

    def close(self):
        self.driver.quit()
