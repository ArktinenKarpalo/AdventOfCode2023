import sys
input = sys.stdin.read().strip().split("\n\n")

def ref(g, r):
    for i in range(1, 1+min(r, len(g)-r)):
        for j in range(len(g[0])):
            if g[r-i][j] != g[r+i-1][j]:
                return False
    return True

ans = 0
for g in map(lambda x: x.split(), input):
    for r in range(1, len(g)):
        if ref(g,r):
            ans +=  r*100
    g = list(zip(*g))
    for c in range(1, len(g)):
        if ref(g,c):
            ans +=  c
print(ans)
