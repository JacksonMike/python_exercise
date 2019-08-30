'''
 IP地址:网络号+主机号 C类地址 192.168.1.0表示网络号,不可用 192.168.1.255表示广播地址可用,仅有254个地址可用
 ip地址与网络掩码按位与操作得到网络号,在同一个网络号才能通信 1&a=a 0&a=0
 hub集线器:链接多台电脑
 集线器:可立即使用,不用配置;仅起转发作用,网络风暴
 交换机:需要等待,需要配置;根据Mac地址选择行的发送
 mac地址网卡的序列号
 ping ->icmp 协议 ping一个电脑的时候使用的
 arp协议:根据IP获取Mac地址,即一个电脑的网卡号.
 rarp协议:相反根据Mac获取iP
 arp-a:缓存列表,一定时间内数据不会晴空,容易引起arp攻击
 arp=d:删除
 路由器:选择信息传送的线路,链接不同的网段,使之通信.每台计算机还要设置网关
 tcp/ip协议规定:跨网之间不能通信
 mac地址在两个设备通信时候发生变化,标记实际转发时的设备地址 而IP地址始终不变,标记逻辑上的地址
 netmask:和IP地址一起确定网络号
 默认网关:发送的IP不再同一网段内,会把这个数据发给默认网关.
 浏览器中输入百度上网过程:
 1先解析出baidu.com对应的IP:使用arp协议获取默认网关的Mac地址
                          组织数据发送给默认网关
                          默认网关拥有转发数据的能力,转发给路由器
                          路由器根据自己的路由协议,选择一个合适的路径转发数据给目的网关
                          目的网关(即DNS服务器所在的网关)把数据转给DNS服务器
                          DNS服务器查询并解析出的对应的IP地址之后,按照原来的路线,发送给请求这个域名的浏览器
 2得到IP后,发出tcp三次握手进行连接
 3使用http协议发出请求数据给web服务器
 4web服务器收到数据请求之后,通过查询自己的服务器得到相信的结果,原路返回给浏览器
 5浏览器接收到数据后,通过渲染功能显示这个结果
 6浏览器关闭tcp连接,4次挥手

 三次握手:(c客户端 s服务器) C:syn j; S:sys k,ack j+1; C:ack k+1    确认=发送+1;
 tcp中一方收到对方的数据后,一定要发送ack确认包给对方,但是udp没有这个过程,tcp比udp稳定
 四次挥手:C调用close方法即将关闭 发送:fin seq x+2,ack:y+1; S知道这个消息 发送:ack x+3;S也调用close方法
         关闭 发送fin seq:y+1;C确认这个消息: 发送ack:y+2;
 osi七层模型:物理层 数据链路层 网络层 传输层 会话层 表示层 应用层
 arp根据IP找Mac地址
 rarp根据Mac地址找IP
 icmp ping的时候
 DHCP 自动获取IP
 Static手动获取IP
'''