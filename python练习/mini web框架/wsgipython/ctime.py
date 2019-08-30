import time


def application(env, start_response):
    # 状态码
    status = "200 OK"
    # headers决定返回文件的类型
    headers = [
        ("Content_Type", "text/plain")
    ]
    # 返回给服务器以构成起始行和响应头
    start_response(status, headers)
    # 作为响应体返回给服务器
    return time.ctime()
''' 

env 用户的请求信息 为字典 键值
start_response 函数，服务器提供,参数为状态码和响应头

'''