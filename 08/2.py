import sys
import re
import collections
import math
route, map_ = sys.stdin.read().strip().split("\n\n")

lol = {}

for x in map_.split("\n"):
    a, b, c = re.match("^(.*) = \((.*), (.*)\)$", x).groups()
    lol[a] = (b,c)
cur = []
ans = 0
pnt = 0
for x in lol.keys():
    if x[2] == 'A':
        cur.append(x)
lol2 = collections.defaultdict(int)
llo3 = {}
offsetit = collections.defaultdict(int)
while not all(x[2] == 'Z' for x in cur):
    ans += 1
    for idx,x in enumerate(cur):
        if route[pnt] == 'L':
            cur[idx] = lol[x][0]
        else:
            cur[idx] = lol[x][1]
        offsetit[idx] += 1
        if cur[idx][2] == 'Z':
            offsetit[idx] = 0
            if (idx,pnt,x) in lol2:
                llo3[idx] =ans-lol2[(idx,pnt,x)] 
            lol2[(idx,pnt,x)] = ans
 
    if ans > 100000 and 0 in offsetit.values():
        break
    pnt = (pnt+1)%len(route)

pf = [llo3[2]]
rot = math.lcm(*pf)
bst = 1
while sum(offsetit.values()) != 0:
    ans += rot
    for idx,x in enumerate(offsetit):
        offsetit[idx] = (offsetit[idx]+rot)%llo3[idx]
    if list(offsetit.values()).count(0) > bst:
        pf = []
        for idx,x in enumerate(offsetit.values()):
            if x == 0:
                pf.append(llo3[idx])
        rot = math.lcm(*pf)
        bst = list(offsetit.values()).count(0)
print(ans)
