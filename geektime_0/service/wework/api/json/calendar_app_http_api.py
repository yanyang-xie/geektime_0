from dataclasses import asdict

from geektime_0.service.wework.api.json.calendar_http_api import CalendarHttpApi
from geektime_0.service.wework.api.json.schedule_http_api import ScheduleHttpApi
from geektime_0.service.wework.framework.http import Http
from geektime_0.service.wework.model.calendar_app_api import CalendarAppApi
from geektime_0.service.wework.model.calendar_app_model import CalendarAppModel
from geektime_0.service.wework.model.calendar_model import CalendarModel


class CalendarAppHttpApi(CalendarAppApi):
    def __init__(self):

        super().__init__()
        self.http = Http()


    def refresh_token(self, app: CalendarAppModel):
        r = self.http.request(
            url='https://qyapi.weixin.qq.com/cgi-bin/gettoken',
            params={
                'corpid': app.corpid,
                'corpsecret': app.secret
            }
        )
        self.set_token(r['access_token'])


    def add_calendar(self, calendar: CalendarModel):
        r = self.http.request(
            url='https://qyapi.weixin.qq.com/cgi-bin/oa/calendar/add',
            method='post',
            params={'access_token': self.get_token()},
            json={'calendar': asdict(calendar)}
        )
        return r

    def list(self):
        "企业微信未提供获取已有日历列表的功能，所以我们暂时无法及时清理日历。"
        ...

    def get_calendar(self, calendar_id=''):
        return CalendarHttpApi(self, calendar_id)

    def get_schedule(self, schedule_id):
        return ScheduleHttpApi(self, schedule_id)
