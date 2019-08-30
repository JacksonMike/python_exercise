from socket import *
from time import sleep
# 服务器
tcpSerSocket = socket(AF_INET,SOCK_STREAM)
tcpSerSocket.bind(("",7790))
connectNum = int(input("请输入最大链接数:"))
tcpSerSocket.listen(connectNum)
for i in range(10):
    print(i)
    sleep(1)
print("延时完毕")
while True:
    for i in range(10):
        print(i)
        sleep(1)
    print("延时完毕")
    newSocket,clientAddr = tcpSerSocket.accept()
    print(clientAddr)
    sleep(1)