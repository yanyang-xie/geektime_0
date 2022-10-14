from geektime_0.service.api.api.mall import Mall


class TestMall:
    def setup_class(self):
        print("suite 数据初始化 setup_class()")
        self.mall = Mall()

    def setup(self):
        print("case级别初始化 setup()")

    def test_login(self):
        r = self.mall.login("admin123", 'admin123', '')
        assert r.status_code == 200
        print(r.text)
        assert r.json()['errmsg'] == '成功'
        assert r.json()['data']['adminInfo']['nickName'] == 'admin123'

    def test_login_fail(self):
        r = self.mall.login('admin123', 'wrong', '')
        assert r.status_code == 200
        print(r.text)
        assert r.json()['errmsg'] == '用户帐号或密码不正确'

    def teardown(self):
        print("case teardown()")

    def teardown_class(self):
        print("suite 数据清理 teardown_class()")
