import sys
import re
input = sys.stdin.read().strip().split("\n")
ans = 0
for line in input:
    g = re.match("Card\s+?([0-9]+)\: (.*?)\|(.*?)$", line).groups()
    win = set(map(int, g[1].split()))
    cnt = 0
    for x in map(int, g[2].split()):
        if x in win:
            cnt += 1
    if cnt > 0:
        ans += 2**(cnt-1)
print(ans)
