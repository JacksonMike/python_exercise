from socket import *
# 客户端
connectNum = int(input("请输入要链接服务器的次数:"))
for i in range(int(connectNum)):
    s = socket(AF_INET,SOCK_STREAM)
    s.connect(("127.0.0.1",7790))
    print(i)