import sys
import re
input = sys.stdin.read().strip().split("\n")
ans = 0
for line in input:
    m = re.match("Game ([0-9]+): (.*)", line).groups()
    id = int(m[0])
    sets = m[1].split(";")
    c = {"red": 12, "green": 13, "blue": 14}
    ok = True
    for s in map(lambda x: x.split(","), sets):
        for p in s:
            a, b = p.split()
            if int(a) > c[b]:
                ok = False
    if ok:
        ans += id
print(ans)
