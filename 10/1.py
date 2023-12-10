import sys
import collections
input = sys.stdin.read().strip().split("\n")

pos = None
vrk = collections.defaultdict(list)
for y,line in enumerate(input):
    for x,c in enumerate(line):
        if c == 'S':
            pos = (y,x)
        elif c == '|':
            vrk[(y+1,x)].append((y,x))
            vrk[(y-1,x)].append((y,x))
        elif c == '-':
            vrk[(y,x-1)].append((y,x))
            vrk[(y,x+1)].append((y,x))
        elif c == 'L':
            vrk[(y,x+1)].append((y,x))
            vrk[(y-1,x)].append((y,x))
        elif c == 'J':
            vrk[(y-1,x)].append((y,x))
            vrk[(y,x-1)].append((y,x))
        elif c == '7':
            vrk[(y,x-1)].append((y,x))
            vrk[(y+1,x)].append((y,x))
        elif c == 'F':
            vrk[(y,x+1)].append((y,x))
            vrk[(y+1,x)].append((y,x))
        elif c == '.':
            pass
vis = set()
q = collections.deque()
q.append((pos, 0))
ans = 0
while len(q) > 0:
    cur = q.popleft()
    if cur[0] in vis:
        continue
    ans = max(ans, cur[1])
    vis.add(cur[0])
    for x in vrk[cur[0]]:
        q.append((x, cur[1]+1))

print(ans)
