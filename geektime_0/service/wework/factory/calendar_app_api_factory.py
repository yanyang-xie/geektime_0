from geektime_0.service.wework.api.json.calendar_app_http_api import CalendarAppHttpApi
from geektime_0.service.wework.model.calendar_app_api import CalendarAppApi


class CalendarAppApiFactory:
    @classmethod
    def create(cls, automation):
        if automation == 'json':
            return CalendarAppHttpApi()
        else:
            return CalendarAppApi()
