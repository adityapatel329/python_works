import hashlib
BLOCKSIZE = 65536
hasher = hashlib.md5()

with open('example.txt', 'rb') as file:
    buf = file.read(BLOCKSIZE)

    while len(buf)> 0:
        hasher.update(buf)
        buf = file.read(BLOCKSIZE)

print(hasher.hexdigest())
