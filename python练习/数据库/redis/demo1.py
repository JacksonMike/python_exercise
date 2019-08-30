from redis import *

r = StrictRedis()
# result = r.set("food", "bread")
# result = r.get("food")
# result = r.set("food", "milk")
# result = r.delete("bed", "chair")
result = r.keys()
print(result)

