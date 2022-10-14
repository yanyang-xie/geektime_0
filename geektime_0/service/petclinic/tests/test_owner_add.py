import pytest

from geektime_0.service.petclinic.api.owner import Owner
from geektime_0.service.petclinic.api.owners import Owners
from copy import copy

from geektime_0.service.petclinic.tests.test_data import owner_common
from geektime_0.service.petclinic.tests.test_owner import TestOwner
from geektime_0.service.petclinic.utils.log import log


class TestOwnersAdd(TestOwner):
    def setup_class(self):
        super(TestOwnersAdd, self).setup_class(self)
        log.debug("setup_class TestOwnersAdd")
        "init"
        "在所有测试用例之前只执行一次"

        # 引入业务模型
        self.owners = Owners()

        # 清理数据
        self.owners.clear('seveniruby')

    def setup(self):
        "在每个测试用例之前执行一次"
        "setup"

    def teardown(self):
        "teardown"

    def teardown_class(self):
        "teardown class clear"

        # 可能会因为进程被强制终止，导致teardown_class得不到执行
        self.owners.clear('seveniruby')

    @pytest.mark.parametrize("owner", [
        {'telephone': '6085551023', 'city': 'xx'},
        {'telephone': '6085551023', 'city': 'x'},
        {'telephone': '6085551023', 'city': 'xxxx'},
        {'telephone': '6085551023', 'city': 'ff  xxx'},
        # {'telephone': '', 'firstName': 'hogwarts'},
    ])
    def test_add_success(self, owner):
        # 初始化数据
        owner1 = Owner(**owner)
        owner1.address = '110 W. Liberty St.'
        owner1.firstName = 'hogwarts'
        owner1.lastName = 'seveniruby'

        r = self.owners.add(owner1)
        assert r.status_code == 201

    @pytest.mark.parametrize("owner", [
        {'telephone': '6085551023', 'firstName': ''},
        {'telephone': '6085551023', 'firstName': '11'},
        {'telephone': '6085551023', 'firstName': '1a'},
        {'telephone': '', 'firstName': 'hogwarts'},
        {'telephone': 'abfsfef', 'firstName': 'fffffff'},
    ])
    def test_add_fail(self, owner):
        # 初始化数据
        owner1 = copy(owner_common)
        owner_param = Owner(**owner)
        owner1.telephone = owner_param.telephone
        owner1.firstName = owner_param.firstName

        r = self.owners.add(owner1)
        log.debug(r.text)
        assert r.status_code != 201
        ...
