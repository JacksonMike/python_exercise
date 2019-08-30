import socket
def main():
    #创建一个udp套接字
    udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    #从键盘中获取数据
    send_data = input("请输入要发送的数据:")
    #可以使用套接字接收数据
    udp_socket.sendto(send_data.encode("utf-8"),("192.168.1.102",8080))
                                    # 变成字符串 utf-8全球通用      对方的IP地址和端口号
    #关闭套接字
    udp_socket.close()
if __name__ == '__main__':
    main()

#python3交互模式的一种,ipython3一种更高级的交互模式