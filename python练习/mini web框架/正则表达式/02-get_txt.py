import re

s = """<div>
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
<p>⼤数据，数理统计，机器学习，⾼性能，⼤并发。</p>
                </div>"""
re.sub(r"</?\w+>", "", s)

# 分离域名
v = "https://www.taobao.com/markets/nvzhuang/taobaonvzhuang?spm=a21bo.2017.201867-main.1.5af911d9vRTrdI"
re.sub(r"(https://.+?/).*", lambda x: x.group(1), s)
# x代表引号内整个式子,y=x.group(1)为返回值
s = "never give up but you should give in"
s.split(r" +", s)
re.findall(r"\b[a-zA-Z]+\b", s)
# 匹配单词
