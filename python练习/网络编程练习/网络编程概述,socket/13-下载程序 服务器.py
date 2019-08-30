import socket
def send_file_to_client(new_client_socket,client_addr):
    # 接收客户端需要下载的文件名
    # 接收客户端发送过来的要下载的文件名
    file_name = new_client_socket.recv(1024).decode("utf-8")
    print("客户端(%s)需要下载的文件是:%s" % (str(client_addr), file_name))
    file_content = None
    # 打开这个文件读取数据
    try:
        f = open(file_name,"rb")
        file_content = f.read()
        f.close()
    except Exception as ret:
        print("没有要下载的文件(%s)"%file_name)
    # 发送文件数据给客户端
    #new_client_socket.send("----OK----".encode("utf-8"))
    if file_content:
        new_client_socket.send(file_content)

def main():
    # 创建套接字
    tcp_server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    # 绑定本地信息
    tcp_server_socket.bind(("",9903))
    # 默认套接字由主动到被动
    tcp_server_socket.listen(128)
    while True:
        # 等待客户端链接
        new_client_socket, client_addr = tcp_server_socket.accept()
        # 调用发送文件函数,完成为客户端服务
        send_file_to_client(new_client_socket, client_addr)

        # 关闭套接字
        new_client_socket.close()
    tcp_server_socket.close()
if __name__ == '__main__':
    main()

