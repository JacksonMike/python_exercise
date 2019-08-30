import socket
def main():
    #创建套接字
    udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    #绑定一个本地的对象
    localaddr = ('',8080)
    udp_socket.bind(localaddr)
    #接收数据
    recv_data = udp_socket.recvfrom(1024)
    #打印接收到的数据
    print(recv_data)
    #关闭套接字
    udp_socket.close()
if __name__ == '__main__':
    main()
#返回值是元组 类似(b"haha",(192.168.1.102,8080))
#第一个数据是接收到的数据,第二个数据为发送方的iP和端口