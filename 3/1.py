import sys
input = sys.stdin.read().strip().split()

input = list(map(lambda x: "."+x+".", input))

input.insert(0, "."*len(input[0]))
input.append("."*len(input[0]))

ans = 0

for y in range(len(input)):
    cs = ""
    ok = False
    for x in range(len(input[y])):
        if not (ord(input[y][x]) >= ord('0') and ord(input[y][x]) <= ord('9')) and cs != "":
            if ok:
                ans += int(cs)
            cs = ""
            ok = False
        elif ord(input[y][x]) >= ord('0') and ord(input[y][x]) <= ord('9'):
            cs = cs+input[y][x]
            for i in range(-1, 1+1):
                for j in range(-1, 1+1):
                    if i == 0 and j == 0:
                        continue
                    if input[y+i][x+j] != '.' and not (ord(input[y+i][x+j]) >= ord('0') and ord(input[y+i][x+j]) <= ord('9')):
                        ok = True
print(ans)
