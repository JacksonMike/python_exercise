import re
print(re.match(r"[hH]ello[123456789]","Hello6 world8").group())
print(re.match(r"l","love").group())
# 从头开始匹配
print(re.match(r"l","kl"))
# 搜索整个字符串
print(re.search(r"[a-z]+","liuyangN12349").group())
# re.I使对大小写匹配不敏感
print(re.search(r"[a-z]+","liuyangN12349",re.I).group())
if re.match(r"[0-9]","9"):
    print("m")
# 用空格分割
print(re.split(r"\s+","a,b c "))
# 用逗号分隔
print(re.split(r"[\s\,]+","a,b c"))
print(re.match(r"[0-9]","3954").group(0))
# 搜索全文匹配所有的ab,返回一个列表
print(re.findall(r"ab","abcaabcbacbcabc"))

