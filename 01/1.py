import sys
import re
input = sys.stdin.read().strip().split()
ans = 0
for line in input:
    for c in range(ord('a'), ord('z')+1):
        line = line.replace(chr(c), "")
    ans += int(line[0]+line[-1])
print(ans)
