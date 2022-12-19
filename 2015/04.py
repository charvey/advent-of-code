from aocd import data, submit
import hashlib
import sys

input = data


def findWithPrefix(prefix):
    for i in range(sys.maxsize):
        hash = hashlib.md5((input + str(i)).encode('utf-8')).hexdigest()
        if hash.startswith(prefix):
            return i


submit(findWithPrefix('00000'), part='a')
submit(findWithPrefix('000000'), part='b')
