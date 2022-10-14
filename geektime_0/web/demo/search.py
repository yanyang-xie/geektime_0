import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Search:
    def __init__(self, driver):
        self.driver=driver

    def search(self, keyword) -> str:
        self.driver.find_element(By.ID, 'search-term').send_keys(keyword)
        allure.attach(body=self.driver.get_screenshot_as_png(), attachment_type=allure.attachment_type.PNG)
        self.driver.find_element(By.CSS_SELECTOR, '.searching .show-advanced-search').click()
        allure.attach(body=self.driver.get_screenshot_as_png(), attachment_type=allure.attachment_type.PNG)
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located((By.CLASS_NAME, 'topic-title'))
        )
        allure.attach(body=self.driver.get_screenshot_as_png(), attachment_type=allure.attachment_type.PNG)
        return self.driver.find_element(By.CLASS_NAME, 'topic-title').text.lower()

    def clear_search(self):
        self.driver.find_element(By.ID, 'search-button').click()
        allure.attach(body=self.driver.get_screenshot_as_png(), attachment_type=allure.attachment_type.PNG)

        self.driver.find_element(By.CSS_SELECTOR, '.searching .clear-search').click()
        allure.attach(body=self.driver.get_screenshot_as_png(), attachment_type=allure.attachment_type.PNG)

    def filter(self, tags=[], subject_type=None, range=None):
        ...
