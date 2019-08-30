import json


# d = {"name": "Jim"}
# s = json.dumps(d)
# with open("data.txt", "w") as f:
#     f.write(s)

with open("data.txt", "r") as f:
    data = f.read()
data = json.loads(data)
print(data)