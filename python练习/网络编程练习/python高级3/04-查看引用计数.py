import gc
print(gc.get_count())
print(gc.get_threshold()) #(700, 10, 10)
# 创建对象 - 销毁对象 > 700 开始清理0代链表
# 每清理10次0代链表,清理一次一代链表
# 每清理10次1代链表,清理一次二代链表
a = "hello world"

