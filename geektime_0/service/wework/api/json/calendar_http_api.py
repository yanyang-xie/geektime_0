from dataclasses import asdict

from geektime_0.service.wework.api.json.schedule_http_api import ScheduleHttpApi
from geektime_0.service.wework.framework.http import Http
from geektime_0.service.wework.model.calendar_api import CalendarApi
from geektime_0.service.wework.model.calendar_app_api import CalendarAppApi
from geektime_0.service.wework.model.calendar_model import CalendarModel
from geektime_0.service.wework.model.schedule_model import ScheduleModel


class CalendarHttpApi(CalendarApi):

    def __init__(self, app: CalendarAppApi, calendar_id: str):
        super().__init__(app, calendar_id)
        self.http = Http()

    def add_schedule(self, schedule: ScheduleModel):
        data = asdict(schedule)
        data['cal_id'] = self.cal_id

        r = self.http.request(
            url='https://qyapi.weixin.qq.com/cgi-bin/oa/schedule/add',
            method='post',
            params={'access_token': self.app.get_token()},
            json={'schedule': data}
        )
        return r['schedule_id']

    def add(cls, calendar: CalendarModel):
        ...

    def get_calendar(self):
        r = self.http.request(
            url='https://qyapi.weixin.qq.com/cgi-bin/oa/calendar/get',
            method='post',
            params={'access_token': self.app.get_token()},
            json={'cal_id_list': [self.cal_id]}
        )
        raw = r['calendar_list'][0]

        calendar = CalendarModel()
        calendar.cal_id = raw['cal_id']
        calendar.color = raw['color']
        calendar.summary = raw['summary']
        calendar.shares = raw['shares']
        calendar.organizer = raw['organizer']

        return calendar

    def list_schedules(self):
        r = self.http.request(
            url='https://qyapi.weixin.qq.com/cgi-bin/oa/schedule/get_by_calendar',
            method='post',
            params={'access_token': self.app.get_token()},
            json={'cal_id': self.cal_id}
        )

        return [ScheduleHttpApi.get_model_from_dict(item) for item in r['schedule_list']]
