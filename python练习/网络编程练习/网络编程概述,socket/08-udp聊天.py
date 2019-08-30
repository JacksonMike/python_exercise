import socket
def send_msg(udp_socket):
    '''发送消息'''
    # 获取要发送的内容
    dest_ip = input("请输入IP:")
    dest_port = int(input("请输入端口号"))
    send_data = input("请输入数据内容:")
    udp_socket.sendto(send_data.encode("utf-8"), (dest_ip, dest_port))
def rece_msg(udp_socket):
    '''接收数据'''
    rece_data = udp_socket.recvfrom(1024)
    print("%s:%s" % (str(rece_data[1]), rece_data[0].decode("utf-8")))
def main():
    # 创建套接字
    udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    # 绑定信息
    udp_socket.bind(("",8084))
    #while循环处理
    while True:
        print("----聊天室----")
        print("1:发送消息")
        print("2:接收消息")
        print("3：退出系统")
        op = input("请输入序号:")
        if op == "1":
            # 发送
            send_msg(udp_socket)
        elif op == "2":
            # 接收并显示
            rece_msg(udp_socket)
        elif op == "0":
            break
        else:
            print("请重新输入")
if __name__ == '__main__':
    main()
