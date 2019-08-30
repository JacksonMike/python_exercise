from socket import *
from multiprocessing import *
def dealClicent(newSocket,destAdder):
    while True:
        receData = newSocket.recv(1024)
        if len(receData) > 0:
            print("客户端[%s]:数据%s"%(str(destAdder),receData))
        else:
            print("客户端[%s]已经关闭"%(str(destAdder)))
            break
    newSocket.close()
def main():
    serSocket = socket(AF_INET,SOCK_STREAM)
    serSocket.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    serSocket.bind(("",8081))
    serSocket.listen(5)
    try:
        while True:
            print("等待新的客户端到来")
            newSocket ,destAddr = serSocket.accept()
            print("创建一个进程负责处理[%s]"%str(destAddr))
            client = Process(target=dealClicent,args=(newSocket,destAddr))
            client.start()
    finally:
        serSocket.close()
if __name__ == '__main__':
    main()