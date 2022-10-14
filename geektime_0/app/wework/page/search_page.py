from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.remote.webdriver import WebDriver

from geektime_0.app.wework.page.base_page import BasePage
from geektime_0.app.wework.utils.log import log


class SearchPage(BasePage):

    def search(self, keyword) -> list[dict]:
        # resource-id被混淆 混淆工具本身会提供对应关系的  convert('search_button') = j65
        # content-desc resource-id xpath 研发用的测试框架同样也需要定位 cypress playwright
        self.find(AppiumBy.ID, 'j65').send_keys(keyword)
        result_list = []

        for item in self.driver.find_elements(AppiumBy.ID, 'ezy'):
            r = {}
            cul_list = item.find_elements(AppiumBy.ID, 'cul')
            if len(cul_list) == 0:
                r['type'] = 'app'
            else:
                r['desc'] = cul_list[0].text
                if '包含' in r['desc']:
                    r['type'] = 'group'
                elif '相关聊天记录' in r['desc']:
                    r['type'] = 'chat'
                else:
                    r['type'] = 'contact'

            r['name'] = item.find_element(AppiumBy.XPATH,
                                          '//*[contains(@resource-id, "g9n") or contains(@label, "ios") ]/*[contains(@class, "Text")]').text
            result_list.append(r)

        # for item in self.driver.find_elements(AppiumBy.XPATH,
        #                                       '//*[contains(@resource-id, "g9n")]/*[contains(@class, "Text")]'):
        #     r = {'name': item.text}
        #     result_list.append(r)
        # r['name'] = self.find(AppiumBy.ID, 'g9n')\
        #     .find_element(AppiumBy.CLASS_NAME, 'android.widget.TextView').text

        log.debug(result_list)

        return result_list

    def search_app(self, keyword) -> list[dict]:
        ...

    def clear_search(self):
        self.find(AppiumBy.ID, 'j64').click()
