import pytest

from geektime_0.service.wework.api.json.calendar_app_http_api import CalendarAppHttpApi
from geektime_0.service.wework.model.calendar_app_api import CalendarAppApi
from geektime_0.service.wework.model.calendar_app_model import CalendarAppModel
from geektime_0.service.wework.model.calendar_model import CalendarModel
from geektime_0.service.wework.model.schedule_model import ScheduleModel
from geektime_0.service.wework.utils import project_dir
from geektime_0.service.wework.utils.data import Data


class TestSchedule:
    def setup_class(self):
        calendar_app_model = CalendarAppModel()

        # 实现
        self.calendar_app_api = CalendarAppHttpApi()

        # 抽象
        # self.calendar_app_api = CalendarAppApi()

        self.calendar_app_api.refresh_token(calendar_app_model)

        data_file = project_dir('data/calendar.yaml')
        calendar_data = Data.load_yaml(data_file)
        calendar_model = CalendarModel(**calendar_data)
        self.calendar_api = self.calendar_app_api.get_calendar(calendar_model.cal_id)

    def teardown_class(self):
        r = self.calendar_api.list_schedules()
        for item in r:
            self.calendar_app_api.get_schedule(item.schedule_id).delete()

    @pytest.mark.parametrize("schedule_data", [
        {'summary': 'demo schedule 1', 'organizer': 'sihan'},
        {'summary': 'demo schedule 2', 'organizer': 'sihan'}
    ])
    def test_add(self, schedule_data):
        schedule = ScheduleModel(**schedule_data)
        schedule_id = self.calendar_api.add_schedule(schedule)
        schedule2 = self.calendar_app_api.get_schedule(schedule_id).get_model()
        schedule2.schedule_id = None
        assert schedule == schedule2

    @pytest.mark.parametrize("schedule_data", [
        {'summary': 'demo schedule delete', 'organizer': 'sihan'}
    ])
    def test_delete(self, schedule_data):
        # 删除可以不走新建，用提前初始化的日程列表id代替
        schedule = ScheduleModel(**schedule_data)
        schedule_id = self.calendar_api.add_schedule(schedule)
        schedule2 = self.calendar_app_api.get_schedule(schedule_id)
        r = schedule2.delete()
        assert r['errcode'] == 0
        # todo: 可以通过查询默认日历下的日程是否还在进一步判断，但是因为企业微信的api有问题，导致无法查询
