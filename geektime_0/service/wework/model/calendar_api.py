from dataclasses import dataclass

from geektime_0.service.wework.model.calendar_app_api import CalendarAppApi
from geektime_0.service.wework.model.calendar_model import CalendarModel
from geektime_0.service.wework.model.schedule_model import ScheduleModel


@dataclass
class CalendarApi:
    """
    提供业务的行为定义
    """

    def __init__(self, app: CalendarAppApi, calendar_id: str):
        self.app = app
        self.cal_id = calendar_id

    @classmethod
    def add(cls, calendar: CalendarModel):
        ...

    def update(self, calendar: CalendarModel):
        ...

    def delete(self):
        ...

    @classmethod
    def list(cls):
        ...

    def add_schedule(self, schedule: ScheduleModel):
        ...

    def list_schedules(self):
        ...
