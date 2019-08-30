import re
a = input("请输入您的网易邮箱地址:")
b = [a]
for temp in b:
    # 正则表达式中需要用普通的字符,例如"\","."等,只需要在前面加"\"进行转意
    ret = re.match(r"^[a-zA-Z0-9]{5,13}@163\.com$",temp)

    if ret:
        print("网址%s:符合规范"%ret.group())
    else:
        print("网址%s:不符合 规范"%a)
c = re.match(r"^[a-zA-Z0-9]{5,13}@126|163\.com$","163.com")
print(c.group()) # 结果为163.com
# 也可以匹配126的邮箱
d = re.match(r"^([a-zA-Z0-9]{5,13})@(126|163)\.com$","12345@126.com")
print(d.group(2)) # 126 相应的括号个数
html_str = "<h1>hello</h1>"
print(re.match(r"<\w*>.*</\w*>",html_str).group())
print(re.match(r"<(\w*)>.*</\1>",html_str).group())
html_str = "<body><h1>hello</h1></body>"
print(re.match(r"<(\w*)><(\w*)>.*</\2></\1>",html_str).group())
html_str = "<body><h1>hello</h1></body>"
print(re.match(r"<(?P<p1>\w*)><(?P<p2>\w*)>.*</(?P=p2)></(?P=p1)>",html_str).group())