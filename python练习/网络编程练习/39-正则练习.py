import re
names = ["age","age3","1age","_age","age_","age!"]
for name in names:
    # $作用当正则判断完时,必须结束判断,以...结尾
    ret = re.match(r"^[a-zA-z][a-zA-Z0-9]*$",name)
    # match默认以...开头
    if ret:
        print("变量名%s符合要求"%ret.group())
    else:
        print("变量名%s非法"%name)