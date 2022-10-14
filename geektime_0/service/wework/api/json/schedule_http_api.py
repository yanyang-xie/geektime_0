from geektime_0.service.wework.framework.http import Http
from geektime_0.service.wework.model.calendar_app_api import CalendarAppApi
from geektime_0.service.wework.model.schedule_api import ScheduleApi
from geektime_0.service.wework.model.schedule_model import ScheduleModel


class ScheduleHttpApi(ScheduleApi):
    def __init__(self, app: CalendarAppApi, schedule_id):
        super().__init__(app, schedule_id)
        self.http = Http()

    @classmethod
    def get_model_from_dict(cls, raw: dict):
        schedule = ScheduleModel()
        schedule.summary = raw['summary']
        schedule.start_time = raw['start_time']
        schedule.end_time = raw['end_time']
        schedule.organizer = raw['organizer']
        schedule.schedule_id = raw['schedule_id']
        return schedule

    def get_model(self):
        r = self.http.request(
            url='https://qyapi.weixin.qq.com/cgi-bin/oa/schedule/get',
            method='post',
            params={'access_token': self.app.get_token()},
            json={
                'schedule_id_list': [self.schedule_id]
            }
        )

        raw = r['schedule_list'][0]
        schedule = self.get_model_from_dict(raw)

        return schedule

    def delete(self):
        r = self.http.request(
            url='https://qyapi.weixin.qq.com/cgi-bin/oa/schedule/del',
            method='post',
            params={'access_token': self.app.get_token()},
            json={'schedule_id': self.schedule_id}
        )
        return r
