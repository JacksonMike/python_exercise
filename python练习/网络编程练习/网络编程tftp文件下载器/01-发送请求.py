from socket import *
import struct
# 把数据封装成字符串
sendData = struct.pack("!H8sb5sb",1,b"test.jpg",0,b"octet",0);
# !代表网络中存放大端形式；H(无符号短整型)表示占两个字节,对应1;s占一个字节,8s
#  8个字节的字符串 test.jpg ;b占一个字节,有符号的char类型,对应"0";5s占5个字,对应octet
udpSocket = socket(AF_INET,SOCK_DGRAM)
udpSocket.sendto(sendData,("chenqiandeMacBook-Air.local",69))
udpSocket.close()
'''
确认包 一般struct.pack("!HH",4,p_num) #数据包类型,数据序号
'''