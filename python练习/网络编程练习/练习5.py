import socket
def send_data(udp_socket):
    a = input("请输入对方的IP:")
    b = int(input("请输入对方的端口号:"))
    c = input("请输入要发送的数据:")
    udp_socket.sendto(c.encode("utf-8"),(a,b))

def rece_data(udp_socket):
    d = udp_socket.recvfrom(1024)
    print("%s,%s"%(d[0].decode("gbk"),str(d[1])))

def main():
    udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    udp_socket.bind(("",9989))
    while True:
        print("----这是我的聊天神器------")
        print("1发送消息")
        print("2接收消息")
        print("3退出系统")
        op = input("请输入相应的数字:")
        if op == "2":
            rece_data(udp_socket)
        elif op == "1":
            send_data(udp_socket)
        elif op == "3":
            break
        else:
            print("输入错误,请重新输入")
if __name__ == '__main__':
    main()