import sys
import collections
input = sys.stdin.read().strip().split()

input = list(map(lambda x: "."+x+".", input))

input.insert(0, "."*len(input[0]))
input.append("."*len(input[0]))

ans = 0

gears = collections.defaultdict(list)

for y in range(len(input)):
    cs = ""
    ok = False
    lol = set()
    for x in range(len(input[y])):
        if not (ord(input[y][x]) >= ord('0') and ord(input[y][x]) <= ord('9')) and cs != "":
            for c in lol:
                gears[c].append(int(cs))
            lol.clear()
            cs = ""
            ok = False
        elif ord(input[y][x]) >= ord('0') and ord(input[y][x]) <= ord('9'):
            cs = cs+input[y][x]
            for i in range(-1, 1+1):
                for j in range(-1, 1+1):
                    if i == 0 and j == 0:
                        continue
                    if input[y+i][x+j] == '*' and (y+i, x+j-len(cs)) not in lol:
                        lol.add((y+i,x+j))
                    if input[y+i][x+j] != '.' and not (ord(input[y+i][x+j]) >= ord('0') and ord(input[y+i][x+j]) <= ord('9')):
                        ok = True
for g in gears.values():
    if len(g) == 2:
        ans += g[0]*g[1]
print(ans)
