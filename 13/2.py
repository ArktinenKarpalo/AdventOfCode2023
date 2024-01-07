import sys
input = sys.stdin.read().strip().split("\n\n")

def ref(g, r):
    for i in range(1, 1+min(r, len(g)-r)):
        for j in range(len(g[0])):
            if g[r-i][j] != g[r+i-1][j]:
                return False
    return True

def aa(g, asd):
    sm = 0
    asd = list(map(set, asd))
    for r in range(1, len(g)):
        if ref(g,r):
            if r not in asd[0]:
                sm +=  r*100
                asd[0].add(r)
    g = list(zip(*g))
    for c in range(1, len(g)):
        if ref(g,c):
            if c not in asd[1]:
                sm +=  c
                asd[1].add(c)
    return (sm, asd)


ans = 0
for g in map(lambda x: x.split(), input):
    g = list(map(list, g))
    orig = aa(g, (set(), set()))
    fu = False
    for i in range(len(g)):
        for j in range(len(g[i])):
            if g[i][j] == '#':
                g[i][j] = '.'
                a2 = aa(g, orig[1])
                ans += a2[0]
                g[i][j] = '#'
            if g[i][j] == '.':
                g[i][j] = '#'
                a2 = aa(g, orig[1])
                ans += a2[0]
                g[i][j] = '.'

print(ans//2)
