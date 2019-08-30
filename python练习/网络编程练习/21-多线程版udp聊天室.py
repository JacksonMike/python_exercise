import socket
import threading
def send(udp_socket,a,b):
    while True:
        send_data = input("请输入要发送的数据:")
        udp_socket.sendto(send_data.encode("utf-8"),(a,b))
def receive(udp_socket):
    while True:
        rece_data = udp_socket.recvfrom(1024)
        print(rece_data)
def main():
    udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    udp_socket.bind(("",7891))
    a = input("请输入对方的IP:")
    b = int(input("请输入对方的端口号:"))
    t1 = threading.Thread(target=send,args=(udp_socket,a,b))
    t2 = threading.Thread(target=receive,args=(udp_socket,))
    t1.start()
    t2.start()

if __name__ == '__main__':
    main()