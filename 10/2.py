import sys
import collections
input = sys.stdin.read().strip().split("\n")

pos = None
vrk = collections.defaultdict(list)
def con(x, y, z):
    vrk[x].append(z)
    vrk[y].append(z)
for y,line in enumerate(input):
    y *= 3
    for x,c in enumerate(line):
        x *= 3
        if c == 'S':
            pos = (y+1,x+1)
            # replace with J
            con((y-1,x+1),(y+1,x+1),(y,x+1))
            con((y+1,x),(y,x+1),(y+1,x+1))
            con((y+1,x-1),(y+1,x+1),(y+1,x))
        if c == '|':
            con((y+1,x+1), (y-1,x+1), (y,x+1))
            con((y+1+1,x+1), (y-1+1,x+1), (y+1,x+1))
            con((y+1+2,x+1), (y-1+2,x+1), (y+2,x+1))
        elif c == '-':
            con((y+1,x+1),(y+1,x-1),(y+1,x))
            con((y+1,x+1+1),(y+1,x-1+1),(y+1,x+1))
            con((y+1,x+1+2),(y+1,x-1+2),(y+1,x+2))
        elif c == 'L':
            con((y-1,x+1),(y+1,x+1),(y,x+1))
            con((y+1,x+2),(y,x+1),(y+1,x+1))
            con((y+1,x+1),(y+1,x+3),(y+1,x+2))
        elif c == 'J':
            con((y-1,x+1),(y+1,x+1),(y,x+1))
            con((y+1,x),(y,x+1),(y+1,x+1))
            con((y+1,x-1),(y+1,x+1),(y+1,x))
        elif c == '7':
            con((y+1,x-1),(y+1,x+1),(y+1,x))
            con((y+2,x+1),(y+1,x),(y+1,x+1))
            con((y+1,x+1),(y+3,x+1),(y+2,x+1))
        elif c == 'F':
            con((y+1,x+3),(y+1,x+1),(y+1,x+2))
            con((y+2,x+1),(y+1,x+2),(y+1,x+1))
            con((y+1,x+1),(y+3,x+1),(y+2,x+1))
        elif c == '.':
            pass

vis = set()
q = collections.deque()
q.append((pos, 0))
while len(q) > 0:
    cur = q.popleft()
    if cur[0] in vis:
        continue
    vis.add(cur[0])
    for x in vrk[cur[0]]:
        if cur[0] in vrk[x]:
            q.append((x, cur[1]+1))


lim_min = -1
lim_max = max(len(input),len(input[0]))+1
lim_max *= 3
vis2 = set()
q = collections.deque()
q.append((-1,-1))
ans = 0
while len(q) > 0:
    cur = q.popleft()
    if cur in vis2 or cur in vis:
        continue
    vis2.add(cur)
    if min(cur[0], cur[1]) < lim_min or max(cur[0], cur[1]) > lim_max:
        continue
    q.append((cur[0]+1, cur[1]))
    q.append((cur[0]-1, cur[1]))
    q.append((cur[0], cur[1]+1))
    q.append((cur[0], cur[1]-1))
for y in range(len(input)):
    for x in range(len(input[y])):
        ok = True
        for i in range(3):
            for j in range(3):
                c = (y*3+i,x*3+j)
                if c in vis or c in vis2:
                    ok = False
        if ok:
            ans += 1

print(ans)
