import base64
import json
from dataclasses import dataclass, field

import requests
import yaml
from requests import Response as RequestsResponse

from geektime_0.service.petclinic.utils.data import Data
from geektime_0.service.petclinic.utils.log import log


@dataclass
class Request:
    method: str = None
    host: str = None
    path: str = None
    query: dict = None
    headers: dict = field(default_factory=dict)
    type: str = 'json'
    data: dict = None

    def send(self):
        # 实现requests库的便捷封装或者替换

        #多套环境
        env = Data.load_yaml('data/env.yaml')
        self.host = env[env['default']]

        #token处理
        # self.headers['token']=token

        raw = None

        if self.type == 'json':
            self.headers['Content-Type'] = 'application/json'
            if self.data is None:
                raw = None
            else:
                raw = json.dumps(self.data)
                # 加密
                # raw=base64.encodestring(raw)
        elif self.type == 'xml':
            # 数据格式处理
            ...
        elif self.type == 'form':
            ...
        else:
            raise Exception("not exist format " + self.type)

        log.debug(self)
        requests_response = requests.request(
            method=self.method,
            url=self.host + self.path,
            params=self.query,
            headers=self.headers,
            data=raw,
            auth=None,
            # proxies={
            #     'http': 'http://127.0.0.1:8080',
            #     'https': 'http://127.0.0.1:8080'
            # },
            verify=False
        )
        log.debug(requests_response)
        log.debug(requests_response.text)
        r = Response(requests_response)
        log.debug(r)
        return r


@dataclass
class Response:
    # def __int__(self, urllib):
    #     ...
    def __init__(self, requests_response):
        self.r: RequestsResponse = requests_response

    def json(self):
        return self.r.json()

    def data(self) -> dict:
        return json.loads(base64.decode(self.r.text))

    @property
    def text(self):
        return self.r.text

    @property
    def status_code(self):
        return self.r.status_code
