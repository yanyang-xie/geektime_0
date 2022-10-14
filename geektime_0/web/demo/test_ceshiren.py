import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from geektime_0.web.demo.ceshiren import Ceshiren


class TestCeshirenSearch:
    def setup_class(self):
        self.ceshiren = Ceshiren()
        self.ceshiren.open()

    def setup(self):
        self.search=self.ceshiren.open_search()

    def teardown(self):
        self.search.clear_search()

    def teardown_class(self):
        self.ceshiren.close()

    @pytest.mark.parametrize("keyword", [
        'selenium',
        'appium',
        'requests'
    ])
    def test_search(self, keyword):
        assert keyword in self.search.search(keyword)

    @pytest.mark.parametrize("keyword", [
        'requests'
    ])
    def test_search_service(self, keyword):
        assert keyword in self.search.search(keyword)

