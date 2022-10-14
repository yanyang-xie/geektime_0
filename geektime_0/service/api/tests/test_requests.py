import requests
from jsonpath import jsonpath

proxies = {
    'http': 'http://127.0.0.1:8080',
    'https': 'http://127.0.0.1:8080',
}


def test_get():
    r = requests.get('https://httpbin.ceshiren.com/get', params={"a": 1, "b": 2})
    assert r.status_code == 200


def test_post_form():
    r = requests.post(
        url='https://httpbin.ceshiren.com/post',
        params={'a': 1, 'b': '2'},
        data={'f1': 1, 'f2': 2},
        headers={'header1': 'header  demo'},
        proxies=proxies,
        verify=False
    )
    assert r.status_code == 200
    print(r.json())


def test_post_data():
    r = requests.post(
        url='https://httpbin.ceshiren.com/post',
        params={'a': 1, 'b': '2'},
        data="dddd",
        headers={'header1': 'header  demo'},
        proxies=proxies,
        verify=False
    )
    assert r.status_code == 200
    print(r.json())


def test_post_json():
    r = requests.post(
        url='https://httpbin.ceshiren.com/post',
        params={'a': 1, 'b': '2'},
        json={'f1': 1, 'f2': 2},
        headers={'header1': 'header  demo'},
        proxies=proxies,
        verify=False
    )
    assert r.status_code == 200
    print(r.json())


def test_login():
    r = requests.post(
        'https://litemall.hogwarts.ceshiren.com/admin/auth/login',
        headers={'Origin': 'https://litemall.hogwarts.ceshiren.com'},
        cookies={'cookie1': 'cookie1 value'},
        json={
            'username': 'admin123',
            'password': 'admin123',
            'code': ''
        },
        proxies=proxies,
        verify=False
    )
    assert r.status_code == 200
    print(r.text)
    assert r.json()['errmsg'] == '成功'
    assert r.json()['data']['adminInfo']['nickName'] == 'admin123'


def test_user_list():
    r = requests.get(
        'https://litemall.hogwarts.ceshiren.com/admin/user/list?page=1&limit=20&sort=add_time&order=desc',
        cookies={'X-Litemall-Admin-Token': 'ff8d541c-7506-4210-8874-a518be8d0a6d'},
        headers={'X-Litemall-Admin-Token': 'ff8d541c-7506-4210-8874-a518be8d0a6d'}

    )
    assert r.status_code == 200

    print(r.text)


def test_category():
    r = requests.get(
        'https://ceshiren.com/categories.json'
    )
    assert r.status_code == 200
    print(r.text)
    assert r.json()['category_list']['categories'][0]['name'] == '提问区'
    assert '霍格沃兹答疑区' in jsonpath(r.json(), '$..name')
