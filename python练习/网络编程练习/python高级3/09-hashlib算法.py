import hashlib
t = hashlib.md5()
t.update(b"It is up to you")
print(t.hexdigest())
# md5加密