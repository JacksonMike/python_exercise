a = "xxx.txt"
print(a.endswith(".txt")) #以。。。。结尾
print(a.startswith("xxx"))#以。。。。开头
b = "    ahghdhHHHskd    "
print(b.lower()) #全部小写
print(b.upper()) #全部大写
print(b.center(100)) #居中
print(b.ljust(50))   #向左对齐
print(b.rjust(50))  #向右对齐
print(b.strip())  #消除左右两边空白字符
print(b.rstrip()) #消除右边空白字符
print(b.lstrip()) #消除左边空白字符
c = "as the saying goes and goes we are friends"
print(c.partition("goes")) # 返回元祖，从左往右 ('as the saying ', 'goes', ' and goes we are friends')
print(c.rpartition("goes"))# 从右往左 ('as the saying goes and ', 'goes', ' we are friends')
d = "hello\nworld\npython\nitcast"
print(d.splitlines()) #按照行进行分割
e = "11111112345454"
f = "gdlfalfalfaljfladlaflsadk"
g = "12ghghgh"
print(e.isdigit()) #判断是否是纯数字
print(f.isalpha()) #判断是否是纯字母
print(g.isalnum()) #判断是否为数字和字母
print(g.isspace()) #判断是否是纯空格
h =["world","heima","kfc"]
i = "="
print(i.join(h)) #相连world=heima=kfc

