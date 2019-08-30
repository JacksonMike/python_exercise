from socket import *
from multiprocessing import Process
import re
import sys

# 设置静态文件的根目录
R = "./html"
# 设置动态文件的根目录
P = "./wsgipython"


class Server(object):
    def __init__(self):
        # 设立套接字
        self.server_socket = socket(AF_INET, SOCK_STREAM)
        # 端口复用
        self.server_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

    def bind(self, port):
        # 绑定端口
        self.server_socket.bind(("", port))

    def start_response(self, status, headers):
        """回调函数用来接收请求文件的数据来构造起始行和响应头"""
        # 构造起始行
        response_headers = "HTTP/1.1" + status + "\r\n"
        # 构造响应头
        for h in headers:
            response_headers += "%s :%s\r\n" % h
        self.response_headers = response_headers

    def client_handle(self, client_socket):
        # 将响应数据设为全局变量
        global response
        # 接收请求数据
        request_data = client_socket.recv(1024)
        # 将请求数据按行进行分割
        request_lines = request_data.splitlines()
        # 遍历响应数据
        for line in request_lines:
            print(line)
        # 获得起始行
        request_start_line = request_lines[0]
        # 提取文件请求文件的名字
        file_name = re.match(r"\w+\s+(/[^ ]*)\s",
                             request_start_line.decode("utf-8")).group(1)
        # 如果文件以".py"结尾
        if file_name.endswith(".py"):
            # 导入请求文件
            m = __import__(file_name[1:-3])
            # 将请求的数据和回调函数作为参数传递给结口Application,并进行调用
            env = []
            # 调用的返回值即为响应体
            response_body = m.application(env, self.start_response)
            # 将两者拼接成完整的响应报文
            response = self.response_headers + "\r\n" + response_body
        else:
            if "/" == file_name:
                file_name = "/index.html"
            try:
                file = open(R + file_name, "rb")
            except IOError:
                response_start_line = "HTTP/1.1 404 Not Found\r\n"
                response_headers = "Server: My Server\r\n"
                response_body = "the file is missing"
            else:
                file_data = file.read()
                file.close()
                response_start_line = "HTTP/1.1 200 OK\r\n"
                response_headers = "Server: My Server\r\n"
                response_body = file_data.decode("utf-8")
                response = response_start_line + response_headers + "\r\n" + response_body
        client_socket.send(response.encode("utf-8"))
        client_socket.close()

    def start(self):
        # 使服务器处于监听状态
        self.server_socket.listen(128)
        while True:
            # 使得套接字由被动转为主动
            client_socket, client_address = self.server_socket.accept()
            # 打印客户端地址
            print("用户%s已经连接上了" % str(client_address))
            # 设置子进程来处理客户端
            client_handle_process = Process(target=self.client_handle,
                                            args=(client_socket,))
            # 开启子进程
            client_handle_process.start()
            # 关闭客户端
            client_socket.close()


if __name__ == '__main__':
    # 使得搜索的路径转为"./wsgipython"
    sys.path.insert(1, P)
    server = Server()
    server.bind(8000)
    server.start()
