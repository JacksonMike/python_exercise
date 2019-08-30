import socket
def main():
    # 创建套接字
    tcp_server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    # 绑定本地信息
    tcp_server_socket.bind(("",7893))
    # 设置默认的套接字由主动到被动
    tcp_server_socket.listen(128)
    # 循环为客户端服务
    while True:
        print("等待新的客户端到来:")
        # 等待客户端的连接
        new_client_socket, client_addr = tcp_server_socket.accept()
        print("一个新的客户端已经到来%s"%str(client_addr))
        print(client_addr)
        # 接收客户端发过来的请求
        rece_data = new_client_socket.recv(1024)
        print("客户端发送过来的请求时%s"%rece_data.decode("utf-8"))
        # 回送部分数据给客户端
        new_client_socket.send("-----OK------".encode("utf-8"))
        # 关闭套接字,不为这个客户端服务
        new_client_socket.close()
        print("已经服务完毕.....")
    # 关闭监听套接字,不会有新的套接字到来
    tcp_server_socket.close()
if __name__ == '__main__':
    main()