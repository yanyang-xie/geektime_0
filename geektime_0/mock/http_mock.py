from mitmproxy import http


def request(flow: http.HTTPFlow):
    flow.request.headers["myheader"] = "value"
    flow.request.query["q"]="appium"
    # flow.request.headers["Host"] = "seveniruby.com"
    # flow.request.method = "POST"
    # flow.request.path = "/search?expanded=true&q=geektime"


def response(flow: http.HTTPFlow):
    # request => json
    # filter => jsonpath xpath regex $.a
    # response => jsonpath $.a.b=8

    if "search" in flow.request.path and flow.request.query.get("q") == "appium":
        flow.response.text = flow.response.text.replace("appium", "mock")

