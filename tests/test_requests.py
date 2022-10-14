import requests


def test_form():
    payload = {'key1': 'value1', 'key2': 'value2'}
    r = requests.post("http://127.0.0.1:7777/post", data=payload)


def test_auth():
    r = requests.get('https://httpbin.ceshiren.com/basic-auth/admin/password', auth=('admin', 'password'))
    assert r.status_code == 200


def test_pet_post():
    r=requests.post('http://docker.hogwarts.ceshiren.com:9966/petclinic/api/owners', json={
        "address": "address demo",
        "city": "city demo",
        "firstName": "firstName demo",
        'lastName': 'lastName demo',
        'telephone': '0123456789'
    })

    print(r)
