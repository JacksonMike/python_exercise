
import socket
def main():
    udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    a = ("",9909)
    udp_socket.bind(a)
    while True:
        b = udp_socket.recvfrom(1024)
        c = b[0]  # 数据
        d = b[1]  # IP和端口
        print("%s,%s" % (c.decode("gbk"), str(d)))
    udp_socket.close()
if __name__ == '__main__':
    main()