import datetime
from time import sleep

from geektime_0.service.petclinic.utils.log import log


class TestOwner():
    loaded = False

    def setup_class(self):
        if not TestOwner.loaded:
            log.debug(f"setup_class TestOwner {datetime.datetime.now()}")
            sleep(1)
            TestOwner.loaded = True
