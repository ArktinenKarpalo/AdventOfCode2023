import sys
import collections
input = sys.stdin.read().strip().split()
input = list(map(list, input))
lol = {}
ans = 0
cr = 0
def load(input):
    ld = 0
    for x in range(len(input[0])):
        d = collections.deque()
        for y in range(len(input)):
            if input[y][x] == 'O':
                ld += len(input)-y
    return ld
R = 1000000000
while cr < R:
    cr += 1
    for rt in range(4):
        for x in range(len(input[0])):
            d = collections.deque()
            for y in range(len(input)):
                if input[y][x] == '#':
                    d.clear()
                else:
                    d.append(y)
                if input[y][x] == 'O':
                    nl = d.popleft()
                    input[y][x] = '.'
                    input[nl][x] = 'O'
                    ans += len(input)-nl

        input = list(map(list, zip(*reversed(input))))
    asd = "\n".join(map(lambda x: "".join(x), input))
    if asd in lol:
        cr += ((R-cr)//(cr-lol[asd]))*(cr-lol[asd])
    lol[asd] = cr
print(load(input))
