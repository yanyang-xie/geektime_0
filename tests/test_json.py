import requests
from jsonpath import jsonpath


def test_json_path():
    r = requests.get("https://ceshiren.com/categories.json")
    name_list = jsonpath(r.json(), '$.category_list.categories[0].name')
    assert name_list[0] == '提问区'
    name_list = jsonpath(r.json(), "$..name")
    assert '提问区' in name_list
