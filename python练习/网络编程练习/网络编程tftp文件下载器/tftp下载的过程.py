'''
1 客户端发送请求 是下载还是上传文件(操作类型) 文件名
2 服务器收到请求后确认 如果有该文件 则发送确认信息,或者直接发送文件的一部分
  如果没有该文件,就发送错误信息
3 客户端收到服务器数据后,如果收到错误信息,就停止下载
  如果收到部分文件后,要发送确认信息,将数据写入本地文件
4 循环过程:服务器发送文件一部分,客户端收到并且回复,知道文件下载完
5 如果文件下载完城,应该有一个结束的标志
# 大端数 0x44332211 高位在前,低位在后
# 小端数 0x11223344
'''