from socket import *
import struct
# 每个数据包相当于C语言结构体
udpSocket = socket(AF_INET,SOCK_DGRAM)
# 服务器IP和端口,默认69
tftpAddr = ("192.648.64.1",69)
# 变成动态
fileName = input("请输入要下载的文件:")
fmt = str.format("!H%dsb5sb"%len(fileName))
# 发送请求
msg = struct.pack(fmt,1,fileName.encode(),0,b"octet",0)
# 1下载
udpSocket.sendto(msg,tftpAddr)
# 循环处理与服务器交换的过程
f = None
# f代表打开
while True:
    # 收到数据
    receData = udpSocket.recvfrom(1024)
    '''
    print(receData)
    数据包
    (b'\x00\x03\x00\x01\Test.jpg\......',("10.176.65.54",54444))
    错误包
    (b'\x00\x05\x00\x01\file not found\x00',("10.176.65.54",54449))
    '''
    #  解包         A                                     B
    data = struct.unpack("!HH", receData[0][:4])  # 取元组中的第一个元素(A),再对这个元素进行切片
    # (5,1) 分别为操作码和快编号 返回结果为一个元组
    dataType = data[0]  # 操作码
    dataNo = data[1]  # 块编号
    # 根据包类型进行不同的处理
    if dataType == 5:
        # 出错信息
        print("%s"%receData[0][4:].decode)  # file not found
        break
    elif dataType == 3: #收到正常数据,默认为512字节
        dataLen = len(receData[0][4:])
        if dataType == 1: #收到第一个数据包
            # 正常信息
            f = open(fileName, "wb")
            f.write(receData[0][4:])
        else:             #收到后续数据包
            f.write(receData[0][4:])
        # 给服务器发确认包,
        msg = struct.pack("!HH", 4, dataNo)
        udpSocket.sendto(msg, receData[1])# receData[1]放的是服务器给你发数据的新地址
        # 收到数据包中的数据如果小于512,则文件已经接收完毕
        if dataLen < 512:
            f.close()
            break
udpSocket.close()