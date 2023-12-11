import sys
input = sys.stdin.read().strip().split("\n")
cur_y = 0
galaxies = {}
for y in range(len(input)):
    empty = True
    for x in range(len(input[y])):
        if input[y][x] != '.':
            empty = False
    if empty:
        cur_y += 1000000-1
    cur_y += 1
    for x in range(len(input[y])):
        if input[y][x] == '#':
            galaxies[(y,x)] = cur_y


cur_x = 0
for x in range(len(input[y])):
    empty = True
    for y in range(len(input)):
        if input[y][x] != '.':
            empty = False
    if empty:
        cur_x += 1000000-1
    cur_x += 1
    for y in range(len(input[y])):
        if input[y][x] == '#':
            galaxies[(y,x)] = (galaxies[(y,x)], cur_x)

ans = 0
galaxies = list(galaxies.values())
for i in range(len(galaxies)):
    for j in range(i+1, len(galaxies)):
        ans += abs(galaxies[i][0]-galaxies[j][0])
        ans += abs(galaxies[i][1]-galaxies[j][1])
print(ans)
