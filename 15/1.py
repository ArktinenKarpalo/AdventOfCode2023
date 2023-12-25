import sys
import functools
print(sum(map(lambda x: functools.reduce(lambda y,z: ((y+ord(z))*17)%256, x, 0), sys.stdin.read().strip().split(","))))
