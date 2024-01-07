import sys
import re
input = sys.stdin.read().strip().split("\n")
ans = 0
for line in input:
    m = re.match("Game ([0-9]+): (.*)", line).groups()
    id = int(m[0])
    sets = m[1].split(";")
    c = {"red": 0, "green": 0, "blue": 0}
    for s in map(lambda x: x.split(","), sets):
        for p in s:
            a, b = p.split()
            c[b] = max(c[b], int(a))
    ans += c["red"]*c["green"]*c["blue"]
print(ans)
