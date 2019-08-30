import re


pattern = "itcast"
s = "itheima"
t = "itcast"
result = re.match(pattern, s)
result1 = re.match(pattern, t)
print(result1)

re.match(r"[1-9]?\d?$|100$","0")
# 匹配1-100
r = re.match(r"(\d{5,10})@(qq|163|126)\.(com|cn|net)$", "2101706920@qq.com")
# 匹配邮箱 用r.group()提取
s = "<html><h1>itcast</h1></html>"
re.match(r"<(?P<key1>.+)><(?P<key2>.+)>.+</(?P=key2)></(?P=key1)>", s)
# 用python代替php
re.sub(r"php", "python", "itcast cpp php java ruby php go python")


def replace(result):
    print(result.group())
    r = int(result.group())+10
    return str(r)


re.sub(r"\d+",replace,"python=100,php=0")
"""
\s 匹配 \t \r \n 等,即没有实际意义的字符
\w 匹配符合变量名 命名规则的字符 字母 数字 下滑线
\d = [0-9]
\D = [^0-9]
\w = [a-zA-Z0-9]
\W = [^a-zA-Z0-9]
s = "<div>
                <p>岗位职责：</p>
<p>完成推荐算法、数据统计、接⼝、后台等服务器端相关⼯作</p>
<p><br></p>
<p>必备要求：</p>
<p>良好的⾃我驱动⼒和职业素养，⼯作积极主动、结果导向</p>
<p>&nbsp;<br></p>
<p>技术要求：</p>
<p>1、⼀年以上 Python 开发经验，掌握⾯向对象分析和设计，了解设计模式</p>
<p>2、掌握HTTP协议，熟悉MVC等概念以及相关WEB开发框架</p>
<p>3、掌握关系数据库开发设计，掌握 SQL，熟练使⽤ MySQL 中
的⼀种<br></p>
<p>4、掌握NoSQL、MQ，熟练使⽤对应技术解决⽅案</p>"
<p>5、熟悉 Javascript/CSS/HTML5，JQuery、React、Vue.js</p>
<p>&nbsp;<br></p>
<p>加分项：</p>
<p>⼤数据，数理统计，机器学习，sklearn，⾼性能，⼤并发。</p>
                </div>
"""
t = """<img data-original="https://cs-op.douyucdn.cn/dycatr/game_cate/2baff99c2d776f70d95a43aff087952a.jpg" 
src="https://cs-op.douyucdn.cn/dycatr/game_cate/2baff99c2d776f70d95a43aff087952a.jpg" class="img-pre" style="display: block;">"""
re.search(r"https.+?\.jpg",s).group()