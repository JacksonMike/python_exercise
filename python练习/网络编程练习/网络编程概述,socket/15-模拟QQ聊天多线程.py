from threading import Thread
from socket import *
def receData():
    while True:
        a = udpSocket.recvfrom(1024)
        # \r表示换行,没有输入时候
        print("\r%s:%s"%(str(a[1]),a[0]))
def sendData():
    while True:
        b = input("请输入要发送的内容:")
        udpSocket.sendto(b.encode("gb2312"),(destIp,destPort))
# 可以定义全局变量将变量传入函数
udpSocket = None
destIp = ""
destPort = 0
def main():
    global udpSocket
    global destPort
    global destIp
    destIp = input("请输入对方的IP:")
    destPort = int(input("请输入对方的端口:"))
    udpSocket = socket(AF_INET,SOCK_DGRAM)
    udpSocket.bind(("",4591))
    tr = Thread(target=receData)
    ts = Thread(target=sendData)
    tr.start()
    ts.start()
    tr.join()
    ts.join()
if __name__ == '__main__':
    main()