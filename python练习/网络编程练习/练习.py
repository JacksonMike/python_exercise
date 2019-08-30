import socket
def main():
    udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    udp_socket.sendto(b"1999999",("10.176.135.50",8080))
    udp_socket.close()

if __name__ == '__main__':
    main()