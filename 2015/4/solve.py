import hashlib
import sys

input = 'ckczppom'


def findWithPrefix(prefix):
    for i in range(sys.maxsize):
        hash = hashlib.md5((input + str(i)).encode('utf-8')).hexdigest()
        if hash.startswith(prefix):
            return i


print(findWithPrefix('00000'))
print(findWithPrefix('000000'))
