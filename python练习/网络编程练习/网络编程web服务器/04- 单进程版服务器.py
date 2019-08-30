from socket import *
serScoket = socket(AF_INET,SOCK_STREAM)
# 重复多次绑定
serScoket.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
serScoket.bind(("",8089))
serScoket.listen(5)
while True:
    print("等待新的客户端")
    newSocket, destAddr = serScoket.accept()
    print("为客户端[%s]处理数据"%(str(destAddr)))
    try:
        receData = newSocket.recv(1024)
        if len(receData) >0:
            print("rece[%s]:%s"%(str(destAddr),receData))
        else:
            print("[%s]客户端已经关闭"%(str(destAddr)))
            break
    finally:
        newSocket.close()
serScoket.close()

