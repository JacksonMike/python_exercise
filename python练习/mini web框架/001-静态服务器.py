from socket import *
from multiprocessing import Process
import re

ROOT = "./html"


def hand_client(client_socket):
    request_data = client_socket.recv(1024)
    print("request_data:", request_data)
    request_lines = request_data.splitlines()
    for line in request_lines:
        print(line)
    request_start_line = request_lines[0]
    print("request_start_line:", request_start_line.decode("utf-8"))
    # GET / HTTP/1.1
    file_name = re.match(r"\w+\s+(/[^ ]*)\s",
                         request_start_line.decode("utf-8")).group(1)
    if "/" == file_name:
        file_name = "/index.html"
    try:
        file = open(ROOT + file_name, "rb")
    except IOError:
        response_start_line = "HTTP/1.1 404 Not Found\r\n"
        response_headers = "server: My Server\r\n"
        response_body = "the file is not found"
    else:
        file_data = file.read()
        file.close()

        response_start_line = "HTTP/1.1 200 OK\r\n"
        response_headers = "server: My Server\r\n"
        response_body = file_data.decode("utf-8")
    response = response_start_line + response_headers + "\r\n" + response_body
    client_socket.send(bytes(response,"utf-8"))
    client_socket.close()


def main():
    server_socket = socket(AF_INET, SOCK_STREAM)
    server_socket.bind(("", 8090))
    server_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    server_socket.listen(128)
    while True:
        client_socket, client_address = server_socket.accept()
        hand_client_process = Process(target=hand_client,
                                      args=(client_socket,))
        hand_client_process.start()
        client_socket.close()


if __name__ == '__main__':
    main()
