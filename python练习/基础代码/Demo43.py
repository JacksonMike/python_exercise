def getRMB():
	RMB = 23
	print("所需的人民币是:%d"%RMB)
	return RMB
def getDollar(RMB):
	RMB *= 7
	print("所需的日元是:%d"%RMB)
result = getRMB() #已经调用函数了,并且由于return值是RMB,所以已经将RMB = 23存储在result中
getDollar(result)