from geektime_0.service.petclinic.api.owner import Owner
from geektime_0.service.petclinic.api.owners import Owners
from copy import copy

from geektime_0.service.petclinic.tests.test_data import owner_common
from geektime_0.service.petclinic.tests.test_owner import TestOwner
from geektime_0.service.petclinic.utils.log import log


class TestOwnersList(TestOwner):
    def setup_class(self):
        "init"
        super(TestOwnersList, self).setup_class(self)
        log.debug("setup_class TestOwnersList")
        "在所有测试用例之前只执行一次"

        # 引入业务模型
        self.owners = Owners()

        # 清理数据
        self.owners.clear('seveniruby')
        r=self.owners.list("seveniruby")
        log.debug("list after clear")
        log.debug(r)

        # 初始化数据
        owner1 = copy(owner_common)

        self.owners.add(owner1)
        r = self.owners.list("seveniruby")
        log.debug("list after add1")
        log.debug(r)

        owner2 = copy(owner1)
        # owner2 = owner1

        owner2.firstName = 'ceshiren'

        log.debug(owner1)
        log.debug(owner2)

        self.owners.add(owner2)
        r = self.owners.list("seveniruby")
        log.debug("list after 2")
        log.debug(r)

    def setup(self):
        "在每个测试用例之前执行一次"
        "setup"

    def teardown(self):
        "teardown"

    def teardown_class(self):
        "teardown class clear"

        # 可能会因为进程被强制终止，导致teardown_class得不到执行
        self.owners.clear('seveniruby')

    def test_search_query_null(self):
        r = self.owners.list("")
        assert len(r) > 0

    def test_search_result_null(self):
        r = self.owners.list("ceshiren.com")
        assert r == []
        ...

    def test_search_result_single(self):
        r = self.owners.list("black")
        assert len(r) == 1
        assert r[0].lastName.lower() == 'black'
        ...

    def test_search_result_multi(self):
        r = self.owners.list('seveniruby')
        log.debug("test_search_result_multi")
        log.debug(r)
        assert len(r) == 2
