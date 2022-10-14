from geektime_0.service.wework.api.json.calendar_http_api import CalendarHttpApi
from geektime_0.service.wework.api.rpc.calendar_rpc_api import CalendarRpcApi
from geektime_0.service.wework.api.xml.calendar_xml_api import CalendarXMLApi
from geektime_0.service.wework.model.calendar_api import CalendarApi
from geektime_0.service.wework.model.calendar_app_api import CalendarAppApi


class CalendarApiFactory:
    @classmethod
    def create(cls, automation, app: CalendarAppApi, calendar_id: str):
        if automation == 'json':
            return CalendarHttpApi(app, calendar_id)
        elif automation == 'xml':
            return CalendarXMLApi(app, calendar_id)
        elif automation == 'grpc':
            return CalendarRpcApi(app, calendar_id)
        else:
            return CalendarApi(app, calendar_id)
