# tcp服务器
import socket
def main():
    tcp_server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    tcp_server_socket.bind(("",7798))
    tcp_server_socket.listen(128)
    while True:
        print("等待一个客户端到来:")
        a, b = tcp_server_socket.accept()
        print("一个客户端已经来了:%s"%str(b))
        while True:
            rece_data = a.recv(1024)
            print("客户端的请求是:%s" % rece_data.decode("gbk"))
            if rece_data:
                a.send("Hi".encode("utf-8"))
            else:
                break
        a.close()
        print("为客户端服务完毕")
    tcp_server_socket.close()


if __name__ == '__main__':
    main()