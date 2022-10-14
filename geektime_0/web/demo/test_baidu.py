from selenium import webdriver
from selenium.webdriver.common.by import By


class TestSelenium:
    def setup_class(self):
        self.driver = webdriver.Chrome()

    def test_upload(self):
        self.driver.get('http://www.baidu.com/')

        # self.driver.find_element(By.CLASS_NAME, 'soutu-btn').click()
        # self.driver.find_element(By.CLASS_NAME, 'upload-pic') \
        #     .send_keys('/Users/seveniruby/Dropbox/sihanjishu/startup/霍格沃兹测试学院/banner/通用素材/学院长方形banner.png')
    def teardown_class(self):
        self.driver.close()
