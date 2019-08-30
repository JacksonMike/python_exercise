import socket
# 文件下载服务器
def send_file_to_client(a,b):
    file_name = a.recv(1024).decode("gbk")
    print("客户端%s需要下载的文件是%s"%(str(b),file_name))
    file_content = None
    try:
        f = open(file_name,"rb")
        file_content = f.read()
        f.close()
    except Exception as ret:
        print("没有文件%s"%file_name)
    if file_content:
        a.send(file_content)
def main():
    tcp_server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    tcp_server_socket.bind(("",7080))
    tcp_server_socket.listen(128)
    while True:
        a,b = tcp_server_socket.accept()
        send_file_to_client(a,b)
        a.close()
    tcp_server_socket.close()
if __name__ == '__main__':
    main()