from rediscluster import *


startup_nodes = [
    {"host": "172.16.175.133", "port": "7000"},
    {"host": "127.0.0.1", "port": "7003"},
    {"host": "172.16.175.133", "port": "7001"}
]
src = StrictRedisCluster(startup_nodes=startup_nodes, decode_responses=True)
result = src.set("food", "bread")
print(result)
food = src.get("food")
print(food)
