import pytest

from geektime_0.service.petclinic.utils.log import log
from geektime_0.service.wework.api.json.calendar_app_http_api import CalendarAppHttpApi
from geektime_0.service.wework.model.calendar_app_api import CalendarAppApi
from geektime_0.service.wework.model.calendar_app_model import CalendarAppModel
from geektime_0.service.wework.model.calendar_model import CalendarModel
from geektime_0.service.wework.utils import project_dir
from geektime_0.service.wework.utils.data import Data


class TestCalendar:
    def setup_class(self):
        calendar_app_model = CalendarAppModel()
        self.calendar_app_api = CalendarAppApi()
        # self.calendar_app_api = CalendarAppHttpApi()
        self.calendar_app_api.refresh_token(calendar_app_model)

        data_file = project_dir('data/calendar.yaml')
        calendar_data = Data.load_yaml(data_file)
        self.calendar_model = CalendarModel(**calendar_data)
        self.calendar_api = self.calendar_app_api.get_calendar(self.calendar_model.cal_id)

    @pytest.mark.parametrize("calendar_data", [
        {'summary': 'demo1', 'color': '#000000', 'organizer': 'sihan'},
        {'summary': 'demo2', 'color': '#FFFFFF', 'organizer': 'sihan'}
    ])
    def test_add(self, calendar_data):
        calendar = CalendarModel(**calendar_data)
        r = self.calendar_app_api.add_calendar(calendar)
        assert r['errcode'] == 0

        calendar_id = r['cal_id']
        calendar2 = self.calendar_app_api.get_calendar(calendar_id).get_calendar()
        # 排除cal_id 比对剩下的关键字段
        calendar2.cal_id = None
        assert calendar == calendar2

    def test_list(self):
        calendar_data = self.calendar_app_api.get_calendar(self.calendar_model.cal_id).get_calendar()
        log.debug(calendar_data)
