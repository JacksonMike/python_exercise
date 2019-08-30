import re
# (正则表达式,需要处理的字符串)
print(re.match(r"hello","hello world"))
print(re.match(r"[hH]ello","Hello world"))
print(re.match("速度\d","速度8"))
# 匹配数字
ret = re.match("神探狄仁杰\d","神探狄仁杰1")
print(ret.group())
ret = re.match("神探狄仁杰[1-4]","神探狄仁杰1")
print(ret.group())
# 取值1-4,5-7
ret = re.match("加勒比[1-45-7]","加勒比7")
print(ret.group())
ret = re.match("加勒比[1-4abcd]","加勒比a")
print(ret.group())
ret = re.match("加勒比[1-4a-zA-Z]","加勒比H")
print(ret.group())
# 匹配单词字符:字母数字下划线,也支持中文
ret = re.match("加勒比\w","加勒比哈")
print(ret.group())
# 匹配空格字符,tab键.\t在程序中就是tab键
ret = re.match("加勒比\s\d","加勒比\t9")
print(ret.group())
#所有大写字母正好与小写字母相反
ret = re.match("加勒比\D","加勒比t")
print(ret.group())
#.范围最广
ret = re.match("加勒比.","加勒比h")
print(ret.group())
# 后面接两位
ret = re.match("加勒比\d{1,2}","加勒比10")
print(ret.group())
# 后面接三位
ret = re.match("加勒比\d{1,3}","加勒比100")
print(ret.group())
#手机号
ret = re.match("\d{11}","18772320219")
print(ret.group())
# 上海电话号码
ret = re.match("021-\d{8}","021-12345678")
print(ret.group())
# 问号最多只有一个
ret = re.match(r"021-?\d{8}","021-12345678")
print(ret.group())
ret = re.match(r"\d{3}-?\d{8}","022-12345678")
print(ret.group())
ret = re.match(r"\d{3,4}-?\d{8}","0228-12345678")
print(ret.group())
ret = re.match(r"\d{3,4}-?\d{7,8}","0228-1234567")
print(ret.group())
# 换行打印
html_content = """Kobe
brave
elegant
book"""
print(html_content)
print("="*50)
# 除了\n外的任何字符
print(re.match(r".*",html_content).group())
print("="*50)
# re.S让\n匹配到
print(re.match(r".*",html_content,re.S).group())
# 加号要非空
print(re.match(r".+","k").group())
