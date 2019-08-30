import socket
#  tcp客户端
def main():
    tcp_client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    a = input("请输入要连接的服务器的IP:")
    b = int(input("请输入要连接服务器的端口号:"))
    c = (a,b)
    tcp_client_socket.connect(c)
    d = input("请输入要发送的数据:")
    tcp_client_socket.send(d.encode("gbk"))
    tcp_client_socket.close()
if __name__ == '__main__':
    main()



