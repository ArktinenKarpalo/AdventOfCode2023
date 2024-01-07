import sys
input = sys.stdin.read().strip().split("\n")

ans = 0
for line in input:
    pyr = [list(map(int, line.split()))]
    while pyr[-1].count(0) != len(pyr[-1]):
        pyr.append([])
        for x in range(len(pyr[-2])-1):
            pyr[-1].append(pyr[-2][x+1]-pyr[-2][x])
    pyr.reverse()
    luku = 0
    for x in pyr:
        x.reverse()
        luku = x[-1]-luku
    ans += luku

print(ans)
