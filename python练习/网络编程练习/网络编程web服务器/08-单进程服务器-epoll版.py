'''
标准输入 键盘 sys.stdin
标准输出 屏幕 sys.stdout
标准错误 屏幕 sys.stderr
文件描述符就是数字    sys.stderr.fileno() 的返回值
'''
import socket
import select
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.bind(("",7788))
s.listen(10)
epoll = select.epoll()
epoll.register(s.fileno())