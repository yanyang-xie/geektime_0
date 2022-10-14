from geektime_0.service.wework.model.calendar_app_model import CalendarAppModel
from geektime_0.service.wework.model.calendar_model import CalendarModel


class CalendarAppApi:
    """
    代表应用本身提供的功能
    """

    def __init__(self, ):
        self._access_token = None

    def refresh_token(self, app: CalendarAppModel):
        ...

    def get_token(self):
        return self._access_token

    def set_token(self, token):
        self._access_token = token

    def add_calendar(self, calendar: CalendarModel):
        ...

    def list(self, *calendar_id_list):
        ...

    def get_calendar(self, calendar_id):
        ...
