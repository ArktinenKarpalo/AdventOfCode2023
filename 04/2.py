import sys
import collections
import re
input = sys.stdin.read().strip().split("\n")
ans = 0
wo = collections.defaultdict(int)
for idx,line in enumerate(input):
    wo[idx] += 1
    g = re.match("Card\s+?([0-9]+)\: (.*?)\|(.*?)$", line).groups()
    win = set(map(int, g[1].split()))
    cnt = 0
    for x in map(int, g[2].split()):
        if x in win:
            cnt += 1
    ans += wo[idx]
    if cnt > 0:
        for x in range(idx+1, min(idx+cnt+1, len(input))):
            wo[x] += wo[idx]
print(ans)
