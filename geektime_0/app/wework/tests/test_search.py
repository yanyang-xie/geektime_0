import pytest

from geektime_0.app.wework.page.wework_app import WeWorkApp
from geektime_0.app.wework.utils.log import log


class TestSearch():
    def setup_class(self):
        self.search_app = WeWorkApp()
        self.search_page = self.search_app.search()

    def setup(self):
        ...

    def teardown(self):
        self.search_page.clear_search()

    def teardown_class(self):
        self.search_app.close()

    @pytest.mark.parametrize('keyword, expect', [
        ('seveniruby', 'seveniruby'),
        ('sihan', '思寒'),
        ('hogwarts', 'hogwarts'),
    ])
    def test_search_contact(self, keyword, expect):
        r = self.search_page.search(keyword)
        contact_list = [item for item in r if item['type'] == 'contact']
        assert expect in contact_list[0]['name']

    @pytest.mark.parametrize('keyword, expect', [
        ('seveniruby', 'seveniruby'),
        ('demo', 'demo'),
        ('dishiqi', '第十期'),
    ])
    def test_search_contact(self, keyword, expect):
        r = self.search_page.search(keyword)
        app_list = [item for item in r if item['type'] == 'app']
        assert expect in app_list[0]['name']

    @pytest.mark.parametrize('keyword, expect', [
        ('hogwarts.ceshiren.com', '')
    ])
    def test_search_contact_null(self, keyword, expect):
        r = self.search_page.search(keyword)
        contact_list = [item for item in r if item['type'] == 'contact']
        # Hamcrest https://github.com/hamcrest/PyHamcrest
        assert len(contact_list) == 0
