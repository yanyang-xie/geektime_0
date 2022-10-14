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

caps = {}
caps["platformName"] = "android"
caps["appium:ensureWebviewsHavePages"] = True
caps["appium:nativeWebScreenshot"] = True
caps["appium:newCommandTimeout"] = 3600
caps["appium:connectHardwareKeyboard"] = True

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)

el1 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Clock")
el1.click()
el2 = driver.find_element(by=AppiumBy.XPATH, value="//xk[@content-desc=\"Alarm\"]/android.widget.TextView")
el2.click()
el3 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Add alarm")
el3.click()
el4 = driver.find_element(by=AppiumBy.ID, value="android:id/button1")
el4.click()
el5 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Ringtone Default (Cesium)")
el5.click()
el6 = driver.find_element(by=AppiumBy.ID, value="com.google.android.deskclock:id/dismiss")
el6.click()
driver.back()
el7 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="No label specified")
el7.click()
el8 = driver.find_element(by=AppiumBy.ID, value="com.google.android.deskclock:id/label_input_field")
el8.send_keys("ceshiren.com")
el9 = driver.find_element(by=AppiumBy.ID, value="android:id/button1")
el9.click()

driver.quit()