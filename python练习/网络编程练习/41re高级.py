import re
print(re.search(r"\d+","点击量为1").group())
# 加上"^"相当于match,从头匹配
print(re.search(r"^\d+","888点击量为").group())
# 返回所有的匹配值,不需要.group()
a = re.findall(r"\d+","java=1,python=2,php=3")
print(a)
# 替换,凡事匹配到的都要替换
print(re.sub(r"\d+","998","python=1,java=3"))
def add(temp):
    strNum = temp.group()
    num = int(strNum) - int(strNum)
    return str(num)
ret = re.sub(r"\d+",add,"python = 99")
print(ret)
# 按照冒号和空格切割
print(re.split(r":|  ","h: hk"))