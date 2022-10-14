import requests
from requests import Response


class Mall:
    def login(self, username, password, code) -> Response:
        r = requests.post(
            'https://litemall.hogwarts.ceshiren.com/admin/auth/login',
            headers={'Origin': 'https://litemall.hogwarts.ceshiren.com'},
            cookies={'cookie1': 'cookie1 value'},
            json={
                'username': username,
                'password': password,
                'code': code
            },
        )
        return r

    def list_users(self):
        pass

    def list_orders(self):
        pass

    def logout(self):
        pass
