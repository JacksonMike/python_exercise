def upper_attr(future_class_name,future_class_parents,future_class_attr):
    # 参数:类名 父类名 属性
    new_atter = {}
    for name,value in future_class_attr.items():
        if not name.startswith("__"):
            new_atter[name.upper()] = value
    # 指向Foo函数
    return type(future_class_name,future_class_parents,new_atter)
# metaclass 指定类的创建样子
class Foo(object,metaclass = upper_attr):
    bar = "bip"
print(hasattr(Foo,"bar"))
print(hasattr(Foo,"BAR"))

f = Foo()
print(f.BAR)