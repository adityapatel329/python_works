import hashlib

hasher = hashlib.md5()

with open('download.png','rb') as file:
    buf = file.read()
    hasher.update(buf)

print(hasher.hexdigest())
