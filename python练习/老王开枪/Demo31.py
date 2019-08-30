#抛出自定义异常
class shortInputException(Exception):
    def __init__(self,length,atLeast):
        self.length = length
        self.atLeast = atLeast
def main():
    try:
        s = input("请输入:")
        if len(s) < 3:
            raise shortInputException(len(s),3)
    except shortInputException as result:
        print("%d,%d"%(result.length,result.atLeast))
    else:
        print("没有异常发生")
main()
