import json

from mitmproxy import http

def response(flow: http.HTTPFlow):
    # data=json.loads(flow.response.text)
    # data['xxx']['xxx']=10
    # flow.response.text=json.dumps(data)
    flow.response.text=flow.response.text.replace(":-", ":")
