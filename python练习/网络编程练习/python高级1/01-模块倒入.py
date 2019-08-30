
# 添加路径
import sys
print(sys.path)
sys.path.append("/home")
print(sys.path)

#重新倒入模块
import test
test.test()
# 不退出终端重新导入模块
from imp import*
reload(test)
test.test()

#循环导入 Demo a和b模块
#尽量构建主模块来调用子模块
