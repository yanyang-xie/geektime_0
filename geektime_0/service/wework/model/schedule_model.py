from dataclasses import dataclass
from datetime import datetime, timedelta

now = datetime.now()


@dataclass
class ScheduleModel:
    schedule_id: str = None
    organizer: str = None
    summary: str = None
    start_time: int = int(now.timestamp())
    end_time: int = int((now + timedelta(hours=1)).timestamp())
