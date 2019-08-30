try:
    #11/0
    #open("xxxxx.txt")
    #print(a)
    print("----9-----")
except (NameError,FileNotFoundError):
       #用元组
    print("捕获异常后处理")
except Exception as ret:
    #适用于所有异常类型
    print("捕获所有异常")
    print(ret)
else:
    print("没有异常才会执行的功能")
finally:
    print("----finally-------")

print("-------3")