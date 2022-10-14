import requests

from geektime_0.service.petclinic.utils.log import log


class Http:
    """
    封装requests，实现通用的http处理，也为将来替换requests提供了便捷
    """
    def request(self, url, method='get', params=None, json=None, **kwargs):
        kwargs['url'] = url
        kwargs['method'] = method
        kwargs['params'] = params
        kwargs['json'] = json

        log.debug(kwargs)
        r = requests.request(**kwargs)
        # log.debug(r.text)
        log.debug(r.json())
        return r.json()
