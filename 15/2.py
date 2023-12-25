import sys
import collections
boxs = collections.defaultdict(list)
fcls = collections.defaultdict(int)
input = sys.stdin.read().strip().split(",")

def HASH(s):
    h = 0
    for c in s:
        h += ord(c)
        h *= 17
        h %= 256
    return h

for x in input:
    h = HASH(x.split("=")[0].split("-")[0])
    if x[-1] == "-":
        lbl = x[:-1]
        if lbl in boxs[h]:
            boxs[h].remove(lbl)
    else: # =
        lbl = x.split("=")[0]
        fcl = int(x.split("=")[1])
        fcls[lbl] = fcl
        if lbl not in boxs[h]:
            boxs[h].append(lbl)

ans = 0

for k,b in boxs.items():
    for i2,lbl in enumerate(b):
        ans += (k+1)*(+i2+1)*fcls[lbl]
print(ans)
