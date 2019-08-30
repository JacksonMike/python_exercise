import socket
def main():
    #创建一个udp套接字
    udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    #可以使用套接字发送数据
    udp_socket.sendto(b"Hello 1234",("192.168.1.100",8080))
                    # python3发送的内容是字节不能是字符串必须byte类型所以加b        对方的IP地址和端口号
    #关闭套接字
    udp_socket.close()
if __name__ == '__main__':
    main()

#python3交互模式的一种,ipython3一种更高级的交互模式