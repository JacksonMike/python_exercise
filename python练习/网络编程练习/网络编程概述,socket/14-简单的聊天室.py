from socket import *
def main():
    udpSocket = socket(AF_INET,SOCK_DGRAM)
    # 一个进程标记一个端口号,所以只能绑定一次
    udpSocket.bind(("",8085))
    while True:
        # 收到的第一个哈哈 第二个是IP地址
        receiveInfor = udpSocket.recvfrom(1024)
        address = receiverInfor[1][0]+":"+str(receiveInfor[1][1])
        print("%s"%address)
        print("%s"%receiveInfor[0].decode("gbk"))
    udpSocket.close()
if __name__ == '__main__':
    main()