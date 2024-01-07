import sys
import re
route, map_ = sys.stdin.read().strip().split("\n\n")

lol = {}

for x in map_.split("\n"):
    a, b, c = re.match("^(.*) = \((.*), (.*)\)$", x).groups()
    lol[a] = (b,c)
cur = "AAA"
ans = 0
pnt = 0
while cur != "ZZZ":
    ans += 1
    if route[pnt] == 'L':
        cur = lol[cur][0]
    else:
        cur = lol[cur][1]
    pnt = (pnt+1)%len(route)

print(ans)
