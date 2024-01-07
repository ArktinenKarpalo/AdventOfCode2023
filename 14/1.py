import sys
import collections
input = sys.stdin.read().strip().split()
print(input)
ans = 0
for x in range(len(input[0])):
    d = collections.deque()
    for y in range(len(input)):
        if input[y][x] == '#':
            d.clear()
        else:
            d.append(y)
        if input[y][x] == 'O':
            nl = d.popleft()
            ans += len(input)-nl

print(ans)
