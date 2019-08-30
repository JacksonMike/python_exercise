#  文件下载客户端
import socket
def main():
    tcp_client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    a = input("请输入服务器的IP:")
    b = int(input("请输入服务器的端口号:"))
    tcp_client_socket.connect((a,b))
    down_name = input("请输入下载文件的名字:")
    tcp_client_socket.send(down_name.encode("utf-8"))
    rece_data = tcp_client_socket.recv(1024)

    with open("new" + down_name,"wb") as f:
        f.write(rece_data)
    tcp_client_socket.close()
if __name__ == '__main__':
    main()