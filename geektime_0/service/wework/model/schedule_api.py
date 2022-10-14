from dataclasses import dataclass

from geektime_0.service.wework.model.calendar_app_api import CalendarAppApi
from geektime_0.service.wework.model.schedule_model import ScheduleModel


@dataclass
class ScheduleApi:

    def __init__(self, app: CalendarAppApi, schedule_id):
        self.schedule_id = schedule_id
        self.app = app

    def get_model(self):
        ...

    def update(self, schedule: ScheduleModel):
        ...

    def delete(self):
        ...

    def del_attendees(self):
        ...
