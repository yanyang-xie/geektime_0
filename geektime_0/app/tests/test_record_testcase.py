# This sample code uses the Appium python client v2
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

# For W3C actions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput


class TestRecordTestCase:
    def setup_class(self):
        caps = {}
        caps["platformName"] = "android"
        caps['appPackage'] = 'com.google.android.deskclock'
        caps['appActivity'] = 'com.android.deskclock.DeskClock'

        caps["appium:ensureWebviewsHavePages"] = True
        caps["appium:nativeWebScreenshot"] = True
        caps["appium:newCommandTimeout"] = 3600
        caps["appium:connectHardwareKeyboard"] = True

        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
        self.driver.implicitly_wait(5)

    def setup(self):
        ...

    def test_add_clarm(self):
        com = "ceshiren.com"
        self.driver.find_element(by=AppiumBy.XPATH,
                                 value="//xk[@content-desc=\"Alarm\"]/android.widget.TextView").click()
        self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Add alarm").click()
        # self.driver.find_element(by=AppiumBy.ID, value="android:id/button1").click()
        self.driver.find_element(by=AppiumBy.CSS_SELECTOR, value="android.widget.Button[text=OK]").click()

        self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Ringtone Default (Cesium)").click()
        self.driver.find_element(by=AppiumBy.ID, value="com.google.android.deskclock:id/dismiss").click()
        self.driver.back()
        self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="No label specified").click()

        self.driver.find_element(by=AppiumBy.ID, value="com.google.android.deskclock:id/label_input_field").send_keys(
            com)
        self.driver.find_element(by=AppiumBy.ID, value="android:id/button1").click()
        assert com in self.driver.find_element(by=AppiumBy.ID, value='com.google.android.deskclock:id/edit_label').text

    def teardown(self):
        ...

    def teardown_class(self):
        ...
        # self.driver.quit()
