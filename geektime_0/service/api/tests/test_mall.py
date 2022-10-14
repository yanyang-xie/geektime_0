import requests


class TestMall:
    def setup_class(self):
        print("suite 数据初始化 setup_class()")

    def setup(self):
        print("case级别初始化 setup()")

    def test_login(self):
        r = requests.post(
            'https://litemall.hogwarts.ceshiren.com/admin/auth/login',
            headers={'Origin': 'https://litemall.hogwarts.ceshiren.com'},
            cookies={'cookie1': 'cookie1 value'},
            json={
                'username': 'admin123',
                'password': 'admin123',
                'code': ''
            },
        )
        assert r.status_code == 200
        print(r.text)
        assert r.json()['errmsg'] == '成功'
        assert r.json()['data']['adminInfo']['nickName'] == 'admin123'

    def test_login_fail(self):
        r = requests.post(
            'https://litemall.hogwarts.ceshiren.com/admin/auth/login',
            headers={'Origin': 'https://litemall.hogwarts.ceshiren.com'},
            cookies={'cookie1': 'cookie1 value'},
            json={
                'username': 'admin123',
                'password': 'wrong',
                'code': ''
            },
        )
        assert r.status_code == 200
        print(r.text)
        assert r.json()['errmsg'] == '用户帐号或密码不正确'

    def teardown(self):
        print("case teardown()")

    def teardown_class(self):
        print("suite 数据清理 teardown_class()")
