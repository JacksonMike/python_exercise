f = open("test.txt","r")
print(f.read(2)) # 每次读两个字节,空格也算
print(f.read(2))
print(f.read(2))