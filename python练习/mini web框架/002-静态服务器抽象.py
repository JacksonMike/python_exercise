from socket import *
from multiprocessing import Process
import re


# 根目录,文件的根路径
ROOT = "./html"


class Server(object):
    def __init__(self):
        # 建立套接字
        self.server_socket = socket(AF_INET, SOCK_STREAM)
        # 重复使用端口
        self.server_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

    def bind(self, port):
        # 绑定端口
        self.server_socket.bind(("", port))

    def start(self):
        # 使服务器处于监听状态
        self.server_socket.listen(128)
        while True:
            # 客户端连接,套接字由被动变为主动
            client_socket, client_address = self.server_socket.accept()
            # 打印客户端的信息
            print("用户%s连接上了" % str(client_address))
            # 采用多线程方式处理客户端数据
            hand_client_process = Process(target=self.hand,
                                          args=(client_socket,))
            # 开启多线程
            hand_client_process.start()
            # 关闭客户端
            client_socket.close()

    def hand(self, client_socket):
        """客户端处理方法"""
        # 客户端请求数据
        request_data = client_socket.recv(1024)
        # 打印请求数据
        print("request_data:", request_data)
        # 对请求数据按行进行分割
        request_lines = request_data.splitlines()
        # 遍历请求数据
        for line in request_lines:
            print(line)
        # 提取请求数据起始行
        request_start_line = request_lines[0]
        # 打印起始行
        print("request_start_line:", request_start_line.decode("gbk"))
        # GET /index.html HTTP/1.1
        # 提取请求的文件名称
        file_name = re.match(r"\w+\s+(/[^ ]*)\s",
                             request_start_line.decode("gbk")).group(1)
        # 当请求文件为空时,确立默认的请求文件
        if "/" == file_name:
            file_name = "/index.html"
        # 对请求文件是否存在进行判断
        try:
            file = open(ROOT + file_name, "rb")
        # 若不存在,构造响应的响应消息
        except IOError:
            response_start_line = "HTTP/1.1 404 Not Found\r\n"
            response_headers = "Server: My Server\r\n"
            response_body = "the file is not found"
        # 若存在,读取文件数据,作为响应体,并构造响应消息的起始行和响应体
        else:
            file_data = file.read()
            file.close()
            response_start_line = "HTTp/1.1 200 OK\r\n"
            response_headers = "Server: My Server\r\n"
            response_body = file_data.decode("utf-8")
        # 确立最终的响应消息格式
        response = response_start_line + response_headers + "\r\n" + response_body
        # 发送响应消息给客户端
        client_socket.send(response.encode("gbk"))
        # 关闭客户端,结束子线程
        client_socket.close()


if __name__ == '__main__':
    # 创建服务器对象
    server = Server()
    # 绑定端口
    server.bind(8091)
    # 开启线程
    server.start()
