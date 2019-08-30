#!/usr/bin/env python3
import time


HTML_ROOT_DIR = "./html"


class Application(object):
    def __init__(self, urls):
        # 设置路由表
        self.urls = urls

    def __call__(self, env, start_response):
        """使由类创建出来的对象仍然可以被调用"""
        # 获取请求资源的路径
        path = env.get("PATH_INFO", "/")
        # 如果请求资源为静态文件
        if path.startswith("/static"):
            # 提取文件名
            file_name = path[7:]
            try:
                # 判断文件是否存在
                file = open(HTML_ROOT_DIR + file_name, "rb")
            except IOError:
                # 若不存在,构造相应的起始行和响应头
                status = "404 Not Found"
                headers = []
                start_response(status, headers)
                # 返回结果为响应体
                return "Not Found"
            else:
                # 若存在,读取文件内容
                file_data = file.read()
                file.close()
                # 构造相应的起始行和响应头
                status = "200 OK"
                headers = []
                start_response(status, headers)
                # 将读取内容作为响应体,返回给服务器
                return file_data.decode("utf-8")
        # 遍历路由列表
        for url, handler in self.urls:
            # 如果请求路径和路由列表中的路径相匹配,执行相对应的功能函数,
            # 函数已经将起始行和响应头的信息返回服务器,所以只需要返回响应体
            if path == url:
                return handler(env, start_response)
        # 如若没有匹配,若不存在,构造相应的起始行和响应头
        status = "404 Not Found"
        headers = []
        start_response(status, headers)
        # 返回响应体
        return "Not Found"


def say_time(env, start_response):
    # 状态码
    status = "200 OK"
    # 响应头
    headers = [
        ("Content_Type", "text/plain")
    ]
    # 回调函数,将自身的状态码和响应头发送给服务器
    start_response(status, headers)
    # 返回结果为响应体
    return time.ctime()


def say_hi(env, start_response):
    status = "200 OK"
    headers = [
        ("Content_Type", "text/plain")
    ]
    start_response(status, headers)
    return "hello world"


# 使接口唯一
urls = [
        ("/", say_time),
        ("/sayhello", say_hi),
        ("/ctime", say_time)
    ]
# 这是一个路由列表,表中元素分别为请求资源的路径和相对应的功能函数
# 创建对象
app = Application(urls)

"""
if __name__ == '__main__':
    urls = [
        ("/", say_time),
        ("/sayhello", say_hi),
        ("/ctime", say_time)
    ]
    app = Application(urls)
    server = HTTPServer(app)
    server.bind(8000)
    server.start()
"""





