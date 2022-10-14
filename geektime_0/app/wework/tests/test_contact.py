from geektime_0.app.wework.page.wework_app import WeWorkApp


class TestContact:
    def setup_class(self):
        self.wework_app = WeWorkApp()
        self.contact_page = self.wework_app.contact()

    def setup(self):
        ...

    def teardown(self):
        ...

    def test_add_contact(self):
        # todo: 数据清理，可以适当跟接口、数据库脚本结合
        name = '15600534782'
        self.contact_page.add_contact(name, name)
        self.contact_page.back()
        r = self.wework_app.search().search(name)
        assert name in r[0]['name']
        assert 'contact' in r[0]['type']
