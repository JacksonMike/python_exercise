import socket
def main():
    udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    a = input("请输入对方的IP:")
    b = int(input("请输入对方的端口号:"))
    c = input("请输入要发送的数据:")
    udp_socket.sendto(c.encode("utf-8"),(a,b))
    e = udp_socket.recvfrom(1024)
    print(e)
    udp_socket.close()
if __name__ == '__main__':
    main()