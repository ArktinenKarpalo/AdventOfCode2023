import sys
import collections
input = sys.stdin.read().strip().split("\n")
ans = 0
for line in input:
    a,b = line.split()
    b = list(map(int, b.split(",")))
    d = collections.defaultdict(int)
    d[(0,0)] = 1
    for i in range(len(a)):
        for j in range(len(b), len(b)+2):
            if a[i] != '#':
                d[(i+1, j)] += d[(i,j)]
        for j in range(len(b)):
            if a[i] != '#':
                d[(i+1, j)] += d[(i,j)]
            ok = True
            for k in range(b[j]):
                if i+k >= len(a):
                    ok = False
                    break
                if a[i+k] == '.':
                    ok = False
                    break
            if i+b[j] < len(a) and a[i+b[j]] == '#':
                ok = False
            if ok:
                d[(i+b[j]+1, j+1)] += d[(i,j)]
    ans += d[(len(a), len(b))]
    ans += d[(len(a)+1, len(b))]


                
print(ans)
