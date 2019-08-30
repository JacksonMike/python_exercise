import time
from rest_framework.throttling import SimpleRateThrottle

VISIT_RECORD = {}


class MyThrottle(object):
    """一分钟只允许访问5次"""

    def __init__(self):
        self.history = []

    def allow_request(self, request, view):
        # 获取IP地址
        ip = request.META.get("REMOTE_ADDR", "")
        print(ip)
        if ip not in VISIT_RECORD:
            VISIT_RECORD[ip] = [time.time(), ]
        else:
            history = VISIT_RECORD[ip]
            self.history = history
            history.insert(0, time.time())
            # 确保列表中一前一后的时间间隔在范围内
            while self.history[0] - self.history[-1] > 60:
                self.history.pop()
            # 判断列表长度
            if not len(self.history) <= 5:
                return False
        return True

    def wait(self):
        return 60 - (self.history[0] - self.history[-1])


"""
VISIT_RECORD = {"127.0.0.1": [1565838731.628951]}
history = []
"""


class DrfThrottle(SimpleRateThrottle):
    scope = "WD"

    def get_cache_key(self, request, view):
        return self.get_ident(request)
