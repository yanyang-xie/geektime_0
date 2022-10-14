import os

import pytest

from geektime_0.service.wework.factory.calendar_app_api_factory import CalendarAppApiFactory
from geektime_0.service.wework.model.calendar_app_model import CalendarAppModel
from geektime_0.service.wework.model.calendar_model import CalendarModel
from geektime_0.service.wework.model.schedule_model import ScheduleModel
from geektime_0.service.wework.utils import project_dir
from geektime_0.service.wework.utils.data import Data


class TestScheduleFactory:
    def setup_class(self):
        # 默认使用json实现，可以通过外部变量动态控制，方便在持续集成中运行不同的实现
        automation = os.getenv('automation', 'json')
        calendar_app_model = CalendarAppModel()
        # self.calendar_app_api = CalendarAppHttpApi()
        # 使用简单工厂方法创建对应的api
        self.calendar_app_api = CalendarAppApiFactory.create(automation)
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
