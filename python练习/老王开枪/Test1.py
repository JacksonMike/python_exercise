a = "Jim"
b = "Jack"
c = "Mike"
d = "Hard"
name_list = [a,b,c]
name_list.append(d)
e = name_list.count(b)
print(e)
print(name_list)
for a in name_list:
    print(a)
infor_tuple = ("Jim",12,12)
print(infor_tuple)
print(infor_tuple.count("Jim"))
for item in infor_tuple:
    print(item)

o = {"name":"Jim","age":15,"job":"cook"}
print("%s %d %s"%(o["name"],o["age"],o["job"]))

card_list =[{"name":"Jim","age":12},{"name":"Jack","age":13}]
for temple in card_list:
    print(temple)
    print(temple["name"])
string = "Hello World"
for m in string:
    print(m)
a = 10
print("%x"%id(a))