import json

i = 10
f = 3.14
s = 'hello'
l = [12, 'yuan', True]
d = {'name': 'yuan', 'age': 18}

print(json.dumps(i))  # '10'
print(json.dumps(f))  # '3.14'
print(json.dumps(s))  # '"hello"'
print(json.dumps(l))  # '[12,"yuan",true]'
print(json.dumps(d))  # '{"name":"yuan","age":18}'
