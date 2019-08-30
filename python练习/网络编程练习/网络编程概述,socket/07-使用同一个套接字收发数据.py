import socket
def main():
    # 创建套接字
    udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    # 获取对方的IP和端口号
    dest_ip = input("请输入IP")
    dest_port =int(input("请输入端口号")) #input得到的是字符串"",要用int类型进行转换
    # 从键盘中获取数据
    send_data = input("请输入数据")
    # 使用套接字收发数据
    udp_socket.sendto(send_data.encode("utf-8"),(dest_ip,dest_port))
    # 接收回来的数据
    rece_data = udp_socket.recvfrom(1024)
    # 套接字可以同事收发数据
    print(rece_data)
    # 关闭套接字
    udp_socket.close()
if __name__ == '__main__':
    main()
# 单工：收音机 只朝一个方向
# 半双工：可以收发数据 但同一时刻只能收或者发 对讲机
# 全双工：同一时刻既可以收又可以发 电话
# socket套接字是全双工