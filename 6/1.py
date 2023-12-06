import sys
input = sys.stdin.read().strip().split("\n")

time = list(map(int, input[0].split(":")[1].split()))
dist = list(map(int, input[1].split(":")[1].split()))
ans = 1
for idx in range(len(time)):
    wt = 0
    for ht in range(1, time[idx]):
        if ht*(time[idx]-ht) > dist[idx]:
            wt += 1
    ans *= wt

print(ans)
