from socket import *
serSocket = socket(AF_INET,SOCK_STREAM)
serSocket.bind(("",8080))
serSocket.setblocking(False)
serSocket.listen(100)
# 储存客户端
clientAddrList = []
while True:
    # 处理客户端
    try:
        clientSocket, clientAddr = serSocket.accept()
    except:
        pass
    else:
        print("一个新的客户端到来%s"%(str(clientAddr)))
        clientSocket.setblocking(False)
        clientAddrList.append((clientSocket,clientAddr))
    # 处理数据
    for clientSocket,clientAddr in clientAddrList:
        try:
            receData = clientSocket.recv(1024)
        except:
            pass
        else:
            if len(receData) > 0:
                print("%s:%s" % (str(clientAddr), receData))
            else:
                clientSocket.close()
                clientAddrList.remove((clientSocket,clientAddr))
                print("%s 已经下线"%(str(clientAddr)))



