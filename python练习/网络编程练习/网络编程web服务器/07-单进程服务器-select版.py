import socket
import select
import sys
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(("",8084))
server.listen(10)
inputs = [server,sys.stdin]
running = True
while True:
    a,b,c = select.select(inputs,[],[])
    # a检测套接字是否接收 b检测套接字是否发送数据 c检测套接字是否异常
    for sock in a:
        if sock == server:
            clientSocket,clientAddr = server.accept()
            inputs.append(clientSocket)
            print("客户端:%s"%str(clientAddr))
        elif sock == sys.stdin:
            cmd = sys.stdin.readline()
            running = False
            break
        else:
            data = sock.recv(1024)
            if data:
                sock.send(data)
                print("客户端%s:数据%s"%(str(clientAddr),data))
            else:
                inputs.remove(sock)
                sock.close()
    if not running:
        break
server.close()




