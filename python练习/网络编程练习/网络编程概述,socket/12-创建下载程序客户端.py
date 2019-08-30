import socket

def main():
    # 创建套接字
    tcp_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    # 获取服务器的IP和Port
    dest_ip = input("请输入下载的服务器IP:")
    dest_port = int(input("请输入下载服务器的端口号:"))
    # 链接服务器
    tcp_socket.connect((dest_ip,dest_port))
    # 获取下载文件的名字
    download_file_name = input("请输入要下载文件的名字:")
    # 将文件的名字发送到服务器
    tcp_socket.send(download_file_name.encode("utf-8"))
    # 接收文件中的数据
    rece_data = tcp_socket.recv(1024)
    if rece_data:
        # 保存接收到的数据到一个文件中
        with open("[新]" + download_file_name, "wb") as f:
            f.write(rece_data)
    # 关闭套接字
    tcp_socket.close()

if __name__ == '__main__':
    main()