from dataclasses import asdict
from typing import List

from geektime_0.service.petclinic.api.owner import Owner
from geektime_0.service.petclinic.framework.http import Request
from geektime_0.service.petclinic.utils.log import log


class Owners:
    def list(self, lastName) -> List[Owner]:

        # GET https://spring-petclinic-rest.k8s.hogwarts.ceshiren.com/petclinic/api/owners?lastName=seveniruby HTTP/1.1
        # GET https://spring-petclinic-rest.k8s.hogwarts.ceshiren.com/petclinic/api/owners?lastName=seveniruby HTTP/1.1
        # r = requests.get(
        #     'https://spring-petclinic-rest.k8s.hogwarts.ceshiren.com/petclinic/api/owners',
        #     params={'lastName': lastName},
        #     proxies={
        #         'http': 'http://127.0.0.1:8080',
        #         'https': 'http://127.0.0.1:8080'
        #     },
        #     verify=False
        #
        # )

        # https://spring-petclinic-rest.k8s.hogwarts.ceshiren.com/petclinic/api/owners
        # https://spring-petclinic-rest.k8s.hogwarts.ceshiren.com/petclinic/api/owners?lastName=seveniruby
        # https://spring-petclinic-rest.k8s.hogwarts.ceshiren.com/petclinic/api/owners??lastName=seveniruby
        #
        request = Request()
        request.host = 'https://spring-petclinic-rest.k8s.hogwarts.ceshiren.com'
        # request.host = 'http://127.0.0.1:7777'
        request.path = '/petclinic/api/owners'
        request.method = 'get'
        request.query = {'lastName': lastName}
        r = request.send()

        if r.status_code == 200:
            owner_list = []
            for item in r.json():
                if isinstance(item, dict):
                    item.pop('pets')
                    owner = Owner(**item)
                    owner_list.append(owner)
            return owner_list
        else:
            return []

    def add(self, owner):
        # r = requests.post(
        #     'https://spring-petclinic-rest.k8s.hogwarts.ceshiren.com/petclinic/api/owners',
        #     json=asdict(owner)
        # )

        request = Request()
        request.host = 'https://spring-petclinic-rest.k8s.hogwarts.ceshiren.com'
        request.path = '/petclinic/api/owners'
        request.method = 'post'
        request.type = 'json'
        request.data = asdict(owner)
        r = request.send()

        log.debug(r.status_code)
        log.debug(r.text)
        return r

    def update(self, owner):
        ...

    def delete(self, owner_id):
        log.debug('delete')
        # r = requests.request(
        #     'delete',
        #     f'https://spring-petclinic-rest.k8s.hogwarts.ceshiren.com/petclinic/api/owners/{owner_id}',
        # )
        #
        request=Request()
        request.method='delete'
        request.host='https://spring-petclinic-rest.k8s.hogwarts.ceshiren.com'
        request.path=f'/petclinic/api/owners/{owner_id}'
        r=request.send()


        log.debug(r)
        log.debug(r.text)
        return r

    def clear(self, lastName):
        for item in self.list(lastName):
            log.debug(item)
            log.debug('delete')
            self.delete(item.id)
